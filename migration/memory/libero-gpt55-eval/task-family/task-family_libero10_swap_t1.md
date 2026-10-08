---
id: task-family_libero10_swap_t1
scope: task-family
suite: libero10
regime: swap
task_id: 1
task_language: put both the cream cheese box and the butter in the basket
evidence:
  cells:
  - 10_swap_t1_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two named BOXES (cream_cheese "Cream Cheese / Fresh Taste" blue-oval box, butter
"FARM FRESH BUTTER" red box) must both go into a table-right basket, among 4
distractor groceries (alphabet_soup can, tomato_sauce can, ketchup bottle, milk
carton, OJ carton). LIVING_ROOM frame. Tests brand-noun disambiguation (SAM3 and
Pi0 grounding both fail on the brand) and multi-object basket placement. Because
both items are BOXES, placement is far easier than the sibling 2-CAN task (t0).

## Winning technique
1. Identify each target by RGB label in agentview hi-res + wrist confirm. Do NOT
   trust SAM3 (scores ~0.03-0.12 on the brand nouns).
2. Butter first (cleaner target): pre-position eef over the wrist-verified box at
   z~0.56; pi0_pick "pick up the butter box" max_chunks=12; success = peak_lift
   >0.05 AND gripper opening ~0.04 (holding, not 0=air); set_gripper +1 steps 8.
3. Lift to z~0.63, carry to basket via a y-waypoint (never Δy>0.30/move), center
   over the cavity, descend to ~0.54, release, retreat straight up. Verify butter
   sitting in basket in agentview.
4. Cream cheese second: traverse back via waypoints, wrist-confirm the "Cream
   Cheese" box behind the OJ carton, pre-position over it z~0.56, pi0_pick "pick
   up the cream cheese box" max_chunks=12, firm grip.
5. Carry over the basket's OPEN area (offset from the placed butter), descend
   until OSC stalls (box resting on butter is fine), release. Predicate fires.
   Success criterion: libero_terminated becomes true at the second release.

## Magic numbers
- pi0_pick max_chunks=12 (band 10-14), lift_thresh=0.05. Both boxes grasp on the
  first pi0_pick from a pre-positioned pose.
- set_gripper +1 steps=8 to firm after each pick.
- pre-position z ~0.56; carry z 0.63-0.65 (clears all distractor tops <0.54).
- basket release descend target z~0.54 (empty) ; second box may stall high
  (~0.578, resting on first box) — release anyway, it still counts as In().
- step_clip 0.02-0.025. NEVER command Δxy>0.30 in one move_to (split via y=0).

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| agentview "butter top" region gave z~0.51 = reflective can lid, gripper landed over the tomato_sauce can | standing box next to a shiny can lid read at the same z; region captured the lid (A1, non-fatal) | move over the xy, look in WRIST; back_project the box from wrist (flat box top z~0.455), re-pre-position |
| SAM3 "cream cheese box"/"butter box" score <0.2, no world_xyz | brand-noun grounding unreliable | read the RGB label in the hi-res crop; pixel-pick + back_project manually |

## Re-localization per scene
- butter: RGB "FARM FRESH BUTTER" red/orange box with a cow; standing. Confused
  with tomato_sauce can lid in agentview z-scan — reject any candidate whose
  wrist view shows a round metal lid; keep only the box face. Score floor N/A
  (manual pick). ABSOLUTES here (x≈-0.06,y≈0.069) are per-scene; do NOT cache.
- cream_cheese: RGB blue "Cream Cheese / Fresh Taste" oval on white box; standing,
  tucked behind the OJ carton. Distinguish from OJ (orange) and milk (white/red).
  Per-scene (x≈-0.03,y≈-0.238); do NOT cache.
- basket: fabric-lined, shallow (liner surface z~0.51-0.55, no deep floor).
  Cavity center from liner pixels; re-derive per scene, movable.

## Fragility flags
- Butter-vs-can-lid confusion in the agentview z-scan is the one likely trap;
  ALWAYS wrist-confirm box identity before pi0_pick. Fallback: back_project the
  box face from the wrist camera to get the true flat-box surface z.

## Difficulty and reliability
- Solved in 1 attempt, no reset. Expected single-shot rate high (boxes are
  forgiving in the basket; unlike the 2-CAN sibling t0 which needs separated
  deep-floor placements and took 3 attempts). Main risk is target identification,
  not placement.

## Cross-refs
- [[box-vs-can-lid-wrist-disambiguation]]
- [[boxes-tolerate-stacking-in-basket]]
