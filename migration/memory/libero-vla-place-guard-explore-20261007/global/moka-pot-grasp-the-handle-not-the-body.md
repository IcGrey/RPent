---
id: moka-pot-grasp-the-handle-not-the-body
scope: global
kind: strategy
title: Grasp a moka pot by its thin side handle, not its wide body or cap
applies_when: picking a moka pot (or any wide low-poly pot/kettle with a slim handle)
  when top-down body grasps stall and Pi0 will not close
symptom:
- moka pot
- pi0 never closes
- gripper opening 0.078
- descent stalls on shoulder
- cap grasp slips
- wide body grasp
evidence:
  cells:
  - 10_task_t8_s0
  attempts: 3
  solved_seeds:
  - 0
confidence: single-shot
related: []
---

A moka pot is reliably grasped top-down by its thin side HANDLE; its wide octagonal body and thin cap knob are both un-graspable and Pi0 refuses to close on it.

**Why:** The pot's upper chamber/shoulder is ~7.8cm across — essentially the gripper's full open span (~8cm) — so open fingers collide with the shoulder and the OSC descent stalls before the fingers can straddle the body; the only narrow top-down feature (the cap knob, ~1cm) gives a gap-0.012 pinch that slips. The handle is a slim (~1.5-2cm) rigid tube offset laterally from the body, so fingers descend around it without shoulder collision and close to a firm gap ~0.020. Pi0 (pi0_pick) descended but never issued a close command on this pot in 3/3 tries — its trained distribution does not commit to this geometry.

**How to apply:**
- Localize the handle's top-of-curve segment (back_project pixels). Note the tube axis; rotate the
  wrist yaw ~90deg so the fingers close ACROSS the tube (not along it). A 90deg rotate_wrist drifts
  the eef ~0.1-0.15m — re-center over the handle before descending.
- Descend to tube level (~z where finger tips meet the tube), set_gripper +1. Confirm gap ~0.016-0.024
  (tube) — NOT ~0.012 (cap, slips) and NOT ~0.078 (blocked open, no grip). Lift and confirm the pot
  hangs upright by the handle.
- To place: the body hangs offset from the grip (here ~+0.038 x, +0.067 y; measure per pick, it can
  swing). Use the measured offset to choose a clearance-preserving pre-contact handoff. Call pi0_place before final descent or insertion.
- Do NOT waste attempts on pi0_pick or on top-down body/cap grasps for this object class.

**Falsify:** If a future scene has a moka pot whose upper chamber is clearly narrower than the gripper
span and pi0_pick closes and lifts it, or a top-down body grasp seats and lifts it, then the body/Pi0
route is viable there and this lesson is over-general.

**Related:** [[task-family_libero10_task_t8]]
