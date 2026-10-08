---
id: support-assisted-axis-reorientation
scope: global
kind: strategy
title: Support an elongated held object on the destination floor before chaining yaw
  and pitch rotations
applies_when: an elongated held object must be reoriented inside a shallow container
  and airborne wrist rotations slip, drift, or exceed the reachable workspace
symptom:
- bottle bridges drawer mouth
- in-hand rotation drops object
- long axis points along container depth
- horizontal carry stalls
- object must lie across container width
evidence:
  cells:
  - 10_task_t3_s0
  attempts: 73
  solved_seeds:
  - 0
confidence: single-shot
related:
- co-vary-pitch-clears-yawed-reach-wall
- rotate-wrist-90deg-drifts-eef-recenter-after
---


Support the object's base on the destination floor before chaining yaw, pitch, and yaw rotations, then verify the long axis from back-projected endpoints before the final insertion.

**Why:** In the solved run, carrying the bottle upright to the drawer and lowering it to support allowed yaw +1.57, pitch +1.40, then yaw +1.57 while `gripper:+1` remained engaged. Airborne/sequential rotations in earlier attempts often slipped or threw the object. The successful sequence produced endpoint samples spanning world x with nearly constant y. The exact load-sharing mechanism was not measured; support carrying part of the object's weight is the observed difference.

**How to apply:** Carry the object upright at a safe altitude; descend until the base is supported but the grip remains load-bearing. Hold `gripper:+1` continuously. Use yaw increments around 1.57 rad (tested tolerance about ±0.05), pitch around 1.40 rad, and per-step orientation clips 0.03–0.04 rad. After every rotation, re-localize visible endpoints in world xy; continue only if the desired container-width axis is confirmed. If the subsequent Cartesian insertion stalls, preserve orientation with `move_pose` rather than reverting to position-only control.

**Falsify:** The lesson is false or needs narrowing if the same supported yaw/pitch/yaw sequence repeatedly drops the object, fails to change its world-axis orientation, or performs no better than the same rotations in free space under matched grasps.

**Related:** [[co-vary-pitch-clears-yawed-reach-wall]] [[rotate-wrist-90deg-drifts-eef-recenter-after]]
