---
id: support-guided-weak-hook-translation
scope: global
kind: strategy
title: Translate a weak hooked grasp with surface support before lifting over thresholds.
applies_when: A narrow rim or handle hook survives gentle motion but slips under airborne
  rotation or long carry.
symptom:
- weak hook
- grip collapse
- long carry slip
- supported slide
evidence:
  cells:
  - 10_task_t9_s0
  attempts:
  - 89
  - 90
confidence: single-shot
related:
- support-assisted-axis-reorientation
---


A weak internal hook can move an object much farther when the object base remains supported and the wrist unloads only enough to clear friction.

**Why:** Table support reduces the load carried by the narrow hook; in the winning run a 7 mm vertical unload cleared a friction stall while the hook remained intact. The exact force mechanism beyond this observation is unknown.

**How to apply:** Verify an object-sized gap, hold gripper +1, lower until base support stalls the z servo, translate in 3-10 cm stages, and raise only 5-10 mm when sliding stalls. Change to co-varied lift/pitch only at the threshold.

**Falsify:** The object slips or tips during a short supported translation despite a verified retained gap and multiple 5-10 mm unload heights.

**Related:** [[support-assisted-axis-reorientation]]
