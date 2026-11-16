# CAD

The live design stays in Fusion's cloud. This folder holds exported snapshots, so anyone can open the design without your Fusion account.

## What to export here, at each milestone

- `desktop-arm_vX.f3d`: the Fusion archive (File > Export > .f3d)
- `desktop-arm_vX.step`: the neutral format any CAD tool can open

Drawing PDFs go in `../drawings/`. DXF flat patterns go in `../dxf/`.

## Conventions

- **Units:** mm.
- **One component per physical part.** Name each one with the part number from `bom/bom.csv`, for example `ARM-003 Shoulder bracket`.
- **Bought parts** (servos, bearings, screws) are modelled at their real datasheet dimensions or taken from the manufacturer's CAD model. Use their `SRV-`, `BRG-` and `FST-` numbers.
- **Plate parts** use Fusion's sheet metal rules with your chosen material and thickness, so the flat patterns and DXFs come out right.
- **Origin:** put the base centre on the desk at the origin, with Z up. That keeps forward kinematics, Fusion measurements and later ROS work consistent.
- **Physical properties:** assign the real material to every component, so the mass, centre of mass and inertia are correct. Project 2 reuses those numbers.
