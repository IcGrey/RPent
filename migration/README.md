# RPent server migration

This branch preserves the local LIBERO VLA-placement experiment on base
ca48092f41ac3191f5d0514c881978ed1ff11095. It does not include the fork's newer
unrelated commits. Experiment outputs, model weights and credentials are transferred separately
over SSH. A snapshot of the experimental memory is included below.

## Rebuild

On an Ubuntu/Debian host with a working NVIDIA driver, install git, curl,
build-essential, pkg-config, libegl1, libgl1, libglib2.0-0, ffmpeg and uv.
From this checkout:

```bash
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r migration/requirements-frozen.txt
uv pip install --no-deps -e .
```

The frozen requirements record the actual source environment, including pinned
Git dependencies. Installation and rendering must be verified on the destination.
Copy checkpoints and LIBERO-Pro assets separately. Regenerate the LIBERO-Pro
asset configuration if paths differ. Copy the desired memory corpus, including
_internal, separately; preserve the original frozen evaluation corpus.

## Relay adapter

Copy lab-relay.config.toml and lab-relay.key privately into ~/.codex (key mode
600). Do not commit these files. Install the same Codex CLI and Node versions as
the source. The source Codex executable was supplied by VS Code extension
openai.chatgpt-26.930.61225-linux-x64; it is not bundled here.

```bash
export RPENT_CODEX_EXECUTABLE=/absolute/path/to/codex
export CODEX_BIN="$PWD/migration/rpent-codex-lab"
export LIBERO_TYPE=pro MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
export PI05_CHECKPOINT_PATH="$PWD/checkpoints/RLinf-Pi05-LIBERO-130-fullshot-SFT"
export SAM3_CHECKPOINT_PATH="$PWD/checkpoints/sam3/sam3.pt"
rpent-check-llm --planner codex --model gpt-5.5 --json
```

The adapter reads the existing Responses provider configuration and injects the
key into the child environment. RPENT_RELAY_CONFIG_DIR optionally changes the
configuration directory. Python 3.11+ must be on PATH.

## Experiment queue

repro/run_failure_exploration.py preserves the existing manifest-driven queue.
It still uses source-machine paths: adapt ROOT, adapter, memory, caches and Node
PATH on the new host. Create a fresh manifest/output directory; do not copy old
PIDs or adopted_runs. The manifest records cases, frozen_memory_hashes, GPUs,
model, sessions, attempts_per_session, planner_timeout_s, max_turns,
max_episode_steps and auto_merge_memory.

Validate CUDA, assets, model loading, image/tool calls and one bounded episode
before starting a multi-GPU batch. Existing relay latency and placeholder-call
issues are unresolved; this branch preserves the experiment, not a fix for those
issues. Planner timeouts skip the normal automatic memory merge even if the
environment succeeded. Review success and memory publication separately.

## Included experimental memory

`migration/memory/libero-vla-place-guard-explore-20261007` contains the exact
158-file snapshot, including `_internal/inbox` continuation notes. Checksums are
in `migration/memory-manifest.json`. This is unfinished exploration memory, not
a validated or frozen evaluation release. Old unsuccessful observations remain
historical evidence; 28-task runs timed out and did not complete normal automatic
memory merging. Original evaluation memory is not included.

To continue exploration, copy the snapshot to a writable corpus:

```bash
mkdir -p memory
cp -a migration/memory/libero-vla-place-guard-explore-20261007 memory/
```

The snapshot preserves source paths for traceability. On a server with a different
checkout path, replace `/data/gc02/RPent` in the WORKING copy with the destination
checkout path before use. References to deleted historical logs are provenance,
not available assets: do not follow them as executable recipes. Do not modify the
snapshot in place while running experiments; point `--memory-dir` to the copy.
