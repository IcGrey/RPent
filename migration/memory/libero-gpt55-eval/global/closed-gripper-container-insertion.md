---
id: closed-gripper-container-insertion
scope: global
kind: strategy
title: Descend into open containers before releasing.
applies_when: Object is already held above a basket or open container and the In predicate
  may require volume entry before settling
symptom:
- object over basket
- release not firing
- rim catch
- held can over container
evidence:
  cells:
  - object_swap_t5_s0
confidence: single-shot
related: []
---


For open-container placement, a centered held object can satisfy `In()` during a slow closed-gripper descent into the cavity, before an explicit release.

**Why:** observed in object_swap_t5_s0; cause likely predicate volume/contact geometry, but exact simulator predicate timing was not inspected.
**How to apply:** after a verified grasp, hold `gripper:+1`, center over the visually localized cavity, descend vertically with small `step_clip` around 0.010-0.015 to a low in-cavity z, then release only if termination has not already fired.
**Falsify:** if repeated centered descents leave the object visibly inside the container but `terminated:false`, the predicate requires release/settle rather than held insertion for that task.
**Related:**
