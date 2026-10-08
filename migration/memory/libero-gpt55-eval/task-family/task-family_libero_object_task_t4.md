---
id: task-family_libero_object_task_t4
scope: task-family
suite: libero_object
regime: task
task_id: 4
task_language: Pick the milk and place it in the basket
evidence:
  cells:
  - object_task_t4_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- basket-insertion-open-retreat
---


## Applicable pattern
Single grocery carton into a woven basket in the low object-table frame. The task tests semantic selection of the milk carton, basket-cavity localization, and controlled insertion past a flexible/rimmed container edge.

## Winning technique
Identify the red-white Dairy Fresh Milk carton in agentview_high, localize multiple pixels on the carton for a coarse xy anchor, then move above it for wrist confirmation of the same target. Use Pi0 only for `pick up the milk`, stop after lift, and firm the gripper. Carry slowly with `gripper:+1` through staged waypoints toward the basket; do not sweep directly through nearby bottles. Place at the visible basket interior, not at the rim median. If the first release leaves the carton perched or tilted on the liner/rim, reclose on the carton at the current pose, make a short diagonal/downward correction deeper into the basket, release again, and retreat upward/open. In this run, termination fired during the open-gripper retreat after the carton settled.

## Magic numbers
`pi0_pick max_chunks=12` worked (usable band 8-16 for grasp-only milk; avoid long pick-and-place behavior).
`lift_thresh=0.05`, `gripper_closed_thresh=0.06` worked for the carton.
`set_gripper +1 steps=8` worked (band 5-10) after pick and for re-closing on a perched carton.
Carry z `0.20-0.22` in object frame worked for the milk carton.
Slow carry `step_clip=0.010-0.012` avoided losing the carton during the long y traverse.
Basket insertion waypoint around the perceived cavity with eef z `0.17` worked; final seating correction requested z `0.13` but contact stalled at z about `0.153`, which was enough.
NEVER carry with `gripper:-1`; it opens and drops the carton.
NEVER rely on the basket region median alone; it can be biased by rim/liner geometry.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| First release leaves milk tilted/perched and `terminated=false` | A1: carton still crossing basket lip/liner rather than fully inside | Reclose at current pose, perform a short diagonal/downward correction deeper into the basket, release again, then retreat open |
| Nearby salad dressing tipped during carry | A1: carry path passed close to clutter near the basket mouth | Keep the milk held, continue if target still controlled; on future seeds use a slightly higher/inside approach and staged waypoints that avoid non-target bottles |
| Termination absent immediately on release though object looks inside | A1: predicate fired only after gripper opened and began retreating/settling | Retreat upward with gripper open after release; do not keep squeezing or dragging the object |

## Re-localization per scene
Milk: in agentview_high, choose the red-and-white rectangular Dairy Fresh Milk carton, not the blue cream cheese box or orange sauce bottles. Good manual pixels are on the carton face/top away from thin edges; this run used examples near `[410,420]`, `[450,425]`, `[500,415]` only as counter-examples, not reusable coordinates. Wrist can confirm the same carton after moving above the agentview anchor; do not let the wrist choose a different grocery item.
Basket cavity: identify the white-lined woven basket semantically in agentview_high. Use pixels/regions on the visible open interior and liner, but expect rim bias. Wrist confirmation during carry is useful because the open liner fills the wrist view. This run's absolute basket points must not be cached; use them only as evidence that rim/liner projections can differ by several cm.

## Fragility flags
Most fragile step is insertion into the basket: a tall carton can bridge the near rim even when the eef xy is over the opening. Fallback is reclose plus a short deeper/downward seating correction, then release and retreat open.

## Difficulty and reliability
Solved in 1 attempt, with one in-episode placement correction. Expected single-shot rate is moderate if the carton is held firmly and basket insertion is corrected rather than treated as a new pick. No unsolved sub-goal remained in this seed.

## Cross-refs
[[basket-insertion-open-retreat]]
