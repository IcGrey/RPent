---
id: task-family_libero_spatial_task_t5
scope: task-family
suite: libero_spatial
regime: task
task_id: 5
task_language: Pick the akita black bowl on the cookie box and place it on the plate
evidence:
  cells:
  - spatial_task_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick the black patterned bowl that satisfies the support relation, here the bowl elevated on the cookie box, and place it on the red-ring white plate. The distractor bowl on the ramekin looks identical, so the support relation and RGB support object are the target identity signal.


## Re-localization per scene

Distractor bowl: visually identical black/white patterned bowl on a gray ramekin in the upper/right area. Reject it because the support is not a red cookie box.


Cookie box: RGB shows a red/orange cookie package under the target bowl. Text-prompt segmentation was unreliable in this run, selecting the ramekin; use the support color/label and the bowl elevation relation instead.
