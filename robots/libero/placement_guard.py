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

"""Opt-in, per-grasp placement ordering and recovery audit."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

RECOVERY_SPEC = {
    "name": "placement_recovery",
    "description": (
        "Experimental placement guard recovery. scripted_fallback requires an "
        "executed pi0_place for this grasp and a concrete observed reason. "
        "empty_gripper declares a visually verified empty/lost grasp, NOT a way "
        "to release a held object. Neither mode moves the robot. Both are audited."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "mode": {"type": "string", "enum": ["scripted_fallback", "empty_gripper"]},
            "reason": {
                "type": "string",
                "description": "Current visual evidence and why recovery is needed.",
            },
        },
        "required": ["mode", "reason"],
        "additionalProperties": False,
    },
}


class PlacementGuard:
    """Require VLA before scripted opening of a potentially held object.

    Grasp and empty-gripper declarations are not ground-truth object detection.
    This guards tool ordering, and logs declarations separately from execution.
    """

    def __init__(self, audit_path: Path) -> None:
        self.audit_path = audit_path
        self.grasp = 0
        self.pending = False
        self.attempted = False
        self.fallback_reason: str | None = None

    def log(self, event: str, **details: Any) -> None:
        self.audit_path.parent.mkdir(parents=True, exist_ok=True)
        with self.audit_path.open("a") as stream:
            stream.write(
                json.dumps({"event": event, "grasp": self.grasp, **details}) + "\n"
            )

    def reset(self) -> None:
        self.pending = self.attempted = False
        self.fallback_reason = None
        self.log("episode_reset")

    def recover(self, mode: str, reason: str) -> dict[str, Any]:
        if mode not in {"scripted_fallback", "empty_gripper"}:
            raise ValueError("unsupported placement recovery mode")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError("a concrete recovery reason is required")
        if not self.pending:
            return {"error": "no pending grasp to recover"}
        if mode == "scripted_fallback" and not self.attempted:
            self.log("recovery_refused", mode=mode, reason=reason)
            return {
                "error": "pi0_place must execute for this grasp before scripted fallback"
            }
        self.log("recovery_declared", mode=mode, reason=reason)
        if mode == "empty_gripper":
            self.pending = self.attempted = False
            self.fallback_reason = None
        else:
            self.fallback_reason = reason.strip()
        return {"mode": mode, "reason": reason, "physical_steps": 0}

    def before(self, name: str, arguments: dict[str, Any]) -> dict[str, Any] | None:
        opening = name == "release"
        if name in {
            "move_to",
            "move_pose",
            "set_gripper",
            "rotate_wrist",
            "rotate_pitch",
        }:
            default = 1.0 if name.startswith("rotate_") else -1.0
            grip = float(arguments.get("gripper", default))
            if not math.isfinite(grip):
                raise ValueError("gripper must be finite")
            opening = grip < 0
        # A fresh pick can open fingers internally. The contact VLA is not a
        # placement bypass, including when no grasp has yet been declared.
        blocked = name == "pi0_doubled" or (
            self.pending
            and ((opening and not self.fallback_reason) or name == "pi0_pick")
        )
        if blocked:
            self.log("action_refused", tool=name, arguments=arguments)
            return {
                "error": "placement guard refused action",
                "reason": (
                    "Use pi0_place after visual retention and safe target handoff. "
                    "For scripted opening after a real place attempt, call "
                    "placement_recovery(mode='scripted_fallback', reason=...). "
                    "For a visually empty/lost grasp, declare mode='empty_gripper'. "
                    "pi0_doubled is disabled in this experiment."
                ),
                "physical_steps": 0,
            }
        if name == "pi0_pick" or (
            not self.pending
            and name
            in {"move_to", "move_pose", "set_gripper", "rotate_wrist", "rotate_pitch"}
            and float(
                arguments.get("gripper", 1.0 if name.startswith("rotate_") else -1.0)
            )
            > 0
        ):
            self.grasp += 1
            self.pending = True
            self.attempted = False
            self.fallback_reason = None
            self.log("grasp_started", tool=name)
        if opening and self.pending:
            self.log("scripted_fallback_action", tool=name, reason=self.fallback_reason)
        return None

    def after(self, name: str, result: dict[str, Any], opening: float | None) -> None:
        if name == "pi0_place":
            executed = result.get("steps_used", 0) > 0
            if executed:
                self.pending = True
                self.attempted = True
            self.log("vla_place", executed=executed, result=result)
            if result.get("release_detected"):
                self.pending = False
                self.attempted = False
                self.fallback_reason = None
        elif (
            self.fallback_reason
            and opening is not None
            and math.isfinite(opening)
            and opening >= 0.07
        ):
            self.log(
                "scripted_opening_observed",
                opening=opening,
                reason=self.fallback_reason,
            )
            self.pending = self.attempted = False
            self.fallback_reason = None
