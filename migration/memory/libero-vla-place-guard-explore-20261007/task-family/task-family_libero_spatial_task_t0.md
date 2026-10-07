---
id: task-family_libero_spatial_task_t0
scope: task-family
suite: libero_spatial
regime: task
task_id: 0
task_language: Pick the akita black bowl not between the plate and the ramekin and
  place it on the plate
evidence:
  cells:
  - spatial_task_t0_s0
  attempts: 8
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Duplicate bowl disambiguation plus hard rimmed-surface placement. The target is the patterned black bowl that does not lie between the red-rim plate and gray ramekin; final success requires the bowl to be seated on the plate, not merely visually overlapping a rim.


## Re-localization per scene
Target bowl: agentview prompt/description `upper right black patterned bowl`; visually patterned black/white bowl with yellow rim, not the duplicate between the plate and ramekin. Reject any wrist-only re-identification that jumps to the lower/front duplicate.
Ramekin: gray/silver cup-like dish beside the duplicate bowls; use it only as a relation landmark to identify which bowl is between plate and ramekin.
This run's absolute coordinates are counter-examples only and must not be cached; object positions must be re-derived from the current seed's images.
