---
id: task-family_libero10_swap_t4
scope: task-family
suite: libero10
regime: swap
task_id: 4
task_language: put the white mug on the left plate and put the yellow and white mug
  on the right plate
evidence:
  cells:
  - 10_swap_t4_s0
  attempts: 24
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- held-offset-rotation-reach
- place-order-never-carry-over-placed-object
- libero10-left-right-sign-verify-empirically
---


## Applicable pattern

Two visually distinct mugs must remain upright on two look-alike plates while a tall distractor constrains the carry corridor. In this swap cell, the successful predicate binding used visual image sides, not the previously assumed robot-frame left/right mapping.

## Winning technique

Localize both mugs, both ceramic red-ring plates, and the red distractor from agentview RGB plus median back-projection; wrist-refine the same plate candidates. Manipulate the difficult yellow/white mug first. Pre-position over its agentview anchor, use the short prompt `grasp the yellow and white mug` with `max_chunks=8`, accept the loaded ~11 mm rim hook from visual lift evidence, firm for 8 steps, lift high, and use level `move_pose` to yaw +1.57. Measure the held body offset after yaw. Route through far negative x, approach the image-right/+y plate, correct using wrist geometry, then add the empirically required +0.04 m world-x footprint bias. Descend vertically until support stalls, open in 1/2/3/5-step stages, release, and retreat straight up.

Route the empty gripper back through far negative x, restore yaw 0, and pre-position at the white mug's handle side. Use `grasp the white mug by the handle`, `max_chunks=8`; require visible lift and exterior contact. Firm, lift high, yaw +1.57 level, and re-measure the held-body offset. Carry to the image-left/-y plate, apply wrist correction plus the same +0.04 m x footprint bias, descend vertically to support, and open in stages. Termination fired during the 3-step opening stage.

Per-step success criteria: target visibly airborne after each pick; red distractor upright after each corridor segment; pitch near zero after yaw; held-body/plate center agreement within ~1 cm before descent; descent stalls from support rather than lateral collision; mug remains upright during staged opening.

## Magic numbers

- Pi0 grasp-only: `max_chunks=8` (usable band 7-8); reissue rather than extending beyond 8.
- Grip firming: 8 steps (usable band 8-10).
- Carry height: eef z 0.70-0.72 m (usable band 0.68-0.74 m).
- Offset redirection: yaw +1.57 rad (usable band 1.53-1.61), pitch target 0.
- Loaded motion: `step_clip=0.006-0.012`; final descent `0.003` (usable band 0.003-0.006).
- Empirical landing correction: +0.04 m world x after same-frame wrist correction (observed useful band +0.035 to +0.045 m).
- Staged opening: 1, 2, 3, then 5 steps; check termination after each.
- Safe route: far negative-x corridor around x=-0.24 to -0.27 m, with each XY leg below 0.30 m.
- NEVER carry with gripper -1.
- NEVER let Pi0 continue into placement.
- NEVER side-push an upright mug on a plate.
- NEVER cache this seed's absolute coordinates or infer semantic identity from wrist alone.

## Failure modes

| symptom | root cause (A<N>) | fix |
|---|---|---|
| Both mugs tipped on release | A1 used inside-rim hooks and off-center landings | Require support contact, staged opening, yaw-offset control |
| Correct plates but both mugs tipped | A2 inside-finger wall/rim contacts shoved cups while opening | Prefer exterior handle grasp; stage rim-hook release |
| White became horizontal during yaw flip | A3 used a 180° in-air wrist flip with residual tilt | Use level simultaneous pose and only +90° |
| Upright alignment still leaned after release | A4 short rim hooks landed with uncompensated offsets | Measure offset after each pick |
| White edge-seated; yellow drifted on slope | A5 handle hang exceeded center reach and yellow remained rim-hooked | Rotate hang into x before carry |
| Centered top-down grasp stalled on rim | A6 open fingers could not pass the wider rim | Do not script a deep top-down body pinch |
| Pitched side pinch closed on air | A7 tested clear side geometry without capturing both walls | Use trained handle/rim contact |
| Thin plate could not be grasped | A8 direct rim closure collapsed to air | Leave plates fixed |
| Pi0 plate pull was directionally asymmetric | A9 +y plate moved outward | Avoid language-grounded plate relocation |
| Scripted rim drag lost contact | A10 top-down closure did not retain thin plate | Change held-object offset, not plate pose |
| Both upright but systematic negative-x miss | A11 held surface pixels overestimated body center | Calibrate from post-release footprint |
| Centered robot-frame placements stayed false | A12 wrong predicate binding for this cell | Test image-side binding |
| Reversed test damaged yellow before completion | A13 long handle prompt tipped yellow | Yellow first, short plain prompt |
| Reversed placements confounded by red contact | A14 direct carry grazed distractor | Far-negative-x corridor |
| Clean reversed placement still false | A15 footprint centering was only visual, not calibrated | Add quantitative footprint calibration |
| Recovery push tipped white | A16 side contact coupled into tilt | No post-placement pushes |
| Red occupied destination | A17 white carry crossed distractor | Use farther -x corridor and staged y waypoints |
| Yellow leaned after narrow recovery grasp | A18 wide-looking contact collapsed after firming | Use the stable short anchored pick from the initial scene |
| Handle-root prompt produced only 14.7 mm | A19 neutral-yaw yellow handle targeting missed exterior load | Use plain yellow prompt at anchored body |
| Pre-yaw +1.57 entered cavity | A20 handle-root geometry put fingers inside | Yaw only after lifting |
| Pre-yaw -1.57 showed clearance but no load | A21 apparent 47.7 mm opening collapsed to air on lift | Judge load from lift plus wrist evidence |
| Same-frame surface correction left 3.5-4.3 cm -x bias | A22 sampled inner/base surface was not footprint center | Add +0.04 m world-x empirical bias |
| Precisely centered robot-frame binding stayed false | A23 target assignment, not geometry, was wrong | Reverse to image-side binding while preserving calibrated mechanics |

## Re-localization per scene

- Yellow/white target mug: agentview authority; short two-tone yellow body with white interior, distinct from the tall red patterned mug and textured white mug. Manual RGB points plus 3-8 interior/body back-projections worked. If using segmentation, try `yellow and white mug`, then `short yellow cup with white rim`; reject any mask >5 cm from the agentview anchor or on the red mug.
- White target mug: agentview authority; short textured/pebbled white porcelain body with a side handle. Prompts `white textured mug` or `white mug by the handle`; reject smooth red/yellow candidates and wrist jumps >5 cm.
- Plates: ceramic white discs with concentric red rings, not generic flat circular surfaces. Agentview identifies both semantics; wrist region midpoint refines the visible well/rim. Use the entire visible plate well, not one rim pixel.
- Red distractor: tall red patterned mug between the carry lanes; localize its top/footprint to design a far-negative-x route.
- This run's coordinates (mugs near x=-0.04/-0.17 and plates near y=±0.30) are counter-examples only and must not be cached.

## Fragility flags

The yellow acquisition and assignment binding are most fragile. If Pi0 drifts to the red mug, abort before contact, return above the agentview yellow anchor, and retry the short prompt. If both mugs are upright and quantitatively centered but the predicate remains false, test the alternate plate binding in a clean reset rather than pushing the mugs.

## Difficulty and reliability

Converged in 24 attempts. The physical placement recipe became reliable over the final attempts, but semantic left/right binding required empirical falsification of the robot-frame assumption. Expected single-shot reliability is low-to-moderate until the binding is verified, then moderate because yellow rim-hook acquisition remains sensitive. Only seed 0 is solved.

## Cross-refs

[[held-offset-rotation-reach]]
[[place-order-never-carry-over-placed-object]]
[[libero10-left-right-sign-verify-empirically]]
