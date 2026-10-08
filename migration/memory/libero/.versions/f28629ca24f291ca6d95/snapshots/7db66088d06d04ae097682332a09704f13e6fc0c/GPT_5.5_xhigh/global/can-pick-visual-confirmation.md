---
id: can-pick-visual-confirmation
scope: global
kind: perception
title: Trust visual grasp evidence over Pi0's pick boolean for cylindrical groceries.
applies_when: A Pi0 can or bottle pick reports failure but the target may be visibly
  held.
symptom:
- pi0 false negative
- gripper threshold
- can held
- pick success false
evidence:
  cells:
  - object_swap_t0_s0
  attempts:
  - 1
confidence: single-shot
related: []
---


A cylindrical grocery pick can be valid even when `pi0_pick.success` is false, if the wrist/agentview images show the target lifted in the gripper and the original spot is empty.

**Why:** Pi0's success boolean depends partly on a gripper-closure threshold; a real can grasp can leave the fingers more open than `gripper_closed_thresh` while still being mechanically stable.
**How to apply:** After `pi0_pick`, inspect wrist and agentview before abandoning the attempt. If peak lift is high, gripper opening is not fully shut, and the named target is visibly held, run `set_gripper({"gripper":1,"steps":5})` and continue scripted carry. Treat this as valid even with `success=false` when visual evidence is clear.
**Falsify:** If repeated can grasps with `success=false` and similar gripper openings visibly drop before carry despite `set_gripper +1`, this heuristic is too permissive for that object/pose.
**Related:**
