---
id: task-family_libero_object_task_t9
scope: task-family
suite: libero_object
regime: task
task_id: 9
task_language: Pick the chocolate pudding and place it in the basket
evidence:
  cells:
  - object_task_t9_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- brand-label-over-segmentation
- high-drop-over-cavity
---


## Applicable pattern
Grocery-package into basket: choose the named packaged food by readable RGB label, use Pi0 only for the grasp, then script a closed-gripper carry over the basket liner and release from above the rim.

## Winning technique
Identify the chocolate pudding semantically in agentview_high: the small brown rectangular box with readable "Chocolate Pudding" text, near the basket and distinct from butter/OJ/bottles. Move above that agentview anchor and confirm in wrist that the same labeled box is centered under the gripper. Use `pi0_pick` with a short noun prompt, verify a nonzero gripper gap and visible held box, then carry with `gripper:+1` in staged waypoints to the basket cavity. Align the held box over the visible white liner, biasing slightly past the near/front rim, and release from the high-over-cavity band; this run terminated immediately on release.

## Magic numbers
`pi0_pick max_chunks=12` worked (usable band 10-16); avoid long task-language Pi0 runs that might continue into an unscripted place.
`lift_thresh=0.05` worked (default band 0.05-0.08 for box-like groceries).
`gripper_closed_thresh=0.06` worked; final opening about 0.0466 indicated a held box.
Low object-frame pre-pick hover `z=0.18` worked (band 0.17-0.20).
Closed-gripper carry/release `z=0.20` worked (band 0.19-0.21) for dropping a flat box into the basket.
Use `step_clip=0.006-0.012` during the basket approach; the final centering nudge used 0.006.
NEVER carry with omitted gripper or `gripper:-1`; that opens the gripper and drops the package.
NEVER cache this run's absolute xy; object and basket positions must be re-localized per scene.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | A1 solved on first attempt | keep the same identity-first, wrist-confirmed over-cavity release pattern |

## Re-localization per scene
Chocolate pudding: use agentview_high RGB label, small brown rectangular "Chocolate Pudding" box. It can be confused with other rectangular packages such as butter by geometry alone, so readable label and color are the identity authority. Manual pixels on the top/label are enough; reject edge/table pixels that back-project to table z or jump several cm from the candidate. This run saw a firm sample near x=-0.109, y=0.079, z=0.018, listed only as a counter-example to caching.
Basket cavity: use agentview_high to identify the woven basket with white fabric liner. Region back-project over the visible opening/liner gives a broad cavity band, but rim and liner folds bias the estimate; use wrist after carrying to confirm the held package is over the open liner. This run released around x=-0.054, y=0.256, z=0.201, listed only as a counter-example to caching.

## Fragility flags
Most likely break is rim bias at release: if the box is visually over the near lip, keep `gripper:+1` and nudge a few cm deeper into the liner before opening. If release does not terminate but the box is visibly inside, retreat open upward with a small `step_clip=0.008-0.012`; if it is perched, use a short capped closed-gripper seating push rather than repeated high drops.

## Difficulty and reliability
Converged in 1 attempt on seed 0. Expected single-shot rate is moderate to high when the pudding label is readable and the release is over the liner; residual risk is Pi0 edge-grasping the small box or releasing onto the basket rim.

## Cross-refs
[[brand-label-over-segmentation]] [[high-drop-over-cavity]] [[basket-insertion-open-retreat]]
