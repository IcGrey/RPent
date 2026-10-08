---
id: sam3-brand-noun-can-collision
scope: global
kind: perception
title: Disambiguate look-alike cans by RGB label, never by SAM3 brand-noun prompt
applies_when: two or more similar cans/cylinders are present and the task names one
  by brand ("tomato sauce", "alphabet soup", a soup can)
symptom:
- same box for different prompts
- two cans
- wrong can grabbed
- sam3 low score
- brand noun
- tomato sauce
- alphabet soup
evidence:
  cells:
  - 10_task_t0_s0
  attempts: 1
confidence: single-shot
related: []
---


SAM3 cannot reliably ground grocery BRAND nouns; when two similar cans are
present, prompts for two different brands often return the SAME can.

**Why:** SAM3's text grounding keys on coarse shape/appearance, not on printed
brand text. Both "tomato sauce can" and "alphabet soup can" matched the single
most can-like object (highest objectness), regardless of which brand was on it.
The score was even high (0.77-0.90) for the wrong prompt, so score is not a guard.

**How to apply:** Decide can identity in the agentview hi-res RGB by LABEL colour
and imagery, not by the SAM3 label: e.g. tomato_sauce = red/tomato label,
alphabet_soup = blue label. Use SAM3 only to get a pixel/box for a can you have
ALREADY identified by eye. Confirm again in the wrist cam (label rim colour)
before pi0_pick. Do not let the wrist re-identify freely — it locks onto
look-alikes too.

**Falsify:** If, on a scene with two brand-labeled cans, distinct brand prompts
reliably return distinct cans with the correct one top-ranked, this no longer
holds.

**Related:** [[pi0-pick-may-place-at-trained-left]]
