---
id: remeasure-loaded-offset-before-descent
scope: global
kind: strategy
title: Remeasure a held payload after every loaded servo before descending
applies_when: a large asymmetric object is carried by a handle and precise support
  placement depends on body-to-EEF offset
symptom:
- payload offset changed
- centered before move but off target
- loaded servo changed hang
- yawed reach wall
evidence:
  cells:
  - 10_task_t2_s0
  attempts: 107
  solved_seeds:
  - 0
confidence: single-shot
related:
- held-offset-rotation-reach
- rotate-wrist-90deg-drifts-eef-recenter-after
---


Treat the held body offset as locally measured state, not a constant across loaded motion.

**Why:** In the winning run, a pan-body offset measured before a loaded servo predicted centering, but the next image showed about 5.9 cm residual y error; remeasuring and correcting that residual while airborne led to predicate success on release. The cause of the offset change is observed but unknown.

**How to apply:** After each large yaw or loaded Cartesian move, segment or manually sample 3-5 interior payload pixels, compute body-minus-EEF, set EEF xy to destination-minus-offset, servo with step_clip 0.003-0.006, and repeat until residual is within about 1-2 cm. Stop at a visually verified pre-contact handoff with clearance for the entire payload. Call pi0_place for final descent and release; do not execute historical support probes.

**Falsify:** If repeated post-servo measurements show the body-to-EEF offset invariant within 5 mm across yaw and loaded translation, the repeated measurement loop is unnecessary for that grasp.

**Related:** [[held-offset-rotation-reach]] [[rotate-wrist-90deg-drifts-eef-recenter-after]]
