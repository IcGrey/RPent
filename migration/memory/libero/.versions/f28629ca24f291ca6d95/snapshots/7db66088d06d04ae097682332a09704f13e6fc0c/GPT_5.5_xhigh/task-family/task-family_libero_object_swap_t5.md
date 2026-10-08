---
id: task-family_libero_object_swap_t5
scope: task-family
suite: libero_object
regime: swap
task_id: 5
task_language: Pick the tomato sauce and place it in the basket
evidence:
  cells:
  - object_swap_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Object-frame grocery-to-basket task with visually similar packaged distractors. The task tests semantic ID of the tomato sauce can and basket-cavity placement under swapped layout.

## Winning technique
Identify the tomato sauce in agentview_high by label/shape/color before moving; it is the green/red cylindrical can, not the orange juice carton or milk carton. Localize it with either SAM3 phrase `the tomato sauce can` or manual pixels on the can body/top, approach above it in the low object frame, and use Pi0 only for the grasp with `pick up the tomato sauce can`.

After Pi0 lifts, judge the grasp from images and gripper gap rather than the `success` flag. In the winning run the flag was false because gripper opening was just above threshold, while the can was clearly held over the basket. Firm with `set_gripper +1`, keep gripper closed, center over the basket mouth, and descend into the cavity. The predicate fired during closed-gripper insertion before an explicit release.

## Magic numbers
`max_chunks=20` for tomato sauce Pi0 grasp (band 18-24). The heuristic may read false if `final_gripper_opening≈0.061` with threshold 0.06; inspect images before discarding the grasp.

Low object-frame approach height: `z=0.18` over the can (band 0.17-0.20).

Basket insertion target: `z=0.125` with closed gripper (band 0.12-0.15), `step_clip=0.012` (band 0.010-0.015).

Never carry with `gripper:-1`; hold `+1` after the pick.

Never let wrist semantics override agentview for sauce/carton/can identity; wrist is geometry only.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Pi0 pick reports `success:false` despite can visibly held | A1: final gripper opening 0.0616 was just above threshold 0.06 | Trust wrist/agentview evidence and nonzero held-object pose; firm grip and continue |

## Re-localization per scene
Tomato sauce: prompt `the tomato sauce can` worked with score 0.793 in agentview. It looks like a green/red cylindrical can and can be confused with orange juice carton colors or other can-like groceries; verify the mask overlays the cylinder at image-left and not a carton face. Do not cache this run's xyz `[-0.099,-0.2374,0.0639]`; it is only a counter-example for the swap layout.

Basket: prompt `the basket interior` worked with score 0.301 and highlighted the white liner. For geometry, prefer a region over the open cavity or wrist confirmation; rim masks are biased high and outward. Do not cache this run's cavity xyz; the successful insertion used the can already held at approximately basket-center xy.

## Fragility flags
The most fragile step is accepting/rejecting the Pi0 grasp when its heuristic is near threshold. If the can is visibly in the gripper with gap around 0.03-0.07, continue with `set_gripper +1`; if the original can location is not empty or the wrist shows no can, re-pre-position over the agentview-identified target and retry the prompt ladder.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot rate is good when tomato sauce identity is fixed from agentview before Pi0 and the basket insertion is vertical/centered. No unresolved mechanism remained in this run.

## Cross-refs

