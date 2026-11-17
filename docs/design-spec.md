# Design spec and requirements

Fill in the values this week, then freeze them. After that, change a requirement only by adding a dated line to the change log at the bottom. A real design review works that way, and it stops the goalposts moving while you design.

The values below are suggestions from the summer plan. Replace them with your own decisions.

## Purpose

A 3-joint desktop arm that can pick up and place a 100 g object within about 250 mm of its base. It should be designed so that it could be made from laser-cut plate and bought parts.

## Requirements

|ID|Requirement|Value (suggested, edit this)|Why|
|-|-|-|-|
|R1|Reach a point on the desk, measured horizontally from the base axis|≥ 250 mm, with the elbow not fully straight|Pick-and-place happens on the desk, below the shoulder|
|R2|Payload at full reach, arm horizontal|100 g|Small objects; sets the servo and structure loads|
|R3|Servo torque margin at every joint|Rated torque ≥ 2 × worst-case static torque|Hobby servo ratings are usually stall torque, and the arm also needs torque to accelerate|
|R4|Strength of the most loaded part at the worst pose|FEA safety factor ≥ 2 against yield|Margin for dynamic loads and material variation|
|R5|Joint range, with no collisions across it|Base ≥ 180°, shoulder ≥ 120°, elbow ≥ 120°|Reach the whole front half of the desk|
|R6|Stability at full reach with payload|Does not tip: centre of mass stays inside the base footprint, or the base clamps to the desk|The arm is useless if it falls over|
|R7|Manufacture|All structural parts 3 mm 5052 aluminium, laser-cut or bent; no 3D-printed parts; all fasteners M3|One material to design around; fewer tools to assemble|

## Decisions

* Link lengths: upper arm L1 = 140 mm, forearm to tool point L2 = 140 mm (L1 + L2 ≥ R1)
* Shoulder axis height: about 100 mm above the desk (the 140 mm links assume this)
* Plate material and thickness: 3mm 5052 aluminium (if parts are bent, choose a grade that bends well; some aluminium grades crack at tight bends)
* Servo model for each joint: DSSERVO DS3218MG (270° version) at all three joints; see [servo-selection.md](servo-selection.md)
* Gripper or plain end plate: End plate, gripper if time

## Out of scope for Project 1

* Electronics, wiring and firmware (Project 2 covers control)
* Building the physical arm, costing and supplier pricing (dropped on 18 Nov to focus on CAD, simulation and Python)

## Change log

|Date|Change|Reason|
|-|-|-|
||||



