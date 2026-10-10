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

"""Prepare a fresh 160-episode manifest; never start the experiment."""

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--libero-root", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = (
        args.output or root / "logs" / f"no-memory-qwen-place20-{stamp}"
    ).resolve()
    if not output.is_relative_to(root / "logs"):
        parser.error("--output must be inside this checkout's logs directory")
    if output.exists():
        parser.error("output already exists; choose a fresh directory for a full rerun")
    if args.libero_root is not None:
        libero = args.libero_root.resolve()
    else:
        spec = importlib.util.find_spec("liberopro")
        if spec is None or spec.origin is None:
            parser.error("install LIBERO-Pro or provide --libero-root")
        libero = Path(spec.origin).parent / "liberopro"
    for name in ("assets", "bddl_files", "init_files"):
        if not (libero / name).is_dir():
            parser.error(f"missing LIBERO-Pro directory: {libero / name}")
    memory = root / "memory" / "no-memory-qwen36flash-place20"
    marker = "# Memory\n\nNo exploration experience is available.\n"
    allowed = {"MEMORY.md", "global", "task-family", "task-specific"}
    if memory.exists():
        if any(
            p.is_symlink() or str(p.relative_to(memory)) not in allowed
            for p in memory.rglob("*")
        ):
            parser.error("memory directory contains experience or symlinks")
        if (memory / "MEMORY.md").exists() and (
            memory / "MEMORY.md"
        ).read_text() != marker:
            parser.error("memory index is not empty")
    memory.mkdir(parents=True, exist_ok=True)
    (memory / "MEMORY.md").write_text(marker)
    for scope in ("global", "task-family", "task-specific"):
        (memory / scope).mkdir(exist_ok=True)
    config = root / "repro" / "libero-config"
    config.mkdir(parents=True, exist_ok=True)
    # JSON is also valid YAML; avoid importing the simulator during preparation.
    (config / "config.yaml").write_text(
        json.dumps(
            {
                "assets": str(libero / "assets"),
                "bddl_files": str(libero / "bddl_files"),
                "benchmark_root": str(libero),
                "datasets": str(libero.parent / "datasets"),
                "init_states": str(libero / "init_files"),
            },
            indent=2,
        )
        + "\n"
    )
    profile = json.loads(
        (root / "repro/no-memory-qwen36flash-place20-profile.json").read_text()
    )
    suites = [
        f"libero_{family}_{regime}"
        for family in ("10", "goal", "object", "spatial")
        for regime in ("swap", "task")
    ]
    cases = [
        {
            "suite": suite,
            "task": task,
            "seed": seed,
            "episode": f"task-{task:02d}-seed-{seed}",
            "timeout": 5000 if suite.startswith("libero_10_") else 1200,
            "baseline_episode": None,
        }
        for task in range(10)
        for seed in range(2)
        for suite in suites
    ]
    manifest = {**profile, "memory_dir": str(memory), "cases": cases}
    output.mkdir(parents=True)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(output)


if __name__ == "__main__":
    main()
