---
id: pick-before-contact-skill-keeps-wrist-clean
scope: global
kind: strategy
title: In multi-part tasks, do the pi0_pick grasp BEFORE any pi0_doubled contact skill,
  to keep a clean vertical wrist
applies_when: A task needs both a grasp/place AND a contact skill (knob/button/drawer
  via pi0_doubled), and the grasp target is awkward (wide/smooth/round). Order the
  subtasks so the grasp comes first.
symptom:
- pi0_pick descends onto the object but the gripper never closes
- gripper stays open (0.06-0.08) through the whole pick
- manual close slips off a smooth/wide object on lift
- wrist has a persistent tilt (large quat x/y component) that rotate_pitch/rotate_wrist/move_pose
  cannot null out
evidence:
  cells:
  - 10_swap_t2_s0
  attempts: 2
  solved_seeds:
  - 0
confidence: single-shot
related: []
---


For an awkward grasp (e.g. a moka pot's wide smooth octagon), pi0_pick only closes
reliably from a CLEAN VERTICAL wrist; if a prior pi0_doubled (or a failed pi0_pick)
has already tilted the wrist, pi0_pick refuses to close. So sequence the task to do
the grasp first, while the wrist is still at its home vertical orientation.

**Why:** pi0_doubled contact skills (and pi0_pick's own servoing) leave the eef in a
tilted orientation (observed quat y-component ~-0.26, ~30deg) that the scripted
rotate_pitch/rotate_wrist/move_pose primitives did NOT restore to true vertical in
this env. Pi0.5's pick policy appears to need an approximately top-down approach to
commit its close command; from a tilted pose it keeps re-approaching and never
closes. (Mechanism for the "cannot null the tilt" part: observed, cause unknown —
likely an OSC null-space/orientation-target artifact.)

**How to apply:**
- If a task = grasp/place + turn-a-knob (or press/open), do the PICK+PLACE first,
  then the pi0_doubled contact skill last. The place target and the contact target
  are usually different fixtures, so ordering is free.
- Before pi0_pick, verify the wrist quat is near-identity (|x|,|y| small). If it is
  tilted from earlier motion, and you cannot restore it, RESET (explore mode) and
  re-order so the grasp is first.
- Judge the grasp by gripper width + wrist/agentview, not pi0_pick.success (it
  reported false on a good grasp here).

**Falsify:** A run where pi0_pick reliably closes on the same awkward object from a
visibly tilted wrist, or where rotate_pitch/move_pose restores true vertical and a
grasp-after-contact-skill ordering succeeds just as often.

**Related:** [[task-family_libero10_swap_t2]]
