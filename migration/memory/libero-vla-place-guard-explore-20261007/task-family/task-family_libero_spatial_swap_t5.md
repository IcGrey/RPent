---
id: task-family_libero_spatial_swap_t5
scope: task-family
suite: libero_spatial
regime: swap
task_id: 5
task_language: Pick the akita black bowl on the ramekin and place it on the plate
evidence:
  cells:
  - spatial_swap_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Pick the black patterned bowl satisfying an elevated support relation, here the bowl on the ramekin, and place it on the ceramic plate while rejecting an identical table-level bowl and a stove burner look-alike.


## Re-localization per scene
Target bowl: in agentview_high, look for the black patterned bowl elevated on top of the gray ramekin. Prompt `the black patterned bowl` worked in the wrist once the gripper was above the agentview anchor. Reject the table-level duplicate even if it segments cleanly.

Ramekin landmark: gray ridged cup under the target bowl. It is used for relation identity only; do not place on it.

Plate destination: white ceramic disc with red concentric rings near the table front. Sample pixels inside the plate, not on the rim. Reject the dark gray stove burner with ring grooves; it is not the plate.

