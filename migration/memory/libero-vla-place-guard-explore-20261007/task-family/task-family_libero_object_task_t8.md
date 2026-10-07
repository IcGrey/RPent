---
id: task-family_libero_object_task_t8
scope: task-family
suite: libero_object
regime: task
task_id: 8
task_language: Pick the salad dressing and place it in the basket
evidence:
  cells:
  - object_task_t8_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---
## Applicable pattern

Single upright grocery bottle into the low object-frame basket. This task tests semantic selection of the ranch/salad-dressing bottle among several labeled grocery distractors plus basket insertion.


## Re-localization per scene

Salad dressing: identify the dark green cap/body with a white ranch/salad-dressing label in agentview_high. It can be confused with ketchup or BBQ sauce if the prompt is treated as a generic bottle, so use readable RGB identity first and wrist only to refine the same chosen candidate.

Basket: white fabric-lined woven basket. Agentview region back-projection over the whole basket can be rim-biased; target the visible liner/cavity center for placement reasoning.

