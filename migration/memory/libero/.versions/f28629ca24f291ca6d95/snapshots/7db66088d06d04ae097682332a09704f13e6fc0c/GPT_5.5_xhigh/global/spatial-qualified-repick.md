---
id: spatial-qualified-repick
scope: global
kind: strategy
title: Re-issue a pick with a nearby landmark when generic picking makes only contact.
applies_when: A generic Pi0 pick contacts the target object but leaves it upright
  or ungrasped, and a distinctive nearby landmark is visible in the scene.
symptom:
- contact-only
- gripper-open
- no-lift
- prompt-ladder
- repick
evidence:
  cells:
  - goal_swap_t9_s0
  attempts: 2
confidence: single-shot
related: []
---


A spatially qualified repick can succeed immediately after a generic pick has put Pi0 close to the correct object but failed to close on it.

**Why:** observed, cause unknown. In this cell, the generic wine-bottle prompt moved the wrist into contact without lifting; the prompt naming the same target plus nearby bowl caused Pi0 to close, lift, and complete the rack placement.
**How to apply:** If the object remains upright and the gripper is open after the generic pick, do not immediately reset. Re-issue `pi0_pick` with the same noun plus a stable nearby landmark, with `max_chunks` around 22-26 and normal `lift_thresh=0.05`. Verify by gripper gap and images.
**Falsify:** If repeated spatially qualified repicks from near-contact states still leave the gripper open or tip the object across multiple seeds, treat this as a task-specific coincidence rather than a general strategy.
**Related:**
