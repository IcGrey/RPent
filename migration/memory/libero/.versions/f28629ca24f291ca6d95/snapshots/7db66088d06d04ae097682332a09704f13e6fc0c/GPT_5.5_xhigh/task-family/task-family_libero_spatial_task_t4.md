---
id: task-family_libero_spatial_task_t4
scope: task-family
suite: libero_spatial
regime: task
task_id: 4
task_language: Pick the akita black bowl on the top of the wooden cabinet and place
  it on the plate
evidence:
  cells:
  - spatial_task_t4_s0
  attempts: 5
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- visual-over-pick-heuristic
- near-target-repick
---


## Applicable pattern
This task tests spatial grounding among duplicate akita black bowls: choose the patterned bowl elevated on top of the wooden cabinet, not the lower duplicate in the open drawer, then place it on the red-rim plate.

## Winning technique
Use agentview_high for identity: the target is the elevated bowl on the cabinet top; the destination is the red-ring white plate on the table. Wrist over the cabinet can confirm geometry but must not switch to the lower duplicate.

A reliable sequence was: move above the cabinet-top bowl at safe kitchen height, run full task-language `pi0_pick` with `max_chunks=30`, inspect visual grasp evidence, keep `gripper:+1`, and script a high carry to the plate. Descend low enough that the bowl rests on the plate before release. If the release leaves the upright bowl on the plate/rim but the predicate remains false, do a short local `pi0_pick` from the low near-plate pose with prompt `pick up the black bowl`; in the solved run this reseated the bowl and terminated.

Success criteria: source bowl visibly leaves the cabinet top, the duplicate lower bowl remains in the drawer, gripper remains closed during carry, release leaves the bowl upright at the red-rim plate, and the short local repick terminates if release alone does not.

## Magic numbers
Kitchen frame: home eef z about 1.17; target bowl top surface about z=1.17; plate surface about z=0.91.

Initial target hover: eef z=1.27 (band 1.25-1.29), xy over the perceived cabinet-top bowl.

First grasp: full task-language `pi0_pick`, `max_chunks=30` (band 28-32), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Carry: always pass `gripper:1`; waypoints under 0.30 xy each; `step_clip=0.012` for high carry (band 0.010-0.015).

Plate descent: use the perceived plate interior, then bias eef slightly so the held bowl bottom, not the gripper center, lands inside the plate. Solved descent used about z=1.08 then z=1.015 with `step_clip=0.006-0.008`.

Release: `max_steps=50` (band 40-60), low over plate.

Near-target reseat: from the low near-plate pose, `pi0_pick` prompt `pick up the black bowl`, `max_chunks=12` (band 10-14), same thresholds.

NEVER carry with `gripper:-1` after the grasp.

NEVER trust a fully shut gripper after a failed source pick as proof of capture; inspect the bowl/source in RGB.

NEVER cache absolute xyz across seeds; the numbers above are counter-examples from this run only.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pi0 contacts the cabinet bowl but leaves it in place after close pre-positioning | A1: tight wrist-centered preposition over the bowl interior led to interior/rim contact without a secure hook | Prefer home/default or high-hover full task-language Pi0; judge the grasp by source-empty and held-bowl visual evidence |
| Bowl released upright near the red-rim plate but predicate false | A2: held-bowl offset was not compensated, so release landed on/near the rim | Descend lower and bias the eef so the bowl bottom, not gripper center, is over the plate interior; then use a short local repick if still upright and close |
| Full task prompt places the bowl on the plate but still edge-biased and false | A3: Pi0 learned delivery can solve semantics but does not reliably center the On predicate | Interrupt/script the final carry and apply near-target reseat rather than only opening |
| Full task prompt sometimes stalls at source despite earlier delivery success | A4: Pi0 high-cabinet grasp behavior is stochastic; scripted closing after a miss just closes on air/rim | If source is not visibly emptied or bowl not held, reset or retry a changed grasp plan rather than continuing |

## Re-localization per scene
Target bowl: identify by relation and RGB. It is the patterned black/white bowl elevated on the dark wooden cabinet top. Confused with the identical patterned bowl lower/front in the open drawer; reject the lower one by elevation and support surface. Agentview pixels on the interior/top pattern worked; rim/edge pixels can hit the cabinet. Wrist confirmation from above is accepted only if it sees the same elevated bowl near the agentview anchor.

Destination plate: red concentric rim, white center, on the table. Confused with neither ramekin nor bowls in this scene; classify semantically before using depth because the task says plate. Use several interior/ring pixels and estimate the center from the visible disc, not a single rim point.

Relation landmark cabinet: dark wooden cabinet with the target bowl on top and duplicate bowl in the open drawer. Use it only to disambiguate which bowl is on top; do not use hidden object names or BDDL coordinates.

This run's absolute coordinates must not be cached. Counter-example only: target surface sampled near x=-0.01, y=-0.26 to -0.28, z=1.17; plate interior near x=0.09, y=0.215, z=0.91.

## Fragility flags
Most fragile step: first source grasp. Full task-language Pi0 can either secure the elevated bowl in about 7 chunks or fail at the rim. Continue only with visual evidence that the target bowl is held/source-empty.

Second fragile step: final plate predicate. A visually plausible edge placement may not terminate. If the bowl is upright and adjacent/on the plate, the short local repick is a validated fallback for this cell.

## Difficulty and reliability
Solved on attempt 5 after four archived failures. Expected single-shot reliability is moderate rather than high because the source grasp is stochastic and release alone is edge-sensitive. The validated recovery is robust when the bowl remains upright near the plate.

## Cross-refs
[[visual-over-pick-heuristic]]
[[near-target-repick]]
