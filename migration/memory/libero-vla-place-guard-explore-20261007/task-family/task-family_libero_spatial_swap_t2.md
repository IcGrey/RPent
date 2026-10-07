---
id: task-family_libero_spatial_swap_t2
scope: task-family
suite: libero_spatial
regime: swap
task_id: 2
task_language: Pick the akita black bowl from table center and place it on the plate
evidence:
  cells:
  - spatial_swap_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick the patterned black bowl satisfying the spatial phrase "from table center" and place it on the semantically red-ringed white plate. The scene includes a matching patterned bowl on the right and a gray stove burner that can confuse text segmentation.


## Re-localization per scene
Plate: the destination is the white ceramic plate with red rings, below the center bowl. Segment phrase "the white plate with red rings" worked; point prompt [759,548] also worked. Reject the gray stove burner because it is a fixture with dark concentric rings, not a plate.
