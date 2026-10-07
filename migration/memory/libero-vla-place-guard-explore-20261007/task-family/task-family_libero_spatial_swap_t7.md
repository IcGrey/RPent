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
related: []
---
## Applicable pattern
Pick one of two visually identical black bowls, where the task relation selects the bowl on the stove, then place it on a visually distinct red-ring plate. The main test is relation-grounded target selection under swap plus bowl-on-plate offset handling.


## Re-localization per scene
Target bowl: prompt/phrase `the black bowl on the stove`; it is the patterned ceramic bowl whose base overlaps the gray stove burner/cook-region. Confused with the identical patterned bowl on the dark cabinet top. Reject any candidate not physically on the stove surface, even if closer or larger in the camera.

Plate: prompt/phrase `the white plate with red rings`; it is a ceramic disc with red concentric rings on table height. Confused with the gray stove burner because both are circular/ringed; RGB semantics decide plate vs burner before depth geometry.

Stove relation landmark: gray metallic burner/cook-region under the target bowl. Use only to disambiguate the bowl; the destination is the plate, not the burner.

