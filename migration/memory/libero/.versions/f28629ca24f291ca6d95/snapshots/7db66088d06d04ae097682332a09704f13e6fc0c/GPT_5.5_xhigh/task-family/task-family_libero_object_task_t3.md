---
id: task-family_libero_object_task_t3
scope: task-family
suite: libero_object
regime: task
task_id: 3
task_language: Pick the ketchup and place it in the basket
evidence:
  cells:
  - object_task_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- high-drop-over-cavity
- brand-label-over-segmentation
---


## Applicable pattern
Single tall labeled grocery bottle into a soft/rimmed basket in the low object-table frame. The task tests brand/label identity among similar condiment bottles and cavity-centered placement.

## Winning technique
Use agentview_high.png as identity authority: choose the orange tomato ketchup bottle, not the BBQ sauce or salad dressing. Segment or point-prompt the ketchup for coarse xy, move above that same anchor, and verify in wrist before Pi0 grasp. Use Pi0 only for the grasp, then clamp and carry with gripper +1 over the basket interior. A high over-cavity release can terminate even if a lower z command stalls above the liner, provided the bottle is centered inside the opening.

Winning sequence here: `move_to` above ketchup at low-frame z around 0.18, `pi0_pick("pick up the ketchup", max_chunks=20, lift_thresh=0.08)`, judge grasp manually from gripper gap and images, `set_gripper +1` for 8 steps, `move_to` over basket cavity at z around 0.25 with slow step_clip, optional gentle descent, then `release`.

## Magic numbers
Ketchup segmentation: prompt `the tomato ketchup bottle`, score 0.816 here; accept only when overlay is on the orange bottle with Tomato Ketchup label.
Basket segmentation: prompt `the basket interior`, score 0.231 here; low score is usable if overlay covers the white liner/cavity, but reject rim-only masks.
Low object-table frame: initial eef z about 0.26; carry/place over basket at z=0.24-0.27 worked.
Pi0 grasp: `max_chunks=20` (band 16-24), `lift_thresh=0.08` (band 0.05-0.08 for tall bottles), `gripper_closed_thresh=0.06`.
Firm grip: `set_gripper +1`, 8 steps (band 5-12).
Carry: `gripper:+1` throughout, `step_clip=0.015` (band 0.012-0.02) for tall bottle stability.
Never rely on `pi0_pick.success` alone: this run reported false despite a real grasp.
Never use basket rim pixels as the place target; center the visible white liner/cavity.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | A1 solved | Keep agentview label identity, wrist visual confirmation, high over-cavity release. |

## Re-localization per scene
Ketchup: identify by readable orange/red Tomato Ketchup label and gray cap in agentview_high.png. It can be confused with BBQ sauce because both are condiment-shaped; reject masks on the lower orange BBQ bottle or green-capped salad dressing. Prompt `the tomato ketchup bottle` worked; fallback is manual point prompting on the readable label or cap/body pixels.
Basket cavity: identify the woven basket with white cloth liner. Use `the basket interior` and verify overlay covers the inner liner, not just the rim. If mask centroid is rim-biased, use the visible cavity center from wrist/agentview and bias inward from front/side walls.
This run's absolute xyz values are counter-examples only and must not be cached: ketchup segment [-0.1326, 0.0587, 0.0705], basket-interior segment [-0.0513, 0.2744, 0.1102], release eef about [-0.0405, 0.2522, 0.2594].

## Fragility flags
Most fragile step is placement over the basket: a rim-biased target can leave the bottle perched. Fallback is to re-localize the cavity from the wrist and use a high over-cavity release; if it perches and predicate is false, use the existing rim-perch contact-seat strategy.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot rate is good if label identity is verified before picking and release is over the interior cavity. The Pi0 success flag was misleading, so manual grasp verification remains required.

## Cross-refs
[[high-drop-over-cavity]] [[brand-label-over-segmentation]]
