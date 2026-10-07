---
id: vla-place-guard-policy
scope: global
kind: infra
title: Guarded VLA placement exploration and recovery accounting.
applies_when: This guarded placement experiment.
confidence: single-shot
evidence:
  cells:
  - vla-place-pilot-20261006/explore-r2
  - vla-place-pilot-20261006/eval
related: []
---
Use agentview to identify named objects and target spatial relations, then
wrist/depth to refine the SAME candidates. Re-localize every run. Keep payload
orientation and clearance during carry; EEF center is not object center.

This experiment requires pi0_place for final placement at a visually confirmed,
pre-contact handoff. Explicitly inspect retention and target entry/clearance first.
Curated pre-placement excerpts are supplied in task-family/preplacement_*.json. Their coordinates are historical references requiring re-localization. Final placement scripts remain excluded; do not search another corpus.
The harness guards all scripted opening after pick/closure, including default open
move_to/move_pose, and re-picking. A zero-step rejected pi0_place is not an attempt.
Only after a real VLA attempt may placement_recovery(mode="scripted_fallback",
reason=<observed issue and support/clearance check>) permit a scripted release.
An actually empty/lost grasp must be declared with mode="empty_gripper" and current
visual evidence before retrying. Never use that declaration to release a held item.

Use a single-object placement prompt. Keep opening defaults 0.07 m / 3 steps.
For the book start with at most 20 VLA steps (4 chunks) because earlier 40/80-step
calls pitched it into the divider. For mugs a 60-step (12-chunk) initial window
can encompass the previous 48-step release. These are exploration candidates.
After exhaustion inspect held-object-to-target error and orientation, not just
visibility. If progress remains safe, continue for at most 20 steps per call,
re-observing each time; stop the handoff trial by 120 cumulative VLA steps.
Do not continue after harmful drift, loss, divider contact or a support miss.

After release_detected while nonterminal inspect target support, tilt and hooks.
Retreat straight up open, then re-observe before any lateral motion. Stop all
physical actions on terminated; termination while held is not release evidence.
Record handoff pose/image, payload geometry, exact prompt, per-call and cumulative
budget, stop_reason, release/post-retreat stability, recovery declarations and final
native result. Failed handoffs are evidence; scripted fallback is not VLA success.
On an exploration reset change handoff, prompt or budget based on the failure;
do not reset merely to run a fully scripted placement instead. Save failures too.
