---
id: task-family_libero10_swap_t5
scope: task-family
suite: libero10
regime: swap
task_id: 5
task_language: pick up the book and place it in the back compartment of the caddy
evidence:
  cells:
  - 10_swap_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related: []
---


## Applicable pattern
Pick a standing black binder ("book") and drop it into a specific compartment of
a multi-compartment desk caddy. Tests (a) semantic disambiguation of WHICH
compartment is the "back compartment", and (b) a clean top-down insert of a tall
thin object into a snug opening. Solved first try, no reset.

## Winning technique
1. `pi0_pick "pick up the book"` (max_chunks=16, lift_thresh=0.05). Pi0 grasps
   near the TOP of the standing binder. Success signal: peak_lift ~0.07m,
   gripper opening ~0.03 (holding, not shut). Book then hangs vertically ~0.13m
   below the eef.
2. `set_gripper +1 steps=8` to firm the grip.
3. `move_to` STRAIGHT UP to z~1.22 so the hanging book base clears the caddy rim
   (~z1.03-1.05) before any lateral motion.
4. Traverse to over the back-compartment center in 2 hops (each |dx|<0.30):
   mid waypoint, then final xy, both at carry z~1.21, gripper=1.
5. `move_to` DOWN to z~1.08 with step_clip=0.015, gripper=1. It STALLS ~z1.157
   when the book base contacts the compartment floor — that stall = seated.
6. `release` (max_steps=20). Predicate did NOT fire yet at this point.
7. `move_to` STRAIGHT UP to z~1.24, gripper=-1, step_clip=0.02. libero_terminated
   flips true as the gripper clears the settled book.

## Magic numbers
- pi0_pick max_chunks=16 (band 12-20), lift_thresh=0.05.
- carry z ~1.21-1.22 (must put book base above caddy rim z~1.03-1.05).
- descend target z~1.08; it self-stalls ~1.157 on floor contact (do NOT force lower).
- descend step_clip=0.015; retreat step_clip=0.02.
- traverse hop rule: keep each move_to |dx| and |dy| < 0.30.
- NEVER traverse laterally with the book base below the caddy rim (collides front wall).

## Failure modes
| symptom | root cause (A#) | fix |
|---|---|---|
| (none — solved on A1) | - | - |
| predicate false immediately after release | gripper still occupying the opening | retreat straight up; predicate fired once gripper cleared |

## Re-localization per scene
- BOOK: standing black binder (lever-arch look, round hole on cover). Grasp via
  `pi0_pick "pick up the book"` from home — Pi0 finds the top on its own. Median
  a few hi-res pixels on the cover for its xy only if pre-positioning.
- CADDY BACK COMPARTMENT: this caddy has a big LEFT compartment (undivided,
  full-depth), a MIDDLE column split front/back, and a RIGHT elevated
  compartment. The only front/back PAIR is the middle column, so "back
  compartment" = the middle-REAR opening and "front compartment" = the small
  middle-front one. Get its interior center with region `back_project` over the
  dark interior pixels (this run: center ~(-0.454,-0.152); DO NOT cache — swap
  re-randomizes, re-derive every scene). World frame here: +x = toward robot
  (bottom of image), +y = image-right; "back" = smaller/more-negative x.
- Book footprint (~8cm x 3cm) matched the compartment (~8cm y x 5cm x) at the
  default wrist yaw, so no rotate_wrist was needed. If the held book's wide face
  lies along the compartment's SHORT axis, rotate_wrist 90deg before descending.

## Fragility flags
- Compartment identity is the main risk. If a clean insert+release does NOT fire
  the predicate, SUSPECT WRONG COMPARTMENT before wrong physics — re-classify the
  middle-rear vs left/right openings in RGB.
- Book must be lifted above the rim before traversing, or the base clips the
  caddy front wall.

## Difficulty and reliability
Solved single-shot in 8 primitives, 1 attempt. Expected high single-shot rate;
the delicate parts are compartment ID and rim clearance, both handled by the
sequence above.

## Cross-refs
- [[predicate-fires-after-gripper-retreat]]
