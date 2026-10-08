---
id: near-goal-contact-regrasp
scope: global
kind: strategy
title: Use short local regrasp contact after visible near-goal placement stalls.
applies_when: A movable object is visibly on or partly on the target surface after
  release, but the task predicate is still false and open-gripper pushes risk losing
  control.
symptom:
- nonterminal-release
- edge-perched
- predicate-false
- duplicate-object
- near-goal
evidence:
  cells:
  - spatial_swap_t6_s0
  attempts: 49
confidence: single-shot
related: []
---


A short Pi0 pick/contact prompt grounded in the object's current near-goal relation can finish a placement that scripted release and open-gripper nudges leave just outside the accepted predicate region.

**Why:** observed, cause unknown. In this run the bowl was already visibly on/partly on the plate after a controlled release; a 5-chunk local `pi0_pick` with prompt `pick up the bowl on the plate` produced a small regrasp/contact motion and the benchmark predicate fired.

**How to apply:** First get the object upright and visibly overlapping the correct destination using scripted carry with `gripper:1`. Release once. If `terminated=false` but the object is still near-goal and not toppled, issue a short local Pi0 pick/contact prompt naming the current relation, with `max_chunks=5-6`, `lift_thresh=0.03-0.04`, and no long placement prompt. Stop immediately if termination fires. Do not use this as a free semantic place skill from far away.

**Falsify:** If the local contact moves the object away from the destination or repeatedly grabs a duplicate object despite a near-goal relation prompt, this tactic does not apply in that scene.

**Related:**
