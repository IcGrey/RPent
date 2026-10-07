---
id: task-family_libero_spatial_swap_t4
scope: task-family
suite: libero_spatial
regime: swap
task_id: 4
task_language: Pick the akita black bowl in the top layer of the wooden cabinet and
  place it on the plate
evidence:
  cells:
  - spatial_swap_t4_s0
  attempts: 34
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
LIBERO spatial swap t4 presents two identical patterned bowls near a cabinet and a red-ring plate. In this swap cell, the successful predicate followed the drawer/open-cabinet bowl from the seed-0 reference, while many visually plausible cabinet-top-bowl placements did not terminate.


## Re-localization per scene
Drawer/open-cabinet bowl: looks like the black floral patterned bowl sitting inside the pulled-out wooden drawer/cabinet cavity. Agentview phrase: `the patterned black bowl in the open drawer of the wooden cabinet`; fallback: manually sample pixels on the visible interior/bottom of that bowl. Reject wrist refinements that jump to the elevated cabinet-top duplicate.

Cabinet-top duplicate: same patterned bowl on the upper dark wooden top. It is a distractor for this solved swap predicate despite matching the literal phrase in the task text in prior failed runs.

Plate: white ceramic disc with red concentric rings. Agentview phrase: `the white plate with red rings`; fallback: sample the white interior and ring midpoint, not the rim edge. Confused with none in this scene except fixture discs in other kitchen scenes.
