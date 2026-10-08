---
id: task-family_libero_spatial_swap_t1
scope: task-family
suite: libero_spatial
regime: swap
task_id: 1
task_language: Pick the akita black bowl next to the ramekin and place it on the plate
evidence:
  cells:
  - spatial_swap_t1_s0
  attempts: 6
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- relation-anchored-wrist-refine
---


## Applicable pattern
Duplicate patterned bowls with a spatial relation target: pick the bowl next to the ramekin and place it on the red-ring plate. The task tests relation-grounded identity under swap plus bowl-on-plate release offsets.

## Winning technique
Use agentview only for semantic identity: target is the patterned black bowl adjacent to the gray ramekin; the lower patterned bowl near cookies is a distractor. Move above the bowl/ramekin pair so the wrist sees both the target bowl and the ramekin, then refine the same candidate in wrist.

The solved run used wrist samples on the target bowl after a relation-safe approach, then `pi0_pick` with `pick up the akita black bowl`, `max_chunks=20`, `lift_thresh=0.05`, `gripper_closed_thresh=0.06`. After `set_gripper +1`, carry in staged waypoints to avoid the ramekin/distractor, align by wrist so the bowl overlaps the red-ring plate, descend to contact height, and release low.

Success criteria: wrist after pick shows the ramekin-adjacent bowl in the gripper and the lower duplicate still on the table; release must be low enough that the bowl is already over/resting on the plate, not dropped from a high hover.

## Magic numbers
`max_chunks=20` for the generic bowl pick (usable band 18-22); this grasp completed in 8 chunks.
`lift_thresh=0.05` (band 0.05-0.07) for the bowl rim pick.
`set_gripper +1` for 8 steps (band 5-10) immediately after the pick.
Kitchen-frame pre-position z: `1.12` (band 1.10-1.13) over the target bowl.
Carry z: `1.08-1.10` (band 1.08-1.12), with staged xy waypoints under 0.30 m.
Low release eef z: `1.005` requested, final about `1.015` (band 1.00-1.03), after visual bowl/plate overlap.
Never use wrist as a free duplicate-bowl identifier; accept wrist geometry only when it shows the same relation context or is consistent with the agentview-selected candidate.
Never command the A2-style far positive-x/negative-y release offset `[0.168,-0.100]`; it placed the bowl off/edge-over the plate.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Bowl partly on red-ring plate but predicate false | A1 underestimated the held-bowl offset and released too high/edge-biased | Align visually in wrist, descend to contact height before release |
| Farther positive-x/negative-y eef release still missed | A2 corrected in the wrong direction relative to the held bowl | Use lower x and less negative y than A2; solved release used eef around `[0.125,-0.005]` with low z |
| Pre-grasp wrist centered the lower duplicate | A3 replayed stale eef coordinates instead of relation grounding the scene | First move to a relation-safe pose where target bowl and ramekin are both visible, then refine geometry |
| SAM/point segmentation returned wall/table or far-depth outliers for bowl | A4 bowl rim/interior masks were unreliable from agentview in this layout | Use agentview for identity, not precise bowl xy; let wrist refine after relation-safe approach |
| Stopped before pick due to duplicate ambiguity | A5 returned to stale pre-grasp coordinates without a reliable semantic-to-geometry anchor | Park over the bowl/ramekin pair and verify the ramekin-adjacent bowl in wrist before Pi0 |

## Re-localization per scene
Target bowl: visually patterned black/white bowl with yellow rim next to the gray ramekin. Prompt to Pi0 can keep the object name, but segmentation should use visual wording such as `the patterned black bowl next to the ramekin`; in this cell SAM/point segmentation was not reliable enough for final xy.

Ramekin: small gray ribbed cup/bowl. Use it as the relation landmark. In wrist, confirm it is beside the target bowl and not the lower duplicate.

Plate: white ceramic disc with red concentric rings. Do not confuse it with the gray stove burner; classify in RGB before placement. Plate agentview samples in the solved run were around `[0.135,-0.035,0.912]`, but these absolutes are counter-examples only and must not be cached.

Reject rule: if wrist samples identify a bowl without the ramekin relation context, or jump to the lower bowl near cookies, reject and reposition. This run's successful wrist target samples were about 15 cm in y away from the ramekin samples, matching the visible adjacency in the wrist view.

## Fragility flags
Most fragile step is duplicate target grounding before the pick. If wrist shows the lower bowl dominant or lacks the ramekin, do not pick; reposition so the ramekin-adjacent bowl and ramekin are both in view.

Second fragile step is placement offset. If the bowl overlaps only the plate edge in wrist, do a small xy correction and descend before release. Avoid post-release nudging unless the object is upright and visibly on the plate edge.

## Difficulty and reliability
Converged on attempt 6 after five failed/aborted attempts. Expected single-shot rate should improve if the relation-safe wrist localization is followed exactly, but still moderate because the bowl rim grasp yields a tight gripper reading and placement offset is grasp-dependent.

## Cross-refs
[[relation-anchored-wrist-refine]]
