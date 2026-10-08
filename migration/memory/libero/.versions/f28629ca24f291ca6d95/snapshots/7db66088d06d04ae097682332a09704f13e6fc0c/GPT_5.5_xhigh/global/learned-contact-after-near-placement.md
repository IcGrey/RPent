---
id: learned-contact-after-near-placement
scope: global
kind: strategy
title: Use learned contact to finish near placements.
applies_when: A scripted release leaves the correct object visibly near or partly
  on the target surface but the predicate remains false.
symptom:
- near miss
- on plate false
- rim supported
- tipped near target
- scripted push failed
evidence:
  cells:
  - spatial_task_t8_s0
  attempts:
  - 20
confidence: single-shot
related: []
---


A near-placement that fails the predicate can still be recoverable by `pi0_doubled` contact rather than another reset or more scripted xy nudges.

**Why:** observed, cause unknown. In this cell, scripted low releases and small closed-gripper pushes left the bowl visually near/on the plate but false; `pi0_doubled` physically seated the bowl and immediately terminated.
**How to apply:** after confirming the correct object is near the target surface and not irrecoverably lost, call `pi0_doubled` with a short goal phrase such as `put the black bowl on the plate`, `max_chunks=20` (observed success at 8 chunks). Use this as recovery/contact, not as the initial pick/place shortcut.
**Falsify:** if repeated contact calls from a visually near target state do not move the object or worsen placement without ever terminating, prefer a reset and change the earlier release geometry.
**Related:** [[task-family_libero_spatial_task_t8]]
