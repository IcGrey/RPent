---
id: task-family_libero10_task_t4
scope: task-family
suite: libero10
regime: task
task_id: 4
task_language: put the yellow and white mug on the left plate and put the white mug
  on the right plate
evidence:
  cells:
  - 10_task_t4_s0
  attempts: 69
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- held-offset-rotation-reach
---


## Applicable pattern

Two upright mugs must be placed on opposite edge plates without tipping, while “left/right” must be resolved from the successful physical predicate rather than image convention.

## Winning technique

Use viewer-relative mapping: bicolor yellow-white mug to image-left/world -y plate; porcelain white mug to image-right/world +y plate. Grasp each by handle/handle-root with a short max_chunks=8 call, firm, lift high, rotate the held payload about +90 degrees, remeasure its body offset, then carry through a +x corridor using move_pose at the retained yaw. Descend until plate-supported with the grip closed, then release. Yellow first was safe because the porcelain route stayed on the opposite side and used a high +x corridor.

Success criteria: nonzero retained gap; wrist-confirmed airborne target; same-frame held-body center aligned to wrist-refined plate center; stable grip gap through descent; termination on final release.

## Magic numbers

- pi0 max_chunks=8 (usable band 7-10); reissue from a changed handle-side prepose rather than extending a rogue trajectory.
- Firm grip 8-10 steps (usable band 8-12).
- Carry z=0.70-0.72 m (usable band 0.68-0.75).
- Held yaw rotation about +1.57 rad (usable band 1.35-1.60 after actual-yaw measurement).
- move_pose step_clip=0.006-0.008 for carry; 0.003-0.004 for support descent.
- Yellow support EEF z about 0.577 m at yaw 1.574; porcelain support stall about 0.565 m at yaw 1.370. Treat these as counter-examples, not cached coordinates.
- NEVER carry with gripper=-1.
- NEVER reuse a held offset from another pick.
- NEVER infer plate center from a clipped agentview fragment; wrist-center it.

## Failure modes

| symptom | root cause (attempt) | fix |
|---|---|---|
| clean-looking placements under both signs remain false | edge-biased plate centers, wrong mapping, or release geometry were confounded across A6-A65 | use viewer mapping plus same-frame wrist body/plate alignment and final-release predicate |
| inverted mug or large-yaw carry sweeps clutter | rotation/traverse performed before reaching a clear corridor (A66-A69) | rotate at high clear pose and carry via +x corridor |
| distractor brace attempt tips target | Pi0 red acquisition drifted through yellow (A70-A71) | do not manipulate distractor; solve with offset redirection |
| scripted plate pushes do nothing | top-down fingers pass above/interior of rim (A72) | leave plates fixed; wrist-localize true centers |
| true-center egocentric configuration remains false | semantic assignment is wrong despite clean geometry (A73) | viewer-relative mapping |
| yawed payload cannot reach plate center with move_to | held offset consumes the edge-axis reach | rotate offset into x and use move_pose |

## Re-localization per scene

- Yellow-white target: agentview semantic authority; bicolor yellow/white tapered mug with yellow handle. Prompt “grasp the yellow mug by the handle loop”. Reject fully open fingers or cavity-only contact.
- White target: textured porcelain-white mug, not the red patterned distractor. Prompt “grasp the white mug by the handle”. A winning exterior/handle-root gap was about 32 mm before firming.
- Plates: white ceramic discs with concentric red rings. Use wrist view over each plate and back-project its visible center; agentview edge fragments underestimate the outer plate center by several centimeters.
- Absolute coordinates from this seed must not be cached. Counter-example only: plate centers were near y=-0.292 and +0.319.

## Fragility flags

Most fragile is the far +y porcelain delivery. If natural hang demands EEF y beyond reach, rotate the held mug about +90 degrees at high z, measure the new offset, then move_pose at the actual yaw. Recenter after every rotation drift.

## Difficulty and reliability

Solved on the 69th archived attempt across multiple agents. Expected single-shot reliability is low until both semantics and per-pick offsets are handled; once the winning viewer mapping, handle grasps, +90-degree offset redirection, and wrist plate centers are used together, the final predicate fired during release.

## Cross-refs

[[held-offset-rotation-reach]]
[[rotate-wrist-90deg-drifts-eef-recenter-after]]
[[pi0-grasp-tall-mug-by-handle]]
[[place-order-never-carry-over-placed-object]]
