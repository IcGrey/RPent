---
id: point-prompt-after-text-misground
scope: global
kind: perception
title: Switch to point prompts when text masks ignore the intended relation.
applies_when: A scene has duplicate objects or look-alike circular surfaces and SAM
  text segmentation selects the wrong instance
symptom:
- wrong-mask
- duplicate-object
- look-alike-surface
- relation-ignored
evidence:
  cells:
  - spatial_swap_t2_s0
  attempts: 2
confidence: single-shot
related: []
---


When a free-text segmentation prompt grounds the category but not the relation, choose the semantic target in agentview_high yourself and use a point prompt on that exact candidate.

**Why:** SAM text prompts in this solved run selected both the right distractor bowl and the stove burner before a point prompt on the visually chosen center bowl produced the correct mask.
**How to apply:** Inspect agentview_high for semantic identity first; if the overlay is wrong, stop changing noun wording and point-prompt a firm interior pixel on the chosen target. Accept the mask only if the overlay covers the intended object and the world xyz is consistent with the manual anchor.
**Falsify:** Text segmentation consistently returns the relation-satisfying instance across duplicate/look-alike layouts without point prompting.
**Related:** []
