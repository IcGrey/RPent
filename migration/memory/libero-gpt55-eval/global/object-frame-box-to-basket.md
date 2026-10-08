---
id: object-frame-box-to-basket
scope: global
kind: strategy
title: Place flat grocery boxes into baskets by targeting the liner interior.
applies_when: Object-frame task asks for a flat box or carton to be placed in a basket
symptom:
- basket
- box
- rim
- object-frame
- grocery
evidence:
  cells:
  - object_swap_t6_s0
  attempts: 1
confidence: single-shot
related: []
---


For object-frame basket tasks with flat grocery boxes, use agentview for label identity, wrist only for same-candidate geometry, then release over the basket liner interior even if the final descent stalls above the requested low z.

**Why:** The basket rim and woven sidewalls produce biased placement coordinates, while the predicate fired once the held box was visually inside the white liner at eef z about 0.15.
**How to apply:** Back-project 3-5 target label/top pixels, move above at z 0.17-0.20, `pi0_pick` with a short object prompt, lock with `set_gripper +1` for 5-10 steps, carry at z 0.20-0.24 with `step_clip` about 0.012, and release over the liner/cavity rather than a rim pixel.
**Falsify:** A future run where a visually centered release over the liner at comparable height fails while a rim-biased or deeper-only release succeeds would weaken this lesson.
**Related:**
