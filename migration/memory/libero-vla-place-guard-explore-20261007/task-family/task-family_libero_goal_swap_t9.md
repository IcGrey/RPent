---
id: task-family_libero_goal_swap_t9
scope: task-family
suite: libero_goal
regime: swap
task_id: 9
task_language: Put the wine bottle on the rack
evidence:
  cells:
  - goal_swap_t9_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
A tall bottle must be put on the swapped wine rack. The hard part is reliable bottle acquisition; the rack is a large slatted fixture that can be visually identified and localized from agentview_high.


## Re-localization per scene
Rack: in agentview_high it is the slatted wooden rack on image-left/robot-left, with tan slats, gray rails, and dark red side blocks. Back-project several pixels on the slat faces/channels, not on the vertical support rails. The usable placement surface is broad; this run's absolutes are counter-examples only and must not be cached.
Confusers: stove burner/plate are flat discs and not the destination; the rack is semantically the only slatted wooden fixture.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_swap_t9_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_swap_t9.json`.
