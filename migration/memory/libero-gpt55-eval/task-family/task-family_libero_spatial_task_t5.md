---
id: task-family_libero_spatial_task_t5
scope: task-family
suite: libero_spatial
regime: task
task_id: 5
task_language: Pick the akita black bowl on the cookie box and place it on the plate
evidence:
  cells:
  - spatial_task_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- near-target-repick
---


## Applicable pattern
Pick the black patterned bowl that satisfies the support relation, here the bowl elevated on the cookie box, and place it on the red-ring white plate. The distractor bowl on the ramekin looks identical, so the support relation and RGB support object are the target identity signal.

## Winning technique
Use agentview high-resolution RGB to choose the lower bowl resting on the red cookie box, not the similar bowl on the gray ramekin. Segment or back-project that bowl, move above it, then accept a wrist refinement only if it is within 3-5 cm of the agentview anchor. Grasp with a short generic prompt, firm the grip, carry at kitchen safe height, and descend until the bowl visibly contacts the red-ring plate before releasing.

In this solved run, the first release placed the bowl on the plate but did not fire. A short local repick/contact from the low near-plate pose with `pick up the black patterned bowl`, `max_chunks=12`, triggered `terminated:true` while the bowl was already seated on the plate.

## Magic numbers
Kitchen frame: pre-position/carry z=1.08-1.10; do not use living-room z values.

Target wrist refinement accept band: <=0.03-0.05 m from the agentview anchor.

Initial grasp: `pi0_pick` prompt `pick up the black patterned bowl`, `max_chunks=20` (band 16-20), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Firm grip: `set_gripper +1` for 8 steps (band 5-10).

Carry: `step_clip=0.018` (band 0.012-0.020), keep `gripper:+1`.

Plate descent: eef z=0.965-1.00 in kitchen frame; release low enough that the bowl rests on the plate.

Near-target repick recovery: `max_chunks=12` (band 10-14) from an upright bowl already on/adjacent to the plate.

Never let SAM3's `cookie box under the black bowl` mask override RGB identity if it selects the gray ramekin under the distractor bowl.

Never use the gray stove burner as the destination; it is a flat ring but not the plate.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| `the cookie box under the black bowl` segmentation highlights the ramekin under the distractor bowl | A1: SAM3 grounded the support-like object below the upper distractor bowl instead of the cookie box | Use agentview RGB relation manually: target is the bowl on the red cookie box; reject masks that land on the gray ramekin. |
| Release leaves bowl visibly on the plate but `terminated:false` | A1: first scripted placement was still biased on the accepted plate region or not settled enough | Clear the gripper upward, then use a short local `pi0_pick`/contact from the low near-target pose; this triggered termination in A1. |

## Re-localization per scene
Target bowl: prompt `the black bowl on the cookie box` worked with score 0.369 in this run. Confirm in RGB that the mask is on the lower black/white patterned bowl elevated on a red cookie box. Fallback: manually sample pixels on the visible bowl interior/rim and compare support object color; do not cache this run's absolute `[0.0566, 0.0404, 0.9463]`.

Distractor bowl: visually identical black/white patterned bowl on a gray ramekin in the upper/right area. Reject it because the support is not a red cookie box.

Plate: prompt `the white plate with red rings` worked with score 0.977. It is a white ceramic plate with concentric red rings; reject the gray stove burner even though both are flat circular surfaces. Do not cache this run's absolute `[0.0614, 0.2101, 0.9097]`.

Cookie box: RGB shows a red/orange cookie package under the target bowl. Text-prompt segmentation was unreliable in this run, selecting the ramekin; use the support color/label and the bowl elevation relation instead.

## Fragility flags
The most fragile step is final seating on the plate. If a low release leaves the bowl upright and visibly overlapping the correct plate but the predicate stays false, try a short local repick/contact from the current low near-plate pose before resetting.

The second fragile step is relation grounding: identical bowls require support-object classification. The gray ramekin and red cookie box are separable in agentview RGB; the wrist should refine geometry only after the agentview target is chosen.

## Difficulty and reliability
Solved in 1 attempt, but the final predicate required a recovery contact after a visibly plausible release. Expected single-shot reliability is moderate: the pick is easy once over the target, while the plate seating predicate is sensitive to centimeter-scale offsets.

## Cross-refs
[[near-target-repick]]
