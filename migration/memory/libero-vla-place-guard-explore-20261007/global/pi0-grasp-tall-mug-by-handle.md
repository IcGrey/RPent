---
id: pi0-grasp-tall-mug-by-handle
scope: global
kind: primitive
title: Grasp a tall wide-mouth mug by its handle, not from above
applies_when: picking a tall mug/cup whose open top is wider than the gripper, where
  pi0_pick keeps descending into the cup and grabbing air
symptom:
- pi0 descends into mug
- gripper stays open ~0.06
- peak_lift ~0
- grabbed air
- mug not lifted
- cup interior visible in wrist
evidence:
  cells:
  - 10_task_t6_s0
  attempts: 3
confidence: single-shot
related:
- pi0-pick-prompt-specificity
---


For a tall mug with a mouth wider than the gripper opening, `pi0_pick "grasp the
{color} mug"` drives the gripper straight down into the open top and closes on
nothing; prompt it to grasp the HANDLE instead.

**Why:** The default pick prompt makes pi0 aim at the object's top-center. On a
wide-mouth mug the two fingers straddle the rim and enter the cavity, so closing
grips air (finger separation stays ~0.06, no lift). The thin side handle is a
solid, narrow feature pi0 can pinch (finger separation closes to ~0.01).
**How to apply:** Pre-position ~15-20 cm above the mug, offset the eef slightly
toward the handle side / +y, then `pi0_pick "grasp the {color} mug by the handle"`
with max_chunks 12-18. Confirm grip_opening ~0.01 and peak_lift > 0.15. pi0 often
also auto-carries the eef forward after lifting — that is fine; firm with
set_gripper +1 and take over the carry. The mug then hangs with its base offset
~(+0.05,-0.03 m) from the eef; use the measured offset to reach a pre-contact handoff with the entire mug clear of the rim. Call pi0_place for final alignment, descent and release.
**Falsify:** A tall mug that pi0 lifts cleanly from the plain top-center prompt
(narrow mouth), or a handle-grasp that fails to close on the handle.
**Related:** [[predicate-gated-by-eef-proximity-retreat-clear]]
