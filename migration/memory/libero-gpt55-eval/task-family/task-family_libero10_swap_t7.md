---
id: task-family_libero10_swap_t7
scope: task-family
suite: libero10
regime: swap
task_id: 7
task_language: put both the alphabet soup and the cream cheese box in the basket
evidence:
  cells:
  - 10_swap_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two-target pick-and-place into ONE basket. The test is (a) DISAMBIGUATION — one of
the two cans (alphabet soup) is a target, the other (tomato sauce) is a distractor,
plus a ketchup bottle; and (b) sequencing two placements into the same container.
Under `_swap` the object positions are re-randomized per seed, so re-derive every xyz.

## Winning technique
Do the BOX first, then the CAN (order not critical here — basket is large — but box
first keeps the interior clear).
1. Identify targets in agentview hi-res BEFORE touching anything: crop each can and
   read the label. Alphabet soup = BLUE label "AL..SO.."; tomato sauce = RED/GREEN
   label with tomato pictures (distractor). Cream cheese = blue rectangular box.
   Success criterion: you can name each object from the RGB crop, not from `_1` names.
2. back_project 3+ pixels on each target + basket interior; median the xy.
3. Cream cheese box: pre-position eef directly over box (~z0.60), `pi0_pick "pick up
   the cream cheese box"` max_chunks16. Success = gripper opening ~0.04 + lift >0.05m.
   `set_gripper +1 steps8` to firm.
4. Carry to basket via a mid waypoint at carry z (~0.62), holding gripper +1 the whole
   way. Descend into cavity with step_clip 0.02; it STALLS on the floor (~z0.58 here).
   `release`; retreat straight up. Box should be gone from the table (occluded by rim
   in agentview = in basket).
5. Alphabet soup can: go to can via a mid waypoint, pre-position over it, `pi0_pick
   "pick up the alphabet soup can"`. NOTE Pi0 auto-carries the can toward +y (its
   trained place = robot-left = the basket) — this HELPS here. success flag may read
   FALSE even on a good grasp; judge by gripper opening (~0.06 = can held) + wrist cam.
   `set_gripper +1 steps5` (short, can is laterally weak).
6. Move the can over the basket cavity (~(0.05,0.18,0.58)) holding gripper +1. The
   In-basket predicate fires as soon as the can CENTER is inside the rim box — it fired
   here mid-descent WITH THE CAN STILL GRIPPED, before any release was needed.

## Magic numbers
- pre_pos_z over table objects = 0.60 (band 0.58-0.62); carry_z = 0.62 (band 0.60-0.63).
- pi0_pick max_chunks = 16 (band 12-20) for both grasps.
- set_gripper firm: box steps=8, can steps=5 (short for laterally-weak can).
- descend into basket step_clip = 0.02; floor stall z ~0.58 this scene (do NOT cache).
- release z into basket ~0.58; basket rim z ~0.548.
- NEVER command single-move Δy > 0.30 — split box->basket (Δy~0.41) and can->basket into waypoints.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| (none — solved on attempt 1) | — | — |
| POTENTIAL: grabbing the tomato-sauce can | look-alike can, brand-blind | ID by label crop in agentview hi-res before picking; alphabet soup=blue label |
| POTENTIAL: pi0_pick "success:false" read as a miss | success flag heuristic unreliable for cans | judge grasp by gripper qpos (~0.06 held) + wrist cam, per Rule 1b |

## Re-localization per scene
- alphabet_soup: agentview hi-res, BLUE label can, prompt/crop-read "alphabet soup".
  Confused with tomato_sauce (red/green tomatoes) — reject the red-label can. Score
  floors on brand nouns are low; identify by colour+label, not SAM3 brand score.
- cream_cheese: blue rectangular box, distinct shape (only box on table).
- basket: woven basket, silver cloth liner; interior center via region back_project;
  rim is z-biased so use interior pixels. Absolutes here (box(0.094,-0.20),
  can(-0.154,-0.142), basket(0.04,0.21)) are THIS scene only — do NOT cache.

## Fragility flags
- Most fragile step: correctly identifying alphabet soup vs tomato sauce. A wrong
  first grab is expensive. Mitigation: label-read crops up front.
- Second fragile: Pi0 auto-carry on the can can end at an off-center basket spot; firm
  grip and re-center over the cavity before descending.

## Difficulty and reliability
Solved in 1 attempt, 13 primitives. Expected single-shot rate high IF disambiguation is
done up front. Nothing left unsolved.

## Cross-refs
[[basket-two-cans-wedge-not-stack]] [[probe-container-floor-by-stall-height]]
[[pi0-pick-autocarries-to-trained-place]]
