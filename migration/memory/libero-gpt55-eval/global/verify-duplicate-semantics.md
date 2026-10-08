---
id: verify-duplicate-semantics
scope: global
kind: perception
title: Re-check duplicate identity before tuning a non-firing placement.
applies_when: A task has duplicate objects and repeated visually plausible placements
  do not trigger the predicate
symptom:
- nonterminal
- duplicate
- wrong-target
- visually-overlapping
evidence:
  cells:
  - spatial_swap_t4_s0
confidence: single-shot
related: []
---


Repeated clean-looking placements can be wasted work when the wrong duplicate was selected up front.

**Why:** The benchmark predicate is tied to the task-relevant object instance, while identical objects are visually interchangeable except for their spatial relation. In this cell, many cabinet-top-bowl placements looked correct but did not terminate; the drawer/open-cabinet duplicate terminated when placed with the seed-0 swap recipe.
**How to apply:** For duplicate objects, keep a semantic-doubt branch alive. If three or more clean placements on the right surface stay non-terminal, re-read task/reference memory and run a bounded perception-only duplicate audit before changing small placement offsets again.
**Falsify:** A future run shows the same duplicate selection terminating after only final-contact changes, with the alternate duplicate failing under an otherwise matched recipe.
**Related:** None.
