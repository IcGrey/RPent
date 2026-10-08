---
id: near-miss-corrective-pick
scope: global
kind: strategy
title: Use a short pick as corrective contact after a near-miss placement.
applies_when: An object has been released partly on or against the destination surface,
  visual overlap is close, and scripted pushes have poor seating authority.
symptom:
- near miss
- rim placement
- release false
- visual overlap
- push failed
evidence:
  cells:
  - spatial_swap_t8_s0
  attempts: 15
confidence: single-shot
related: []
---


A short `pi0_pick` from an already-near destination pose can act as corrective contact/regrasp and may fire the predicate when repeated lateral pushes do not.

**Why:** observed, cause unknown; in this cell the official predicate fired during the corrective pick from the near-plate pose after release left the bowl partly on the plate.
**How to apply:** only use after confirming the target object is already at/against the destination; keep the prompt short (`pick up the <object>`), use `max_chunks` around 12-20, and stop as soon as `terminated:true` appears.
**Falsify:** if the corrective pick lifts the object away from the destination or repeatedly fails to improve/terminate from close visual overlap, this is not the right recovery.
**Related:**
