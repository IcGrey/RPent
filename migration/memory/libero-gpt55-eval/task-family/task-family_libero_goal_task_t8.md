---
id: task-family_libero_goal_task_t8
scope: task-family
suite: libero_goal
regime: task
task_id: 8
task_language: Put the wine bottle on the plate
evidence:
  cells:
  - goal_task_t8_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- can-pick-visual-confirmation
---


## Applicable pattern
Tall cylindrical bottle-to-plate placement in the kitchen frame. The hard part is not target identity: it is carrying with the correct gripper sign and releasing deep enough inside the plate footprint for the On predicate.

## Winning technique
Identify the wine bottle globally as the tall dark green bottle with cork, and the destination as the white ceramic plate with red rings rather than the nearby stove burner. Back-project several agentview_high pixels on each; use wrist only to confirm the same bottle candidate before grasping.

Move above the bottle at kitchen carry height, run `pi0_pick` with the short prompt `pick up the wine bottle`, and verify the grasp from gripper opening plus the wrist/agentview images. Lock with `set_gripper +1`, carry to a point over the perceived plate center, and descend to a low kitchen release pose while holding `gripper:+1`. If the first release leaves the bottle on the near plate edge and does not terminate, re-close and make a very small closed-gripper nudge deeper toward the plate center before releasing again.

## Magic numbers
`pre_pos_z=1.15` for approach above the upright bottle (band 1.13-1.17).
`pi0_pick max_chunks=20` (band 15-22), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.
`set_gripper +1` for 8 steps after the pick (band 5-10).
`carry_z=1.12` (band 1.10-1.15) with `step_clip=0.015` for the loaded carry.
`release/seat eef_z=1.02-1.03` over the plate with `step_clip=0.01` or lower.
If edge release does not terminate, use a closed-gripper contact nudge of about 2-3 cm in xy at the same z with `step_clip=0.006` (band 0.005-0.008), then release.
NEVER omit `gripper:1` during carry or lowering; `move_to` defaults open if unspecified.
NEVER classify the gray stove burner as the plate; use RGB semantics before placing.

## Failure modes
| symptom | root cause (A<N>) | fix |
| first release leaves `terminated:false` while bottle is visibly on the near/front plate area | A1: bottle footprint was edge-biased after low release at the perceived plate center; the held bottle hung forward of the eef | re-close, make a short closed-gripper nudge deeper toward plate center at eef z about 1.03, then release again |

## Re-localization per scene
Wine bottle: look for the tall dark green cylindrical bottle with a cork/gold top. Agentview_high is sufficient for identity; sample body/top pixels away from silhouette edges and median xy. The wrist view from above the agentview anchor should show the same dark bottle under the gripper; reject wrist geometry if it jumps to the bowl or cabinet.

Plate: look for the white ceramic disc with red concentric rings. It can be confused with the gray stove burner because both are circular and flat in depth, so classify by RGB before using back_project. Sample the white inner region and ring-balanced pixels, not the rim alone; use the perceived center as a target, then bias a few cm deeper if the bottle hangs toward the near edge. Absolute coordinates from this run are counter-examples only and must not be cached.

## Fragility flags
The most fragile step is the low release: a correct bottle grasp and a visually plausible placement may still not terminate if the bottle is on the plate rim/edge. Fallback is a short closed-gripper contact nudge at the same low z followed by a second release.

## Difficulty and reliability
Converged in 1 attempt with one in-episode recovery nudge. Expected single-shot rate is good when the grasp is visually confirmed and the release is followed by a low centering check. Residual risk: bottle hanging offset varies by grasp, so future runs should inspect the plate contact before deciding whether to nudge.

## Cross-refs
[[can-pick-visual-confirmation]]
