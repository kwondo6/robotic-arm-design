# Desktop Robotic Arm: Design and Simulation

<!-- Week 4: put the motion GIF and a render here, then a one-paragraph summary. -->

A 3-joint desktop robotic arm designed in Autodesk Fusion as if it were going to be manufactured: 3 mm aluminium plate, off-the-shelf bearings, M3 fasteners and DS3218MG servos. It is checked against written requirements with Fusion stress and motion studies, and with Python kinematics, workspace and servo-torque analysis.

**Status:** Week 1 of 4: requirements and concept.

## Spec at a glance

| | |
| --- | --- |
| Joints | Base rotation, shoulder, elbow, plus an end plate (a gripper if time allows) |
| Reach | 250 mm on the desk (L1 = L2 = 140 mm) |
| Payload | 100 g |
| Actuators | DSSERVO DS3218MG servo at every joint |
| Construction | 3 mm 5052 aluminium, laser-cut or bent; off-the-shelf bearings; M3 fasteners; no 3D-printed parts |

The full numbered requirements are in [docs/design-spec.md](docs/design-spec.md). The checks are in [docs/verification-plan.md](docs/verification-plan.md).

## Repository layout

| Folder | What goes in it |
| --- | --- |
| `docs/` | Design spec, verification plan, servo selection, and the design note in Week 4 |
| `python/` | Kinematics, workspace and torque scripts |
| `cad/` | Fusion exports (`.f3d` archive and `.step`), plus the CAD conventions |
| `drawings/` | Drawing PDFs: one assembly drawing with a BOM and two part drawings |
| `dxf/` | Flat patterns for every plate part |
| `bom/` | Parts list with the part numbers used to name Fusion components (`bom.csv`) |
| `media/` | Renders, plots, GIFs and the concept sketch |

## Running the Python

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python python\arm_2link_pose.py
```

First-time setup on Windows is covered in [SETUP.md](SETUP.md).

## Plan

| Week | Dates | Milestone |
| --- | --- | --- |
| 1 | 16–22 Nov 2026 | Tools installed, Python basics, requirements, first verification plan, concept sketch, servo chosen |
| 2 | 23–29 Nov | Parts modelled in Fusion from plate and sheet metal; first assembly |
| 3 | 30 Nov–6 Dec | Joints and limits, motion study, physical properties, stress study, drawings, flat patterns |
| 4 | 7–13 Dec | Kinematics, workspace and torque plots, verification results, GIF, design note. Tag v1.0 |

### This week

- [ ] Tools installed and first push to GitHub ([SETUP.md](SETUP.md))
- [x] `python/arm_2link_pose.py` runs
- [ ] Fill in and freeze [docs/design-spec.md](docs/design-spec.md)
- [ ] First draft of [docs/verification-plan.md](docs/verification-plan.md)
- [ ] Concept sketch saved as `media/concept-sketch.jpg`
- [x] Servo chosen: DS3218MG ([docs/servo-selection.md](docs/servo-selection.md))

### Done when (v1.0)

- [ ] README with renders and a GIF
- [ ] Drawings PDF and DXF files
- [ ] Python scripts that run with one command
- [ ] Completed verification table
- [ ] 2-page design note

## Progress log

One line at the end of each week: what got done, and the top three tasks for next week.

- **2026-11-18:** Python 3.15 environment working. Decided 140/140 mm links, 3 mm 5052 aluminium, an end plate and DS3218MG servos. Dropped costing to focus on CAD, simulation and Python.
- **2026-11-16:** Repo set up with folder layout, spec and verification templates, and the Week 1 starter script.
