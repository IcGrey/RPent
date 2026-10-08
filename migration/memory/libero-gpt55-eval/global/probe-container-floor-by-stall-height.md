---
id: probe-container-floor-by-stall-height
scope: global
kind: perception
title: Find a container's true floor by descend-until-OSC-stall and read the stall
  height
applies_when: you must place a held object on the floor of a container (basket/drawer/box)
  whose interior floor you cannot see from above (occluded by rim/liner/other objects)
  and depth/segment centroids are rim-biased
symptom:
- descend into basket stalls high above floor
- cannot tell floor from wall
- object placed on rim not floor
- second object lands on first
- unsure if seated
evidence:
  cells:
  - 10_swap_t0_s0
  attempts: 4
  solved_seeds:
  - 0
confidence: single-shot
related:
- basket-two-cans-wedge-not-stack
---


Descend the held object with move_to (small step_clip ~0.02) and read the eef z where
it stalls: a LOW stall = the object bottomed on the FLOOR (seated); a HIGH stall = it
is resting on a wall/rim or on another object. Reposition xy and re-descend until the
stall drops to the floor value.

**Why:** move_to OSC servo stops making downward progress the instant the held object
contacts a rigid surface. The eef z at stall directly encodes the contact height, so
the same descend that seats an object also probes the geometry — a cheap, coordinate-free
way to map an occluded interior floor pocket without trusting a segment centroid.

**How to apply:**
- Carry over a candidate interior xy, descend to a z below the expected floor with
  step_clip 0.02; inspect final eef z and final_dist.
- Establish the FLOOR value once (e.g. seating object #1): note its stall z (this run
  ~0.542). Any later stall markedly higher (this run ~0.616-0.622, i.e. +0.07-0.08)
  means wall/rim/on-object, NOT floor — do not release there; shift xy and retry.
- The interior may extend OFF-FRAME (clipped at the image edge); probe a few xy to
  bound the pocket. Re-derive per scene; never cache the absolute stall z.
- Combine with the wrist cam for a sanity check, but the stall height is the reliable
  signal when the wrist view is filled by the held object.

**Falsify:** If a soft/compliant container lets the object sink so stall height does
not distinguish floor from wall, or if OSC stalls high even on the true floor (IK
singularity — then switch to move_pose), this heuristic breaks.

**Related:** [[basket-two-cans-wedge-not-stack]]
