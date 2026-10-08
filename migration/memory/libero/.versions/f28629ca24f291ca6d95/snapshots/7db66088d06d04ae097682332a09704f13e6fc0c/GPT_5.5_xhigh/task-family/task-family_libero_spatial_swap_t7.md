---
id: task-family_libero_spatial_swap_t7
scope: task-family
suite: libero_spatial
regime: swap
task_id: 7
task_language: Pick the akita black bowl on the stove and place it on the plate
evidence:
  cells:
  - spatial_swap_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- relation-selected-identical-object
---


## Applicable pattern
Pick one of two visually identical black bowls, where the task relation selects the bowl on the stove, then place it on a visually distinct red-ring plate. The main test is relation-grounded target selection under swap plus bowl-on-plate offset handling.

## Winning technique
Use agentview_high for identity: choose the patterned black bowl visibly seated on the gray stove burner, rejecting the identical bowl on the dark cabinet top. Back-project several pixels on the stove bowl and plate, keeping absolute coordinates scene-local only. Move above the stove bowl at a kitchen-frame pre-grasp z around 1.08, run `pi0_pick` with the relation prompt `pick up the black bowl on the stove`, verify gripper closure and wrist image, then `set_gripper +1` before carry.

Carry at z around 1.08 with `gripper:+1` and use a positive-y placement offset so the bowl body, not the gripper center, overlaps the plate. Descend gradually to eef z around 0.98 before release. If the first release leaves the bowl on or near the plate but `terminated=false`, a short in-place Pi0 contact/re-pick prompt `pick up the black bowl` from the plate pose can re-seat the bowl and trigger the predicate.

## Magic numbers
Kitchen-frame pre-grasp/carry z=1.08 (usable band 1.06-1.10) for this bowl/stove scene.

`pi0_pick` relation prompt max_chunks=20 (observed success at 8 chunks; usable band 8-20). Avoid letting Pi0 place; use it only for grasp or local contact after an already-correct placement.

`set_gripper +1` for 10 steps after grasp (usable band 8-12) before carry.

Bowl-on-plate eef y offset: start around plate_y + 0.04 to +0.05, but inspect the held bowl offset in agentview/wrist because the actual held offset can differ; in this run a correction toward plate_y + ~0.005 was needed before descent.

Release/contact z around 0.98 in kitchen frame (usable band 0.97-1.02). Do not release high above the plate.

NEVER use the cabinet-top bowl just because it is visually prominent; the relation says `on the stove`.

NEVER cache absolute xyz from this run; re-localize the stove bowl and plate in every scene.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| First release shows bowl visually near/on plate but `terminated=false` | A1: held bowl offset left the bowl body too close to the plate edge after a scripted release at eef about [-0.127, 0.190, 0.978] | Use image inspection after release; if the bowl is already at the plate, try a short in-place Pi0 contact/re-pick prompt to re-seat, or reset and increase/decrease the y offset based on held-bowl image evidence. |

## Re-localization per scene
Target bowl: prompt/phrase `the black bowl on the stove`; it is the patterned ceramic bowl whose base overlaps the gray stove burner/cook-region. Confused with the identical patterned bowl on the dark cabinet top. Reject any candidate not physically on the stove surface, even if closer or larger in the camera.

Plate: prompt/phrase `the white plate with red rings`; it is a ceramic disc with red concentric rings on table height. Confused with the gray stove burner because both are circular/ringed; RGB semantics decide plate vs burner before depth geometry.

Stove relation landmark: gray metallic burner/cook-region under the target bowl. Use only to disambiguate the bowl; the destination is the plate, not the burner.

This run's counter-example absolutes were bowl median xy about [-0.282,-0.100] and plate center about [-0.127,0.185]. These are not reusable coordinates.

## Fragility flags
Most fragile step is the final bowl-on-plate release because the gripper-to-bowl offset changes by grasp. Fallback: inspect the held bowl against the plate before release, descend to contact height, then if `terminated=false` but the bowl is already at the plate, use a short local Pi0 contact/re-pick to re-seat rather than redoing the whole stove pick.

## Difficulty and reliability
Solved in 1 attempt with one in-episode corrective Pi0 contact/re-pick after a non-terminating release. Expected single-shot reliability is moderate: target identity is easy from the stove relation, but final placement depends on held-bowl offset.

## Cross-refs
[[relation-selected-identical-object]]
