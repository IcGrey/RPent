---
id: task-family_libero10_task_t5
scope: task-family
suite: libero10
regime: task
task_id: 5
task_language: pick up the cup and place it in the back compartment of the caddy
evidence:
  cells:
  - 10_task_t5_s0
  attempts: 4
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Pick a white/yellow mug ("cup") from the open table and place it into a NAMED
compartment of a brown multi-compartment desk caddy (a fixture). The whole
difficulty is TARGET IDENTITY: the caddy has several look-alike pockets and the
task names one ("back compartment"). The manipulation itself is a trivial
pick + lower-into-pocket. This is a disambiguation task, not a dexterity task.

## Winning technique
1. Pre-position eef directly above the mug: `move_to (mug_x, mug_y, ~1.06) gripper -1`.
2. `pi0_pick "pick up the white and yellow mug" max_chunks=10`. Success criterion:
   gripper opening settles to ~0.01 (holding the rim), peak_lift > 0.05. NOTE the
   pi0 `success` flag can read false (descent_done) even on a good grasp — judge by
   opening + lift, not the flag.
3. `set_gripper +1 steps 8` to firm the rim grip.
4. Raise above the caddy rim: `move_to (mug_x, mug_y, ~1.20) gripper 1` (caddy rim
   top z~1.05; carry high so the mug base clears it).
5. Traverse to over the target pocket in <=0.30 xy hops, gripper 1.
6. Lower into the pocket: `move_to (target, ~1.06) gripper 1 step_clip 0.02`.
   The In predicate fires WHILE STILL GRASPED (LIBERO In checks object pose, held
   or released) — no release needed once libero_terminated flips.
   Per-step success: watch `libero_terminated` on every lowering step.

TARGET = the caddy's LOCAL "back" pocket, which is the SHALLOW center pocket on
the NEAR-robot side (smallest world-x magnitude among the pockets), NOT the deep
far compartments.

## Magic numbers
- pi0_pick max_chunks=10 (band 9-12); rim grasp gripper opening ~0.011 = holding.
- Held-mug offset (rim grasp): mug_center = eef + (dx~+0.02, dy~-0.052). To place
  mug at (X,Y): eef=(X-0.02, Y+0.052).
- Carry z ~1.20 (mug base clears caddy rim z~1.05). Lower target eef z ~1.06.
- Lowering step_clip 0.02; OSC walls at eef z~1.11 (mug base ~1.0) — that is deep
  enough for the shallow near pocket to fire; do NOT keep fighting for lower z.
- NEVER target the deep far compartments for "back compartment" (they never fire).
- NEVER rely on release to fire the predicate — it fires on pose while held.
- NEVER re-grasp a mug already sitting inside a caddy pocket (pi0 won't descend/
  engage; it grabs air). If you mis-place, `reset` rather than re-grasp in-pocket.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| mug seated fully+upright in LEFT deep compartment, no fire | A1: wrong target — LEFT deep pocket is not "back" | target the near shallow center pocket instead |
| mug perched over CENTER-BACK deep pocket, no fire | A2: wrong target + mug too wide to descend the deep narrow pocket | ditto |
| mug perched over RIGHT cavity, no fire | A3: wrong target | ditto |
| pi0_pick grabs air when re-grasping a pocket-seated mug | A1,A3: pi0 won't descend into a caddy pocket to re-grasp | reset for a clean open-table grasp |
| OSC descent into caddy stalls ~z1.11, eef drifts forward | all: far-reach IK near limit at low z | acceptable — the shallow near pocket fires at z~1.11; overshoot eef_x by ~0.02 to counter drift if you need a specific x |

## Re-localization per scene
- Caddy: brown leather desk organizer, fixture (not in object_names). Segment
  "caddy"/"brown organizer"; back_project pocket floors/rims. Long axis = world-y
  (image left-right); depth = world-x (short). Rim top z~1.05, table z~0.90.
- Mug ("cup"): segment "white and yellow mug" (score ~0.7-0.9). Body dia ~0.10m,
  height ~0.09m. Grasp at rim.
- "back compartment": DO NOT cache this run's absolutes. Re-derive per scene: it is
  the caddy's local-back pocket = the shallow pocket on the NEAR-robot side (the
  one with smallest |world-x|, in front of the tall deep row). Confirm the near
  pocket in RGB (a low-walled open pocket, distinct from the tall deep pockets and
  from the raised solid platform). Deep far pockets are DECOYS for this task.

## Fragility flags
- Most fragile step: TARGET CHOICE. If a clean, well-placed mug in a deep pocket
  does not fire, do NOT assume physics/grasp failure — switch pockets (esp. to the
  near shallow one) before anything else. This flipped a near-"impossible" verdict
  into an immediate solve.
- Second: re-grasping a pocket-seated mug is unreliable; prefer reset.

## Difficulty and reliability
- 4 attempts to converge, entirely due to target-identity search (3 wrong pockets
  then the right one). Manipulation was reliable every time. With the target known
  (near shallow center pocket), expected single-shot.
- Nothing stayed unsolved.

## Cross-refs
- [[caddy-back-is-near-robot-pocket]]
- [[libero-in-predicate-fires-while-grasped]]
