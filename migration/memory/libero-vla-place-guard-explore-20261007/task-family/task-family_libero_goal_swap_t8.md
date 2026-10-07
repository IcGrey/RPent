---
id: task-family_libero_goal_swap_t8
scope: task-family
suite: libero_goal
regime: swap
task_id: 8
task_language: Put the bowl on the plate
evidence:
  cells:
  - goal_swap_t8_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Kitchen-frame bowl-to-plate placement under a goal-swap scene. The task tests semantic surface classification: the destination is the red-ring ceramic plate, not the nearby gray stove burner or cabinet top.


## Re-localization per scene
Bowl: look for the patterned black/white bowl with yellow rim. Text segmentation was not needed here; manual agentview pixels plus wrist refinement worked. Sample interior/rim pixels away from silhouette gaps. Reject wrist refinement if it jumps to the cream-cheese box, bottle, stove, or table by more than 3-5 cm.

Plate: look for a white ceramic disc with red concentric rings. It is easily confused with the gray stove burner in depth because both are flat circular surfaces. Use RGB semantics first, then sample inner white and red-ring pixels, not just the rim. Absolute coordinates from this run are counter-examples only and must not be cached.

Distractors: the wine bottle and cream-cheese box sit near the carry path. Use a high two-stage carry that stays clear of them before descending.
