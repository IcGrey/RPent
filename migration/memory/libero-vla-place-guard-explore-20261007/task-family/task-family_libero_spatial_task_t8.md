---
id: task-family_libero_spatial_task_t8
scope: task-family
suite: libero_spatial
regime: task
task_id: 8
task_language: Pick the akita black bowl next to the ramekin and place it on the plate
evidence:
  cells:
  - spatial_task_t8_s0
  attempts: 5
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Spatial-relation duplicate-bowl task: identify the bowl by its relation to the ramekin, place it on the red-rim plate, and recover near-miss bowl placements with a learned contact/settle skill.


## Re-localization per scene
Target bowl: prompt/visual description is the patterned akita black bowl adjacent to the silver ramekin. In this seed it was the upper bowl in agentview. Do not cache that absolute position; select by relation to the ramekin.

Distractor bowl: identical patterned bowl farther from the ramekin. Alternate-target test did not solve; the relation target remains the adjacent bowl.

Ramekin: small silver/gray ribbed cup. Use as relation landmark only.

Plate: white ceramic disc with red concentric rings. Distinguish it from stove/cabinet surfaces by RGB; use the red-rim disc, not the burner.

Wrist refine: use wrist for visual placement alignment, but reject pre-pick wrist world samples that jump more than about 5 cm from the agentview anchor because skewed bowl interiors can back-project to inconsistent x.
