---
id: open-retreat-settles-container
scope: global
kind: strategy
title: Retreat open after container release when the object is visibly inside.
applies_when: Container placement release opens the gripper but the predicate does
  not fire immediately while the object appears inside or wedged near the gripper
symptom:
- release_false
- object_inside_container
- wedged_object
- predicate_on_retreat
evidence:
  cells:
  - object_swap_t4_s0
confidence: single-shot
related: []
---


If a container placement is visually inside but `release` does not terminate, retreat straight up with the gripper open before changing the target or pushing laterally.

**Why:** observed, cause unknown. In object_swap_t4_s0 the ketchup bottle appeared high/wedged after release; an open vertical retreat let it settle and fired the predicate.
**How to apply:** After `release(max_steps=20-40)`, command an open-gripper vertical retreat of about 5-8 cm with small `step_clip` (0.010-0.015 for tall bottles). Keep xy nearly fixed over the cavity.
**Falsify:** If the object is visibly outside the container or the retreat pulls it out with the gripper, this memory does not apply.
**Related:**
