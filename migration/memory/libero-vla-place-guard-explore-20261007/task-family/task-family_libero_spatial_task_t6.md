---
id: task-family_libero_spatial_task_t6
scope: task-family
suite: libero_spatial
regime: task
task_id: 6
task_language: Pick the akita black bowl on the stove and place it on the plate
evidence:
  cells:
  - spatial_task_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
This task tests spatial grounding among duplicate patterned bowls: pick the bowl whose support is the stove cook region/platform, not the identical bowl on the table, then place it on the red-rim plate.


## Re-localization per scene
Target bowl: prompt/description `patterned black bowl on the stove`. It is the patterned gray/black bowl with yellow rim sitting on the gray stove platform/cook region. Confused with the identical patterned bowl on the table; reject the table-level duplicate by support surface and relation.

Destination plate: prompt/description `red-rim white ceramic plate`. It is a white plate with red concentric rings. Confused with flat stove burner geometry if using depth alone; classify by RGB before placing.

Relation landmark stove: gray metal platform/cook region under the target bowl. Use it only to identify the correct bowl; do not cache positions.

