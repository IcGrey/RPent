---
id: task-family_libero_goal_swap_t9
scope: task-family
suite: libero_goal
regime: swap
task_id: 9
task_language: Put the wine bottle on the rack
evidence:
  cells:
  - goal_swap_t9_s0
  attempts: 2
  solved_seeds:
  - 0
  failed_seeds: []
confidence: single-shot
related:
- spatial-qualified-repick
---


## Applicable pattern
A tall bottle must be put on the swapped wine rack. The hard part is reliable bottle acquisition; the rack is a large slatted fixture that can be visually identified and localized from agentview_high.

## Winning technique
Localize the black wine bottle by agentview_high identity and back-project several pixels on the bottle body/top. Localize the slatted wooden rack as the destination, using pixels on the visible slats/slots rather than the side rails. From the clean home/default pose, first run `pi0_pick("pick up the wine bottle", max_chunks=20, lift_thresh=0.05, gripper_closed_thresh=0.06)`. If this makes contact but leaves the bottle upright and the gripper open, immediately re-issue `pi0_pick("grasp the wine bottle next to the bowl", max_chunks=24, lift_thresh=0.05, gripper_closed_thresh=0.06)`. In this solved seed, the second prompt acquired the bottle with gripper gap about 0.024 m, carried it to the rack, and the predicate fired during the Pi0 skill.

## Magic numbers
`max_chunks=20` (band 18-22) for the initial generic bottle pick.
`max_chunks=24` (band 22-26) for the spatial-qualified repick after a contact-only first attempt.
`lift_thresh=0.05` (band 0.05-0.08) for bottle lift detection.
`gripper_closed_thresh=0.06` default is acceptable; judge the real hold from final gripper gap and images.
Rack target in this seed occupied y about -0.17 to -0.19 from visible slats; do not cache these absolutes for another scene.
Never keep escalating neck-adjacent scripted contact after the bottle is disturbed; it tipped the bottle in A1.

## Failure modes
| symptom | root cause (A<N>) | fix |
|---|---|---|
| Pi0 reports success but bottle remains on table and gripper closes nearly to zero | A1: pre-position above the cork/neck biased Pi0 into an air or near-neck miss | In a fresh episode, avoid neck-biased pre-position; start from home or use a spatial-qualified repick while the bottle is still upright |
| Body-focused Pi0 prompt opens fully and does not lift | A1: after the first miss, the bottle had shifted and the policy did not descend enough to engage the body | Reset or reissue with a spatial relation from a clean/contact-only state rather than continuing lower scripted moves |
| Scripted/move_pose descent knocks the bottle sideways | A1: lower-body approach drifted laterally under pitch and contacted the upright bottle without a grip | Treat as unrecoverable for a clean recipe; avoid pose-contact grasp attempts unless deliberately exploring side-grasp recovery |

## Re-localization per scene
Wine bottle: in agentview_high it is the single tall black bottle with a cork/gold top, near the bowl and plate. Back-project pixels on the dark body and cork/top; reject samples that land at table z≈0.90 if they are intended to be body/top samples. Wrist may confirm geometry when close, but do not let wrist choose a different semantic target.
Rack: in agentview_high it is the slatted wooden rack on image-left/robot-left, with tan slats, gray rails, and dark red side blocks. Back-project several pixels on the slat faces/channels, not on the vertical support rails. The usable placement surface is broad; this run's absolutes are counter-examples only and must not be cached.
Confusers: stove burner/plate are flat discs and not the destination; the rack is semantically the only slatted wooden fixture.

## Fragility flags
Most fragile step: bottle grasp. If generic `pick up the wine bottle` leaves the gripper open and the bottle upright, the spatial prompt `grasp the wine bottle next to the bowl` can convert the near-contact state into a successful acquisition. If the bottle tips, reset rather than attempting many side-contact recoveries.

## Difficulty and reliability
Solved in 2 attempts. Expected single-shot reliability is uncertain because the winning run used Pi0 to both grasp and deliver during the second pick skill, but the prompt ladder was decisive on this seed. The rack placement itself did not require a separate scripted release because the official predicate fired during Pi0's delivery.

## Cross-refs
[[spatial-qualified-repick]]
