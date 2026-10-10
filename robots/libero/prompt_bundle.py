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

"""LIBERO prompt bundle assembly."""

from __future__ import annotations

from collections.abc import Mapping

from robots.libero.prompts import evaluate as evaluate_parts
from robots.libero.prompts import explore as explore_parts
from robots.libero.prompts import user as user_parts
from rpent.prompt.utils import Numbered, PromptNode


def system_prompt(
    variables: Mapping[str, object] | None = None,
) -> PromptNode:
    """Assemble the LIBERO system prompt for the selected run mode."""
    if (variables or {}).get("mode", "eval") == "explore":
        prompt = explore_parts.system_prompt()
    else:
        prompt = evaluate_parts.system_prompt(variables)
    if (variables or {}).get("no_memory_vla_place"):
        prompt = dict(prompt)
        for key, value in prompt.items():
            if key.startswith("PROVEN LEVERS"):
                prompt[key] = value.replace(
                    "grip, then YOU script the entire carry + place (Rule 1 — Pi0 never places).",
                    "grip, then plan the carry and use pi0_place near the target (Rule 1).",
                ).replace(
                    "measure each, never reuse). Place eef = plate_center − offset; descend to\n"
                    "       z~0.46 until the mug RESTS on the plate (OSC stalls ~0.51), then release\n"
                    "       and retreat STRAIGHT UP (step_clip 0.012).",
                    "measure each, never reuse). Use plate_center − offset to plan a visible\n"
                    "       pre-contact handoff; call pi0_place for final alignment, descent and\n"
                    "       release, inspect support, then retreat STRAIGHT UP (step_clip 0.012).",
                )
    if (variables or {}).get("require_vla_place"):
        prompt = dict(prompt)
        # The legacy task-specific levers explicitly prohibit VLA placement.
        # Keep that section out of this opt-in experiment, not merely superseded
        # by a distant memory note.
        for key in list(prompt):
            if key.startswith("PROVEN LEVERS"):
                del prompt[key]
            elif key.startswith("MEMORY PROFILE"):
                prompt[key] = (
                    "Use this experiment's global and task-family notes, including curated pre-placement references."
                )
        memory_step = """Read {{memory_dir}}/MEMORY.md, the matching task-family note,
its linked pre-placement reference, and relevant global notes. Reuse identification,
grasp, holding confirmation, safe carry and collision lessons;
re-localize from current images. Record consulted files in the audit. No historical
task-specific or Flash action recipes are supplied for this experiment."""
        workflow = prompt.get("WORKFLOW")
        if isinstance(workflow, Numbered):
            prompt["WORKFLOW"] = Numbered(
                [
                    memory_step
                    if item
                    in (
                        explore_parts.BASE_STEP_READ_SEED0_REFS,
                        evaluate_parts.STEP_READ_LOCAL_MEMORY,
                        explore_parts.STEP_READ_MEMORY,
                    )
                    else item
                    for item in workflow.items
                ]
            )
        prompt["PLACEMENT_EXPERIMENT"] = """This run enforces VLA placement ordering.
After pick, visually confirm retention and carry with clearance to a safe, visible
pre-contact handoff; use pi0_place for final alignment/descent/release. Do not script
the final insertion first. release and scripted opening (including move_to defaults)
are blocked until pi0_place actually executes and you call placement_recovery with
mode='scripted_fallback' and a concrete observed reason. A rejected, zero-step VLA
call does not qualify. Each new grasp needs its own place attempt. For a visually
verified empty/lost grasp, declare placement_recovery(mode='empty_gripper', reason=...)
before re-picking; this is an observation assertion, never a held-object release route.
pi0_doubled is disabled in this experiment. After VLA release, inspect support and
retreat open with clearance. Stop physical actions on task termination.
Curated task-family excerpts stop before final lowering/insertion/release.
Confirm the payload is retained and fully clear of the destination rim or shelf
at the handoff; then call pi0_place. Historical coordinates require fresh perception.
The experiment memory omits full old task-specific/flash action recipes:
missing exact-seed references are expected. Read MEMORY.md and current task-family
notes; do not search another corpus or reconstruct historical placement scripts.
In exploration, test changed handoff/prompt/budget conditions after a failed attempt,
not a reset followed by bypassing the VLA experiment with the old script."""
    return prompt


def user_prompt(variables: Mapping[str, object] | None = None) -> PromptNode:
    """Assemble the LIBERO user prompt tree."""
    return {
        "CELL": user_parts.CELL,
        "MODE": user_parts.MODE,
        "BEGIN": user_parts.BEGIN,
    }


__all__ = ["system_prompt", "user_prompt"]
