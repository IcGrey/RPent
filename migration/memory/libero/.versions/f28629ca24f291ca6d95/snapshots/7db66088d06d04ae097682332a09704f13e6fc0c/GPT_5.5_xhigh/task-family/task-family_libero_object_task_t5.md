---
id: task-family_libero_object_task_t5
scope: task-family
suite: libero_object
regime: task
task_id: 5
task_language: Pick the bbq sauce and place it in the basket
evidence:
  cells:
  - object_task_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- high-drop-over-cavity
- near-target-repick
- basket-insertion-open-retreat
---


## Applicable pattern
Grocery bottle into a soft, cloth-lined basket in the low object-frame scene. The task tests semantic label identification for a narrow upright bottle, plus basket insertion without catching the front rim.

## Winning technique
Identify the BBQ sauce in agentview_high by the brown bottle shape and readable BBQ Sauce label, then refine from the wrist only after moving above that same agentview-selected candidate. Use Pi0 only for the grasp with `pick up the bbq sauce`, confirm by wrist image and a nonzero gripper gap, and hold `gripper:+1` for the carry. For the basket, localize the white lined wicker basket semantically, but choose the visible cloth-lined cavity center rather than the full basket mask centroid. If a low insertion catches or stalls at the front lip, keep the episode if the bottle remains upright and reachable: retreat open, local repick, and release from a higher, more centered over-cavity pose.

## Magic numbers
`pi0_pick` prompt: `pick up the bbq sauce`; `max_chunks=20` (band 12-20), `lift_thresh=0.05` (band 0.05-0.08), `gripper_closed_thresh=0.06`.

Object-frame pre-pick height: z=0.22 (band 0.20-0.24) above the segmented BBQ bottle anchor.

Carry into basket: hold `gripper:+1`; use `step_clip=0.008-0.012` for the tall bottle near the basket.

High over-cavity release: eef z around 0.22 (band 0.20-0.24) with x/y centered over the visible basket opening; in this run `[-0.07, 0.285, 0.23]` was the successful counter-example and must not be cached.

NEVER release with `gripper:+1`; `move_pose` defaults open if omitted, so always pass `gripper:1` while holding.

NEVER trust the full basket mask centroid as the cavity center; it includes rim and side-wall pixels.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| First basket release returned false while the bottle stayed at the front/near outside of the basket | A1 low descent toward z=0.16 stalled at eef z about 0.213, so the tall bottle was not centered deeply enough past the rim | Retreat open, repick locally while upright, then release from a higher and more centered over-cavity pose |
| Basket segmentation gave a plausible mask but not a safe place point | A1 full basket mask included walls/rim/liner and was not the actual cavity center | Use RGB to identify the basket, then use a manually selected visible interior region or wrist view for the cavity |

## Re-localization per scene
BBQ sauce: prompt `the brown bbq sauce bottle` worked with score 0.781. It looks like a narrow brown/orange bottle with a yellow/red BBQ Sauce label and star. It can be confused with other tall cartons only if the label is ignored; reject masks that cover milk/orange juice cartons or the red can.

Basket: prompt `the white lined basket` worked with score 0.738 for semantic identification. It looks like a white cloth-lined wicker basket. Treat the mask xyz as a counter-example if it lands on side walls or rim; use a region over the visible interior liner/cavity instead. This run's absolute coordinates are seed-specific and must not be reused.

## Fragility flags
The fragile step is insertion into the lined basket mouth. Fallback is a local repick only if the BBQ bottle remains upright and close to the basket; otherwise close out the attempt and reset with a planned high centered release from the start.

## Difficulty and reliability
Solved in one episode, but the clean recipe should skip the failed low descent/release and use high centered over-cavity release directly. Expected single-shot rate should be moderate to high if the BBQ label is correctly identified and the basket cavity point is not rim-biased. No unresolved mechanics remained after the local repick and high release.

## Cross-refs
[[high-drop-over-cavity]] [[near-target-repick]] [[basket-insertion-open-retreat]]
