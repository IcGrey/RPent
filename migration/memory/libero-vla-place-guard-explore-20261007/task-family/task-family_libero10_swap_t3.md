---
id: task-family_libero10_swap_t3
scope: task-family
suite: libero10
regime: swap
task_id: 3
task_language: put the black bowl in the bottom drawer of the cabinet and close it
evidence:
  cells:
  - 10_swap_t3_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick a bowl off the tabletop, place it into an already-OPEN bottom drawer, then
relocates the CABINET; the whole difficulty is (a) reaching into/around the
the drawer slides to close — it is NOT necessarily toward the robot.


## Re-localization per scene
- Bowl (akita_black_bowl): agentview hi-res, patterned bowl with a thin yellow rim;
  back_project 3-5 top-surface pixels, median xy. Grasp works from a ~7cm-above
  center. Floor-edge pixel is the CLOSING PROGRESS SIGNAL — watch its world z/xy.
- Cabinet body: find it in agentview; the drawer closes TOWARD it. This run: cabinet
  at image-left (-y), so close = push -y. DO NOT cache this sign; re-derive per seed.
- Absolute xyz from this run are counter-examples only, never cache them.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_swap_t3_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_swap_t3.json`.
