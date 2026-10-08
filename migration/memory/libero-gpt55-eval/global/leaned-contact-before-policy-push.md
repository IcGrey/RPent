---
id: leaned-contact-before-policy-push
scope: global
kind: strategy
title: Turn unreachable held placement into a leaned contact setup before invoking
  policy push
applies_when: A held object cannot be released onto a raised surface because the gripper
  center cannot move far enough over the surface, but the object can be leaned against
  the target boundary
symptom:
- airborne release falls back
- y wall
- held object offset
- raised surface
- contact skill
evidence:
  cells:
  - goal_task_t4_s0
  attempts:
  - 12
  - 13
confidence: single-shot
related: []
---


When an upright held object cannot be carried far enough over a raised target, stage it in physical contact with the target boundary and use a short learned contact push instead of continuing to chase an unreachable release pose.

**Why:** observed, cause unknown. In this cell, the OSC-held plate repeatedly stalled around the drawer-front boundary and fell back to the table on release, but the same held plate terminated when first leaned low against the boundary and then pushed by `pi0_doubled`.

**How to apply:** Keep `gripper:+1` through staging. Use small `step_clip` values around 0.003-0.006 and moderate yaw if needed to make the object face the boundary. Stop when RGB evidence shows contact/leaning at the correct surface boundary, then call a short contact prompt such as `push the <object> onto the top of the <fixture>` with `max_chunks` around 20-28. Do not open the gripper first unless the contact state requires it.

**Falsify:** If a clean repeated run with the same visible lean/contact state and prompt fails to move the object onto the target while a pure airborne release succeeds, this lesson is too broad or task-specific.

**Related:**
