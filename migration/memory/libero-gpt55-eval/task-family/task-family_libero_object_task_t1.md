---
id: task-family_libero_object_task_t1
scope: task-family
suite: libero_object
regime: task
task_id: 1
task_language: Pick the alphabet soup and place it in the basket
evidence:
  cells:
  - object_task_t1_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- brand-label-over-segmentation
---


## Applicable pattern
Object-frame grocery-to-basket task where the named target is one of several similar cans/boxes and the basket is a large movable container. The task tests semantic target identification from agentview plus controlled can insertion into the basket cavity.

## Winning technique
Use agentview_high.png as the semantic authority: identify the blue/yellow alphabet soup can by visible label and reject the red/green tomato sauce can even if segmentation selects it. Back-project 3-5 pixels on the target can for a coarse xy, move above it at z=0.18-0.20, and use wrist only to confirm/refine the same can.

Run `pi0_pick` with a short target prompt (`pick up the alphabet soup can`) and stop after grasp/lift. Confirm by gripper gap and wrist image, then `set_gripper +1`. Carry at z=0.20 through a midpoint to keep each move within the xy cap. Place at the visually centered basket opening, not the liner/rim mask median; descend until the can is visibly inside the cavity, then release.

## Magic numbers
Object frame home z about 0.26 indicates the low table.
Pre-pick/carry z=0.18-0.20 for cans; this cleared clutter and basket rim in this run.
`pi0_pick max_chunks=20` (usable band 16-24), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.
After pick, `set_gripper +1` for 8 steps (usable band 5-12).
Carry `step_clip=0.015` for cans; use a midpoint if y travel is around 0.5 m.
Basket release target z=0.13 nominal; OSC may stop around z=0.15 and still succeed if the can is visibly inside the cavity.
Never trust brand-name SAM3 masks without checking the overlay against the RGB label.
Never carry with `gripper:-1`; that opens and drops the can.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| SAM3 prompt `the alphabet soup can` highlights the lower red/green can | Segmentation grounds can/category/color poorly for grocery brand nouns; observed before A1 motion | Use agentview RGB label reading to choose the blue/yellow alphabet soup can, then use pixels/back_project or point prompts for geometry only |
| Basket segmentation returns liner/rim rather than usable drop point | Cavity mask median is biased by visible fabric/rim; observed in A1 perception | Use region/back_project over the central opening and wrist confirmation near the basket |

## Re-localization per scene
Alphabet soup can: look for the blue/yellow cylindrical can with alphabet-soup text/graphics. Confused with tomato sauce because both are cans; reject any red/green tomato-labeled cylinder. In this seed the correct can was at about [-0.12,-0.24], but absolute coordinates must not be cached.

Basket cavity: look for the woven basket with white liner and open top. Segment phrase `the basket interior` can help find the fixture but may select fabric/rim; use visible opening center and, when close, wrist confirmation. In this seed the drop xy was about [-0.055,0.276], but absolute coordinates must not be cached.

## Fragility flags
Most fragile step is semantic target selection among grocery cans. If a segment overlay disagrees with the readable label, reject it and use manual agentview pixels.

Second fragile step is basket drop depth. If release does not terminate and the can is perched high on the liner, re-close if still held or push/descend gently inside the cavity before another release.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot rate is high if the can label is read in agentview and the basket drop uses the interior opening rather than the rim.

## Cross-refs
[[brand-label-over-segmentation]]
