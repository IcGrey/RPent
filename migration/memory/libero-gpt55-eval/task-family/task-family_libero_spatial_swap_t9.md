---
id: task-family_libero_spatial_swap_t9
scope: task-family
suite: libero_spatial
regime: swap
task_id: 9
task_language: Pick the akita black bowl on the wooden cabinet and place it on the
  plate
evidence:
  cells:
  - spatial_swap_t9_s0
  attempts: 6
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- post-grasp-yaw-offset
---


## Applicable pattern
Pick one of two visually identical patterned bowls by a support relation, then place it on a nearby plate in the kitchen frame. The hard part is not semantic target choice once relation-grounded; it is the large held-bowl offset from Pi0's cabinet-rim grasp.

## Winning technique
Use agentview RGB for identity: the target is the patterned bowl sitting on the wooden cabinet, not the identical patterned bowl on the stove. Reject cabinet-edge back-projection outliers; use wrist close-up only to confirm the same cabinet bowl.

Use the default clean cabinet-bowl Pi0 grasp from above the bowl, then change the carried offset after the grasp: rotate wrist yaw by about +1.57 rad while holding the gripper closed. Carry in short closed-gripper waypoints at high kitchen z, approach the red-ring plate from the reachable side, descend until the wrist view shows the bowl body overlapping the plate, and release.

Success criteria per step: Pi0 lift shows the target raised and the cabinet top empty; after yaw rotation the bowl remains visible in the wrist; before release the wrist frame shows bowl rim/body overlapping the red-ring plate, not merely the EEF centered near it.

## Magic numbers
Pre-pick EEF z=1.25 (band 1.23-1.26) above cabinet bowl; use prompt `pick up the patterned bowl on the wooden cabinet` with `max_chunks=20` (band 14-20), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Post-grasp yaw rotation `delta_yaw=+1.57` (band +1.4 to +1.7) with `gripper=+1`; this is after the clean grasp, not before it.

Carry z waypoints 1.18 then 1.12 (band 1.10-1.20), `step_clip=0.012` (band 0.008-0.015), `gripper=+1` on every carry move.

Final release EEF z about 1.04-1.06 with the bowl already visually over the plate; release `max_steps=50`.

Never rotate wrist before Pi0 for this geometry; A3 showed it damaged the grasp.

Never keep increasing negative x compensation with the original held orientation; A2 hit the workspace edge before the bowl reached the predicate.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Bowl released upright beside or partly overlapping the plate but predicate false | A1 under-compensated the held-bowl offset by aiming EEF near plate center | Judge bowl body in wrist, not EEF center; apply larger or rotated offset compensation |
| Larger same-orientation compensation reaches workspace edge at about x=-0.38/y=0.33 and still misses | A2 default held offset demanded more negative x than cleanly reachable | Change held offset direction after the grasp with post-grasp yaw |
| Pi0 reports success but the bowl is not clearly lifted | A3 pre-grasp yaw changed the pick geometry and hurt the reliable cabinet grasp | Keep the default pre-pick orientation; rotate only after the bowl is held |
| Low closed-gripper contact seating still leaves bowl beside plate | A4 push/seating with original orientation did not slide enough onto plate | Use post-grasp yaw before the plate approach |
| Gripper gap collapses and bowl is lost in transport | A5 small pre-pose/prompt change produced a weak grasp | Use the proven prompt/pre-pose from A1/A2/A4/A6 |

## Re-localization per scene
Target bowl: identify the patterned akita black bowl on top of the wooden cabinet in agentview_high. It looks like a grey/white patterned bowl with a yellow rim, partially clipped by the cabinet edge. Confused with the identical patterned bowl on the stove; use the support relation, not name suffix. Back-project only pixels clearly inside the bowl surface or use wrist confirmation; pixels on the clipped cabinet edge can return impossible off-table xyz and must be rejected.

Destination plate: identify the white ceramic plate with red rings on the open tabletop. It is confused with the grey stove burner only by depth/ring geometry; RGB classification separates them. Agentview samples in this run were around z=0.91 and xy near [-0.21, 0.22], but those absolutes are counter-examples only and must not be cached.

Distractors: the stove bowl is identical but sits on the metal stove support; the ramekin is a white fluted cup on the table; the cookies box is flat and irrelevant except as a wrist-view landmark.

## Fragility flags
The fragile step is final alignment after the post-grasp yaw: the gripper center is not the bowl center. If the wrist shows the plate left/up of the bowl rim, move the EEF slightly beyond the plate until the bowl body overlaps the plate before release. If the bowl disappears or gripper qpos collapses near zero during carry, reset rather than continuing placement tuning.

## Difficulty and reliability
Solved on attempt 6 after five failed classes. Expected single-shot rate is moderate if the clean grasp and post-grasp yaw are reused; without yaw correction the same scene repeatedly missed the plate despite several compensation variants. Remaining uncertainty: the exact yaw sign may depend on Pi0's rim sector, so future seeds should verify the wrist relation after yaw before descending.

## Cross-refs
[[post-grasp-yaw-offset]]
[[relation-selected-identical-object]]
[[visual-over-pick-heuristic]]
