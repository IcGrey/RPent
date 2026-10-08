---
id: near-target-repick
scope: global
kind: strategy
title: Use a short local repick when an upright object lands just short of a placement
  predicate
applies_when: A placed object remains upright adjacent to the correct target surface
  after release, and Pi0 can start from a close low pose
symptom:
- release_false
- near_miss
- upright_object
- placement_short
evidence:
  cells:
  - spatial_task_t1_s0
  attempts: 1
confidence: single-shot
related: []
---


A near-target `pi0_pick` can act as a local reseating move when an object is already upright and adjacent to the intended placement surface.

**Why:** observed, cause unknown. In this run, the first scripted release left the bowl upright just short of the plate predicate; a second `pi0_pick` from the low near-plate pose lifted and seated it on the plate, immediately producing `terminated:true`.
**How to apply:** Only try this when the object is upright, close to the correct surface, and a wrong-object semantic choice is no longer plausible. Use a short generic prompt such as `pick up the black bowl`, `max_chunks` around 10-14, and inspect termination immediately. Do not use it as the first placement plan; script the initial carry and release yourself.
**Falsify:** If repeated close-pose repicks lift the object away from the target surface or trigger Pi0 to move toward a memorized destination, this is not a reliable reseating method for that object/task.
**Related:**
