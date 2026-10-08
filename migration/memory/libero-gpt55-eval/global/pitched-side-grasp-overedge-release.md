---
id: pitched-side-grasp-overedge-release
scope: global
kind: strategy
title: Release wide held objects once they overlap the container edge.
applies_when: A wide bowl or cup collides before reaching a deep drawer or cavity
  target, but the predicate can accept an over-edge drop into the container.
symptom:
- deep insertion stalls
- bowl braced on lip
- drawer lip collision
- release outside
evidence:
  cells:
  - goal_swap_t3_s0
  attempts: 16
confidence: single-shot
related: []
---


A collision-limited approach can still solve if the held object is visibly overlapping the target container; forcing the end effector deeper is not always necessary.

**Why:** observed, cause unknown. In this solved run, a small-step inward/down `move_pose` stalled short of its target, but the bowl had crossed enough of the open top drawer edge that opening the gripper let it settle into the accepted region.
**How to apply:** First create a stable side/rim grasp, keep `gripper:+1`, carry high, and use very small `step_clip` around 0.003-0.005 for the final inward/down pose. Inspect RGB before release; release when the object body overlaps the container interior edge, even if final_dist remains several cm.
**Falsify:** If a release from a clearly over-edge state consistently drops outside or fails the predicate across multiple seeds while a deeper pose later succeeds, this lesson is too broad.
**Related:** [[task-family_libero_goal_swap_t3]]
