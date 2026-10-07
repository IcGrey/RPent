---
id: task-family_libero10_task_t3
scope: task-family
suite: libero10
regime: task
task_id: 3
task_language: put the bottle in the bottom drawer of the cabinet and close it
evidence:
  cells:
  - 10_task_t3_s0
  attempts: 73
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Place a tall bottle into a shallow bottom drawer and close it. The hard parts are a stochastic bottle grasp, avoiding handle wedges, orienting the long axis within the drawer footprint, crossing a yawed low-carry reach wall, and seating before closure.


## Re-localization per scene

- Bottle: agentview semantic authority is the single upright dark-green wine bottle with tan cork. Prompt fallback order: `wine bottle`, `dark green bottle with tan cork`, then a positive point on the body. Wrist refinement is accepted only within 3–5 cm of the agentview anchor. SAM score floor was not established because point/back-project localization was sufficient.
- Drawer cavity: identify the white floor bounded by the black cabinet sidewalls. Use several interior pixels and floor z, not the rim/handle centroid. Wrist region samples across the floor are useful for x-range and y-depth.
- Bottom handle: distinguish the lower handle by vertical image ordering; the open handle is toward robot/front and the cabinet body is toward +y. Wrist RGB can reveal the bar orientation, but the handle is not the bottle target.
- Cabinet body: use RGB fixture semantics; it determines close direction toward +y in this scene.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t3_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t3.json`.
