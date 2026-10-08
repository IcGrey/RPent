---
id: container-slide-axis-toward-fixture-body
scope: global
kind: strategy
title: Close a drawer along the axis toward the cabinet body, and treat zero-motion-under-push
  as a wrong-axis signal
applies_when: closing (or opening) a drawer/sliding fixture whose position was swapped/relocated,
  and a push that "should" close it moves the drawer by nothing
symptom:
- drawer will not close
- push does nothing
- drawer floor edge unchanged after pushing
- pi0_doubled close the drawer does nothing
- container coordinates identical across many pushes
- drawer never moves no matter the force
evidence:
  cells:
  - 10_swap_t3_s0
  attempts: 2
  solved_seeds:
  - 0
confidence: single-shot
related:
- probe-container-floor-by-stall-height
- libero10-left-right-sign-verify-empirically
---


A drawer slides along the axis between its open position and the cabinet body it
retracts into; to close it, push its open-side face TOWARD the cabinet body — do
not assume it closes toward the robot (-x). If a push moves the drawer exactly
0 mm across several tries AND the trained contact skill (pi0_doubled) also does
nothing, you are almost certainly pushing PERPENDICULAR to the rails; rotate the
push ~90 deg.

**Why:** A prismatic drawer joint only accepts force along its rail axis; a force
perpendicular to the rails is fully reacted by the joint constraint, so the drawer
does not translate and an OSC servo just stalls in contact (and the trained policy,
grounded on the base-task geometry, pushes the base axis which the swap invalidated).
Under `_swap` the cabinet is relocated, so the rail axis is whatever direction points
from the open drawer to the cabinet box — read it off the scene, don't inherit it.

**How to apply:**
- Before pushing, locate the CABINET BODY in agentview. The drawer closes toward it.
  Example (one seed): cabinet on image-left (-y) => close = push -y, even though the
  drawer's floor looked like it extended toward +x.
- Use a coordinate-free PROGRESS SIGNAL: back_project a fixed pixel on the drawer
  floor/front before and after each push. If its world xy/z is IDENTICAL to ~4
  decimals, the drawer did not move — change the axis, not the force.
- Put the CLOSED gripper on the open-side face at face height (fingertips ~= eef_z,
  so pick z just below the rim top), then move_to along the closing axis with
  gripper=+1, step_clip 0.02-0.025, max_steps 120-150. One or two pushes seat it.
- Near the cabinet, prefer move_pose over move_to (move_to walls at the OSC IK
  singularity for forward/deep reaches).

**Falsify:** A swapped drawer that DOES close under a push toward the robot (-x)
while the cabinet is on the -y side, or a case where identical-container-coords +
pi0_doubled-fails still means "push harder same axis" rather than "wrong axis".

**Related:** [[probe-container-floor-by-stall-height]] [[libero10-left-right-sign-verify-empirically]]
