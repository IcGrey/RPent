---
id: task-family_libero10_task_t7
scope: task-family
suite: libero10
regime: task
task_id: 7
task_language: put both the ketchup and the cream cheese box in the basket
evidence:
  cells:
  - 10_task_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two-items-into-basket (P1 task variant). Two NAMED targets — a tall ketchup
bottle and a flat cream-cheese box — must both end up inside the basket, while
two distractor cans (alphabet_soup, tomato_sauce) stay put. LIVING_ROOM frame
(eef home z~0.68, table top ~0.43). The basket In() predicate fires on settle
after release when the item is seated inside the interior.

## Winning technique
1. Localize all 5 entities in agentview hi-res first (identity), back_project 1-3
   pixels each. Basket interior x is noisy (reflective fabric) — trust y (~0.21)
   and use interior, not rim.
2. Place the BOX first (empty basket, easy target), then the BOTTLE.
3. Box: pre-pos above at eef z~0.58; `pi0_pick "pick up the cream cheese box"`
   max_chunks~16. Success = lift>0.05 AND gripper opening ~0.02-0.05.
   `set_gripper +1` to firm. Carry at z~0.62 to over interior; descend
   (step_clip 0.02) until OSC stalls ~0.58; `release`.
4. Bottle: split the y-traversal if |Δy|>0.30 via a mid waypoint at carry z.
   Pre-pos above bottle at eef z~0.60; `pi0_pick "pick up the ketchup bottle"`
   max_chunks~18. Pi0 may report success:false yet grasp+carry the bottle to the
   basket — JUDGE BY gripper opening (~0.03 = holding) + wrist cam, not the flag.
   `set_gripper +1`, center over interior (z~0.66), descend (z~0.60, step_clip
   0.02) until stall ~0.625, `release` -> predicate fires.

## Magic numbers
- pre_pos_z box 0.58, bottle 0.60 (band 0.56-0.62)
- carry_z 0.62 (band 0.60-0.66)
- basket descend target 0.57-0.60; OSC stalls ~0.58-0.63 with item inside — expected, do NOT chase target z
- pi0_pick max_chunks: box 16, bottle 18 (band 14-20)
- step_clip 0.02 for basket descend; move_to y single-step <=0.30 (split traversal)
- NEVER carry with gripper -1 (drops item); hold +1 the whole way

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| (none — solved A1) | — | box-first ordering, harnessed Pi0 carry for the bottle |

## Re-localization per scene
- ketchup: red bottle, "Tomato Ketchup" front label; tall (top z~0.54). agentview hi-res label read reliable; wrist for depth only.
- cream cheese box: small blue/white "Cream Cheese" box; flat, top z~0.48.
- basket: woven rim + white fabric lining, right side of table. Interior x from back_project is noisy/rim-biased; use interior center by eye + y median (~0.21). rim top z~0.577.
- distractors alphabet_soup / tomato_sauce cans — do NOT move.
- This run's absolute xyz must NOT be cached; positions re-randomize per seed. Re-derive every coordinate.

## Fragility flags
- Bottle pi0_pick returning success:false while actually holding+carrying is the
  one thing most likely to confuse a future agent. Confirm the hold via
  gripper_qpos opening (~0.03) and wrist/agentview before treating it as a miss;
  do NOT re-issue pi0_pick blindly (you'd drop the held bottle).

## Difficulty and reliability
Solved single-attempt (A1). Expected single-shot rate high for this cell given
clean, well-separated targets and an empty basket. No unsolved residue.

## Cross-refs
[[pi0-pick-carries-past-lift-judge-by-grip]]
