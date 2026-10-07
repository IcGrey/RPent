---
id: task-family_libero_object_swap_t8
scope: task-family
suite: libero_object
regime: swap
task_id: 8
task_language: Pick the chocolate pudding and place it in the basket
evidence:
  cells:
  - object_swap_t8_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Flat grocery box into a woven basket under object-swap perturbation. The hard part is not the pick; it is choosing a basket-interior drop point that lets a long, flat box fall inside instead of perching on the liner or being pushed out over a rim.


## Re-localization per scene
Chocolate pudding: in `agentview_high.png`, look for the flat brown rectangular box with large `CHOCOLATE PUDDING` label. It may be confused with other box/carton groceries only if the label is ignored; the readable brown label disambiguates it from the orange juice carton. Manual pixel back-projection on the top/label worked; SAM was not needed.

Basket: look for the woven rectangular basket with a white cloth liner and open cavity. Agentview region or mask medians can be rim/liner-biased; sample the visible opening and then refine by wrist/visual confirmation during carry. The useful target is not the rim centroid but the interior point where the long box can clear both front and side walls. This run's absolute xyz values are counter-examples only and must not be cached across scenes.

Reject rule: if a basket point puts the held box visually over the front wall or liner lip, reject it and shift toward the interior/back before descending. If a wrist estimate jumps to another grocery item, reject it; wrist is geometry-only after agentview chooses identity.
