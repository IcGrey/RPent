---
id: task-family_libero_object_swap_t1
scope: task-family
suite: libero_object
regime: swap
task_id: 1
task_language: Pick the cream cheese and place it in the basket
evidence:
  cells:
  - object_swap_t1_s0
  attempts: 7
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- high-drop-over-cavity
---


## Applicable pattern
Pick a flat blue-white cream-cheese box among similar groceries and put it into a white-lined woven basket in the low object frame. The hard part is not the grasp; it is rejecting rim-biased basket coordinates and entering over the true liner center.

## Winning technique
Identify the cream cheese from agentview RGB as the small blue-white rectangular box labeled Cream Cheese, then sample several top/face pixels for xy. Move above the basket first and use wrist RGB/depth to locate the visible white liner center, not the exterior woven wall or near rim. Pick from a pre-position above the cream cheese with `pi0_pick("pick up the cream cheese")`; verify gripper opening around 0.04 and wrist view of the held box. Carry with `gripper:1` through central high waypoints, then descend with the held box over the wrist-confirmed liner center. In the solved run the predicate fired during closed-gripper descent before any `release`.

## Magic numbers
Cream-cheese pre-position z: `0.16` in the object frame (usable band `0.15-0.17`).
Pi0 pick: `max_chunks=20` (band `12-20`), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.
Good grasp evidence: final gripper opening about `0.043` (usable band `0.04-0.05`) plus wrist image of the held blue-white box.
Carry z: `0.19-0.21`; use `0.21` when crossing clutter and `0.19` near the basket.
Basket insertion target: wrist-confirmed liner center, observed here near `x≈-0.01,y≈0.258`; do not cache this absolute coordinate across seeds.
Final descent: closed gripper, `step_clip=0.006` (band `0.004-0.008`), target z `0.125` (final eef stalled/terminated around `0.137`).
NEVER use the far outside-lip target around `x≈-0.28,y≈0.27-0.31` for this scene; it repeatedly perched the box outside.
NEVER keep pushing from the outside-lip state as the main plan; it did not seat the box in A4 or A6.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| box released outside/on the right basket lip | basket target was rim/edge biased (A1) | move over the basket and refine the liner center with wrist before carrying |
| upright box tucked under/near basket lip after deeper low release | still approached from the outside-lip geometry (A2) | change the entry side/center, not only z or y |
| high carry to far `+y/-x` target still perches | target remained outside the true cavity (A3) | use wrist-centered liner xy instead of far-left/far-out xy |
| yaw rotation plus Pi0 push did not seat | orientation change did not alter the actual broad-face contact enough from the lip state (A4) | avoid creating the lip state; insert while still held |
| pitch tilt bumped clutter and still released outside | tilt did not compensate for wrong basket target and added collision risk (A5) | carry centrally over the open liner and keep object upright |
| slow open-gripper scripted pushes failed | pushes began after a bad lip placement and did not move the box into the liner (A6) | solve earlier by descending held object over basket center |

## Re-localization per scene
Cream cheese: use agentview RGB, not segmentation alone. It is the small blue-white flat rectangular package with a blue oval label; it can be confused with butter if looking only for a small box, but butter has red/yellow/black Farm Fresh labeling. Sample firm pixels on the top/visible face; reject edge pixels that return table z or jump outside the package.
Basket: use agentview to identify the white-lined woven container, then move above it and use wrist view for geometry. The white liner center is the placement target; exterior woven wall, rim fold, and front/right lip are distractors. Use a wrist region over the open white liner and reject estimates that land on the far outside wall or near rim.
Milk/orange juice/cans: treat as clutter during the carry. The first carry leg can graze cartons if too low or too centered; lift to `0.19-0.21` and use central waypoints that do not drag the held box across them.
This run's absolute coordinates are counter-examples only; swap seeds must re-localize every object and the basket center.

## Fragility flags
Most fragile step: basket localization. If the visible target is near the woven wall or rim, re-observe from wrist above the basket and aim for the liner center.
Second fragility: early carry over clutter. If the held box contacts milk or orange juice, raise the next waypoint and move more centrally before approaching the basket.
Fallback: if a release/placement leaves the box visibly inside but non-terminal, use the existing basket retreat memories; if it is visibly outside/on the lip, reset or re-pick rather than repeating outside pushes.

## Difficulty and reliability
Solved on attempt 7 after six failed placement-geometry attempts. Expected single-shot rate is good if the wrist-centered basket entry is used, because the grasp was reliable across all attempts. Remaining uncertainty: whether other swap seeds move the basket center close enough to a workspace edge to require a different over-basket approach side.

## Cross-refs
[[high-drop-over-cavity]]
