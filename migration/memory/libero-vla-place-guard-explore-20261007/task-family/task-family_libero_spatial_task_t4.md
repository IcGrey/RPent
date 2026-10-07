---
id: task-family_libero_spatial_task_t4
scope: task-family
suite: libero_spatial
regime: task
task_id: 4
task_language: Pick the akita black bowl on the top of the wooden cabinet and place
  it on the plate
evidence:
  cells:
  - spatial_task_t4_s0
  attempts: 5
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
This task tests spatial grounding among duplicate akita black bowls: choose the patterned bowl elevated on top of the wooden cabinet, not the lower duplicate in the open drawer, then place it on the red-rim plate.


## Re-localization per scene
Target bowl: identify by relation and RGB. It is the patterned black/white bowl elevated on the dark wooden cabinet top. Confused with the identical patterned bowl lower/front in the open drawer; reject the lower one by elevation and support surface. Agentview pixels on the interior/top pattern worked; rim/edge pixels can hit the cabinet. Wrist confirmation from above is accepted only if it sees the same elevated bowl near the agentview anchor.

Destination plate: red concentric rim, white center, on the table. Confused with neither ramekin nor bowls in this scene; classify semantically before using depth because the task says plate. Use several interior/ring pixels and estimate the center from the visible disc, not a single rim point.

Relation landmark cabinet: dark wooden cabinet with the target bowl on top and duplicate bowl in the open drawer. Use it only to disambiguate which bowl is on top; do not use hidden object names or BDDL coordinates.

