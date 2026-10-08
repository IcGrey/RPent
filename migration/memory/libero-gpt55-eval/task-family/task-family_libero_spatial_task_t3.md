---
id: task-family_libero_spatial_task_t3
scope: task-family
suite: libero_spatial
regime: task
task_id: 3
task_language: Pick the akita black bowl on the top of the cabinet and place it on
  the plate
evidence:
  cells:
  - spatial_task_t3_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- near-target-repick
---


## Applicable pattern
Duplicate patterned-bowl spatial task where the target bowl is elevated on a dark cabinet top and must be placed on the red-ring ceramic plate. The main test is semantic relation grounding before a difficult edge-of-workspace cabinet-top grasp.

## Winning technique
Use agentview_high for identity: choose the patterned black/yellow-rim bowl visibly on the cabinet top, and reject the duplicate bowl sitting on the cookie box. Use wrist geometry only after moving over the cabinet-top candidate; accept wrist samples that still show the same cabinet-top bowl.

A close lower pre-position plus the full task-language `pi0_pick` can make Pi0 complete the difficult cabinet-top grasp and carry the target to the plate even if its heuristic reports `success:false`. Judge by image and gripper: in the winning run, the target left the cabinet and appeared at the red-ring plate with a nearly closed gripper. Release low at the plate; if predicate remains false but the target is upright on/near the plate, apply a short local repick or low open-gripper contact move. The final predicate fired during a low open-gripper move over the target/plate, not during the first release.

## Magic numbers
Kitchen frame: home eef z about 1.17.
Cabinet-top bowl pre-position z=1.17-1.18 (band 1.16-1.20); the target is elevated on the cabinet, not table-level.
Initial approach step_clip=0.010-0.012 (band 0.008-0.015) near the y workspace edge.
First grasp prompt `pick up the black patterned bowl on top of the cabinet`, max_chunks=14 (band 12-16), can fail by reopening.
Second grasp from lower/closer pose with full task language, max_chunks=20 (band 18-22), may carry/place despite `success:false`; inspect images instead of trusting the heuristic.
Plate center from red-ring plate segmentation; use target y around plate_y + 0.045 when scripting final low contact/placement.
Final low open-gripper move used z=0.965 (band 0.955-0.985), step_clip=0.008 (band 0.006-0.010).
NEVER let a wrist view choose between duplicate bowls; it is geometry-only after agentview has selected the cabinet-top relation.
NEVER assume `pi0_pick.success:false` means failure when the visual trace shows the object moved to the destination.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| First cabinet-top pick lifts then opens, target remains on cabinet | A1 prompt/pose reached the bowl but did not secure the rim; final gripper opening was wide | Re-pre-position lower and slightly deeper over the wrist-refined bowl, then use the full task-language prompt. |
| Release leaves target upright on/near plate but predicate false | A1 bowl footprint is still edge-biased after Pi0 carry | Use short local repick or low open-gripper settling contact at plate_y plus a small positive y offset. |
| Local prompt disturbs duplicate bowl on cookie box | A1 generic or plate prompt lets Pi0 re-ground to the wrong nearby bowl after target is already at plate | Prefer physical low settling of the already placed target; avoid further free semantic Pi0 prompts once the target is at the destination. |

## Re-localization per scene
Target bowl: describe as `the black patterned bowl on top of the dark cabinet`; it is partly image-clipped at the far negative-y/left side and sits on the dark cabinet, not on the cookie box. The segmentation may include cabinet pixels, so use the overlay for identity and wrist for geometry.
Cabinet top landmark: dark rectangular wooden surface with silver drawer handles beneath it; used only to identify the relation and elevation.
Plate destination: `the white plate with red rings`; white ceramic disc with red concentric rings. Do not confuse it with the gray stove burner disc.
Distractor bowl: `the black patterned bowl on the cookie box`; visually identical bowl on the red/yellow cookie box. Reject it by support relation.
This run's absolute coordinates are counter-examples only: target wrist samples clustered around x 0.07-0.10, y -0.30 to -0.33, z about 1.135-1.153; plate segmentation was around x 0.064, y 0.210, z 0.910.

## Fragility flags
The fragile step is the cabinet-top grasp at the negative-y workspace edge. If the first short grasp reopens, do not conclude the target is unreachable; lower/shift the pre-position and try the full task language. After the target reaches the plate, avoid broad Pi0 prompts because duplicate bowls remain in view and can be disturbed.

## Difficulty and reliability
Solved in one attempt with in-episode recovery. Expected single-shot reliability is moderate-low: identity is clear in agentview, but the cabinet-top grasp is edge-constrained and the first release may not fire. The winning run depended on image-based acceptance of a `pi0_pick.success:false` carry and a final low settling move.

## Cross-refs
[[near-target-repick]]
