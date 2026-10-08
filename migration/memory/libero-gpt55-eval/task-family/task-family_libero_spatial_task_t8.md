---
id: task-family_libero_spatial_task_t8
scope: task-family
suite: libero_spatial
regime: task
task_id: 8
task_language: Pick the akita black bowl next to the ramekin and place it on the plate
evidence:
  cells:
  - spatial_task_t8_s0
  attempts: 5
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- learned-contact-after-near-placement
---


## Applicable pattern
Spatial-relation duplicate-bowl task: identify the bowl by its relation to the ramekin, place it on the red-rim plate, and recover near-miss bowl placements with a learned contact/settle skill.

## Winning technique
Use agentview_high for identity: the target is the bowl adjacent to the ramekin, not the other duplicate. Back-project several pixels on the target, ramekin, and plate; keep the relation-correct bowl as the semantic anchor even if wrist geometry is skewed.

Pre-position above the target bowl and call `pi0_pick` with `pick up the black bowl next to the ramekin`, `max_chunks=16` (usable band 8-20), `lift_thresh=0.05`, `gripper_closed_thresh=0.06`. Judge from wrist and gripper gap; a very tight gap can still be a real rim-hook.

Carry with `gripper=+1` through a safe waypoint, then make a low scripted release near the plate. If release leaves the bowl tipped or visibly near/on the plate but `terminated=false`, call `pi0_doubled` with `put the black bowl on the plate`, `max_chunks=20`. In the solved run, the contact skill took 8 chunks and fired the predicate.

## Magic numbers
Kitchen frame: pre-position z=1.08 (band 1.07-1.10), carry z=1.10-1.12, low release z target=1.015 (actual stalls around 1.02-1.03).

`pi0_pick max_chunks=16` (band 8-20); shorter prompt worked better than full task wording.

Hold `gripper=+1` for all carries. Never omit gripper on `move_pose` while holding.

`pi0_doubled max_chunks=20` (observed success at 8 chunks) from a near-plate/tipped state.

Scripted push step_clip=0.0025-0.003 can move the bowl without tipping, but did not terminate in this cell.

## Failure modes
| symptom | root cause (attempt) | fix |
|---|---|---|
| Correct bowl tipped beside/against plate after release | Generic bowl offset did not account for actual rim-hook held offset (A16) | Use visual alignment and keep recovery option open; do not rely on `plate_y + 0.045` alone. |
| Bowl visibly overlapped plate but `terminated=false` | Bowl likely rim-supported or center/base outside hidden On threshold (A17) | Use a qualitatively different contact/settle method, not more tiny xy nudges. |
| Pitch-changed release still non-terminating | Positive pitch changed held footprint but did not seat the bowl on the plate (A18) | Prefer learned contact settle after near placement. |
| Small closed-gripper pushes centered bowl visually but still false | Scripted push vectors did not reach the hidden predicate threshold (A19) | Switch to `pi0_doubled` contact from the near-plate state. |
| Final scripted release tipped bowl near plate | Low release still not reliable for seating bowl (A20) | `pi0_doubled "put the black bowl on the plate"` seated it and terminated. |

## Re-localization per scene
Target bowl: prompt/visual description is the patterned akita black bowl adjacent to the silver ramekin. In this seed it was the upper bowl in agentview. Do not cache that absolute position; select by relation to the ramekin.

Distractor bowl: identical patterned bowl farther from the ramekin. Alternate-target test did not solve; the relation target remains the adjacent bowl.

Ramekin: small silver/gray ribbed cup. Use as relation landmark only.

Plate: white ceramic disc with red concentric rings. Distinguish it from stove/cabinet surfaces by RGB; use the red-rim disc, not the burner.

Wrist refine: use wrist for visual placement alignment, but reject pre-pick wrist world samples that jump more than about 5 cm from the agentview anchor because skewed bowl interiors can back-project to inconsistent x.

## Fragility flags
Most fragile step: bowl release. Several visually plausible placements do not fire. If the bowl is near the plate and not lost, try `pi0_doubled` contact before resetting.

A tight gripper gap after pick can still be a valid bowl rim-hook; confirm by wrist image before declaring a miss.

## Difficulty and reliability
Solved on the fifth attempt of this session after previous archived failures. Expected single-shot reliability is low if relying only on scripted release; higher if treating scripted release as setup for learned contact settle.

## Cross-refs
[[learned-contact-after-near-placement]]
