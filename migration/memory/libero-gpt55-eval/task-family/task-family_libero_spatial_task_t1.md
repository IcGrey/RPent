---
id: task-family_libero_spatial_task_t1
scope: task-family
suite: libero_spatial
regime: task
task_id: 1
task_language: Pick the akita black bowl next to the cookie box and place it on the
  plate
evidence:
  cells:
  - spatial_task_t1_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Spatial-relation bowl-to-plate task with two identical patterned black bowls. The target is chosen by relation to the cookie box, while the destination plate must be classified semantically as the red-rim ceramic plate rather than the visually similar stove burner disc.

## Winning technique
Use agentview_high.png for identity: select the lower patterned black bowl adjacent to the cookie box and reject the upper identical bowl near the ramekin. Back-project several bowl pixels, move close enough to get a wrist view, then accept wrist surface samples only if they remain in the same local neighborhood as the agentview target. Use `pi0_pick` only for the grasp with a short spatial prompt, firm with `set_gripper +1`, carry with gripper held closed, and place over the red-rim plate using a positive y offset for the rim-held bowl. Descend low before releasing. If the first release leaves the bowl upright but just short of the plate predicate, a short near-plate `pi0_pick` can reseat the bowl and may trigger termination.

## Magic numbers
`pi0_pick max_chunks=12` (band 10-14) was enough for the relation-qualified target grasp without letting Pi0 wander into an unrelated long-horizon behavior.
`lift_thresh=0.05` (band 0.05-0.06) and `gripper_closed_thresh=0.06` worked for the bowl pick; the actual final opening was about 0.007-0.010, so visual confirmation is required.
`set_gripper +1` for 10 steps (band 8-12) stabilized the rim grasp.
Carry at `z=1.08` in kitchen frame (band 1.06-1.10) with `step_clip=0.015` (band 0.010-0.020).
Descend to eef `z≈0.965` (band 0.955-0.985) before release so the bowl rests rather than drops.
Use bowl placement offset toward robot-left: target eef y was plate_y plus roughly 0.045-0.065 in this run.
NEVER cache this run's absolute xyz; they are counter-examples only.
NEVER omit `gripper: 1` on carries or move_pose while holding the bowl.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Initial `move_to` toward x≈0.098 stalled at x≈0.001 while y and z reached | A1 used a direct pre-position near the cabinet-side bowl; OSC x reach/pose coupling limited the target approach | Treat the stalled pose as a useful wrist observation if the target remains visible; let Pi0 perform the last approach from the close wrist-confirmed pose. |
| First release left the bowl upright adjacent to the plate, `terminated=false` | A1 placed too far on the near edge of the plate region despite the positive bowl y offset | Re-grasp or use a short near-plate `pi0_pick` from the low pose; in this seed that lifted/seated the bowl onto the plate and fired termination. |

## Re-localization per scene
Target bowl: prompt/describe as `the patterned black bowl next to the cookie box`; it is the lower bowl adjacent to the red-and-white oatmeal raisin cookie box. Reject the upper identical bowl beside the ramekin by the spatial relation, not by object suffix.
Cookie box landmark: red-and-white rectangular box with readable COOKIES label, between the lower bowl and the plate. Use it only for relation grounding unless it moves.
Plate destination: white ceramic disc with red concentric rim rings. It can be confused with the gray stove burner disc in depth; classify by RGB first, then back-project multiple interior/rim pixels.
Distractor surfaces: the stove burner is a dark gray ringed disc on a metal square, not the plate; the ramekin is a small gray cup near the upper bowl.
Wrist refinement: for non-basket objects, accept wrist xy only if it agrees with the agentview-selected candidate within roughly 3-5 cm or clearly sees the same bowl after a close pre-position.
This run's absolutes, such as target-bowl wrist samples around x≈0.09-0.13, y≈-0.07 to -0.03 and plate samples around y≈0.17-0.22, must not be reused on other scenes.

## Fragility flags
The fragile step is plate centering for a rim-held bowl. If release does not terminate but the bowl remains upright near the plate, do not reset immediately; re-localize or issue a short near-plate `pi0_pick`/contact-style correction from the current low pose.

## Difficulty and reliability
Solved in one episode with one in-place recovery. Expected single-shot reliability is moderate: target identity is easy from agentview, but plate centering is sensitive to the held-bowl offset and the first release can land just short.

## Cross-refs

