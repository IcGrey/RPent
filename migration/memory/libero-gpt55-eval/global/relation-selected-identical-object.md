---
id: relation-selected-identical-object
scope: global
kind: perception
title: Select identical targets by the named spatial relation before wrist refinement
applies_when: A task contains duplicate or visually identical objects and names a
  relation such as on, left of, right of, between, or next to
symptom:
- duplicate object
- wrong target
- relation
- swap
- look-alike
evidence:
  cells:
  - spatial_swap_t7_s0
  attempts: 1
confidence: single-shot
related: []
---


When duplicate objects look the same, choose the target from agentview by the spatial relation in the task language, then use wrist only to refine that same candidate's geometry.

**Why:** In the solved run, two identical patterned black bowls were visible; the correct one was selected because it sat on the stove burner, while the decoy sat on the cabinet top. Wrist close-up confirmed the selected candidate but its depth samples skewed toward the visible rim, so wrist geometry alone would not be a reliable semantic selector.

**How to apply:** In agentview_high, identify every duplicate and the relation landmark. Back-project 3-8 pixels on the relation-satisfying candidate and the landmark/surface, then move over that candidate. Accept wrist refinement only if it remains spatially consistent with the agentview anchor; otherwise keep the agentview identity anchor and adjust only with visual evidence.

**Falsify:** A future run where wrist-only identification consistently selects the relation-satisfying duplicate despite an equally visible look-alike, or where agentview relation grounding selects the wrong object after correct relation-landmark classification.

**Related:**
