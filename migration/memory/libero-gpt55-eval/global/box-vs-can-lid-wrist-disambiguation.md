---
id: box-vs-can-lid-wrist-disambiguation
scope: global
kind: perception
title: Wrist-confirm box identity when an agentview z-scan puts a target box at the
  same height as a nearby shiny can lid
applies_when: localizing a standing box that sits next to or behind a metal can, and
  an agentview region/pixel back_project returns a flat surface at can-lid height
  (~z 0.51 in LIVING_ROOM)
symptom:
- gripper landed over the wrong object
- box top reads as can lid
- region back_project captured the lid
- standing box next to can
evidence:
  cells:
  - 10_swap_t1_s0
  attempts: 1
confidence: single-shot
related:
- boxes-tolerate-stacking-in-basket
---


An agentview region/pixel back_project of a standing box that is adjacent to a
metal can can silently return the CAN LID's surface instead of the box top,
because both sit at nearly the same world z; move over the candidate xy and read
the WRIST camera to tell a round metal lid from a box face before grasping.

**Why:** A tomato-sauce/soup can lid and a short box top are both flat, roughly
horizontal surfaces at similar height (~0.51 in LIVING_ROOM). A region
back_project with a z_min filter keeps whichever high, flat pixels fall in the
window — often the shiny lid — and its median xy points at the can, not the box.
The near-vertical wrist view resolves shape (circular lid vs rectangular box
face) that the top-down agentview z-value cannot.

**How to apply:** After the agentview coarse xy, move ~15-20cm above it and open
the wrist view. If the object under the gripper is a round metal lid, reject the
xy; find the box face in the wrist frame and back_project THAT (a flat box top
reads lower, ~0.455, than the can lid ~0.51). Re-pre-position over the box's true
footprint, then pi0_pick. Never grasp on the agentview z-scan alone when a can is
within a few cm of the target box.

**Falsify:** If wrist back_project of the box face returns the same xy/z as the
agentview region (i.e. the lid and box are genuinely the same object or the scan
was already on the box), then the disambiguation step was unnecessary here.

**Related:** [[boxes-tolerate-stacking-in-basket]]
