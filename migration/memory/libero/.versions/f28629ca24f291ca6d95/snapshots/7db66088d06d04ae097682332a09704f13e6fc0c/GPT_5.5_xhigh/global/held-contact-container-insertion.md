---
id: held-contact-container-insertion
scope: global
kind: strategy
title: Use trained contact insertion before opening a held object.
applies_when: A held object is near a rimmed container but scripted gripper-center
  placement leaves the object projected outside the cavity.
symptom:
- held object
- basket
- outside rim
- release false
- contact skill
- gripper closed
evidence:
  cells:
  - object_swap_t3_s0
  attempts:
  - 12
confidence: single-shot
related:
- rim-perch-contact-seat
---


A short `pi0_doubled` placement/contact prompt can complete container insertion while the robot is still holding the object, avoiding the unrecoverable outside-drop state.

**Why:** observed, cause unknown beyond Pi0 contact-policy behavior. In this run, many scripted releases and held pushes left the BBQ bottle outside the basket wall; from a clean held pre-release pose, `pi0_doubled("put the bbq sauce into the basket")` moved the still-held bottle into the basket and triggered the official predicate.
**How to apply:** First make the grasp and identity clean. Carry the object near the container mouth with `gripper:+1`, at a safe height that shows the cavity in wrist view. Before opening, call `pi0_doubled` with a direct placement prompt such as `put the <object> into the <container>` and `max_chunks=10-14`. Stop immediately if termination fires; otherwise inspect before deciding whether to release or reset.
**Falsify:** If future held pre-release `pi0_doubled` calls from a visually aligned container mouth consistently drop or push objects outside instead of improving insertion, narrow this to bottle/basket geometry.
**Related:** [[rim-perch-contact-seat]]
