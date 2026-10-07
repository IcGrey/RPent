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


## Re-localization per scene
Target bowl: identify in agentview_high as the patterned black bowl spatially adjacent to the red-rim plate; reject the patterned bowl by the ramekin. Wrist confirmation should stay within about 3-5 cm of the agentview anchor and show the same bowl, not a free re-identification.
Plate: identify semantically as the white ceramic disc with red concentric rim rings; do not confuse it with the gray stove burner. Use several interior/rim pixels and median back_project xy. This run's absolute coordinates are counter-examples only and must not be cached.
