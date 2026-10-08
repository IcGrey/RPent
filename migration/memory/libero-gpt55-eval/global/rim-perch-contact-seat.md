---
id: rim-perch-contact-seat
scope: global
kind: strategy
title: Use a capped contact skill to seat rim-perched objects into containers.
applies_when: An object has been released at a rimmed container and is visibly perched
  on the lip or liner while the In predicate is still false.
symptom:
- rim-perched
- basket
- release-false
- push-failed
- can
evidence:
  cells:
  - object_task_t2_s0
  attempts: 2
confidence: single-shot
related:
- high-drop-over-cavity
---


A short `pi0_doubled` contact prompt can finish a rim-perched container placement after controlled release and simple OSC pushes fail.

**Why:** The trained contact policy produced the final seating motion for a tomato sauce can perched on a soft basket rim. Scripted inward/downward moves with small step clips changed the contact state but did not trigger the predicate; the contact skill terminated from the same local setup. Cause beyond observed contact-policy behavior is unknown.
**How to apply:** First make the placement as clean as possible: correct object, low over/interior release, gripper opened. If it remains perched, re-close or hold near the object, make at most one small inward/downward contact move with `step_clip=0.004-0.006`, then call `pi0_doubled` with a direct prompt such as `push the <object> into the <container>` and `max_chunks=10-14`. Inspect images; stop as soon as termination fires.
**Falsify:** If repeated capped contact-skill calls from a visibly rim-perched but otherwise aligned object push it out of the container or do no better than scripted pushes, narrow this to the specific basket/can geometry.
**Related:** [[high-drop-over-cavity]]
