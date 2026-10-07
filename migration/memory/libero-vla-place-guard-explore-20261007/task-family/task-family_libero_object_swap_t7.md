---
id: task-family_libero_object_swap_t7
scope: task-family
suite: libero_object
regime: swap
task_id: 7
task_language: Pick the milk and place it in the basket
evidence:
  cells:
  - object_swap_t7_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Single-object grocery-to-basket task in the low object frame. The main risks are confusing milk with other carton/box groceries and biasing the basket target to a rim instead of the interior.


## Re-localization per scene
Milk: in agentview_high, look for the red upright Dairy Fresh Milk carton with readable white `Milk` text and cow graphic. It can be confused with the red/orange butter box; reject boxes that are flat and say butter, and reject the taller orange juice carton by its orange/yellow front.

Basket cavity: in agentview_high, identify the open woven basket with a white liner. Back-project a region over the visible interior, but expect rim/interior mixing; if scripting placement, move above the basket and use wrist_high to choose the true cavity center before release.

