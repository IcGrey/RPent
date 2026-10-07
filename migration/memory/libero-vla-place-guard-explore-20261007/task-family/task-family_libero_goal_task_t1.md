---
id: task-family_libero_goal_task_t1
scope: task-family
suite: libero_goal
regime: task
task_id: 1
task_language: Put the plate on the stove
evidence:
  cells:
  - goal_task_t1_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Move a flat ceramic plate onto a visually similar gray circular stove cook region. The core issue is semantic surface classification plus compensating the large offset caused by Pi0 rim-grasping a thin plate.


## Re-localization per scene



Wrist refinement: useful for plate geometry before grasp because the plate fills the wrist view. For the stove, agentview RGB is the semantic authority; wrist is useful only after carrying near the stove to judge overlap between held plate footprint and burner.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_task_t1_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_task_t1.json`.
