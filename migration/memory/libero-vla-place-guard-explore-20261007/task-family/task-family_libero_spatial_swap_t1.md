---
id: task-family_libero_spatial_swap_t1
scope: task-family
suite: libero_spatial
regime: swap
task_id: 1
task_language: Pick the akita black bowl next to the ramekin and place it on the plate
evidence:
  cells:
  - spatial_swap_t1_s0
  attempts: 6
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Duplicate patterned bowls with a spatial relation target: pick the bowl next to the ramekin and place it on the red-ring plate. The task tests relation-grounded identity under swap plus bowl-on-plate release offsets.


## Re-localization per scene
Target bowl: visually patterned black/white bowl with yellow rim next to the gray ramekin. Prompt to Pi0 can keep the object name, but segmentation should use visual wording such as `the patterned black bowl next to the ramekin`; in this cell SAM/point segmentation was not reliable enough for final xy.

Ramekin: small gray ribbed cup/bowl. Use it as the relation landmark. In wrist, confirm it is beside the target bowl and not the lower duplicate.


Reject rule: if wrist samples identify a bowl without the ramekin relation context, or jump to the lower bowl near cookies, reject and reposition. This run's successful wrist target samples were about 15 cm in y away from the ramekin samples, matching the visible adjacency in the wrist view.
