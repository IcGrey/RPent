---
id: task-family_libero_spatial_task_t9
scope: task-family
suite: libero_spatial
regime: task
task_id: 9
task_language: Pick the akita black bowl on the stove and place it on the plate
evidence:
  cells:
  - spatial_task_t9_s0
  attempts: 11
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Duplicate patterned bowls are present, but the task target is the bowl on the stove. The challenge is not identity after perception; it is getting a rim-hooked bowl base onto the red-ring plate despite a large held offset.


## Re-localization per scene
Target bowl: find the patterned black/white/yellow-rim bowl sitting on the gray stove cook region in agentview_high. Reject the identical bowl on the cabinet by the task relation. Text segmentation can choose the wrong duplicate; manual pixels or point prompts on the stove bowl are safer.
Plate: find the white ceramic disc with red concentric rim rings, not the gray stove burner or silver ramekin. Sample interior/ring pixels and use the midpoint/median as the placement anchor.
Relation landmarks: stove is the gray metal square/circular cook region under the target bowl; cabinet bowl is elevated on the dark cabinet and is a distractor; ramekin is a small silver cup near the plate and can enter wrist view after +yaw rotation.
