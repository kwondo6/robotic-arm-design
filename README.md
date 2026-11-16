# Desktop Robotic Arm: Design, Test Plan and Costing

<!-- Week 4: put the motion GIF and a render here, then a one-paragraph summary. -->

A 3-joint desktop robotic arm designed in Autodesk Fusion as if it were going to be manufactured. It is built from laser-cut plate with off-the-shelf bearings and M3 fasteners, checked against written requirements and costed from real supplier prices. Python is used for kinematics, workspace and servo-torque checks.

**Status:** Week 1 of 4: requirements, concept and servo choice.

## Spec at a glance

| | |
| --- | --- |
| Joints | Base rotation, shoulder, elbow, plus a simple gripper or end plate |
| Reach | about 250 mm |
| Payload | 100 g |
| Actuators | Hobby servos chosen from datasheets |
| Construction | Laser-cut or sheet-metal plate, off-the-shelf bearings, M3 fasteners, no 3D-printed parts |

The full numbered requirements are in [docs/design-spec.md](docs/design-spec.md). The checks are in [docs/verification-plan.md](docs/verification-plan.md).

## Repository layout

| Folder | What goes in it |
| --- | --- |
| `docs/` | Design spec, verification plan, servo selection, and the design note in Week 4 |
| `python/` | Kinematics, workspace and torque scripts |
| `cad/` | Fusion exports (`.f3d` archive and `.step`), plus the CAD conventions |
| `drawings/` | Drawing PDFs: one assembly drawing with a BOM and two part drawings |
| `dxf/` | Flat patterns for every plate part, ready for a laser-cutting quote |
| `bom/` | Costed bill of materials (`bom.csv`) |
| `media/` | Renders, plots, GIFs and the concept sketch |

## Running the Python

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
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
| 4 | 7–13 Dec | Kinematics, workspace and torque plots, costed BOM, verification results, GIF, design note. Tag v1.0 |

### This week

- [ ] Tools installed and first push to GitHub ([SETUP.md](SETUP.md))
- [ ] `python/arm_2link_pose.py` runs; work through the "Try this" exercises at the bottom
- [ ] Fill in and freeze [docs/design-spec.md](docs/design-spec.md)
- [ ] First draft of [docs/verification-plan.md](docs/verification-plan.md)
- [ ] Concept sketch saved as `media/concept-sketch.jpg`
- [ ] Servo chosen in [docs/servo-selection.md](docs/servo-selection.md)

### Done when (v1.0)

- [ ] README with renders and a GIF
- [ ] Drawings PDF and DXF files
- [ ] Costed BOM
- [ ] Python scripts that run with one command
- [ ] Completed verification table
- [ ] 2-page design note

## Progress log

One line at the end of each week: what got done, and the top three tasks for next week.

- **2026-11-16:** Repo set up with folder layout, spec and verification templates, and the Week 1 starter script.
