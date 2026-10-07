---
id: task-family_libero_object_swap_t1
scope: task-family
suite: libero_object
regime: swap
task_id: 1
task_language: Pick the cream cheese and place it in the basket
evidence:
  cells:
  - object_swap_t1_s0
  attempts: 7
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick a flat blue-white cream-cheese box among similar groceries and put it into a white-lined woven basket in the low object frame. The hard part is not the grasp; it is rejecting rim-biased basket coordinates and entering over the true liner center.


## Re-localization per scene
Cream cheese: use agentview RGB, not segmentation alone. It is the small blue-white flat rectangular package with a blue oval label; it can be confused with butter if looking only for a small box, but butter has red/yellow/black Farm Fresh labeling. Sample firm pixels on the top/visible face; reject edge pixels that return table z or jump outside the package.
Basket: use agentview to identify the white-lined woven container, then move above it and use wrist view for geometry. The white liner center is the placement target; exterior woven wall, rim fold, and front/right lip are distractors. Use a wrist region over the open white liner and reject estimates that land on the far outside wall or near rim.
This run's absolute coordinates are counter-examples only; swap seeds must re-localize every object and the basket center.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/object_swap_t1_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_object_swap_t1.json`.
