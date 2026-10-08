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

## Winning technique
Order: BOX first (stable footprint), then CAN.
1. pi0_pick "pick up the cream cheese" from home (max_chunks ~18). Success =
   peak_lift > 0.08 and gripper opening ~0.04 (holding). Confirm with wrist cam:
   the "Cream" box should be raised in the gripper.
2. set_gripper +1 (steps 8) to firm.
3. Carry to basket in waypoints, gripper HELD +1 the whole way (Δy>0.30 must be
   split): high waypoint at carry z~0.62, then over cavity, then descend. OSC
   stalls when the box bottoms on the basket floor (~z 0.58) — that stall IS the
   seat signal.
4. release, then retreat STRAIGHT UP (gripper -1).
5. Pre-position over the can (~15cm above, carry z), verify with wrist that the
   red/tomato-label can is centered under the gripper.
6. pi0_pick "pick up the tomato sauce can". Note: pi0 frequently grasps AND
   carries the can toward its trained "left" (+y) — which here lands right over
   the basket. If it does, just firm/settle it inside; you may not need a manual
   carry.
7. set_gripper +1 (steps 5) or a short descend+release inside the cavity. The
   In(basket) predicate fires as soon as BOTH objects are within the basket
   region — it fired here while the can was still lightly held over the cavity.

## Magic numbers
- pi0_pick max_chunks=18 box / 16 can (band 14-20).
- Box grasp: gripper opening ~0.04 held. Can: opening ~0.06-0.07 = holding a can
  (do NOT read >0.06 as "grasped air" for a can — that is the can diameter).
- set_gripper firm: box steps=8; CAN steps<=5 (avoid squeeze-slip).
- Carry z ~0.62; basket liner floor z ~0.52-0.58; box seats when OSC stalls ~0.58.
- Basket cavity center this scene ~[0.05, 0.23] (DO NOT cache — re-derive).
- step_clip default 0.02-0.025 fine for box; single-step xy <0.30.

## Failure modes
| symptom | root cause (A/N) | fix |
|---|---|---|
| SAM3 "tomato sauce" and "alphabet soup" BOTH return the same can | brand-noun grounding is unreliable | disambiguate cans in RGB: tomato_sauce = red/tomato label; alphabet_soup = blue label. Do not trust SAM3 identity for cans. |
| (anticipated) pi0 dumps held can at trained "left"/IK edge | pi0 pick-and-place training | keep max_chunks<=16; here the "left" happened to be the basket so it helped, but verify where it drops |

## Re-localization per scene
- cream_cheese: agentview hi-res, blue/white box with cursive "Cream Cheese";
  SAM3 "cream cheese box" scored low (~0.23) but box location matched — verify by
  eye. Distinguish from butter (red "FARM FRESH BUTTER" box) and milk carton.
- tomato_sauce: a CAN with a red/tomato label. SAM3 brand nouns unreliable and
  collide with the other can — pick by RGB label colour + tomato imagery. The
  OTHER can (blue label) is alphabet_soup; reject it.
- basket: SAM3 "basket" reliable (~0.7); centroid is rim-biased. Use interior
  liner pixels / region-mode midpoint for the true cavity center. Basket sits at
  robot-left (+y, image-right), partly clipped at frame edge.
- This run's absolute xyz must NOT be cached; listed above only as counter-examples.

## Fragility flags
- Can identity is the single most fragile step. A wrong first grab (grabbing
  alphabet soup) is unrecoverable-ish. Always confirm the can label in the wrist
  cam before pi0_pick.
- Box placement: descend until OSC stalls on the floor before releasing; a
  high release can bounce the box out or perch it on the rim.

## Difficulty and reliability
Solved in 1 attempt, no resets. Expected high single-shot rate IF can identity is
resolved from RGB up front. The pi0 "carry to left = basket" behaviour was a
lucky assist and should not be relied on across seeds where the basket sits
elsewhere.

## Cross-refs
[[pi0-pick-may-place-at-trained-left]]
[[sam3-brand-noun-can-collision]]
