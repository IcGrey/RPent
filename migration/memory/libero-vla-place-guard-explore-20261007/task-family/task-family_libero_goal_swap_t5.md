---
id: task-family_libero_goal_swap_t5
scope: task-family
suite: libero_goal
regime: swap
task_id: 5
task_language: Push the plate to the front of the stove
evidence:
  cells:
  - goal_swap_t5_s0
  attempts: 74
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
This task tests whether the agent can visually localize a swapped stove fixture and discover the semantic front-of-stove region. The visible burner/platform edge is a strong decoy: many placements there look plausible but do not satisfy the predicate.


## Re-localization per scene
Plate: prompt/visual phrase `red-rim white plate` or `white plate with red rings`; confused with the gray burner only in depth, not RGB. Reject any candidate without red rings.
Stove: visual phrase `gray burner on metal square base with black knob/handle`; distinguish from the red-rim plate by gray coil rings and metal base. The winning front zone is semantically tied to the black knob/handle side, so first classify the knob/handle in RGB, then aim beside that side.
Bowl, wine bottle, cream cheese: distractors around the plate. Do not let wrist identity choose among them; wrist only confirms the already selected plate geometry.
Do not cache this run's absolute xyz. Use them only as counter-examples showing which bands failed and which semantic side won.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_swap_t5_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_swap_t5.json`.
