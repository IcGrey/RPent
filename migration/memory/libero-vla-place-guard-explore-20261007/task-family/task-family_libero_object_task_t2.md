---
id: task-family_libero_object_task_t2
scope: task-family
suite: libero_object
regime: task
task_id: 2
task_language: Pick the tomato sauce and place it in the basket
evidence:
  cells:
  - object_task_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Grocery-label can into a soft/rimmed basket. The task tests semantic disambiguation between similar red/orange grocery packages and physical seating of a cylindrical can into a flexible basket cavity.


## Re-localization per scene
Tomato sauce: in agentview_high, choose the red/green cylindrical can with tomato graphics. It can be confused with the orange ketchup bottle by the word tomato and with the blue/yellow alphabet soup can by shape. Prefer manual pixels on the metal lid/upper colored band; reject lower side pixels that back-project to table z. Wrist refinement is accepted only if it stays within about 3-5 cm of the agentview identity anchor.

Basket: visually identify the white-lined woven square container. Use agentview for identity and wrist for geometry when close. The true useful target is the open liner/cavity, not the woven rim or outside wall. In this solved run, absolute basket/can coordinates are counter-examples only and must not be cached.
