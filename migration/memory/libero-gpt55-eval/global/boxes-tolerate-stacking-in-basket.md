---
id: boxes-tolerate-stacking-in-basket
scope: global
kind: strategy
title: For two-BOXES-into-basket, a second box resting on the first still fires In();
  do not require separated deep-floor placements like cans
applies_when: placing a second flat/box-shaped object into a small basket that already
  holds the first item, and the descent stalls high (object resting on the first item
  rather than reaching the floor)
symptom:
- descent stalled high in basket
- box resting on other box
- In predicate
- two items one small basket
- release without reaching floor
evidence:
  cells:
  - 10_swap_t1_s0
  attempts: 1
confidence: single-shot
related:
- box-vs-can-lid-wrist-disambiguation
---


When both target items are boxes, releasing the second box while it rests on the
first (descent stalled ~3cm high, eef z~0.578 vs empty-basket ~0.54) still
satisfies the In(basket) predicate — boxes do not roll off, so you need not
achieve well-separated floor-level placements.

**Why:** The In() region for the basket has vertical extent covering the cavity;
a box that comes to rest on top of / leaning against the first box stays put
(flat faces, high friction) and its centroid remains inside the basket footprint.
Cylinders (cans) at the same high stall roll to the rim/out and fail — the
contrast observed on sibling task 10_swap_t0 (2 cans) which required separated
deep-floor seats and took 3 attempts. Cause of the box's stability: observed,
mechanism (friction + flat contact) inferred not measured.

**How to apply:** For 2-boxes-into-basket, place box #1 flat near one side,
place box #2 over the remaining open area and simply descend until OSC stalls,
then release — do not spend effort forcing box #2 to the floor or separating
them. For 2-CANS, do the opposite: place well-separated and descend until the
can bottoms on the FLOOR (lower stall), never on the other can.

**Falsify:** A cell where a box resting on the first box at high stall does NOT
fire In() (e.g. the box tips out of a very shallow/steep-walled basket) would
bound this to only sufficiently deep baskets.

**Related:** [[box-vs-can-lid-wrist-disambiguation]]
