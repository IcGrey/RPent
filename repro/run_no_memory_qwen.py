# Copyright 2026 The RPent Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run the full no-memory Pi-place evaluation with a Chat Completions planner."""

import hashlib
import json
import os
import queue
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from episode_outcome import planner_timed_out

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(sys.argv[1]).resolve()
manifest = json.loads((OUTPUT / "manifest.json").read_text())
MEMORY = Path(manifest["memory_dir"])
if not os.environ.get("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is required")
pending = queue.Queue()
results, running = [], {}
lock = threading.Lock()
stop = threading.Event()
for case in manifest["cases"]:
    path = OUTPUT / case["suite"] / case["episode"] / "result.json"
    if path.exists():
        results.append(json.loads(path.read_text()))
    else:
        pending.put(case)


def write(path, data):
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    temp.replace(path)


def memory_hashes():
    return {
        str(p.relative_to(MEMORY)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in MEMORY.rglob("*")
        if p.is_file()
    }


initial_memory = memory_hashes()


def publish():
    write(
        OUTPUT / "progress.json",
        {
            "updated": datetime.now(timezone.utc).isoformat(),
            "total": len(manifest["cases"]),
            "completed": len(results),
            "successes": sum(r["environment_success"] for r in results),
            "infrastructure_errors": sum(
                bool(r["verification_errors"]) for r in results
            ),
            "running": list(running.values()),
            "results": results,
            "stopped_for_review": stop.is_set(),
        },
    )


def worker(gpu):
    while not stop.is_set():
        try:
            case = pending.get_nowait()
        except queue.Empty:
            return
        out = OUTPUT / case["suite"] / case["episode"]
        out.mkdir(parents=True, exist_ok=True)
        command = [
            str(ROOT / ".venv/bin/rpent"),
            "--robot",
            "libero",
            "--libero-type",
            "pro",
            "--suite",
            case["suite"],
            "--task",
            str(case["task"]),
            "--seed",
            str(case["seed"]),
            "--planner",
            "api",
            "--model",
            manifest["model"],
            "--base-url",
            manifest["base_url"],
            "--reasoning-effort",
            "none",
            "--cuda-device",
            str(gpu),
            "--memory-profile",
            "local",
            "--memory-dir",
            str(MEMORY),
            "--no-memory-vla-place",
            "--planner-timeout-s",
            str(case["timeout"]),
            "--max-turns",
            "100",
            "--max-episode-steps",
            "10000",
            "--max-tokens",
            "8192",
            "--output-dir",
            str(out),
        ]
        env = os.environ.copy()
        for key in (
            "CODEX_API_KEY",
            "CODEX_BASE_URL",
            "CODEX_SERVICE_TIER",
            "CUDA_VISIBLE_DEVICES",
            "RPENT_CODEX_EXECUTABLE",
            "RPENT_RELAY_CONFIG_DIR",
        ):
            env.pop(key, None)
        env.update(
            PYTHONPATH=str(ROOT),
            RPENT_REPO_ROOT=str(ROOT),
            PYDANTIC_AI_NO_BANNER="1",
            LIBERO_CONFIG_PATH=str(ROOT / "repro/libero-config"),
            OMP_NUM_THREADS="4",
            MKL_NUM_THREADS="4",
            MPLCONFIGDIR=str(out / "matplotlib"),
        )
        invocation = {
            "command": command,
            "gpu": gpu,
            "started_at": time.time(),
            "memory_initial_hashes": initial_memory,
            "baseline_episode": case["baseline_episode"],
        }
        write(out / "invocation.json", invocation)
        with lock:
            running[gpu] = {
                "suite": case["suite"],
                "episode": case["episode"],
                **invocation,
            }
            publish()
        started = time.monotonic()
        timed_out = False
        with (out / "console.log").open("w") as log:
            isolated = [
                "unshare",
                "--user",
                "--map-root-user",
                "--mount",
                str(ROOT / ".venv/bin/python"),
                str(ROOT / "repro/isolated_no_memory_episode.py"),
                str(out),
                str(MEMORY),
                *command,
            ]
            proc = subprocess.Popen(
                isolated,
                cwd=ROOT,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
            (out / "pid").write_text(str(proc.pid))
            try:
                code = proc.wait(timeout=case["timeout"] + 600)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    code = proc.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    code = proc.wait()
        states = (
            json.loads((out / "states.json").read_text()).get("steps", [])
            if (out / "states.json").exists()
            else []
        )
        console = (out / "console.log").read_text(errors="replace")
        transcripts = list(out.glob("transcript*.json"))
        transcript = json.loads(transcripts[0].read_text()) if transcripts else {}
        errors = []
        if memory_hashes() != initial_memory:
            errors.append("memory_changed")
        planner_timeout = planner_timed_out(transcript, console)
        if code != 0 and not planner_timeout:
            errors.append(f"exit_code_{code}")
        if timed_out:
            errors.append("outer_timeout")
        if not states:
            errors.append("no_states")
        if any(
            x in console.lower()
            for x in (
                "insufficient_quota",
                "usage_limit_exceeded",
                "usageLimitExceeded".lower(),
            )
        ):
            errors.append("quota_exhausted")
        stats = transcript.get("stats", {})
        result = {k: case[k] for k in ("suite", "task", "seed", "episode")}
        result.update(
            gpu=gpu,
            exit_code=code,
            elapsed_s=round(time.monotonic() - started, 2),
            environment_success=any(s.get("terminated") is True for s in states),
            agent_error=transcript.get("agent_error"),
            planner_timeout=planner_timeout,
            recorded_states=len(states),
            video_exists=(out / "episode.mp4").exists(),
            memory_unchanged=memory_hashes() == initial_memory,
            verification_errors=errors,
            baseline_episode=case["baseline_episode"],
            stats=stats,
            place_calls=sum(
                s.get("command", {}).get("action") == "pi0_place" for s in states
            ),
        )
        write(out / "result.json", result)
        with lock:
            results.append(result)
            running.pop(gpu)
            if errors:
                stop.set()
            publish()
        print(json.dumps({"event": "completed", **result}), flush=True)


(OUTPUT / "supervisor.pid").write_text(str(os.getpid()))
with lock:
    publish()
with ThreadPoolExecutor(max_workers=len(manifest["gpus"])) as pool:
    list(pool.map(worker, manifest["gpus"]))
write(
    OUTPUT / "summary.json",
    {
        "planned": len(manifest["cases"]),
        "completed": len(results),
        "successes": sum(r["environment_success"] for r in results),
        "results": results,
        "stopped_for_review": stop.is_set(),
    },
)
