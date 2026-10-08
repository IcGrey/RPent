---
id: basket-release-retreat-settle
scope: global
kind: strategy
title: Retreat upward with the gripper open after low basket release.
applies_when: An object is released low inside a basket but the In predicate has not
  fired immediately.
symptom:
- basket release false
- object in basket
- settle
- rim snag
evidence:
  cells:
  - object_swap_t0_s0
  attempts:
  - 1
confidence: single-shot
related: []
---


After a low release into a basket, an open-gripper upward retreat can be the step that lets the object settle and triggers `In`.

**Why:** observed, cause unknown. In this run the can remained angled near the basket lip after `release`, and termination fired during the following upward retreat with `gripper=-1`.
**How to apply:** Insert into the visible basket cavity at low z with small `step_clip` around 0.01, call `release`, then move straight upward or slightly clear of the object while keeping `gripper:-1`. Do not immediately reset or over-push if the object is visibly inside but the release step returns non-terminal.
**Falsify:** If the object is visibly outside the basket or the retreat pulls it out with the gripper, this does not apply; re-localize and recover instead.
**Related:**
