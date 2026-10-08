---
id: task-family_libero_goal_swap_t8
scope: task-family
suite: libero_goal
regime: swap
task_id: 8
task_language: Put the bowl on the plate
evidence:
  cells:
  - goal_swap_t8_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- low-pose-settle-regrasp
- near-target-repick
- low-contact-seat-after-release
---


## Applicable pattern
Kitchen-frame bowl-to-plate placement under a goal-swap scene. The task tests semantic surface classification: the destination is the red-ring ceramic plate, not the nearby gray stove burner or cabinet top.

## Winning technique
Identify the patterned black/white bowl with yellow rim and the white plate with red concentric rings in `agentview_high`. Back-project several pixels on both; refine the bowl with the wrist after moving above the agentview anchor, accepting wrist geometry only because it stays within a few centimeters of the chosen bowl.

Use Pi0 only for the initial bowl grasp, then lock the gripper and carry manually. Carry at kitchen safe height, descend slowly over the plate with a bowl y-offset, and release low. If a low release leaves the bowl visibly on the plate but `terminated:false`, make a tiny low closed-gripper centering nudge. If it still does not fire and the bowl is upright on the correct plate, a short local `pi0_pick` from the on-plate pose can settle/regrasp the bowl and fire the predicate.

## Magic numbers
`pre_pos_z=1.12` for approach above the bowl (band 1.10-1.14).
`pi0_pick max_chunks=20` for the initial grasp (band 16-22), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.
`set_gripper +1` for 8 steps after the grasp (band 5-10).
`carry_z=1.11-1.12` with `step_clip=0.012-0.015` while loaded.
For bowl-on-plate release, target eef y about `plate_y + 0.045` first; in this run the plate center was near y=-0.036 and first eef y was 0.009.
`release_z=1.02-1.03` in kitchen frame (band 1.02-1.04) with `step_clip=0.006-0.008` for low seating.
Low centering nudge: 2-3 cm toward the plate center at z about 1.03, `gripper:+1`, `step_clip=0.006`.
Local settle repick: `pi0_pick('pick up the bowl')`, `max_chunks=10-12`, `lift_thresh=0.04-0.05`, only after the bowl is visibly on the correct plate.
NEVER omit `gripper:1` during carry or descent.
NEVER classify the gray stove burner as the plate; decide from RGB before placing.

## Failure modes
| symptom | root cause (A<N>) | fix |
| low release leaves bowl partly on red-ring plate but `terminated:false` | A1: held bowl offset placed the bowl rim/center edge-biased relative to the official plate region | short low closed-gripper centering nudge toward the plate center, then release again |
| second release still shows bowl on plate but predicate false | A1: scripted contact was insufficient to settle the bowl into the target region | use short local `pi0_pick` from the low on-plate pose; it fired termination in 10 chunks |

## Re-localization per scene
Bowl: look for the patterned black/white bowl with yellow rim. Text segmentation was not needed here; manual agentview pixels plus wrist refinement worked. Sample interior/rim pixels away from silhouette gaps. Reject wrist refinement if it jumps to the cream-cheese box, bottle, stove, or table by more than 3-5 cm.

Plate: look for a white ceramic disc with red concentric rings. It is easily confused with the gray stove burner in depth because both are flat circular surfaces. Use RGB semantics first, then sample inner white and red-ring pixels, not just the rim. Absolute coordinates from this run are counter-examples only and must not be cached.

Distractors: the wine bottle and cream-cheese box sit near the carry path. Use a high two-stage carry that stays clear of them before descending.

## Fragility flags
The fragile step is predicate firing after the low release. A visually correct bowl-on-plate state may still be `terminated:false`; try a small centering nudge first, then a short local settle/regrasp if the bowl remains upright on the correct plate.

## Difficulty and reliability
Converged in 1 attempt with two in-episode recovery actions after the first release. Expected single-shot rate is moderate: the initial pick and carry were reliable, but bowl offset and the official plate region can require local settling. No unresolved wall remained in this seed.

## Cross-refs
[[low-pose-settle-regrasp]]
[[near-target-repick]]
[[low-contact-seat-after-release]]
