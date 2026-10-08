---
id: contact-skill-state-change
scope: global
kind: strategy
title: Use Pi0 pick as a contact skill for fixture state changes.
applies_when: A task asks to change a fixture state such as turning a stove on or
  off rather than transporting an object.
symptom:
- no object target
- stove knob
- peak_lift_zero
- contact task
evidence:
  cells:
  - goal_task_t7_s0
  attempts:
  - 1
confidence: single-shot
related:
- visual-over-pick-heuristic
---


For fixture state-change tasks, `pi0_pick` can be repurposed as a closed-loop contact controller by disabling the lift/closure success thresholds and using the task verb as the prompt.

**Why:** Pi0 has a learned visual contact behavior for stove controls; the benchmark predicate is the fixture state, not object lift, so a zero-lift trajectory can still be the correct manipulation.
**How to apply:** First identify the fixture and contact target in RGB. Then call `pi0_pick` or the equivalent contact wrapper with a short verb prompt such as `turn off the stove`, `max_chunks=16-24`, `lift_thresh=999`, and `gripper_closed_thresh=0`. Judge success from `terminated`, images, and fixture state evidence rather than peak lift.
**Falsify:** If repeated staged calls reach the control region but never change the fixture state, or if the prompt drives toward a loose object instead of the fixture control, this contact-skill shortcut is not grounded for that scene.
**Related:** [[visual-over-pick-heuristic]]
