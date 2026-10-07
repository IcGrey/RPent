---
id: task-family_libero_object_swap_t6
scope: task-family
suite: libero_object
regime: swap
task_id: 6
task_language: Pick the butter and place it in the basket
evidence:
  cells:
  - object_swap_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Object-frame grocery placement: identify a flat rectangular butter box among similar grocery distractors, grasp it with Pi0 only, and script the carry into a woven basket cavity.


## Re-localization per scene
Butter: identify by the red/yellow/blue Farm Fresh Butter label and flat box shape. Confused with chocolate pudding because both are rectangular boxes; reject if the label reads Chocolate Pudding or if wrist refinement jumps away from the agentview-identified butter.
Basket: identify by the white cloth liner and woven walls. Use a region over the open liner/cavity; rim and sidewall depth are biased and should not be cached as the center.
