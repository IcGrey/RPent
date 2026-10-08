---
id: co-vary-pitch-clears-yawed-reach-wall
scope: global
kind: primitive
title: Add a small pitch while using move_pose to cross a yawed Cartesian reach wall
applies_when: a yawed gripper stalls several centimeters short in move_to or move_pose
  at pitch zero, while the target is visually reachable
symptom:
- yawed reach wall
- final distance 5 cm
- carry stalls
- handle unreachable
- OSC stall
evidence:
  cells:
  - 10_swap_t8_s0
  attempts: 1
  solved_seeds:
  - 0
confidence: single-shot
related:
- rotate-wrist-90deg-drifts-eef-recenter-after
---


When a cross-grasp yaw made position-only or pitch-zero servos stall, co-varying a small pitch in move_pose reached the same Cartesian target.

**Why:** observed, cause unknown. In this run yaw +1.57 with pitch 0 stalled 5.05 cm short of one handle, while otherwise identical move_pose with pitch 0.15 reached within 1.1 cm; pitch 0.15 also crossed a carry wall at x=0.083 and reached x=0.141.

**How to apply:** Recover to a safe high central pose, then command move_pose with target_pitch about 0.15 rad (tested band 0.15-0.22), preserve the needed yaw, use step_clip 0.004-0.008 and max_steps 150-180. Re-localize from the wrist after reaching; do not assume the pitch preserves the held-object offset.

**Falsify:** If the same yawed target remains equally short with pitch values across 0.10-0.25, or pitch 0 reaches it within the same tolerance on repeat, pitch was not the lever.

**Related:** [[rotate-wrist-90deg-drifts-eef-recenter-after]]
