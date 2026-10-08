---
id: task-family_libero_spatial_swap_t8
scope: task-family
suite: libero_spatial
regime: swap
task_id: 8
task_language: Pick the akita black bowl next to the plate and place it on the plate
evidence:
  cells:
  - spatial_swap_t8_s0
  attempts: 15
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Spatial-relation disambiguation with two visually identical patterned bowls: choose the bowl next to the red-rim plate, not the bowl near the ramekin, then place it on the plate.

## Winning technique
Use agentview_high for identity and wrist only for geometry. Move above the lower/right bowl, confirm it in wrist, use `pi0_pick` with the short prompt `pick up the akita black bowl`, clamp with `set_gripper +1`, and carry slowly with `gripper:+1` through one or two intermediate waypoints. Descend close to the plate before release. In this solved trace, the first release left the bowl partly on the plate and did not terminate; a second short `pi0_pick` from that near-plate pose acted as corrective contact/regrasp and fired the predicate.

## Magic numbers
`pre_pos_z=1.08` (band 1.06-1.10) over the target bowl in kitchen frame.
`carry step_clip=0.012` (band 0.008-0.015) while holding the bowl.
`release_z=1.00` (band 0.97-1.02) before opening on the plate.
`pi0_pick max_chunks=20` (band 12-20) with `lift_thresh=0.05` and `gripper_closed_thresh=0.06`.
NEVER carry with `gripper:-1`; it opens and drops the bowl.
NEVER let wrist identity override agentview identity when choosing between the two bowls.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Bowl visually overlaps or touches the plate but predicate remains false | A5-A14: many low placements, pushes, yaw variants, and high drops left the bowl on the rim/edge or otherwise outside the accepted region | After a near miss, try one short corrective `pi0_pick`/contact from the near-plate pose instead of more lateral pushing |
| Full +90 degree pre-pick yaw drifts toward +y and weakens lift | A7: yaw changed Pi0 pickup distribution and moved near the workspace edge | Avoid large pre-pick yaw; use default orientation or small/no yaw |
| Open-gripper pushes move the bowl only slightly | A5 and later: open contact lacks reliable seating effect | Prefer correct first placement or corrective closed/Pi0 contact near the plate |
| Trying the other bowl does not solve the task | A13 semantic-binding test | Keep relation grounding: target is the bowl next to the plate |

## Re-localization per scene
Target bowl: identify in agentview_high as the patterned black bowl spatially adjacent to the red-rim plate; reject the patterned bowl by the ramekin. Wrist confirmation should stay within about 3-5 cm of the agentview anchor and show the same bowl, not a free re-identification.
Plate: identify semantically as the white ceramic disc with red concentric rim rings; do not confuse it with the gray stove burner. Use several interior/rim pixels and median back_project xy. This run's absolute coordinates are counter-examples only and must not be cached.

## Fragility flags
Most fragile step is placement acceptance: a visually plausible rim placement may not terminate. Fallback is a single corrective `pi0_pick` from the near-plate pose after release, watching for immediate `terminated:true`.

## Difficulty and reliability
Solved after prior exploratory failures and one successful current trace. Expected single-shot rate is moderate if the target relation is identified correctly and the corrective near-plate Pi0 contact is kept as a fallback.

## Cross-refs

