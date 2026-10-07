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

"""Release handoff contracts using deterministic observations and VLA chunks."""

from types import SimpleNamespace

import numpy as np
import pytest

from robots.libero.flywheel import LIBERO_SPEC
from robots.libero.tools import LiberoPrimitives
from rpent.flywheel.episode import validate_episode


def observation(gap):
    states = np.zeros(8, dtype=np.float32)
    states[2] = 1.1
    states[6:8] = [gap / 2, -gap / 2]
    return {
        "states": states,
        "main_images": np.zeros((256, 256, 3), dtype=np.uint8),
        "wrist_images": np.zeros((256, 256, 3), dtype=np.uint8),
        "task_descriptions": "full task",
    }


class Env:
    def __init__(self, gaps, initial=0.03, done=None):
        self.gaps = iter(gaps)
        self.initial = initial
        self.done = done
        self.terminated = self.truncated = False
        self.actions = []

    def reset(self):
        return observation(self.initial), {}

    def step(self, action):
        self.actions.append(action.copy())
        if self.done == "terminated":
            self.terminated = True
        if self.done == "truncated":
            self.truncated = True
        return observation(next(self.gaps)), 0, self.terminated, self.truncated, {}

    def chunk_step(self, *args, **kwargs):
        raise AssertionError("Placement must inspect every executed step")


class Model:
    def __init__(self, chunk_size):
        self.chunk_size = chunk_size
        self.calls = 0

    def predict(self, obs, *, options):
        assert obs["task_descriptions"] == "place held bowl on plate"
        self.calls += 1
        # Always commanding open does not mean the measured fingers opened.
        actions = np.zeros((self.chunk_size, 7), dtype=np.float32)
        actions[:, 6] = -1
        return actions


def make(gaps, initial=0.03, chunk_size=8, done=None, config=None):
    env = Env(gaps, initial, done)
    model = Model(chunk_size)
    p = LiberoPrimitives(
        env, model, SimpleNamespace(), lambda: None, flywheel_config=config
    )
    p.reset()
    p.start_recording()
    return p, env, model


def place(p, **kwargs):
    return p.pi0_place("place held bowl on plate", holding_confirmed=True, **kwargs)


def test_opening_stops_inside_chunk_and_keeps_original_task():
    p, env, model = make([0.03, 0.078, 0.078, 0.078])
    result = place(p)
    assert result["stop_reason"] == "release_detected"
    assert result["release_detected"] and not result["terminated"]
    assert result["steps_used"] == len(env.actions) == p.recorded_frame_count() == 4
    assert model.calls == 1
    assert p._last_obs["task_descriptions"] == "full task"


def test_transient_opening_resets_and_streak_spans_chunks():
    p, env, model = make([0.078, 0.03, 0.078, 0.078, 0.078], chunk_size=2)
    result = place(p)
    assert result["release_detected"]
    assert len(env.actions) == 5
    assert model.calls == 3


@pytest.mark.parametrize(
    "initial,confirmed", [(0.08, True), (0, True), (0.03, False), (float("nan"), True)]
)
def test_rejects_uncertain_empty_or_open_handoff(initial, confirmed):
    p, env, model = make([], initial=initial)
    result = p.pi0_place("place held bowl on plate", holding_confirmed=confirmed)
    assert result["stop_reason"] == "handoff_rejected"
    assert not result["release_detected"]
    assert not env.actions and model.calls == 0


@pytest.mark.parametrize(
    "limits,steps", [({"max_steps": 3}, 3), ({"max_chunks": 1}, 8)]
)
def test_budget_does_not_force_open_or_retreat(limits, steps):
    p, env, model = make([0.03] * 8)
    result = place(p, **limits)
    assert result["stop_reason"] == "budget_exhausted"
    assert result["budget_exhausted"] and not result["release_detected"]
    assert len(env.actions) == steps


@pytest.mark.parametrize(
    "done,reason",
    [("terminated", "task_terminated"), ("truncated", "environment_truncated")],
)
def test_environment_stop_discards_remaining_actions(done, reason):
    p, env, model = make([0.03], done=done)
    assert place(p)["stop_reason"] == reason
    assert len(env.actions) == 1
    assert place(p)["steps_used"] == 0
    assert model.calls == 1


def test_cancellation_restores_instruction():
    p, env, model = make([0.03])

    def cancel():
        if env.actions:
            raise RuntimeError("cancelled")

    p._check_cancelled = cancel
    with pytest.raises(RuntimeError, match="cancelled"):
        place(p)
    assert len(env.actions) == 1
    assert p._last_obs["task_descriptions"] == "full task"


@pytest.mark.parametrize(
    "args",
    [
        {"max_chunks": 0},
        {"max_steps": -1},
        {"open_hold_steps": 0},
        {"gripper_open_thresh": 0.1},
    ],
)
def test_invalid_parameters_do_not_touch_environment(args):
    p, env, model = make([])
    with pytest.raises(ValueError):
        place(p, **args)
    assert not env.actions and model.calls == 0


def test_collection_preserves_vla_source_and_only_executed_prefix(tmp_path):
    p, env, model = make(
        [0.078] * 3,
        config={"root": tmp_path, "suite": "libero_object", "task_id": 2, "seed": 3},
    )
    p.begin_primitive("pi0_place")
    assert place(p)["release_detected"]
    p.end_primitive()
    path = p.finalize_flywheel()
    assert validate_episode(path, spec=LIBERO_SPEC)["step_count"] == 3
    with np.load(path / "transitions.npz") as data:
        np.testing.assert_array_equal(data["action_source"], [1, 1, 1])


@pytest.mark.parametrize("gap", [float("nan"), float("inf")])
def test_invalid_observation_stops_before_next_action(gap):
    p, env, model = make([gap])
    result = place(p, open_hold_steps=1)
    assert result["stop_reason"] == "invalid_observation"
    assert result["final_gripper_opening"] is None
    assert not result["release_detected"]
    assert len(env.actions) == 1


@pytest.mark.parametrize(
    "actions", [np.empty((0, 7)), np.zeros((3, 8)), np.full((3, 7), np.nan)]
)
def test_invalid_vla_proposal_is_not_executed(actions):
    p, env, model = make([])
    model.predict = lambda *args, **kwargs: actions
    with pytest.raises(ValueError, match="action array"):
        place(p)
    assert not env.actions
    assert p._last_obs["task_descriptions"] == "full task"
