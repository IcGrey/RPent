---
id: task-family_libero10_task_t6
scope: task-family
suite: libero10
regime: task
task_id: 6
task_language: put the red mug on the plate and put the chocolate pudding to the right
  of the plate
evidence:
  cells:
  - 10_task_t6_s0
  attempts: 3
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Two-clause LIVING_ROOM tabletop task: (1) place a TALL red mug On a plate, and
(2) place a chocolate-pudding box "to the right of" the plate. The real
difficulties are NOT the grasps — they are (a) the tall mug's grasp geometry,
(b) the ordering so the second carry does not tip the first placement, and
(c) two predicate subtleties: the "right" side sign, and an eef-proximity gate.

## Winning technique
Order: PUDDING FIRST, MUG LAST (never carry/re-grasp over the placed mug).
1. Pre-position over the pudding box; `pi0_pick "pick up the chocolate pudding box"`
   (chunks ~14) -> lift ~0.08, grip ~0.047. `set_gripper +1`.
2. Carry to the +y (IMAGE-RIGHT) side of the plate, x-aligned with plate center,
   just outside the rim; `release`. (Success: box on table, clearly image-right
   of the plate.)
3. Retreat up, waypoint back toward the mug (keep single-step |Δxy|<0.30).
4. Pre-position ~(mug_x, mug_y+0.045, 0.62); `pi0_pick "grasp the red mug by the
   handle"` (chunks ~15). pi0 hooks the thin handle (grip ~0.01, lift ~0.20) and
   auto-drives the eef forward to ~plate x. `set_gripper +1`.
5. Position eef = plate_center - (0.05,-0.03) [the held-mug base hangs ~+0.05 x,
   -0.03 y from the eef]; descend until OSC stalls (~z0.57 = mug base on plate);
   `release`. (Success: mug upright, base centered within the plate rings.)
6. Retreat the eef straight up AND then LATERALLY AWAY from the mug/plate. The
   predicate may fire only once the gripper is clear (see Failure modes A3).

## Magic numbers
- Frame LIVING_ROOM: eef home z~0.681, table top~0.445, plate top~0.445.
- pudding pi0_pick max_chunks=14 (band 12-16); lift~0.08; grip~0.047.
- mug pi0_pick "by the handle" max_chunks=15 (band 12-18); grip~0.01; lift~0.20.
- mug place: eef offset from plate center = -(0.05,-0.03); descend to OSC stall z~0.56-0.57; step_clip 0.015.
- carry/retreat z 0.60-0.64; single-step |Δxy| < 0.30 ALWAYS (waypoint long moves).
- NEVER carry the second object across the plate's y at the mug's x after the mug is placed.
- NEVER pi0-re-grasp a small object sitting within ~0.15 m of the placed mug (pi0 drifts into it).

## Failure modes
| symptom | root cause (A#) | fix |
|---|---|---|
| Pi0 descends into the mug's open top, gripper stays open ~0.06, no lift | plain prompt "grasp the red mug" on a wide-mouth TALL mug (A1) | prompt "grasp the red mug BY THE HANDLE" |
| Standing mug tipped off plate mid-task | carried the pudding box across x~0.14 at the plate's y, box (hanging below eef) clipped the mug (A1) | ORDER pudding-first, mug-last; never cross over the placed mug |
| Placed pudding at -y (image-left) + perfect mug, no termination | wrong "right" side; "right" here = +y image-right (A2) | place pudding on +y (image-RIGHT) side |
| In-episode pi0 re-grasp of pudding swung into the mug and tipped it | pi0 drifts toward the larger/nearer object during re-grasp (A2) | do not pi0-re-grasp near the placed mug; use scripted grasp or avoid |
| Perfect final config but libero_terminated stays FALSE for many steps | open gripper hovering directly over the just-placed mug gated the predicate (A3) | retreat the eef fully AWAY (laterally) from the placed objects; it fired on the next step |

## Re-localization per scene
- red mug: agentview hi-res, tall red-with-white-pattern mug. Grasp target is the
  thin curved HANDLE (offset to one side). Do NOT trust wrist to re-identify.
- plate: white disc with red concentric rings; use region back_project over the
  rings for a rim-unbiased center. radius ~0.10.
- pudding: brown box reading "CHOCOLATE PUDDING". Distinct; pi0 grasps top-down.
- porcelain mug: white dimpled mug = DISTRACTOR, never named. Ignore.
- This run's absolute xyz MUST NOT be cached (task perturbation re-randomizes);
  they are counter-examples only.

## Fragility flags
- Most fragile step: reading the "right" side. It is +y (image-right) here,
  CONTRARY to the egocentric memory rule — verify empirically per seed (place,
  retreat clear, check; if no fire and geometry is clean, try the OTHER side).
- Second fragile step: concluding failure too early. Always RETREAT THE EEF CLEAR
  of the placed objects before deciding the predicate failed.

## Difficulty and reliability
- Converged in 3 attempts. The two lost attempts were an avoidable tip cascade
  (A1) and a risky in-episode re-grasp (A2); with the known levers (order,
  handle grasp, +y side, retreat-clear) this should be ~single-shot.
- Honest note: the "right" side and the eef-proximity gate were only discovered
  by trial; a fresh seed should budget one probe to confirm the side.

## Cross-refs
- [[pi0-grasp-tall-mug-by-handle]]
- [[predicate-gated-by-eef-proximity-retreat-clear]]
- [[libero10-left-right-sign-verify-empirically]]
- [[place-order-never-carry-over-placed-object]]
