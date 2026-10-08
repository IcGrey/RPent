---
id: task-family_libero_object_task_t0
scope: task-family
suite: libero_object
regime: task
task_id: 0
task_language: Pick the cream cheese and place it in the basket
evidence:
  cells:
  - object_task_t0_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- high-drop-over-cavity
---


## Applicable pattern

Single grocery-box into basket on the low object-frame table. The task is mostly target identity plus avoiding the basket front rim during placement.

## Winning technique

Identify the cream cheese semantically in agentview as the small blue/white box; reject the nearby red/yellow butter box. Move above the cream-cheese xy at low-table pick height, confirm the same blue/white box in wrist view, then use `pi0_pick` only for the grasp. Firm the grip with `set_gripper +1`, carry at a higher over-basket z, aim over the basket liner rather than the front rim, and release from above the cavity so the box drops in.

Success criteria: gripper opening after pick is about 0.04 rather than fully closed, wrist shows the cream-cheese box held, and release from the high over-cavity pose immediately fires `terminated:true`.

## Magic numbers

Object-frame cream-cheese pre-pose z=0.17-0.18 (used 0.17/0.18).

`pi0_pick` prompt `pick up the cream cheese`, `max_chunks=20` (observed success in 8-9 chunks), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Firm with `set_gripper +1`, steps=8 (band 5-10).

Carry/place over basket at z=0.20 (band 0.19-0.21) and release high; do not descend into the rim at z~0.15 before release.

Winning over-cavity release eef was approximately x=-0.03, y=0.272, z=0.200 in this seed; do not cache those absolutes for other scenes.

Never carry with gripper -1; it opens and drops.

## Failure modes

| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| first manual target samples put wrist over tomato-sauce can | A1 sampled the wrong small object area in agentview; the box was partly occluded by the robot body | use the blue/white label as identity, check against the red/yellow butter decoy, and confirm in wrist before Pi0 |
| release leaves cream cheese perched across basket front rim | A1 descended/released around eef y~0.260, z~0.151, where the box contacted the near rim | carry to a deeper over-liner pose and release from z~0.20 so gravity drops it into the cavity |
| open-gripper pushes and `pi0_doubled` rotate the perched box but do not terminate | A1 recovery worked from a bad rim-perched state rather than preventing it | reset/redo cleanly with deeper high release; use pushes only as salvage, not the primary plan |

## Re-localization per scene

Cream cheese: in agentview, look for the small blue/white rectangular box with readable Cream Cheese label. It can be confused with the red/yellow butter box immediately to its right and with can-like back-projection samples if the robot body occludes the view. SAM prompt `the blue and white cream cheese box` scored low (~0.031) but returned a useful box around the target; manual pixel/back-project plus wrist confirmation was more reliable.

Basket: woven rectangular basket with white fabric liner. Agentview/back-project of a broad basket window is rim-biased and may include edge artifacts. Use agentview for semantic identity and wrist/visual alignment for the cavity: target the visible liner center/back-center, not the near woven rim.

This run's absolute coordinates are counter-examples only: cream-cheese xy around (-0.115, 0.057) and successful release near (-0.03, 0.272, 0.20) must not be reused without re-localizing.

## Fragility flags

Most fragile step is basket placement. If the box is still in hand and visually over the front lip, do not descend lower into the rim; move deeper over the liner and release high. If it already perches, recovery is possible but inefficient and did not solve in A1.

## Difficulty and reliability

Solved in 2 attempts. Expected single-shot rate is moderate if the high over-cavity release is used from the start; low front-rim drops are unreliable.

## Cross-refs

[[high-drop-over-cavity]]
