---
id: open-side-bowl-grasp
scope: global
kind: strategy
title: Shift bowl grasps away from nearby fixture clutter.
applies_when: A bowl target is crowded by a cabinet handle, rim, wall, or other fixture
  on one side and Pi0 contacts without lifting.
symptom:
- Pi0 contacts bowl but no lift
- gripper reopens
- crowded bowl grasp
- handle blocks bowl
evidence:
  cells:
  - spatial_swap_t3_s0
confidence: single-shot
related: []
---


When a bowl is crowded by a fixture on one side, re-pre-position from the open side and use a plain visual prompt before increasing chunk budget.

**Why:** the winning grasp followed two failed contact/no-lift attempts near the cabinet side; shifting toward the open table side let Pi0 close on the rim and lift.
**How to apply:** after confirming the target identity in agentview, use wrist geometry to find the bowl, then offset the pre-position a few centimeters away from the obstruction. Use a short prompt such as `pick up the patterned bowl`, `max_chunks=14-18`, `lift_thresh=0.05`, and confirm gripper gap plus wrist evidence.
**Falsify:** if the open-side approach still produces fully closed empty fingers or pushes the bowl off its support, the failure is not just fixture-side contact geometry.
**Related:**
