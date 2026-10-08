---
id: pi0-pick-carries-past-lift-judge-by-grip
scope: global
kind: perception
title: Judge a pi0_pick by grip + wrist, not the success flag — it can grasp then
  carry past the lift check
applies_when: pi0_pick returns success:false (descent_done:false) but the eef has
  moved far from the object and the gripper is not fully closed
symptom:
- pi0_pick success false
- descent_done false
- eef jumped to another region
- gripper opening ~0.03
- object missing from table
evidence:
  cells:
  - 10_task_t7_s0
  attempts: 1
confidence: single-shot
related: []
---


pi0_pick can grasp the target AND keep driving its trained pick-and-place, so it
reports success:false (its lift/descent heuristic never latches) while actually
holding the object and carrying it toward Pi0's trained place location.

**Why:** pi0_pick's success flag is a lift+gripper-closure heuristic evaluated
over the chunk budget; Pi0's underlying policy is pick-AND-place, so after the
grasp it can translate the eef laterally/downward toward its trained drop, which
breaks the "descend then ascend in place" pattern the flag looks for. The grasp
still happened.

**How to apply:** After ANY pick, apply Rule 1b regardless of the success flag.
Read `state.robot0_gripper_qpos`: opening ~0.01-0.05 => holding an object; ~0.0
=> grasped air. Cross-check the wrist/agentview: is the object now off the table
and in the gripper? If holding, DO NOT re-issue pi0_pick (that would open the
gripper and drop it) — instead `set_gripper +1` to firm the grip and script the
carry+place yourself from wherever Pi0 left the eef. On libero_10_task t7 a
ketchup pi0_pick reported success:false yet had carried the bottle to the basket
(gripper opening 0.034); firming + a scripted seat-and-release solved the cell.

**Falsify:** If, when the flag is false, the gripper is consistently fully closed
(~0.0) and the object remains on the table at its original pose, then the flag is
reliable and this note is wrong.

**Related:** [[task-family_libero10_task_t7]]
