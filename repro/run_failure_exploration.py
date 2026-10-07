"""Run the approved failed-task exploration queue; preserve every run artifact."""
import concurrent.futures
import fcntl
import hashlib
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import time

from exploration_outcome import classify_exit

ROOT = Path('/data/gc02/RPent')
OUT = Path(sys.argv[1]).resolve()
M = json.loads((OUT / 'manifest.json').read_text())
lock = (OUT / 'runner.lock').open('w')
fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
(OUT / 'supervisor.pid').write_text(str(os.getpid()))
env = dict(os.environ)
for key in ('CODEX_BASE_URL', 'CODEX_API_KEY', 'CODEX_SERVICE_TIER', 'CUDA_VISIBLE_DEVICES'):
    env.pop(key, None)
env.update(CODEX_BIN=M['adapter'], MUJOCO_GL='egl', PYOPENGL_PLATFORM='egl',
           LIBERO_TYPE='pro', HF_HOME='/data/gc02/cache/huggingface',
           XDG_CACHE_HOME='/data/gc02/cache', HF_HUB_DISABLE_XET='1',
           PI05_CHECKPOINT_PATH=str(ROOT/'checkpoints/RLinf-Pi05-LIBERO-130-fullshot-SFT'),
           SAM3_CHECKPOINT_PATH=str(ROOT/'checkpoints/sam3/sam3.pt'))
env['PATH'] = '/data/gc02/tools/node-v22.14.0-linux-x64/bin:' + env['PATH']
adopted = {int(x["gpu"]): x for x in M.get("adopted_runs", [])}
pending = queue.Queue()
for case in M['cases']:
    if not any(x['case'] == case for x in adopted.values()):
        pending.put(case)

def worker(gpu):
    while True:
        adoption = adopted.pop(gpu, None)
        if adoption:
            case = adoption["case"]
        else:
            try:
                case = pending.get_nowait()
            except queue.Empty:
                return
        name = f"{case['suite']}-t{case['task']}-s0"
        output = OUT / name
        if (output/'process-result.json').exists():
            continue
        output.mkdir(exist_ok=True)
        cmd = [str(ROOT/'.venv/bin/rpent'), '--robot', 'libero', '--libero-type', 'pro',
               '--suite', case['suite'], '--task', str(case['task']), '--seed', '0',
               '--planner', 'codex', '--model', M['model'], '--reasoning-effort', 'xhigh',
               '--cuda-device', str(gpu), '--memory-profile', 'local', '--memory-dir', M['memory'],
               '--output-dir', str(output), '--require-vla-place', '--max-turns', str(M['max_turns']),
               '--planner-timeout-s', str(M['planner_timeout_s']), '--max-episode-steps', str(M['max_episode_steps']),
               '--explore', '--explore-sessions', str(M['sessions']),
               '--explore-attempts-per-session', str(M['attempts_per_session']),
               '--auto-merge-memory' if M.get('auto_merge_memory', False) else '--no-auto-merge-memory']
        (output/'command.json').write_text(json.dumps(cmd, indent=2))
        start = adoption['started_at'] if adoption else time.time()
        if adoption:
            pid = adoption['pid']
            print(json.dumps({'event':'adopted','case':name,'gpu':gpu,'pid':pid}),flush=True)
            while True:
                stat = Path(f'/proc/{pid}/stat')
                if not stat.exists():
                    break
                try:
                    fields = stat.read_text().rsplit(')',1)[1].split()
                except FileNotFoundError:
                    break
                if fields[0] == 'Z' or fields[19] != adoption['proc_start_ticks']:
                    break
                time.sleep(5)
            code = None  # Existing process is not our child; do not invent its exit code.
        else:
            print(json.dumps({'event':'started', 'case':name,'gpu':gpu}), flush=True)
            with (output/'console.log').open('a') as log:
                proc = subprocess.Popen(cmd, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
                (output/'pid').write_text(str(proc.pid))
                code = proc.wait()
        result = {'case':case, 'exit_code':code, 'elapsed_s':round(time.time()-start,1), 'gpu':gpu,
                  'native_success':False, 'pi0_place_calls':0, 'scripted_fallbacks':0}
        for f in output.glob('sessions/*/states.json'):
            for step in json.loads(f.read_text()).get('steps',[]):
                result['native_success'] |= bool(step.get('terminated'))
                command = step.get('command') or {}
                result['pi0_place_calls'] += command.get('action') == 'pi0_place'
                result['scripted_fallbacks'] += (command.get('action') == 'placement_recovery' and command.get('mode') == 'scripted_fallback')
        console = (output/'console.log').read_text(errors='replace') if (output/'console.log').exists() else ''
        result['outcome'] = classify_exit(code, console)
        (output/'process-result.json').write_text(json.dumps(result, indent=2))
        print(json.dumps(result), flush=True)
        # Stop this lane on infrastructure errors; do not burn through the queue.
        if result['outcome'] in ('infrastructure_error', 'unknown_exit'):
            return

with concurrent.futures.ThreadPoolExecutor(max_workers=len(M['gpus'])) as pool:
    list(pool.map(worker, M['gpus']))
results = [json.loads(f.read_text()) for f in OUT.glob('*/process-result.json')]
frozen = ROOT/'memory/libero-gpt55-eval'
unchanged = all((frozen/k).is_file() and hashlib.sha256((frozen/k).read_bytes()).hexdigest()==v for k,v in M['frozen_memory_hashes'].items())
(OUT/'batch-result.json').write_text(json.dumps({'completed':len(results),'planned':len(M['cases']),
    'frozen_memory_unchanged':unchanged,'results':results},indent=2))
