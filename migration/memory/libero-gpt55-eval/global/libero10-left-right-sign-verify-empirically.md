---
id: libero10-left-right-sign-verify-empirically
scope: global
kind: perception
title: Do not trust a fixed left/right sign for "right/left of X" predicates; verify
  empirically
applies_when: a task says put an object to the left/right of a reference and you must
  choose +y vs -y for the placement
symptom:
- put to the right of the plate
- left/right of
- egocentric
- geometrically clean placement no termination
- wrong side
evidence:
  cells:
  - 10_task_t6_s0
  attempts: 3
confidence: single-shot
related:
- predicate-gated-by-eef-proximity-retreat-clear
---


The "right"/"left of X" goal predicate sign is NOT reliably robot-egocentric:
in libero_10 task-t6 "to the right of the plate" fired for +y (IMAGE-RIGHT /
viewer perspective), the OPPOSITE of the common egocentric rule (+y=robot-left=
image-right, so right=-y). Verify the side empirically instead of assuming.

**Why:** observed. The corpus egocentric heuristic (+y = robot-left = image-right)
predicts right = -y = image-left, but this cell's predicate evaluated the pudding
"to the right of the plate" as satisfied at +y and unsatisfied at -y. The sign
convention of the underlying spatial predicate here is viewer/world +y = "right",
not robot-egocentric. Do not over-generalize either sign.
**How to apply:** When a clean placement of the CORRECT object on your guessed
side does not terminate (and the eef is retreated clear, see related), flip to
the OTHER side before suspecting the co-clause (e.g. the On() half). Budget one
probe per new seed: place, retreat clear, check; if false and geometry is clean,
try the opposite y-sign. Keep the co-object's placement fixed while flipping.
**Falsify:** A libero_10 left/right cell that fires on the egocentric side
(right=-y), confirming the egocentric rule for that task — record it as a
counter-example so the sign is treated as task-specific, not global.
**Related:** [[predicate-gated-by-eef-proximity-retreat-clear]]
