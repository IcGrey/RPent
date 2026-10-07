---
id: task-family_libero10_swap_t5
scope: task-family
suite: libero10
regime: swap
task_id: 5
task_language: pick up the book and place it in the back compartment of the caddy
evidence:
  cells: [10_swap_t5_s0]
  attempts: 1
  solved_seeds: [0]
  failed_seeds: []
confidence: single-shot
related:
  - vla-place-guard-policy
---
## Applicable pattern
Place the upright black book into the rear cell of the caddy's split middle column. The task tests caddy-compartment topology and guarded VLA insertion/release, not just dropping into any dark pocket.

## Winning technique
Identify the book in agentview as the upright black binder with gray pages and cover holes. Identify the destination as the rear/upper cell of the split middle caddy column; reject the paired front cell and both full-depth side pockets.

Move above the book, use wrist only to refine the same book candidate, then `pi0_pick("pick up the book")`. Confirm the grasp from a nonzero gripper gap and wrist view of the retained upright book. Firm the grip, lift vertically to full rim clearance, and carry through one high midpoint to the rear-cell handoff.

At the handoff, keep the book upright and above the split middle rear cell. Use short `pi0_place("place the book in the back compartment of the caddy")` windows. In this run two 20-step windows lowered and aligned the book but did not open; a scripted fallback release at the slot-aligned pose followed by a straight-up open retreat triggered termination as the book settled.

## Magic numbers
`pi0_pick max_chunks=20` (band 18-22), `lift_thresh=0.05` (band 0.05-0.06), `gripper_closed_thresh=0.06` (band 0.055-0.065).

High carry/handoff clearance: lift to kitchen high carry around `z=1.29-1.30` before lateral movement; do not move laterally while the hanging book is below the caddy rim.

Long carry: split book-to-caddy travel into at least one midpoint, with `step_clip=0.015-0.020` and gripper held closed.

VLA placement: start with `max_chunks=4`, `max_steps=20` (usable short-window band 20-40 cumulative before reassessing). Do not let one uninterrupted VLA placement run for 40-80 steps if the book starts pitching toward a divider.

Fallback release: after an executed VLA attempt and observed no-open drift, `placement_recovery(mode="scripted_fallback")`, then `release(max_steps=20)`, then vertical open retreat. The retreat may be the step that fires termination.

NEVER treat the side pockets as the destination.

NEVER rotate or drag a low held book inside the dividers.

NEVER use a zero-step rejected VLA call to justify scripted fallback.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| No failed full attempts in this cell; A1 solved. Two in-attempt VLA windows budget-exhausted without opening. | A1: Pi0 placement lowered/aligned the book but kept the gripper closed and began dividerward pitch. | Stop VLA before a jam, declare `scripted_fallback` with the observed no-open/pitch reason, release in place, and retreat straight up open. |
| Scripted release returns nonterminal even with the gripper open. | A1: predicate did not fire until the book settled after the gripper cleared away. | Inspect for hooks, then retreat vertically open rather than adding lateral motion. |

## Re-localization per scene
Book: segment prompt `the black upright book` worked in agentview with score 0.75. It looks like a vertical black binder with gray page block and round cover holes. Reject the yellow mug and any black caddy interior; the book has pages and a narrow upright rectangular silhouette. Wrist prompt `the black book` worked after moving over the same agentview book, but wrist identity is only a geometry check.

Destination: SAM did not ground `the back compartment of the brown caddy` (score below threshold), so use manual agentview topology. The caddy is brown with multiple dark pockets. The target is the rear/upper cell in the split middle column; the lower paired cell is the front compartment and the left/right full-depth pockets are distractors. Interior pixels beat mask medians because rims and dividers bias the depth.

Reject rule: if wrist or segment localizes a caddy surface more than about 5 cm from the agentview rear split-cell anchor or lands on a side pocket/front cell, reject it and keep the agentview topology choice.

Counter-example absolutes from this one seed only, not reusable coordinates: book agentview segment near `[-0.053, -0.013, 0.968]`; rear split-cell region median near `[-0.454, -0.155, 0.999]`; front paired cell near `[-0.386, -0.151, 0.958]`.

## Fragility flags
Most fragile step: the VLA handoff can keep the gripper closed and pitch the book into a divider. Use short observed increments, stop when dividerward pitch begins, and fallback only after a real VLA attempt with the book still slot-aligned.

Second fragility: release may be nonterminal until the open gripper retreats vertically. Do not conclude wrong compartment from the release step alone when the book is visibly supported in the target.

## Difficulty and reliability
This cell converged in one attempt with a guarded VLA-plus-fallback placement. Expected single-shot rate is moderate: localization and grasp are reliable, but the insertion is sensitive to book pitch and whether the policy opens. The validated outcome is successful with `pi0_place` alignment plus scripted fallback; this run is not evidence that native VLA release alone succeeds.

## Cross-refs
[[vla-place-guard-policy]]
