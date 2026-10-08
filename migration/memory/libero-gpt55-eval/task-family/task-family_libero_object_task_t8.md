---
id: task-family_libero_object_task_t8
scope: task-family
suite: libero_object
regime: task
task_id: 8
task_language: Pick the salad dressing and place it in the basket
evidence:
  cells:
  - object_task_t8_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- brand-label-over-segmentation
- basket-insertion-open-retreat
---


## Applicable pattern

Single upright grocery bottle into the low object-frame basket. This task tests semantic selection of the ranch/salad-dressing bottle among several labeled grocery distractors plus basket insertion.

## Winning technique

Use agentview_high RGB as the identity authority: the salad dressing is the dark green/white ranch bottle at the front center. Back-project several firm pixels on that bottle, move above the same xy at low-table pre-pose height, and accept wrist geometry only if it stays within the agentview anchor. Localize the white-lined woven basket from agentview as a cavity on image right. In this seed, `pi0_pick` with the short prompt `pick up the salad dressing` grasped the bottle and continued into its trained basket placement, terminating immediately.

Success criteria: wrist view before pick shows the same dark green bottle under the gripper; after `pi0_pick`, gripper opening is around 0.037 rather than fully closed and agentview shows the bottle upright inside the basket with `terminated:true`.

## Magic numbers

Object-frame bottle pre-pose z=0.17-0.18 (used 0.18).

Use `move_to` with `step_clip=0.010-0.012`, `tol=0.012`, and max_steps about 100; a several-cm residual in x can still be acceptable if wrist confirms the target under the gripper.

`pi0_pick` prompt `pick up the salad dressing`, `max_chunks=20` (worked at 18 chunks), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Basket cavity y is near the lined interior, not the front rim; use the region center/visual liner rather than a rim median.

Never cache this seed's absolute xy. The observed salad dressing xy was around (0.15, 0.02) after wrist refinement and basket interior y around 0.25-0.27.

## Failure modes

| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | solved in A1 | keep the short prompt and wrist-confirmed target identity |

## Re-localization per scene

Salad dressing: identify the dark green cap/body with a white ranch/salad-dressing label in agentview_high. It can be confused with ketchup or BBQ sauce if the prompt is treated as a generic bottle, so use readable RGB identity first and wrist only to refine the same chosen candidate.

Basket: white fabric-lined woven basket. Agentview region back-projection over the whole basket can be rim-biased; target the visible liner/cavity center for placement reasoning.

This run's absolutes are counter-examples only: do not reuse salad dressing xy around (0.15, 0.02) or basket xy around (0.01, 0.255) without re-localizing.

## Fragility flags

Most fragile step is prompt grounding among several sauce/bottle-like distractors. If Pi0 picks ketchup or BBQ sauce, reset for a clean recipe and pre-position more tightly above the visually identified ranch bottle before calling `pi0_pick`.

If Pi0 grasps but does not place, switch to the standard scripted carry: `set_gripper +1`, carry at z=0.20-0.22, move over the basket liner, release over the cavity, then retreat open.

## Difficulty and reliability

Solved in 1 attempt. Expected single-shot rate is moderate: the short prompt worked here, but relying on Pi0 to complete placement violates the usual grasp-only discipline and may be less robust than scripted carry on other seeds.

## Cross-refs

[[brand-label-over-segmentation]] [[basket-insertion-open-retreat]]
