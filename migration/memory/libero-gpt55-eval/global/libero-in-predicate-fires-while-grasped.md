---
id: libero-in-predicate-fires-while-grasped
scope: global
kind: strategy
title: Test placement targets by holding the object over them and watching libero_terminated,
  before releasing
applies_when: an In()/On() place task where the correct destination among several
  look-alikes is uncertain, or where releasing risks tipping/losing the object
symptom:
- wrong compartment
- which container
- ambiguous target
- place predicate not firing
- cannot re-grasp
- tipped after release
- in predicate
evidence:
  cells:
  - 10_task_t5_s0
  attempts: 4
  solved_seeds:
  - 0
confidence: single-shot
related:
- caddy-back-is-near-robot-pocket
---


LIBERO In()/On() success predicates check the OBJECT'S POSE, not the gripper
state, so `libero_terminated` flips the moment the held object's pose satisfies
the region — you do NOT have to release first.

**Why:** libero_terminated mirrors the BDDL goal predicate, which is a function
of object poses only. Releasing is irrelevant to the check (confirmed: placing a
mug in the correct caddy pocket fired while still grasped; placing/releasing in
three WRONG pockets never fired).
**How to apply:**
- To disambiguate among candidate destinations, carry the still-grasped object
  (gripper +1) low over each candidate and read `libero_terminated` from the
  returned state. Move to the next candidate if it stays false — no release, no
  re-grasp, no commitment. This turns an N-way target guess into N cheap probes.
- Only `release` after the flag is already true (or to seat a confirmed target).
- Corollary: a non-firing predicate with a clean, low, upright placement is
  evidence of WRONG DESTINATION, not wrong physics — switch targets first.
- Caveat: some tasks pair In() with a "not in gripper"/stack-stability term; if a
  held probe won't fire but the geometry looks perfect, release once to check.
**Falsify:** a place task where the predicate provably requires the gripper open
(object released) and a correctly-posed held object does NOT fire.
**Related:** [[caddy-back-is-near-robot-pocket]]
