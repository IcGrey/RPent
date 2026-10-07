---
id: task-family_libero_goal_task_t6
scope: task-family
suite: libero_goal
regime: task
task_id: 6
task_language: put the wine bottle in the bowl
evidence:
  cells:
  - goal_task_t6_s0
  attempts: 3
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Place a tall wine bottle into an open bowl in the kitchen frame. The task is mainly about grasp-only Pi0 control and accounting for the large held-object offset: the gripper center does not need to be inside the bowl as long as the bottle body is released over the cavity.


## Re-localization per scene

Bottle: identify as the dark green wine bottle with tan cork/top. Agentview identity is reliable because it stands immediately below/near the bowl and differs from the blue cream-cheese box, plate, and stove. Sample pixels on the neck/body, not table gaps. Wrist refinement is accepted only near the agentview anchor.

Bowl: identify as the patterned black/white open bowl with yellow rim. Use RGB to reject the red-ring plate and gray stove burner. For the destination, sample interior floor/walls and use the cavity center; rim pixels bias the target outward. Wrist can confirm the open cavity once overhead.



## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_task_t6_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_task_t6.json`.
