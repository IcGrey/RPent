---
id: task-family_libero_spatial_swap_t2
scope: task-family
suite: libero_spatial
regime: swap
task_id: 2
task_language: Pick the akita black bowl from table center and place it on the plate
evidence:
  cells:
  - spatial_swap_t2_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- point-prompt-after-text-misground
---


## Applicable pattern
Pick the patterned black bowl satisfying the spatial phrase "from table center" and place it on the semantically red-ringed white plate. The scene includes a matching patterned bowl on the right and a gray stove burner that can confuse text segmentation.

## Winning technique
Use agentview_high for identity. Reject free-text masks that select a distractor or burner, then point-prompt the center bowl. Pre-position open above the center-bowl xy at kitchen-frame safe height, run a short grasp-only Pi0 prompt, lock the gripper, carry to the plate center with a small +y bowl offset, descend until the bowl is close to plate contact, and release.

## Magic numbers
Kitchen pre-position over bowl: z=1.08 (usable band 1.06-1.10).
Pi0 pick: max_chunks=12 (usable band 10-16), lift_thresh=0.05, gripper_closed_thresh=0.06.
Grip firming: set_gripper +1 for 8 steps (usable band 5-10).
Carry/place: plate_x, plate_y+0.045, z=1.02, then descend to z=0.96 (usable band 0.96-0.99) before release.
NEVER trust text SAM alone when duplicate patterned bowls and a ringed stove burner are visible; verify overlay identity.
NEVER carry with gripper -1; keep +1 until release.

## Failure modes
| symptom | root cause (A<N>) | fix |
| --- | --- | --- |
| Text prompt selected right patterned bowl | A1: SAM grounded category and ignored table-center relation | Use agentview identity and point-prompt the target pixels |
| Text prompt selected stove burner | A1: burner has a circular patterned/ringed appearance | Classify destination/fixtures semantically in RGB and reject burner masks for bowl target |
| Reset before motion | A1: operator error, no manipulation data | Re-run perception after reset and execute cleanly |

## Re-localization per scene
Target bowl: look for the black/white floral-patterned bowl at table center, not the matching bowl on the right. Text segment phrases are unreliable in this cell; point-prompt a firm interior pixel on the chosen bowl after visual identity. This run's accepted pixel [588,526] and xyz [-0.0957,-0.0034,0.9297] are counter-examples only and must not be cached.
Plate: the destination is the white ceramic plate with red rings, below the center bowl. Segment phrase "the white plate with red rings" worked; point prompt [759,548] also worked. Reject the gray stove burner because it is a fixture with dark concentric rings, not a plate.

## Fragility flags
Most fragile step is semantic grounding in the presence of duplicate bowls and a ringed burner. Fallback is manual/point-prompt segmentation from agentview_high, not another free-text noun phrase.

## Difficulty and reliability
Solved on the first manipulated episode after one accidental reset. Expected single-shot rate is good if the target is point-prompted and the bowl is lowered to near-contact before release; text-only segmentation is not reliable here.

## Cross-refs
[[point-prompt-after-text-misground]]
