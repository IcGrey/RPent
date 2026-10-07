---
id: task-family_libero_object_task_t4
scope: task-family
suite: libero_object
regime: task
task_id: 4
task_language: Pick the milk and place it in the basket
evidence:
  cells:
  - object_task_t4_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Single grocery carton into a woven basket in the low object-table frame. The task tests semantic selection of the milk carton, basket-cavity localization, and controlled insertion past a flexible/rimmed container edge.


## Re-localization per scene
Milk: in agentview_high, choose the red-and-white rectangular Dairy Fresh Milk carton, not the blue cream cheese box or orange sauce bottles. Good manual pixels are on the carton face/top away from thin edges; this run used examples near `[410,420]`, `[450,425]`, `[500,415]` only as counter-examples, not reusable coordinates. Wrist can confirm the same carton after moving above the agentview anchor; do not let the wrist choose a different grocery item.
Basket cavity: identify the white-lined woven basket semantically in agentview_high. Use pixels/regions on the visible open interior and liner, but expect rim bias. Wrist confirmation during carry is useful because the open liner fills the wrist view. This run's absolute basket points must not be cached; use them only as evidence that rim/liner projections can differ by several cm.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/object_task_t4_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_object_task_t4.json`.
