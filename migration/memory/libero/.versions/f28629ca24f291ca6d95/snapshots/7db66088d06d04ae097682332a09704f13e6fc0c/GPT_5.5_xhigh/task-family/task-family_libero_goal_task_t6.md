---
id: task-family_libero_goal_task_t6
scope: task-family
suite: libero_goal
regime: task
task_id: 6
task_language: put the wine bottle in the bowl
evidence:
  cells:
  - goal_task_t6_s0
  attempts: 3
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- avoid-full-task-prompt-after-miss
---


## Applicable pattern

Place a tall wine bottle into an open bowl in the kitchen frame. The task is mainly about grasp-only Pi0 control and accounting for the large held-object offset: the gripper center does not need to be inside the bowl as long as the bottle body is released over the cavity.

## Winning technique

Localize the dark green wine bottle and the patterned bowl from `agentview_high.png`, then refine geometry from the wrist after pre-positioning over the bottle. Use the bowl's RGB appearance (black/white patterned interior, yellow rim) as the destination and pick an interior/cavity point, not the rim.

Move above the bottle with the gripper open. Use grasp-only `pi0_pick("pick up the wine bottle")`; if a short call misses but leaves the scene clean, retry from the same pose with a moderate chunk budget. Confirm by gripper gap around 0.015 and wrist/agentview evidence, then `set_gripper +1`. If Pi0 carries the bottle toward the cabinet, recover with closed-gripper high waypoints back over the bowl. Release when the held bottle body is visually over the bowl cavity, even if the eef target cannot fully reach the nominal y coordinate.

## Magic numbers

Kitchen frame: initial eef z about 1.17; table/bowl interior surface about z=0.90-0.93.

Bottle pre-position: eef z=1.08 (usable band 1.055-1.09) over perceived bottle xy.

Grasp prompt: `pick up the wine bottle`; avoid full task wording after a miss.

Pi0 chunks: max_chunks=14 succeeded after max_chunks=8 missed cleanly. Use 12-16 as the first retry band if 8 is too short; 20 can work but may leave an awkward vertical held offset.

Grip lock: `set_gripper +1` for 8 steps (band 8-10) after a visual/proprioceptive grasp.

Carry/recovery: keep gripper +1; high waypoint around z=1.18 (band 1.16-1.20), step_clip 0.010-0.012.

Release: open over the bowl with eef around x=-0.04, y=-0.036 to -0.055, z=1.11-1.13 in this seed; do not cache these absolutes. The transferable rule is to aim the held bottle body over the bowl, not the eef origin.

NEVER use full task prompt `put the wine bottle in the bowl` for recovery unless deliberately testing Pi0 end-to-end behavior; in A2 it knocked both objects over.

## Failure modes

| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Release opens with `terminated=false`, bottle at near/front rim | A1: placement used bowl center as eef target without enough held-bottle offset compensation; low y correction stalled at eef y about -0.072 | Aim so the bottle body is over the cavity; move through high waypoints before descending/releasing |
| Pi0 misses after reset, gripper remains open | A2/A3: max_chunks=8 or some repeated starts can stop before closure/lift | Retry in-place from a clean pose with same grasp-only prompt and max_chunks around 14 |
| Bowl and bottle tip near cabinet | A2: full task prompt caused Pi0 to continue into a rogue end-to-end place/release behavior | Keep Pi0 grasp-only; never use full task prompt for this cell after a miss |

## Re-localization per scene

Bottle: identify as the dark green wine bottle with tan cork/top. Agentview identity is reliable because it stands immediately below/near the bowl and differs from the blue cream-cheese box, plate, and stove. Sample pixels on the neck/body, not table gaps. Wrist refinement is accepted only near the agentview anchor.

Bowl: identify as the patterned black/white open bowl with yellow rim. Use RGB to reject the red-ring plate and gray stove burner. For the destination, sample interior floor/walls and use the cavity center; rim pixels bias the target outward. Wrist can confirm the open cavity once overhead.

This run's absolute coordinates are counter-examples only: bottle samples were near x=-0.17, y=-0.05 and bowl interior near x=-0.10, y=-0.05, but future seeds must re-back-project.

## Fragility flags

Most fragile step: Pi0 grasp duration. Too few chunks misses; full-task wording can cause a rogue place. Fallback is a clean in-place retry with the same short prompt and max_chunks in the 12-16 range, then immediate `set_gripper +1`.

Second fragility: held-bottle offset. If the bottle appears at the near rim, do not release unless the body is visibly inside; move high first and correct the eef so the body, not the gripper origin, crosses the bowl.

## Difficulty and reliability

Solved in 3 attempts. Expected single-shot rate is moderate if the grasp-only prompt and 12-16 chunk retry are used and the release is chosen by visual held-body alignment. Failures were recoverable only while the bowl stayed upright; tipped bowl plus bottle near the cabinet was unrecoverable and needed reset.

## Cross-refs

[[avoid-full-task-prompt-after-miss]]
