---
id: task-family_libero_goal_swap_t6
scope: task-family
suite: libero_goal
regime: swap
task_id: 6
task_language: Put the cream cheese on the bowl
evidence:
  cells:
  - goal_swap_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Move a flat rectangular grocery box into a rigid bowl in a cluttered kitchen-frame scene. The main risks are box edge/back-projection bias and collision with the nearby wine bottle during the carry.


## Re-localization per scene
Cream cheese: agentview RGB shows a small blue rectangular package with "Cream Cheese" label; use it as the semantic authority. If top/edge pixels return table z, move above the same candidate and wrist-sample the visible rectangular face/edges, accepting only points within a few cm of the agentview candidate.
Bowl: black/white patterned round bowl with a yellowish rim, not the nearby white/red plate or stove burner. Agentview identifies the destination; wrist samples on the visible patterned interior and rim estimate center. Use the interior midpoint, not a rim-only mask median.
