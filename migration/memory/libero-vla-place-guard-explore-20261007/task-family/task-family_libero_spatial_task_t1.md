---
id: task-family_libero_spatial_task_t1
scope: task-family
suite: libero_spatial
regime: task
task_id: 1
task_language: Pick the akita black bowl next to the cookie box and place it on the
  plate
evidence:
  cells:
  - spatial_task_t1_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Spatial-relation bowl-to-plate task with two identical patterned black bowls. The target is chosen by relation to the cookie box, while the destination plate must be classified semantically as the red-rim ceramic plate rather than the visually similar stove burner disc.


## Re-localization per scene
Target bowl: prompt/describe as `the patterned black bowl next to the cookie box`; it is the lower bowl adjacent to the red-and-white oatmeal raisin cookie box. Reject the upper identical bowl beside the ramekin by the spatial relation, not by object suffix.
Cookie box landmark: red-and-white rectangular box with readable COOKIES label, between the lower bowl and the plate. Use it only for relation grounding unless it moves.
Plate destination: white ceramic disc with red concentric rim rings. It can be confused with the gray stove burner disc in depth; classify by RGB first, then back-project multiple interior/rim pixels.
Distractor surfaces: the stove burner is a dark gray ringed disc on a metal square, not the plate; the ramekin is a small gray cup near the upper bowl.
Wrist refinement: for non-basket objects, accept wrist xy only if it agrees with the agentview-selected candidate within roughly 3-5 cm or clearly sees the same bowl after a close pre-position.
