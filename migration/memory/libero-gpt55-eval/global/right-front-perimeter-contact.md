---
id: right-front-perimeter-contact
scope: global
kind: strategy
title: Test perimeter contact zones before rejecting a fixture-relative placement.
applies_when: A fixture-relative goal says front or side and central visual bands
  fail despite clean object placement
symptom:
- central_band_false
- front_of_fixture_false
- held_descent
- perimeter_zone
evidence:
  cells:
  - goal_task_t5_s0
  attempts: 10
confidence: single-shot
related:
- visual-over-pick-heuristic
---


A fixture-relative predicate may be satisfied at a specific perimeter/contact zone rather than the visually central face band.

**Why:** observed, cause unknown. In this run, multiple push and held-placement attempts at central front, negative-y, diagonal front-edge, and far/back stove zones stayed false, but a held descent at the stove right/front perimeter terminated before release.
**How to apply:** After semantically classifying the fixture in RGB, sample candidate perimeter zones around the fixture rather than only its center. For box-like objects, use Pi0 grasp-only, carry with `gripper:+1`, and descend while still holding at the candidate perimeter; keep z targets in the frame-appropriate band and watch for termination during contact/stall.
**Falsify:** If a future cell with the same final-region predicate terminates reliably from a central band release and not from perimeter contact, this is not a general fixture-relative rule.
**Related:** [[visual-over-pick-heuristic]]
