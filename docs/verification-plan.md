# Verification plan

One row per requirement in [design-spec.md](design-spec.md). Write each pass criterion before you run its check, so the result is a test, not a description. Fill in **Result** and **Status** as each check is done, mostly in Weeks 3 and 4.

| ID | Requirement | Method | Pass criterion | Result | Status |
| --- | --- | --- | --- | --- | --- |
| R1 | Reach | Python forward kinematics + Fusion measurement | Tool point reaches ≥ 250 mm horizontally | | Not started |
| R2 | Payload | Included in R3 and R4 load cases | 100 g at full reach used in both checks | | Not started |
| R3 | Servo torque margin | Python torque sweep across the workspace | Rated torque ÷ peak static torque ≥ 2 at every joint | | Not started |
| R4 | Strength | Fusion static stress study, arm horizontal, full payload | Minimum safety factor ≥ 2 | | Not started |
| R5 | Joint range | Fusion joint limits + motion study + interference check | Ranges met with no collisions | | Not started |
| R6 | Stability | Fusion centre of mass at full reach with payload | Centre of mass inside the base footprint (or base clamp designed) | | Not started |
| R7 | Manufacture | Inspection of the CAD and the DXF files | Every structural part has a flat pattern in ≤ 2 thicknesses; only M3 fasteners | | Not started |
| R8 | Cost | Costed BOM with an online laser-cutting quote | Total ≤ NZ$250 | | Not started |

**Status values:** Not started · In progress · Pass · Fail (then change the design or log a spec change)

## Notes and evidence

Link each result to its evidence: a plot in `media/`, a screenshot of the stress study, or a line in `bom/bom.csv`.
