---
id: low-contact-seat-after-release
scope: global
kind: strategy
title: Use short low contact to seat an upright object after an off-center release
applies_when: An object is already upright on the intended surface but the On predicate
  did not fire after release
symptom:
- release_false
- rim_perched
- on_predicate_not_firing
- object_upright_on_target
evidence:
  cells:
  - spatial_swap_t5_s0
  attempts: 1
confidence: single-shot
related: []
---


A short capped Pi0 contact/pick command from a low pose can seat an already upright object enough to fire an On predicate after a manual release leaves it perched on the target rim.

**Why:** observed, cause unknown; in this run the object was already on the correct plate but off-center, and the short low contact moved or settled it enough for termination without a fresh carry.

**How to apply:** First verify the object identity and destination are correct in RGB. Retreat just enough for a clean view, move low over the target center with the gripper open at a safe floor-limited z, then issue a short prompt such as `pick up the black bowl` with max_chunks around 10-12. Stop once the predicate fires; do not let Pi0 perform a full pick-and-place.

**Falsify:** If the object is tipped, off the destination surface, or the destination was a semantic look-alike, this should not be expected to work; a successful re-pick and re-place or reclassification would be required.

**Related:**
