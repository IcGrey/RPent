---
id: task-family_libero_spatial_task_t2
scope: task-family
suite: libero_spatial
regime: task
task_id: 2
task_language: Pick the akita black bowl next to the plate and place it on the plate
evidence:
  cells:
  - spatial_task_t2_s0
  attempts: 4
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- bowl-eef-y-offset
---


## Applicable pattern
Spatial-task variant with two identical patterned black bowls: choose the bowl satisfying the relation `next to the plate`, then place that bowl on the same red-ringed white plate.

## Winning technique
Use agentview_high for semantic identity: the target is the patterned bowl adjacent to the red-ringed white plate, not the bowl near the cookies box or stove. Confirm with segmentation/back-projection, then park above the target and accept wrist refinement only if it remains within about 3-5 cm of the agentview anchor. Use Pi0 only for grasping with `pick up the black bowl next to the plate`; after lift, firm the gripper, carry to the plate center with the bowl placement offset `eef_y = plate_y + 0.045`, descend until the bowl is low enough to contact/settle on the plate, and release.

Success criteria: wrist/agentview shows the target bowl lifted, the distractor bowl remains untouched, the held bowl overlaps the plate before release, and `release` returns `terminated:true`.

## Magic numbers
`pi0_pick.max_chunks=20` (usable band 16-24); successful grasp used 7 chunks.
`lift_thresh=0.05` (band 0.05-0.06) and `gripper_closed_thresh=0.06`.
`set_gripper +1` for 8 steps (band 5-10) after the pick.
Kitchen-frame pre-position over bowl: z=1.08 (band 1.06-1.10).
Carry to plate offset: z=1.03 (band 1.02-1.05), `step_clip=0.012` (band 0.008-0.015).
Final settle before release: target z=0.985, observed final eef z about 0.995 (band 0.99-1.01).
Never cache this run's absolute xy; only reuse the perception procedure and offsets.
Never let wrist re-identify which bowl is the target; agentview relation chooses identity.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Bowl released partly on the plate edge, predicate false | A1 used the generic y-offset but did not settle low enough/cleanly; later recovery changed the scene and kept missing the target region | Redo from a clean episode, preserve the simple plate_y + 0.045 offset, and descend to about z=0.995 final eef before release |
| Low offset-compensated release still left bowl on or near rim | A2 overcompensated the apparent held offset instead of using the stable plate relation | Use plate center plus the known bowl y offset, not large ad hoc inward corrections |
| Higher free-drop and larger inward offsets overshot the plate | A3 tried to solve rim contact with bigger xy corrections | Avoid overshooting; make a small centered carry and solve by low settle before release |

## Re-localization per scene
Target bowl: prompt `the black bowl next to the plate` worked in agentview with score 0.574. It looks like a black-and-white patterned bowl with a yellow rim touching/adjacent to the red-ringed plate. Confusable with the identical bowl near the cookies; reject any mask whose xy is closer to the cookies box than to the plate.
Plate: prompt `the white plate with red rings` worked in agentview with score 0.984 and wrist with score 0.98. It is a white ceramic disc with red concentric rings; do not confuse it with stove burner rings.
Distractor bowl: prompt `the black bowl near the cookies box` worked in agentview with score 0.676. Keep it as a negative relation landmark.
This run's absolute anchors, for counter-example only: target bowl about `[0.002, 0.323]`, plate about `[0.068, 0.209]`, distractor about `[-0.096, 0.003]`.

## Fragility flags
The fragile step is placement: releasing too high or with large ad hoc xy corrections leaves the bowl on the plate rim. Fallback is to return to the plate_y + 0.045 offset, descend slowly with the gripper closed until the bowl visibly rests on the plate, then release.

## Difficulty and reliability
Solved after prior failed variants in the same cell notes; the final clean trajectory solved in 6 primitive steps. Expected single-shot reliability is moderate if identity is resolved in agentview and the final settle is low; lower if the target bowl is placed close enough to the plate rim that the gripper contacts the plate while descending.

## Cross-refs
[[bowl-eef-y-offset]]
