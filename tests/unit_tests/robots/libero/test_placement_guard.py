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

"""Placement ordering, fallback accounting and mode isolation."""

import re
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from robots.libero.placement_guard import PlacementGuard
from robots.libero.prompt_bundle import system_prompt
from robots.libero.toolkit import LiberoToolkit
from rpent.prompt.utils import format_prompt


@pytest.mark.parametrize(
    "name,args",
    [
        ("release", {}),
        ("move_to", {}),
        ("move_pose", {}),
        ("set_gripper", {"gripper": -1}),
        ("rotate_wrist", {"gripper": -1}),
        ("rotate_pitch", {"gripper": -1}),
        ("pi0_pick", {"prompt": "pick"}),
        ("pi0_doubled", {"prompt": "place"}),
    ],
)
def test_guard_refuses_bypasses_before_any_physics(tmp_path, name, args):
    kit = LiberoToolkit.__new__(LiberoToolkit)
    kit._placement_guard = PlacementGuard(tmp_path / "audit.jsonl")
    kit._placement_guard.before("pi0_pick", {})
    kit._primitives = SimpleNamespace(
        env=SimpleNamespace(terminated=False, truncated=False)
    )
    physical_handler = Mock()
    result = kit._execute_primitive(name, physical_handler, **args)
    assert result["physical_steps"] == 0
    physical_handler.assert_not_called()


def test_real_execution_and_reason_required_per_grasp(tmp_path):
    guard = PlacementGuard(tmp_path / "audit.jsonl")
    guard.before("pi0_pick", {})
    assert guard.before("move_to", {"gripper": 1}) is None
    guard.after("pi0_place", {"steps_used": 0, "stop_reason": "handoff_rejected"}, 0.04)
    assert "error" in guard.recover("scripted_fallback", "still held")
    guard.after(
        "pi0_place", {"steps_used": 20, "stop_reason": "budget_exhausted"}, 0.04
    )
    assert guard.before("release", {}) is not None
    with pytest.raises(ValueError):
        guard.recover("scripted_fallback", " ")
    guard.recover("scripted_fallback", "book pitched toward divider; support rechecked")
    assert guard.before("release", {}) is None
    guard.after("release", {}, 0.08)
    assert guard.before("move_to", {"gripper": -1}) is None
    guard.before("pi0_pick", {})
    assert "error" in guard.recover("scripted_fallback", "old attempt does not count")
    assert '"event": "scripted_fallback_action"' in guard.audit_path.read_text()


def test_vla_release_allows_retreat_and_reset_clears_attempt(tmp_path):
    guard = PlacementGuard(tmp_path / "audit.jsonl")
    guard.before("pi0_pick", {})
    guard.after("pi0_place", {"steps_used": 18, "release_detected": True}, 0.076)
    assert guard.before("move_to", {}) is None
    guard.before("set_gripper", {"gripper": 1})
    assert guard.before("release", {}) is not None
    guard.recover("empty_gripper", "current wrist view shows object left on table")
    assert guard.before("pi0_pick", {}) is None
    guard.reset()
    assert guard.before("release", {}) is None
    assert not guard.attempted


def test_disabled_guard_preserves_dispatch():
    kit = LiberoToolkit.__new__(LiberoToolkit)
    kit._placement_guard = None
    kit._primitives = SimpleNamespace(begin_primitive=Mock(), end_primitive=Mock())
    handler = Mock(return_value={"steps_used": 1})
    assert kit._execute_primitive("release", handler) == {"steps_used": 1}
    handler.assert_called_once_with()


@pytest.mark.parametrize("mode", ["explore", "eval"])
def test_experiment_prompt_removes_legacy_vla_prohibition(mode):
    variables = dict.fromkeys(
        re.findall(
            r"\{\{(\w+)\}\}",
            str(system_prompt({"mode": mode, "memory_profile": "local"})),
        ),
        "offline",
    )
    regular = format_prompt(
        system_prompt({"mode": mode, "memory_profile": "local"}), variables=variables
    )
    guarded = format_prompt(
        system_prompt(
            {"mode": mode, "memory_profile": "local", "require_vla_place": True}
        ),
        variables=variables,
    )
    assert "Pi0 never places" in regular
    assert "Pi0 never places" not in guarded
    assert "PER-TASK RECIPES THAT WORKED" not in guarded
    assert "placement_recovery" in guarded


def test_no_memory_place_preserves_baseline_except_conflicting_placement_levers():
    baseline = system_prompt({"mode": "eval", "memory_profile": "local"})
    changed = system_prompt(
        {"mode": "eval", "memory_profile": "local", "no_memory_vla_place": True}
    )
    assert baseline.keys() == changed.keys()
    for key in baseline:
        if not key.startswith("PROVEN LEVERS"):
            assert baseline[key] == changed[key]
    variables = dict.fromkeys(re.findall(r"\{\{(\w+)\}\}", str(changed)), "offline")
    rendered = format_prompt(changed, variables=variables)
    assert "PROVEN LEVERS" in rendered
    assert "PER-TASK RECIPES THAT WORKED" in rendered
    assert "Pi0 never places" not in rendered
    assert "pi0_place" in rendered
    assert "pi0_doubled is disabled" not in rendered
    assert "plan the carry and use pi0_place near the target" in rendered
    assert "call pi0_place for final alignment, descent" in rendered
