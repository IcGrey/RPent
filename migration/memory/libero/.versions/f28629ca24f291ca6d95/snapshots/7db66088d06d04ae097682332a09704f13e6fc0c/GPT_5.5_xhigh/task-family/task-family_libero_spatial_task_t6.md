---
id: task-family_libero_spatial_task_t6
scope: task-family
suite: libero_spatial
regime: task
task_id: 6
task_language: Pick the akita black bowl on the stove and place it on the plate
evidence:
  cells:
  - spatial_task_t6_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- near-target-repick
---


## Applicable pattern
This task tests spatial grounding among duplicate patterned bowls: pick the bowl whose support is the stove cook region/platform, not the identical bowl on the table, then place it on the red-rim plate.

## Winning technique
Use agentview_high as semantic authority: identify the patterned black bowl sitting on the gray stove platform and the red-rim white ceramic plate. Move high over each candidate and use wrist_high/back_project only to refine the same candidate geometry.

A successful sequence was: high hover over the stove bowl, concise Pi0 grasp prompt `pick up the black bowl on the stove`, hold with `gripper:1`, carry through safe waypoints to the plate, descend until the bowl visibly overlaps/rests on the plate, release, then use a short local near-target `pi0_pick` prompt `pick up the black bowl` if release leaves the upright bowl on the plate/rim but the predicate is false. In this run the reseat step terminated.

Success criteria: the stove platform is visibly emptied, the table bowl remains undisturbed, gripper gap after pick is small but nonzero, the carried bowl stays upright, and the local reseat reports `terminated:true` if the first release is edge-biased.

## Magic numbers
Kitchen frame: home eef z about 1.17; plate surface about z=0.91.

Target hover: z=1.08 (band 1.07-1.10) over wrist-refined stove-bowl xy.

First grasp: `pi0_pick` prompt `pick up the black bowl on the stove`, `max_chunks=20` (band 18-22), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`.

Carry: always pass `gripper:1`; use waypoints under 0.30 xy; `step_clip=0.008-0.012` for bowl carry.

Plate placement: descend in small steps to eef z about 1.00-1.03, bias eef beyond the plate center enough that the held bowl footprint, not the gripper center, overlaps the plate.

Release: `max_steps=50` (band 40-60). If false and upright/overlapping plate, apply near-target reseat.

Near-target reseat: `pi0_pick` prompt `pick up the black bowl`, `max_chunks=12` (band 10-14), same thresholds; in the solved run it functioned as a low contact/reseat and terminated without a lift.

NEVER choose the identical table bowl; the relation `on the stove` is the disambiguator.

NEVER carry with `gripper:-1` after the grasp.

NEVER cache this run's absolute xyz across seeds.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Release leaves bowl upright and visibly overlapping the red-rim plate but predicate remains false | A1: scripted placement was edge-biased; the bowl footprint overlapped the rim/side rather than centered enough for On | Use the short local near-target reseat `pi0_pick` from the low pose; this solved A1 |
| Agentview target samples disagree by many centimeters | A1: one pixel hit stove/background edge rather than bowl surface | Discard outlier samples and refine over the same semantic candidate with wrist |

## Re-localization per scene
Target bowl: prompt/description `patterned black bowl on the stove`. It is the patterned gray/black bowl with yellow rim sitting on the gray stove platform/cook region. Confused with the identical patterned bowl on the table; reject the table-level duplicate by support surface and relation.

Destination plate: prompt/description `red-rim white ceramic plate`. It is a white plate with red concentric rings. Confused with flat stove burner geometry if using depth alone; classify by RGB before placing.

Relation landmark stove: gray metal platform/cook region under the target bowl. Use it only to identify the correct bowl; do not cache positions.

This run's absolute coordinates must not be cached. Counter-example only: wrist-refined target hover was near x=-0.30, y=-0.12; plate center was near x=0.055, y=0.222.

## Fragility flags
Most fragile step: final centering on the plate. A visually plausible release can still be edge-biased and false; if the bowl stays upright and close/on the plate, use the near-target reseat immediately.

Second fragile step: target identity. The duplicate bowl on the table looks identical; agentview relation grounding must precede any Pi0 pick.

## Difficulty and reliability
Solved on attempt 1 with one local recovery after a false release. Expected single-shot reliability is moderate: first grasp was clean, but release centering is sensitive to held-bowl offset and often needs the reseat fallback.

## Cross-refs
[[near-target-repick]]
