---
id: post-grasp-yaw-offset
scope: global
kind: strategy
title: Rotate a held bowl after a reliable grasp to move its offset into reach
applies_when: A reliable Pi0 bowl grasp carries the object with a large offset that
  makes direct placement miss or hit the workspace edge
symptom:
- held offset
- workspace edge
- bowl beside plate
- gripper center wrong
- placement misses
evidence:
  cells:
  - spatial_swap_t9_s0
  attempts: 6
confidence: single-shot
related:
- visual-over-pick-heuristic
---


When the grasp is reliable but the carried bowl offset points toward an unreachable placement correction, preserve the grasp and rotate the wrist after the lift so the object offset can be compensated along a reachable axis.

**Why:** Pi0's cabinet-rim grasp held the bowl with a large offset from the EEF. Direct compensation in the original orientation repeatedly required more negative x than the OSC workspace allowed. A post-grasp yaw rotation of about +1.57 rad changed the visible bowl-to-gripper relationship while keeping the grasp, allowing a short reachable descent where the bowl body overlapped the plate.
**How to apply:** First get a visually confirmed grasp with the original successful prompt and pose. Hold `gripper=+1`, apply `rotate_wrist` after the lift (`delta_yaw` roughly +/-1.57; choose sign by wrist view), then carry slowly with `step_clip=0.008-0.015`. Before release, use wrist RGB to verify the object body, not EEF center, overlaps the target surface.
**Falsify:** If rotating after the grasp consistently drops the object or leaves the bowl-to-gripper offset unchanged in wrist view, this strategy is not the right lever for that grasp.
**Related:** [[visual-over-pick-heuristic]]
