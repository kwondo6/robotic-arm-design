# Design spec and requirements

Fill in the values this week, then freeze them. After that, change a requirement only by adding a dated line to the change log at the bottom. A real design review works that way, and it stops the goalposts moving while you design.

The values below are suggestions from the summer plan. Replace them with your own decisions.

## Purpose

A 3-joint desktop arm that can pick up and place a 100 g object within about 250 mm of its base. It should be designed so that it could be made from laser-cut plate and bought parts.

## Requirements

| ID | Requirement | Value (suggested, edit this) | Why |
| --- | --- | --- | --- |
| R1 | Horizontal reach, shoulder axis to tool point | ≥ 250 mm | Usable desktop workspace |
| R2 | Payload at full reach, arm horizontal | 100 g | Small objects; sets the servo and structure loads |
| R3 | Servo torque margin at every joint | Rated torque ≥ 2 × worst-case static torque | Hobby servo ratings are usually stall torque, and the arm also needs torque to accelerate |
| R4 | Strength of the most loaded part at the worst pose | FEA safety factor ≥ 2 against yield | Margin for dynamic loads and material variation |
| R5 | Joint range, with no collisions across it | Base ≥ 180°, shoulder ≥ 120°, elbow ≥ 120° | Reach the whole front half of the desk |
| R6 | Stability at full reach with payload | Does not tip: centre of mass stays inside the base footprint, or the base clamps to the desk | The arm is useless if it falls over |
| R7 | Manufacture | All structural parts laser-cut or sheet metal in at most 2 thicknesses; no 3D-printed parts; all fasteners M3 | Low-cost, quotable parts; fewer tools to assemble |
| R8 | Cost of the full BOM | ≤ NZ$250 (check after the first quote) | Keep the design realistic |

## Decisions to make this week

- Link lengths: upper arm L1 = ___ mm, forearm to tool point L2 = ___ mm (L1 + L2 ≥ R1)
- Plate material and thickness: ___ (if parts are bent, choose a grade that bends well; some aluminium grades crack at tight bends)
- Servo model for each joint: see [servo-selection.md](servo-selection.md)
- Gripper or plain end plate: ___

## Out of scope for Project 1

- Electronics, wiring and firmware (Project 2 covers control)
- Building the physical arm; the BOM is priced but nothing is bought

## Change log

| Date | Change | Reason |
| --- | --- | --- |
| | | |
