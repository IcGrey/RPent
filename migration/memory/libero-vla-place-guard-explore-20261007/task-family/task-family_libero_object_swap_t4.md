---
id: task-family_libero_object_swap_t4
scope: task-family
suite: libero_object
regime: swap
task_id: 4
task_language: Pick the ketchup and place it in the basket
evidence:
  cells:
  - object_swap_t4_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Object-frame grocery-to-basket task with a tall-ish sauce bottle target among look-alike condiment bottles. The task tests semantic target identification from agentview, conservative wrist refinement of the same candidate, and basket-cavity placement without over-descending into the low-frame floor.


## Re-localization per scene
Ketchup: prompt/description for perception is `red tomato ketchup bottle with gray cap`, not just `sauce`. It looks like the orange-red bottle with a white/green label reading Tomato Ketchup. Confusable with BBQ sauce (darker brown/orange bottle) and salad dressing (green cap/green label). Agentview identity is mandatory; wrist only refines the already chosen candidate.

Basket: woven rectangular basket with white cloth liner. Use region-mode `back_project` over the visible interior cloth/open cavity. Rim pixels and outside wall pixels are biased; the true placement point is the cavity center.

