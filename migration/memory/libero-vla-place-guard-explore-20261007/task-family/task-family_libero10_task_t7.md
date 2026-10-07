---
id: task-family_libero10_task_t7
scope: task-family
suite: libero10
regime: task
task_id: 7
task_language: put both the ketchup and the cream cheese box in the basket
evidence:
  cells:
  - vla-place-pilot-20261006/explore
  - vla-place-pilot-20261006/explore-r2
confidence: single-shot
related: []
---
## Applicable pattern
Two-items-into-basket (P1 task variant). Two NAMED targets — a tall ketchup
bottle and a flat cream-cheese box — must both end up inside the basket, while
two distractor cans (alphabet_soup, tomato_sauce) stay put. LIVING_ROOM frame
after release when the item is seated inside the interior.


## Re-localization per scene
- distractors alphabet_soup / tomato_sauce cans — do NOT move.
- This run's absolute xyz must NOT be cached; positions re-randomize per seed. Re-derive every coordinate.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t7_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t7.json`.
