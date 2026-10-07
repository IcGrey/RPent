---
id: relation-anchored-wrist-refine
scope: global
kind: perception
title: Anchor duplicate-object wrist refinement to a visible relation landmark.
applies_when: A task chooses one of multiple identical objects by a spatial relation,
  and wrist views can contain the wrong duplicate.
symptom:
- wrong duplicate
- wrist ambiguity
- stale coordinates
- relation target
- segmentation outlier
evidence:
  cells:
  - spatial_swap_t1_s0
  attempts: 6
confidence: single-shot
related: []
---


When duplicate objects are distinguished only by a relation, first move to a pose where the relation landmark and intended object appear together in the wrist view, then refine geometry for that same candidate; do not let wrist or stale coordinates choose among duplicates.

**Why:** The wrist camera is geometrically precise but locally ambiguous. In this solved run, stale eef coordinates and agentview bowl masks repeatedly drifted toward the lower duplicate, while a relation-safe wrist view containing both the target bowl and ramekin separated target bowl samples from ramekin samples and led to a clean pick.
**How to apply:** Use agentview RGB to choose the semantic relation, move 10-20 cm above the pair, require the relation landmark to be visible in wrist, sample the target in wrist, and reject any wrist candidate that lacks the landmark context or jumps to the known distractor. Keep Pi0 prompt short for the grasp, then carry with clearance to the pre-contact handoff and call pi0_place.
**Falsify:** If a future run shows wrist-only duplicate selection succeeding reliably without the relation landmark visible, or relation-anchored wrist samples repeatedly choose the wrong duplicate despite correct agentview identity, this lesson is too strong.
**Related:** []
