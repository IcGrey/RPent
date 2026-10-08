---
id: brand-label-over-segmentation
scope: global
kind: perception
title: Let readable RGB labels overrule low-confidence category masks.
applies_when: Grocery or packaged-object tasks name a brand/flavor/label and similar
  packages share shape or color.
symptom:
- wrong-object
- low-score-segment
- brand-confusion
- similar-cans
evidence:
  cells:
  - object_task_t1_s0
  attempts: 1
confidence: single-shot
related: []
---


When a task names a specific grocery label, use agentview_high.png label/appearance as the identity authority and treat SAM masks as geometry candidates only after the overlay matches that identity.

**Why:** SAM-style segmentation may ground the general category (`can`) instead of the named label; in object_task_t1_s0, `the alphabet soup can` selected the tomato sauce can even though the alphabet soup label was visually readable in agentview.
**How to apply:** First choose the target by RGB label and global layout in agentview_high.png. Back-project manual pixels on that chosen package, or use point prompting on it. Reject any text mask whose overlay lands on a look-alike, regardless of plausible score. Use wrist only to refine geometry for the same candidate.
**Falsify:** A future run where the text mask consistently selects the correct labeled package across similar grocery distractors without manual RGB checking would weaken this rule.
**Related:**
