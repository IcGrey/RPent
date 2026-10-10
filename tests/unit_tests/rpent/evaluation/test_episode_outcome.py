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

"""Regression checks for no-memory evaluation timeout classification."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from repro.episode_outcome import planner_timed_out


@pytest.mark.parametrize("budget", [1200, 5000])
def test_timeout_without_console_message(budget: int) -> None:
    assert planner_timed_out({"agent_error": f"planner timed out after {budget}s"}, "")


@pytest.mark.parametrize("error", [None, "HTTPStatusError: 503", "ReadTimeout"])
def test_other_errors_are_not_planner_timeouts(error: str | None) -> None:
    assert not planner_timed_out(
        {"agent_error": error, "elapsed_s": 5008},
        "Model says: planner timed out after 5000s",
    )


def test_legacy_transcript_uses_explicit_log_evidence() -> None:
    assert planner_timed_out({}, "[codex-planner] Codex SDK timed out after 1200s")
    assert not planner_timed_out({"elapsed_s": 5008, "finish": None}, "")


def test_prepare_fresh_queue_without_starting(tmp_path: Path) -> None:
    root = Path(__file__).resolve().parents[4]
    checkout = tmp_path / "checkout"
    (checkout / "repro").mkdir(parents=True)
    for name in (
        "prepare_no_memory_qwen.py",
        "no-memory-qwen36flash-place20-profile.json",
    ):
        shutil.copyfile(root / "repro" / name, checkout / "repro" / name)
    assets = tmp_path / "benchmark"
    for name in ("assets", "bddl_files", "init_files"):
        (assets / name).mkdir(parents=True)
    output = checkout / "logs" / "fresh"
    command = [
        sys.executable,
        str(checkout / "repro/prepare_no_memory_qwen.py"),
        "--output",
        str(output),
        "--libero-root",
        str(assets),
    ]
    subprocess.run(command, check=True, capture_output=True, text=True)
    manifest = json.loads((output / "manifest.json").read_text())
    assert len(manifest["cases"]) == 160
    assert len({(c["suite"], c["task"], c["seed"]) for c in manifest["cases"]}) == 160
    assert manifest["gpus"] == list(range(8))
    assert {c["timeout"] for c in manifest["cases"]} == {1200, 5000}
    assert manifest["pi0_place_defaults"]["max_chunks"] == 20
    assert list(output.iterdir()) == [output / "manifest.json"]
    assert (Path(manifest["memory_dir"]) / "MEMORY.md").read_text() == (
        "# Memory\n\nNo exploration experience is available.\n"
    )
    assert subprocess.run(command, capture_output=True).returncode != 0
