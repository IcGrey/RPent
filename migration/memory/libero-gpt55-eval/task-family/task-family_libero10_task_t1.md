---
id: task-family_libero10_task_t1
scope: task-family
suite: libero10
regime: task
task_id: 1
task_language: put both the alphabet soup and the butter in the basket
evidence:
  cells:
  - 10_task_t1_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two-items-into-a-lined-basket. Pick two distinct table groceries (a can + a box)
and place BOTH inside a woven basket that has a tall soft cloth liner standing
above its rim. Predicate = In(soup,basket) AND In(butter,basket); it fires when
the second item enters the basket volume (fired on descent, no explicit release
needed for the final item). The real difficulty is NOT the grasps (both easy) —
it is not disturbing the basket between the two placements.

## Winning technique
1. Localize all three entities from agentview hi-res back_project (see re-localization).
2. Pick the CAN FIRST (it is the item far from the basket): pre-position eef ~15cm
   above the can top, verify via wrist it sits between the fingers, then
   `pi0_pick "pick up the can"`. Success criterion: agentview shows the can lifted
   into the gripper and its table spot empty (the pi0 success flag may be FALSE for
   a good can grasp — ignore it, judge visually).
3. `set_gripper +1 steps 5` (cans are laterally weak — do not over-firm).
4. Carry at HIGH z (~0.72) to the basket interior center; descend to eef z~0.57
   (OSC stalls ~0.58 on floor contact); `release`.
5. Retreat STRAIGHT UP to eef z>=0.72 with NO lateral motion. (This is the crux.)
6. Pick the BOX LAST: pre-position over it, `pi0_pick "pick up the butter box"`,
   `set_gripper +1 steps 8`, lift straight up, carry high to the basket offset
   ~+0.02 in y from the first item, descend to eef z~0.56 -> predicate fires.

## Magic numbers
- carry/traverse z = 0.72 (band 0.70-0.74) — keeps finger tips above the liner.
- retreat-up z after a basket release = 0.74 (>=0.72 REQUIRED).
- descend-into-basket eef z = 0.56-0.58 (OSC stalls ~0.58 on floor).
- basket rim top z ~0.52-0.54; liner stands above it.
- pi0_pick can: max_chunks=14 (band 12-16), lift_thresh=0.05.
- pi0_pick box: max_chunks=12 (band 10-14), lift_thresh=0.05.
- set_gripper firm: can steps=5, box steps=8.
- 2nd-item place offset ~+0.02 y from 1st item (keeps both inside, no perch).
- NEVER traverse laterally at eef z<=0.62 within ~10cm of the basket — fingers snag the liner.

## Failure modes
| symptom | root cause (A#) | fix |
|---|---|---|
| basket dragged then lifted off table, dangling from gripper, OSC can't set it down | A1: after placing item 1, retreated only to z=0.62 then moved LATERALLY toward item 2; open finger tips (~8-10cm below eef) at eef z0.62 sit at rim/liner height (~0.52) and hooked the tall cloth liner | retreat STRAIGHT UP to z>=0.72 before any lateral move; and order items so the final action is a place (no post-basket traverse) |
| pi0_pick reports success:false on the can | opening 0.0625 > gripper_closed_thresh 0.06 (can is ~6cm) | ignore the flag; confirm grasp from agentview (can raised, spot empty) |

## Re-localization per scene
- alphabet_soup: blue can with silver lid, "AL"/sunflower art, sits behind the
  orange-juice carton on the LEFT. Confuser: the tomato_sauce can (red/green,
  oranges) elsewhere on the table — do NOT grab that one. Prompt for pi0 by
  position (pre-position over it), not by brand. SAM prompt "the blue can" ok.
- butter: red/white "FARM FRESH BUTTER" box, standing upright, center. pi0_pick
  "pick up the butter box" grasps it top-down cleanly.
- basket: woven, on the RIGHT, partly off the right frame edge (segment box
  clipped at col 1024) -> its true center is slightly more +y than the visible
  median; interior center ~(0.02,0.23) worked. Tall soft white liner above rim.
- THIS RUN'S ABSOLUTE XYZ ARE COUNTER-EXAMPLES ONLY — re-derive every coordinate
  from the current scene's back_project.

## Fragility flags
- The between-placements retreat is the one step that breaks the task (A1 cascade).
  Fallback if a lateral move must happen low: keep gripper CLOSED (+1) so fingers
  are narrow, or route the traverse well away (>15cm) from the basket.
- If the 2nd item lands perched on the 1st and the predicate won't fire, nudge it
  a few cm in y off the first item and re-release.

## Difficulty and reliability
Converged in 2 attempts; A1 lost purely to the liner-snag retreat error, A2 clean.
Expected single-shot rate high IF the retreat-high + place-last discipline is
followed from the start. Both grasps are reliable (box top-down, can from a
verified pre-position).

## Cross-refs
- [[retreat-high-before-lateral-near-lined-basket]]
