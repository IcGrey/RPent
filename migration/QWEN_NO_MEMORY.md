# Qwen no-memory + Pi place full rerun

This experiment uses `openai-chat:qwen3.6-flash` through the API planner and
`https://kjapi.botsmart.net/v1`. The queue contains eight LIBERO-Pro suites,
tasks 0–9 and seeds 0–1: 160 episodes on GPUs 0–7.

## Destination setup

Follow [README.md](README.md) to install the frozen Python environment and
system rendering dependencies. This API experiment does not need the Codex
relay adapter. Copy these large assets privately to the destination:

- `checkpoints/RLinf-Pi05-LIBERO-130-fullshot-SFT/`
- `checkpoints/sam3/sam3.pt`
- The source environment's LIBERO-Pro `assets`, `bddl_files` and `init_files`
  directories. Preserve the exact initial-state files used by the source run;
  do not assume a fresh dependency installation has identical data.

Activate the destination environment from the checkout root:

```bash
source .venv/bin/activate
export LIBERO_TYPE=pro MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PI05_CHECKPOINT_PATH="$PWD/checkpoints/RLinf-Pi05-LIBERO-130-fullshot-SFT"
export SAM3_CHECKPOINT_PATH="$PWD/checkpoints/sam3/sam3.pt"
unset CUDA_VISIBLE_DEVICES
read -rsp 'Relay API key: ' OPENAI_API_KEY; echo
export OPENAI_API_KEY
```

The Linux host must allow unprivileged user/mount namespaces and have `unshare`,
`mount` and `umount`. Verify the eight GPUs and assets before launching.
Credentials remain in the process environment and must not be committed.

## Prepare without running

```bash
python repro/prepare_no_memory_qwen.py
```

This prints a new absolute output directory and writes its `manifest.json`.
It also creates the empty memory corpus and regenerates `repro/libero-config`
for this host. If assets live elsewhere, supply
`--libero-root /absolute/path/to/liberopro` (the directory containing `assets`,
`bddl_files` and `init_files`). It does not load policies or send API requests.
Do not copy old progress files, results or PIDs into this fresh output directory.

## Start on the destination

For a durable background run, replace the output path below with the path
printed by the preparation command. A user systemd manager must be available;
enable user lingering if this host needs it to keep jobs alive after logout.

```bash
RPENT_OUTPUT=/absolute/path/to/RPent/logs/no-memory-qwen-place20-TIMESTAMP
systemd-run --user --unit=rpent-qwen-place20-rerun --collect \
  --property=Type=exec --property=KillMode=mixed \
  --setenv="OPENAI_API_KEY=$OPENAI_API_KEY" \
  --setenv="LIBERO_TYPE=$LIBERO_TYPE" \
  --setenv="MUJOCO_GL=$MUJOCO_GL" \
  --setenv="PYOPENGL_PLATFORM=$PYOPENGL_PLATFORM" \
  --setenv="PI05_CHECKPOINT_PATH=$PI05_CHECKPOINT_PATH" \
  --setenv="SAM3_CHECKPOINT_PATH=$SAM3_CHECKPOINT_PATH" \
  --working-directory="$PWD" \
  --property="StandardOutput=append:$RPENT_OUTPUT/supervisor.log" \
  --property="StandardError=append:$RPENT_OUTPUT/supervisor.log" \
  "$PWD/.venv/bin/python" "$PWD/repro/run_no_memory_qwen.py" "$RPENT_OUTPUT"
```

`progress.json` reports completed results and active episodes; each episode
contains a transcript, states, result and video when motion occurred. Restarting
the runner with the same output path resumes existing results; preparing a new
directory is required for a full rerun. Do not run two supervisors on one output.

## Fixed experiment settings

The empty memory has no global, task-family or task-specific experience. Base
system instructions and operation guides remain, with only conflicting Pi
placement instructions adapted. The LLM can call `pi0_place`; it is optional,
and parameter overrides and scripted recovery remain allowed. Defaults are
20 chunks, 100 steps, opening threshold 0.07 m and open hold 3 steps.

Each episode permits 100 model requests, 8192 output tokens per request and
10000 environment steps. Planner budgets are 5000 seconds for `libero_10_*`
and 1200 seconds for the other suites. `reasoning_effort=none` is requested,
but the relay/model may still return thinking. Invalid tool parameters must be
corrected within the same request budget; strict validation remains enabled.

The private mount namespace hides other memory, logs, archives and repro data,
while exposing only the current episode, empty read-only memory and writable
LIBERO configuration. Checkpoints and installed benchmark assets stay visible.

Planner errors are saved as `agent_error` in transcripts. Explicit planner
budget timeouts count as unsuccessful episodes without stopping the queue;
unexpected exit errors, quota errors, missing states and memory changes stop
admission of new work for inspection. Elapsed time alone is not timeout evidence.

## Request upload diagnostics

Each episode owns a loopback proxy that forwards Chat Completions requests to
the relay. It preserves the JSON payload and writes the same HTTP request body
in 64 KiB pieces, with explicit `Content-Length`. This is one request, not
separate uploads requiring a merge API. The proxy uses a 600-second write
timeout by default; change `upload_write_timeout_s` in the prepared manifest
before launching if needed. The overall episode planner budget still applies.
The API SDK also retains its own request timeout and retry policy.

`upload-diagnostics.jsonl` records request size, bytes handed to the transport,
transport phases, response-header timing and exception type. It does not record
request/response bodies, authorization headers or raw exception messages.
Bytes handed to the transport are not proof the remote application received
them. Proxy transport failures return an HTTP 502 with a redacted diagnostic;
the diagnostic exception type distinguishes `WriteTimeout` from other failures.

The proxy and episode share an owned process group. The normal exit closes the
proxy; the supervisor's outer timeout terminates both. Chunking enables progress
measurement but has no demonstrated throughput benefit. Increasing the timeout
may help a slow upload, but does not fix sustained blocking or reduce request size.
