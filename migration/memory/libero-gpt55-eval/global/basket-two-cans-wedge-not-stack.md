---
id: basket-two-cans-wedge-not-stack
scope: global
kind: strategy
title: For a second object into a nearly-full container, wedge it against a closed
  wall, not onto the first object toward the open rim
applies_when: task requires putting TWO (or more) objects into one small container/basket
  whose floor only fits one, and a place onto/next-to the first object keeps rolling
  or sliding back out
symptom:
- second object rolls out of basket
- lands outside In-region
- predicate never fires
- can rolled to corner
- placed on top and slipped
- both-in-basket wont terminate
evidence:
  cells:
  - 10_swap_t0_s0
  attempts: 4
  solved_seeds:
  - 0
confidence: single-shot
related:
- basket-floor-is-single-can-pocket
---


A LIBERO "In container" predicate checks each object's CENTER is inside the container
rim bounding box (below the rim), NOT that objects sit flat — so a second object that
touches/leans on the first still counts, provided it comes to REST inside; place it
wedged against a CLOSED wall biased away from the container's lowest/open rim.

**Why:** The container floor is often a single-object pocket, so object #2 lands on
object #1's shoulder and rolls off. Which way it rolls decides pass/fail: toward the
low front rim it exits the region (fail); toward a tall closed wall it is caught and
its center stays inside (pass). The predicate is center-in-box, so a caught leaning
object satisfies it.

**How to apply:**
- Seat object #1 on the floor (descend until OSC stall at the LOW floor height).
- Carry object #2 HIGH enough to clear object #1, then position it against a CLOSED
  wall (the side furthest from the lowest rim — often the back or the far side that is
  clipped off-frame) immediately next to object #1.
- Descend until it stalls (it will stall high, resting on object #1 / the wall) and
  release from that low stall height — minimal drop = minimal roll.
- Bias the release xy AWAY from the open/low rim by ~2-4cm. Do NOT center it over the
  open rim, and do NOT place it toward the open side of object #1's shoulder.
- Retreat STRAIGHT up; the predicate typically fires on the next step once it settles.

**Falsify:** If a container's In-region actually requires objects to be flat/upright,
or if a wall-wedged leaning object with center inside still fails to terminate, this
is wrong.

**Related:** [[basket-floor-is-single-can-pocket]]
