---
id: reverse-entry-corridor-clearance
scope: global
kind: strategy
title: Clear a released wrist by reversing the corridor that successfully entered.
applies_when: A released object is cavity-side but axial or vertical wrist retreat
  re-hooks or extracts it.
symptom:
- wrist trapped
- object extracted
- asymmetric opening
- retreat stall
evidence:
  cells:
  - 10_task_t9_s0
  attempts:
  - 90
confidence: single-shot
related: []
---


After release and in-place orientation neutralization, reverse the same collision-free pose corridor used for insertion instead of inventing a new axial retreat.

**Why:** The entry corridor is empirically collision-free for that wrist/object/fixture geometry. In this run an axial retreat stalled with asymmetric contact, while reversing the positive-x pitch ladder cleared the open wrist without extracting the mug.

**How to apply:** Record the last 2-4 successful entry poses. Release, open fully, neutralize orientation in place, then replay those poses in reverse with gripper -1 and step_clip 0.004-0.008. Inspect after each stage.

**Falsify:** Reversing the exact entry corridor still moves the released object outward or cannot restore symmetric open fingers.

**Related:** none
