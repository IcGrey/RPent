---
id: task-family_libero_spatial_task_t7
scope: task-family
suite: libero_spatial
regime: task
task_id: 7
task_language: Pick the akita black bowl on the top of the cabinet and place it on
  the plate
evidence:
  cells:
  - spatial_task_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Pick the spatially qualified black bowl from the top of the cabinet and place it on the visually classified plate. The task tests relation-grounded duplicate-bowl selection plus a stable bowl carry from an elevated cabinet surface.

## Winning technique
Use agentview_high for identity: choose the patterned bowl resting on the dark cabinet, not the matching bowl on the metal cook region. Localize the cabinet bowl with several firm bowl-surface pixels, then move above it at kitchen-frame high z. Confirm the same candidate in wrist_high after pre-position, then use Pi0 only for the grasp with a short prompt such as `pick up the black bowl on the cabinet`.

After Pi0 lifts, inspect the wrist/agentview evidence and lock the gripper with `set_gripper +1`. Carry closed to the plate at a safe high z, then use wrist view to correct the held bowl over the plate before descending. Release only after the bowl is visibly over the plate and low enough to contact or nearly contact the plate surface.

## Magic numbers
Kitchen-frame cabinet bowl pre-position z=1.25 (usable band 1.23-1.27) above the cabinet-top bowl.

Pi0 grasp prompt `pick up the black bowl on the cabinet`, max_chunks=20 (band 12-20), lift_thresh=0.05, gripper_closed_thresh=0.06. This run succeeded in 7 chunks.

After grasp, `set_gripper +1` for 8 steps (band 5-12) before carrying.

Carry z=1.18 (band 1.16-1.22) with gripper=+1 and step_clip about 0.012 for the elevated bowl.

Final release eef z about 1.00 (band 0.99-1.03) in the kitchen frame. Do not release high; the bowl should be close to the plate.

Do not let the wrist re-identify the target bowl; use it to refine/confirm the same cabinet-top candidate selected in agentview.

Do not treat the stove/cook-region disc as the plate; classify the white red-ring plate in RGB first.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| none observed | A1 solved | Keep the short relation-specific pick prompt and visually correct the held bowl over the plate before the final descent. |

## Re-localization per scene
Target bowl: in agentview_high, look for the patterned black bowl with yellow rim sitting on the dark cabinet top. It can be confused with the identical bowl on the metal cook region; reject candidates not physically on the cabinet surface. Segment phrasing to try: `the black bowl on the cabinet`; fallback: manual pixels on the interior/rim surface of the cabinet-top bowl.

Plate: in agentview_high, use RGB semantics for the white ceramic plate with red concentric rings. It can be confused geometrically with the metal cook region under the distractor bowl; reject dark/metal ring discs and fixture surfaces. Segment phrasing to try: `the white plate with red rings`; fallback: manual pixels on the visible inner plate surface.

Cabinet landmark: dark rectangular cabinet at image-left/side with silver handles. Use only as a relation landmark, not as a place target.

This run's absolute xyz must not be cached. Counter-example only: target samples centered near [0.012,-0.270,1.155] and plate samples near [0.056,0.191,0.908] in seed 0.

## Fragility flags
The most fragile step is release centering because the held bowl offset depends on Pi0's rim pinch. If the bowl appears side-offset in wrist view at carry height, make a small x/y correction before descending rather than blindly applying a cached bowl offset.

A near-zero gripper opening after pick can still be a valid rim pinch if wrist/agentview show the bowl lifted. Verify visually before resetting or retrying.

## Difficulty and reliability
Solved in 1 attempt on seed 0. Expected single-shot reliability should be decent if agentview selects the cabinet-top bowl and the placement is visually corrected at the wrist before release. Remaining uncertainty: no failed attempts explored alternate grasps or offsets, so the exact held-bowl offset should be measured visually per run.

## Cross-refs
None promoted from this run; candidate global lessons were already covered by prompt instructions and no readable global memory index was available for dedupe.
