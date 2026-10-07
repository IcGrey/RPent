---
id: task-family_libero10_task_t0
scope: task-family
suite: libero10
regime: task
task_id: 0
task_language: put both the cream cheese and the tomato sauce in the basket
evidence:
  cells:
  - 10_task_t0_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Two-groceries-into-basket. Grab two named items (a flat BOX = cream cheese,
a CAN = tomato sauce) from a cluttered tabletop of look-alike grocery items and
drop both into an open woven basket. The real difficulty is IDENTITY, not
physics: the scene contains distractors (ketchup bottle, milk carton, OJ,
butter, a second can = alphabet soup) and SAM3 cannot tell the two cans apart.


## Re-localization per scene
- cream_cheese: agentview hi-res, blue/white box with cursive "Cream Cheese";
  eye. Distinguish from butter (red "FARM FRESH BUTTER" box) and milk carton.
- tomato_sauce: a CAN with a red/tomato label. SAM3 brand nouns unreliable and
  collide with the other can — pick by RGB label colour + tomato imagery. The
  OTHER can (blue label) is alphabet_soup; reject it.
  liner pixels / region-mode midpoint for the true cavity center. Basket sits at
  robot-left (+y, image-right), partly clipped at frame edge.
- This run's absolute xyz must NOT be cached; listed above only as counter-examples.


## Current exploration continuation
Before executing, read `/data/gc02/RPent/memory/libero-vla-place-guard-explore-20261007/_internal/inbox/10_task_t0_s0/wip/continuation-context.txt` and any existing `notes.md` there. Retain prior failed-attempt evidence; continue exploring VLA placement rather than repeating known failed handoffs.

## Pre-placement memory and VLA handoff
Read the curated pre-placement reference linked below. Reuse historical identification, grasp prompts, grip thresholds, orientation and collision-clearance technique; re-localize every target. Historical coordinates describe the old scene, NOT executable coordinates for this scene. These are excerpts of a historically solved trajectory, not independently validated grasp controllers or a guarantee every intermediate pick succeeded.

After EACH pickup, inspect current agentview/wrist and gripper state to confirm the intended payload is retained. Move with the full payload clear of obstacles, maintaining a stable grasp. Stop the scripted carry at a visible PRE-CONTACT pose above the support or in front of the container opening: payload, not just EEF, must clear rim/dividers, and must be aligned with the intended target using its current gripper offset. If the reference ends before such a pose, plan a new clearance-preserving carry; do not restore the missing historical final descent.

At that verified handoff call pi0_place with holding_confirmed=true and a single-object target instruction. VLA owns final centering, descent, insertion and release. Do not script those first. Existing guarded fallback and post-release stability checks remain in force. After one object's stable placement, re-observe before using the next object's grasp excerpt. Multi-object order is a historical reference, not a requirement if it creates collision risk. Contact-only fixture operations are separate subtasks, not object placement.

Curated reference: `task-family/preplacement_10_task_t0.json`.
