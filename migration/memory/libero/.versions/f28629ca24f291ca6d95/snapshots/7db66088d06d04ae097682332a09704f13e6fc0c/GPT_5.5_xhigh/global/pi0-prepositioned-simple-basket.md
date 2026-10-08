---
id: pi0-prepositioned-simple-basket
scope: global
kind: strategy
title: Pre-position Pi0 over the visually identified object for simple basket drops.
applies_when: A single grocery object must go into an open basket and Pi0's learned
  place behavior may already match the goal.
symptom:
- basket
- grocery
- milk
- pi0_pick
- pre-position
evidence:
  cells:
  - object_swap_t7_s0
  attempts: 1
confidence: single-shot
related: []
---


A precise visual pre-position over the target can turn `pi0_pick` into a complete solution for simple object-to-basket goals when Pi0's learned destination matches the task.

**Why:** observed, cause unknown; in this cell, starting directly over the visually verified milk let Pi0 grasp and carry it into the basket, terminating the predicate at the pick step.
**How to apply:** identify the target in agentview_high, back-project 3-5 pixels for xy, move open gripper to roughly 0.18 m z in the low object frame, confirm the same item in wrist_high, then use a short prompt such as `pick up the milk` with `max_chunks=20`. If strict grasp-only control is needed, reduce `max_chunks` to 8-12 and script the basket carry/release.
**Falsify:** Pi0 repeatedly carries the object to a non-basket site despite identical pre-positioning, or termination does not fire when the object visibly lands inside the basket.
**Related:**
