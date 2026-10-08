---
id: caddy-back-is-near-robot-pocket
scope: global
kind: perception
title: A container's named front/back compartment is in the CONTAINER's local frame,
  not the robot's — "back" can be the near-robot pocket
applies_when: task says put X in the "back"/"front"/"left"/"right" compartment/region
  of a multi-pocket caddy/organizer/tray/shelf
symptom:
- back compartment
- front compartment
- caddy
- organizer
- which pocket
- deep pocket wont fire
- place predicate not firing
- ambiguous compartment
evidence:
  cells:
  - 10_task_t5_s0
  attempts: 4
  solved_seeds:
  - 0
confidence: single-shot
related:
- libero-in-predicate-fires-while-grasped
---


For "put the cup in the back compartment of the caddy", the target region was the
SHALLOW pocket on the NEAR-robot side of the caddy — the caddy's own local
"back", which happened to face the robot. The deep far pockets (which read as the
intuitive "back" in the robot's view) were decoys and never fired.

**Why:** BDDL region sites are defined in the fixture's LOCAL frame. The object's
canonical orientation decides which pocket is "back"/"front"; it is independent of
where the robot sits. A caddy can be placed with its local back toward the robot.
**How to apply:**
- Do NOT equate "back" with "far from robot (most negative x)". Enumerate ALL
  pockets, get each world xy, and treat the named side as a HYPOTHESIS, not a fact.
- Use the hold-and-watch probe ([[libero-in-predicate-fires-while-grasped]]) to
  test candidate pockets cheaply. If the deep/far pockets fail, TEST THE NEAR one
  — even if its name ("front") seems to contradict the task word ("back").
- Physical fit is a strong prior on the WRONG target too: here only the deep
  pockets fit a low seat, which lured 3 attempts into them; the correct near
  pocket is shallow and the mug just perches — and that fires.
- Order probes to cover both local-frame interpretations (near AND far) before
  concluding a task is kinematically hard.
**Falsify:** a caddy/tray task where "back compartment" reliably maps to the
far-from-robot pocket across seeds, i.e. the region is defined in the world/robot
frame not the fixture frame.
**Related:** [[libero-in-predicate-fires-while-grasped]]
