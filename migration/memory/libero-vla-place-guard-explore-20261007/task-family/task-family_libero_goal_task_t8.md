---
id: task-family_libero_goal_task_t8
scope: task-family
suite: libero_goal
regime: task
task_id: 8
task_language: Put the wine bottle on the plate
evidence:
  cells:
  - goal_task_t8_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Tall cylindrical bottle-to-plate placement in the kitchen frame. The hard part is not target identity: it is carrying with the correct gripper sign and releasing deep enough inside the plate footprint for the On predicate.


## Re-localization per scene
Wine bottle: look for the tall dark green cylindrical bottle with a cork/gold top. Agentview_high is sufficient for identity; sample body/top pixels away from silhouette edges and median xy. The wrist view from above the agentview anchor should show the same dark bottle under the gripper; reject wrist geometry if it jumps to the bowl or cabinet.

Plate: look for the white ceramic disc with red concentric rings. It can be confused with the gray stove burner because both are circular and flat in depth, so classify by RGB before using back_project. Sample the white inner region and ring-balanced pixels, not the rim alone; use the perceived center as a target, then bias a few cm deeper if the bottle hangs toward the near edge. Absolute coordinates from this run are counter-examples only and must not be cached.
