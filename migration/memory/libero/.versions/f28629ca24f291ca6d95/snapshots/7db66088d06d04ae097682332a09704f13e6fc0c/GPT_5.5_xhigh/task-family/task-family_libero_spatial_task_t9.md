---
id: task-family_libero_spatial_task_t9
scope: task-family
suite: libero_spatial
regime: task
task_id: 9
task_language: Pick the akita black bowl on the stove and place it on the plate
evidence:
  cells:
  - spatial_task_t9_s0
  attempts: 11
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- pregrasp-yaw-recenter
- visual-over-pick-heuristic
---


## Applicable pattern
Duplicate patterned bowls are present, but the task target is the bowl on the stove. The challenge is not identity after perception; it is getting a rim-hooked bowl base onto the red-ring plate despite a large held offset.

## Winning technique
Identify the stove bowl in agentview_high by the relation to the gray stove cook region, and identify the red-ring white plate separately. Rotate the wrist yaw by about +1.57 rad while open, then explicitly move back over the perceived stove-bowl xy before Pi0; the rotation alone shifts the EEF off target. Use `pi0_pick("pick up the bowl on the stove", max_chunks=16)` and accept the grasp if wrist/agentview show the correct bowl held even when `success:false`. Firm with `set_gripper +1`, preserve yaw with `move_pose`, carry through a mid waypoint, descend low over the plate, make one small left/back correction, and release with a long settle.

## Magic numbers
`rotate_wrist(delta_yaw=+1.57)` before grasp; after rotating, re-preposition over the stove bowl at z around 1.12 before Pi0.
`pi0_pick max_chunks=16` (band 14-18) with `lift_thresh=0.05` and `gripper_closed_thresh=0.06`; do not discard the grasp solely because the lift heuristic is false.
Carry with `move_pose`, `gripper=1`, `target_yaw=+1.57`, `step_clip=0.008` (band 0.006-0.010).
Descend with `step_clip=0.004` (band 0.003-0.006) to eef z around 1.015 (band 1.012-1.026).
Winning final correction was one short left/back adjustment before opening; avoid long post-release push chains.
NEVER omit `gripper=1` on `move_pose` while holding.
NEVER rotate +1.57 and call Pi0 without re-centering over the stove bowl.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Visibly on/near plate but predicate false | A1 used generic bowl +y compensation and post-release pushes; bowl base stayed outside predicate | Change held geometry and first release pose, not repeated pushes |
| Wrist-guided centering never reaches overlap | A2/A3 varied x/y after inconsistent rim hooks | Change grasp/orientation or measure the current held offset |
| Yaw change still releases beside plate | A4 used +yaw but release xy was not compensated enough | Preserve +yaw and use a lower, plate-biased release |
| Adjacent setdown plus lateral push misses | A5 low side pushes moved the bowl but did not climb/seat over plate rim | Prefer direct low release from held state |
| Measured offset under-aims front/right | A6/A7 offsets varied by grasp and top silhouette misled placement | Bias toward bowl base support point and verify low overlap before release |
| Extreme xyz with vertical hook still misses | A8 held offset varied larger than prior estimate | Change orientation, not only xyz |
| -1.57 yaw worsens alignment | A9 side-on carry put plate left/back of bowl in wrist view | Use opposite yaw sign or return to vertical |
| +1.57 yaw drifts off target before grasp | A10 rotation moved wrist over ramekin/plate | After rotation, explicitly move_to the stove-bowl anchor before Pi0 |

## Re-localization per scene
Target bowl: find the patterned black/white/yellow-rim bowl sitting on the gray stove cook region in agentview_high. Reject the identical bowl on the cabinet by the task relation. Text segmentation can choose the wrong duplicate; manual pixels or point prompts on the stove bowl are safer.
Plate: find the white ceramic disc with red concentric rim rings, not the gray stove burner or silver ramekin. Sample interior/ring pixels and use the midpoint/median as the placement anchor.
Relation landmarks: stove is the gray metal square/circular cook region under the target bowl; cabinet bowl is elevated on the dark cabinet and is a distractor; ramekin is a small silver cup near the plate and can enter wrist view after +yaw rotation.
This run's absolute coordinates are counter-examples only: stove-bowl agentview median around [-0.178,-0.107], plate around [0.093,0.176]. Do not cache them across seeds.

## Fragility flags
Most fragile step: +yaw pre-grasp rotation changes EEF xy, so Pi0 will ground on the wrong neighborhood unless the EEF is moved back over the stove bowl before the pick. Fallback: if +yaw grasp is not visually held, reset and try the same yaw with a slightly lower/closer re-preposition rather than changing the plate placement first.

## Difficulty and reliability
Solved on attempt 11 after ten failed attempts. Expected single-shot reliability is moderate only if the +yaw re-center and low compensated release are reproduced; direct vertical-hook placement and post-release pushes were low reliability in this scene.

## Cross-refs
[[pregrasp-yaw-recenter]]
[[visual-over-pick-heuristic]]
[[post-grasp-yaw-offset]]
