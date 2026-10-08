---
id: visual-over-pick-heuristic
scope: global
kind: strategy
title: Trust visual grasp evidence over the Pi0 pick success flag.
applies_when: A pi0_pick reports success false but the object is visibly moved or
  held and gripper/image evidence contradicts the heuristic
symptom:
- pick_false
- visual_success
- heuristic_false
- object_moved
evidence:
  cells:
  - spatial_task_t3_s0
confidence: single-shot
related: []
---


A `pi0_pick.success:false` result can still be a useful or even task-critical manipulation when the images show the correct object moved to the right place.

**Why:** The Pi0 pick success flag is a heuristic based on lift and gripper closure thresholds, not the task predicate or a semantic grasp oracle. In this run, a full task-language pick reported false but carried the cabinet-top bowl to the plate; continuing from the visual state solved the task.
**How to apply:** After every `pi0_pick`, inspect agentview/wrist and gripper width. If the target is visibly held, moved to the destination, or staged in a recoverable pose, continue from that physical state rather than resetting or retrying the same grasp. Keep Pi0 capped to the grasp/recovery role and use scripted low contact or release to finish.
**Falsify:** If visual inspection shows the target remained at its source or only a distractor moved, the false flag should be treated as a failed grasp/re-grounding event.
**Related:**
