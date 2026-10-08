---
id: task-family_libero10_swap_t0
scope: task-family
suite: libero10
regime: swap
task_id: 0
task_language: put both the alphabet soup and the tomato sauce in the basket
evidence:
  cells:
  - 10_swap_t0_s0
  attempts: 4
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two grocery CANS (alphabet soup + tomato sauce) both go into ONE small basket. The
grasps are easy and reliable; the ENTIRE difficulty is fitting BOTH cans so each
one's center stays inside the basket rim box. The basket interior floor is a
single-can pocket, so the second can cannot sit flat beside the first — it must be
wedged/leaned and, critically, kept from rolling out over the low front rim.

## Winning technique
1. Localize both cans from agentview hi-res. One can is usually isolated; the OTHER
   is often OCCLUDED behind the ketchup 'Fancy' bottle — crop the hi-res image and
   back-project its silver lid pixels to get xy (do NOT trust a single SAM3 mask;
   brand-noun prompts collapse both cans onto the visible one).
2. Pre-position eef directly over can #1, `pi0_pick` (max_chunks~14,
   gripper_closed_thresh 0.04). Success = peak_lift ~0.21m AND min_gripper_opening
   ~0.055-0.065 (= a can diameter, NOT grasped air). `set_gripper +1 steps5` to firm.
3. Carry over the basket interior at z~0.63; DESCEND until OSC stall. Stall at
   eef z~0.542 == can seated on FLOOR -> release. (A high stall ~0.62 means you are
   over a wall/rim, not the pocket — reposition in xy, do not release.) Retreat up.
4. Traverse to can #2 (split any |Δxy|>0.30 into a midpoint). Pre-position, `pi0_pick`,
   firm. When can #2 is behind the ketchup, a top-down grasp from directly above the
   can lid leaves the ketchup standing.
5. Carry can #2 HIGH (z~0.66) so it clears seated can #1. Now WEDGE it against a
   basket WALL right next to can #1, biased toward a CLOSED side (far +y or back -x),
   AWAY from the open +x front rim. Descend until stall (it will stall ~0.616 on
   can #1 / the wall), release there. Retreat STRAIGHT up.
6. The predicate fires on the next step once can #2 comes to rest with its center
   inside the rim box.

## Magic numbers
- pi0_pick: max_chunks=14 (band 12-16), gripper_closed_thresh=0.04. peak_lift ~0.21m.
- holding-a-can gripper opening: ~0.055-0.065 (never ~0.0 = air).
- set_gripper +1 steps=5 to firm (cans are laterally weak; keep steps<=5).
- descend step_clip=0.02; carry z=0.63 (can #1) / 0.66 (can #2, clears seated can #1).
- FLOOR-seat OSC stall eef z ~= 0.542 (this seed). Wall / on-can stall ~= 0.616-0.622.
  Treat any stall >~0.58 as "NOT floor" and reposition; do NOT cache the absolute z.
- NEVER release can #2 biased toward the open front rim (the +x side, rim ~x+0.075).
- NEVER command a single |Δxy|>0.30 move_to (OSC IK flip); split with a midpoint.

## Failure modes
| symptom | root cause (A<N>) | fix |
| can #1 released high over front rim toppled onto table beside basket | A1: released at eef z~0.584 over the rim, not seated | descend until OSC stall ~z0.542 (floor) BEFORE release |
| can #2 landed ON can #1 (stall ~0.581) then rolled to x0.100, OUTSIDE rim | A2: placed can #2 only ~3-4cm from can #1, biased toward the OPEN +x front rim | wedge can #2 against a CLOSED wall (far +y / back -x), biased AWAY from +x; release low |
| re-grasp of a settled upright can stalls on its flat top (~7cm gripper vs 6.5cm can) | A1/A2 | do NOT rely on re-grasp recovery; get each placement right first time |
| descend into basket stalls high (z~0.62) far above floor | A4 (recovered) | you are over a WALL/rim; reposition xy over the open pocket and re-descend |

## Re-localization per scene
- tomato_sauce can: RED/tomato + GREEN band label. SAM3 'tomato sauce can' or
  'soup can' scores ~0.85 and boxes it. Isolated/front-left this seed.
- alphabet_soup can: BLUE label, silver "Melissa & Doug" lid. Often OCCLUDED behind
  the ketchup 'Fancy' bottle. SAM3 brand nouns FAIL (collapse onto the other can);
  instead crop hi-res around the ketchup, find the blue can body + silver lid, and
  back-project lid pixels. Reject a candidate whose top z is table-level (that's the
  ketchup cap, ~z0.58 elevated but a different xy).
- basket cavity: fully visible OR clipped at the +y frame edge depending on seed.
  The +y interior can extend OFF-FRAME. Find the FLOOR pocket by descend-until-stall
  probing, not by trusting a segment centroid (rim/liner biased). Floor pocket is
  ~single-can sized. DO NOT cache this run's absolute xyz; re-derive per scene.

## Fragility flags
- MOST FRAGILE STEP: can #2 placement. There is effectively one shot (re-grasp of a
  settled can is a hard wall). If unsure, bias hard toward a closed wall and release
  from the lowest stall you can reach. Fallback: if it perches high on can #1, a
  closed-gripper downward nudge toward a closed wall may seat it (untested here).
- Occluded can identity: verify in the wrist that the lid centered under the gripper
  is a CAN lid (silver "Melissa & Doug"), not the ketchup cap, before pi0_pick.

## Difficulty and reliability
Solved on attempt 4 (2 prior agents failed on can #2 placement, 1 was mid-episode).
Grasps are ~single-shot reliable. The can #2 wedge is the gate: expect it to need
1-2 tries to find a contained wall. Expected single-shot rate: LOW-MEDIUM until the
"wedge-against-closed-wall, not on-can-toward-front-rim" rule is applied.

## Cross-refs
[[basket-two-cans-wedge-not-stack]]
[[basket-floor-is-single-can-pocket]]
