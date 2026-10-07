---
id: task-family_libero_object_swap_t3
scope: task-family
suite: libero_object
regime: swap
task_id: 3
task_language: Pick the bbq sauce and place it in the basket
evidence:
  cells:
  - object_swap_t3_s0
  attempts: 12
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern
Grocery-label disambiguation plus basket insertion for a tall bottle whose held offset makes scripted static releases miss the cavity. The task is solved by using agentview for BBQ identity, Pi0 only for the initial grasp, and a trained contact/placement skill while still holding near the basket.


## Re-localization per scene
BBQ sauce: use agentview_high RGB label and layout. It is a short brown/orange bottle with readable `BBQ` on the label, behind the green-capped salad dressing bottle and left of the center ketchup bottle in this seed. Segment prompts by brand nouns are fragile; manual pixels on the label/body worked better than relying on free segmentation. Reject any wrist/free-Pi0 identity that jumps to the green-capped dressing or the `Fancy Tomato Ketchup` bottle.
Basket: white fabric-lined woven square container at image-right. Agentview back-projection of the rim/interior is biased by the wall and liner folds; use RGB to classify the cavity, and wrist only to confirm the true white-lined opening. This run's absolute positions are counter-examples only and must not be cached.
Ketchup/salad dressing: both are distractors. Ketchup is the taller center-right bottle with `Fancy Tomato Ketchup`; salad dressing is the front-left green-capped bottle. They are the main wrong-target risks.
