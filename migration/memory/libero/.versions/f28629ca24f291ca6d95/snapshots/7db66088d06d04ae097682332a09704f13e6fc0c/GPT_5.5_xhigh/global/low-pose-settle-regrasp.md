---
id: low-pose-settle-regrasp
scope: global
kind: strategy
title: Use a low regrasp to settle an object that is already on the target.
applies_when: An object has been released partly on the correct target surface but
  the official predicate has not fired.
symptom:
- released on target but terminated false
- partly on plate
- predicate did not fire after release
evidence:
  cells:
  - spatial_swap_t3_s0
confidence: single-shot
related: []
---


A short Pi0 grasp from the low, already-near-target pose can settle or lift the object into the target region when a scripted release leaves it partly registered but not terminated.

**Why:** observed, cause unknown; in this cell the second `pi0_pick` from the low-on-plate pose moved the bowl enough for `terminated:true` without a reset.
**How to apply:** only use after RGB confirms the object is on the correct semantic surface. Keep the prompt visual and short, e.g. `pick up the patterned bowl`, with `max_chunks=14-18`, `lift_thresh=0.05`, and inspect termination immediately after the call.
**Falsify:** if the object is on the wrong surface or the second pick lifts it away without termination, this is not a reliable settle mechanism for that geometry.
**Related:**
