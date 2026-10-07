---
id: task-family_libero_goal_swap_t2
scope: task-family
suite: libero_goal
regime: swap
task_id: 2
task_language: Put the wine bottle on the top of the drawer
evidence:
  cells:
  - goal_swap_t2_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Place a tall bottle onto a swapped drawer/cabinet top surface. The task tests visual fixture re-localization under swap: the destination is the dark drawer top, not the nearby slatted wine rack or stove.


## Re-localization per scene
Wine bottle: look for the single dark green bottle with a tan cap. Agentview cap or upper-edge pixels may back-project to table depth; use visible bottle-body pixels and confirm in wrist after pre-position. In this run, table-biased samples at rows 430 and 450 were rejected and the lower body sample near (470,505) was used; do not cache these absolute pixels or xyz.
Drawer top: look for the dark flat horizontal cabinet/drawer top above the handles, adjacent to the slatted rack. Back-project multiple top-surface pixels and take the middle of the span. Reject slatted rack wood strips and vertical handle pixels; they are not the placement surface. This run used a center near the middle of three top samples, but absolute coordinates must not be reused.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/goal_swap_t2_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_goal_swap_t2.json`.
