---
id: task-family_libero_spatial_swap_t5
scope: task-family
suite: libero_spatial
regime: swap
task_id: 5
task_language: Pick the akita black bowl on the ramekin and place it on the plate
evidence:
  cells:
  - spatial_swap_t5_s0
  attempts: 1
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- low-contact-seat-after-release
---


## Applicable pattern
Pick the black patterned bowl satisfying an elevated support relation, here the bowl on the ramekin, and place it on the ceramic plate while rejecting an identical table-level bowl and a stove burner look-alike.

## Winning technique
Use agentview_high as the identity source: choose the elevated bowl visibly sitting on the gray ramekin, not the identical table-level bowl. Back-project several target pixels, move above that anchor, and accept wrist refinement only when it stays within the agentview candidate.

Use a +y rim-biased bowl grasp pose near the refined bowl anchor. If the first short spatial prompt contacts without lifting, retreat open and retry with the full task language from the disturbed upright pose. After a confirmed lift, carry with gripper=1 to the plate, descend low enough for contact, and release.

If the release leaves the bowl upright but perched on the plate rim and the predicate does not fire, do not assume wrong object immediately. Retreat for a clear view, move low over a more centered plate pose with gripper open, and use a short Pi0 pick/contact prompt from above the bowl; in this run that low contact seated the bowl and terminated.

## Magic numbers
Kitchen frame: home eef z about 1.17; use carry z=1.08-1.12 for bowls in this compact scene.

Bowl-on-ramekin wrist refinement: approach about 0.14-0.17 m above the visible bowl surface; accepted wrist segment score 0.953 for `the black patterned bowl`.

Rim-biased bowl pick: refined bowl xy plus about +0.045 y, eef z around 1.08 before Pi0.

Pi0 initial prompt: `pick up the black bowl on the ramekin`, max_chunks=10 can contact but may not lift.

Pi0 retry prompt: full task language with max_chunks=20 lifted in 7 chunks after the bowl was tipped but upright.

Carry/placement: move with gripper=1, step_clip=0.012, descend to eef z about 0.98 before release.

Post-release seating: open-gripper low pose around plate center with eef z about 0.96-0.98, then short `pick up the black bowl` max_chunks about 12 can act as a low contact/seat. Do not use long free-running Pi0 place behavior after a successful pick.

NEVER choose between duplicate bowls by object name suffix; use the spatial relation.

NEVER classify the dark stove burner as the destination plate; the plate is white with red rings.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| First Pi0 pick contacted the elevated bowl but did not lift, peak_lift about 0.004 m | A1: rim-biased pose was too far onto the bowl/ramekin stack for the short spatial prompt | Retreat with gripper open and retry from the upright disturbed pose using the full task language |
| Release left the bowl upright on the plate but `terminated=false` | A1: bowl was perched on the plate rim, not centered deeply enough for the On predicate | Reposition low over the plate and use a short low contact/seat action; predicate fired during the next Pi0 contact |
| Open-gripper low settle plus release did not terminate | A1: passive settle moved the bowl only partway and lacked enough controlled contact | Use a short capped Pi0 contact prompt from above instead of repeated passive releases |

## Re-localization per scene
Target bowl: in agentview_high, look for the black patterned bowl elevated on top of the gray ramekin. Prompt `the black patterned bowl` worked in the wrist once the gripper was above the agentview anchor. Reject the table-level duplicate even if it segments cleanly.

Ramekin landmark: gray ridged cup under the target bowl. It is used for relation identity only; do not place on it.

Plate destination: white ceramic disc with red concentric rings near the table front. Sample pixels inside the plate, not on the rim. Reject the dark gray stove burner with ring grooves; it is not the plate.

This run's absolute coordinates are counter-examples only and must not be cached: target wrist segment near [-0.218, 0.179, 0.970], plate samples centered roughly [0.087, 0.019, 0.927].

## Fragility flags
The most fragile step is centering the bowl on the plate after release. If release does not terminate but the correct bowl is upright on the plate, recover with low controlled contact rather than resetting or doing a high re-pick.

The second fragile step is the first elevated rim grasp. A failed short spatial prompt can still leave the bowl recoverable if it remains upright; retry with full task language from a clean above pose.

## Difficulty and reliability
Solved in one episode with in-place recovery. Expected single-shot reliability is moderate: identity is easy from agentview, but the placement predicate is sensitive to rim centering and may require a seating contact.

## Cross-refs
[[low-contact-seat-after-release]]
