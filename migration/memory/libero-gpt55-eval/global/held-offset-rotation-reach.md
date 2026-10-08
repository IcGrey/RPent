---
id: held-offset-rotation-reach
scope: global
kind: strategy
title: Rotate a held payload to redirect an unreachable hang offset into a reachable
  axis
applies_when: a correctly grasped object hangs several centimeters beyond the EEF
  along a workspace-edge axis, so centering the object would require an unreachable
  EEF target
symptom:
- payload center unreachable
- held offset consumes reach
- mug hangs off plate
- far plate placement
evidence:
  cells:
  - 10_task_t4_s0
  attempts: 69
  solved_seeds:
  - 0
confidence: single-shot
related:
- rotate-wrist-90deg-drifts-eef-recenter-after
---


Rotate the retained payload about world z so its body-to-EEF offset points along a less constrained axis, then recompute the EEF target from the new measured offset.

**Why:** A yaw rotation applies the same planar rotation to the rigidly held body offset. In the winning run, natural mug hang required an EEF y beyond the reachable plate edge; about +90 degrees redirected most of that offset into x, and move_pose reached the plate-supported pose.

**How to apply:** Firm the grasp; lift to z=0.68-0.75; measure body center minus EEF; rotate_wrist about 1.35-1.60 rad while holding +1; remeasure because yaw and EEF drift; set EEF xy = destination center - new offset; carry with move_pose step_clip 0.006-0.008 and descend at 0.003-0.004.

**Falsify:** If the post-rotation body offset does not rotate with wrist yaw, or if the recomputed EEF target remains outside the reachable workspace on every yaw branch, this strategy does not apply.

**Related:** [[rotate-wrist-90deg-drifts-eef-recenter-after]]
