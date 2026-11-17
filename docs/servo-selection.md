# Servo selection

**Choice (270° versions):**
- **Shoulder: DSSERVO DS3235.** The shoulder carries the most load, and the 200 g payload with a 3× margin (R2, R3) needs more than the DS3218MG gives.
- **Base and elbow: DSSERVO DS3218MG.**

Both servos have the same 40 × 20 mm body and 25T output spline, so their mounts should be nearly identical. Confirm the mounting-hole spacing on both drawings before you reuse one mount design.

## Key specs

| Spec | DS3235 (shoulder) | DS3218MG (base, elbow) |
| --- | --- | --- |
| Stall torque | 29 kg·cm at 5 V, 32 at 6 V, 35 at 7.4 V | 18–19 kg·cm at 5 V (sellers' listings vary), 21.5 at 6.8 V |
| Mass | 60 g (some listings say 65 g) | 60 g |
| Body size | 40 × 20 × 38.5 mm | 40 × 20 × 40.5 mm |
| Output spline | 25T | 25T |
| Control range | 270° (a 180° version also exists) | 270° (a 180° version also exists) |

The calculations use the 5 V figures: **29 kg·cm** for the DS3235 and **18 kg·cm** (the lowest quoted) for the DS3218MG.

## Torque check (R3: stall torque ≥ 3 × worst-case static torque)

The worst case is the arm stretched out horizontally with the full payload. Every mass beyond a joint adds its weight × horizontal distance:

T_shoulder = g × (m_payload·(L1+L2) + m_end·(L1+L2) + m_forearm·(L1 + L2/2) + m_elbow_servo·L1 + m_upperarm·L1/2)

T_elbow = g × (m_payload·L2 + m_end·L2 + m_forearm·L2/2)

The shoulder servo sits at the shoulder joint, so its own mass doesn't add to the load it lifts.

| Quantity | Value used |
| --- | --- |
| L1, L2 | 140 mm each |
| Payload | 200 g |
| End plate | 30 g (placeholder) |
| Forearm | 45 g (estimate for 3 mm aluminium) |
| Elbow servo | 60 g (DS3218MG) |
| Upper arm | 56 g (estimate for 3 mm aluminium) |

| Joint | Static torque | Servo | Margin (stall ÷ static) | R3 (≥ 3×) |
| --- | --- | --- | --- | --- |
| Shoulder | 0.84 N·m ≈ 8.6 kg·cm | DS3235, 29 kg·cm | 3.4× | Pass on paper |
| Elbow | 0.35 N·m ≈ 3.5 kg·cm | DS3218MG, 18 kg·cm | 5.1× | Pass on paper |
| Base | No gravity load, only inertia and friction | DS3218MG | n/a | Carry the arm on the turntable bearing, not the servo shaft |

For comparison, a DS3218MG at the shoulder would give only 2.1×, which is why the shoulder gets the DS3235. Conversion: 1 kg·cm = 0.0981 N·m. In Week 4, replace the estimated masses with Fusion's numbers and check the shoulder torque across the whole workspace in Python.

## CAD models: download them, don't model from scratch

1. **Get the drawings.**
   - **DS3218MG:** DSSERVO's installation drawing (PDF), linked on product pages such as [this one](https://aifitlab.com/collections/dsservo-motor/products/dsservo-ds3218-mg-servo-motor).
   - **DS3235:** the [DS3235 datasheet](https://hajim.rochester.edu/me/sites/kelley/me240/DS3235-270_datasheet.pdf), which includes a dimension drawing.
2. **Download STEP models** from [GrabCAD](https://grabcad.com/library): search for "DS3218MG" and "DS3235".
3. **Check each model against its drawing** before designing mounts: the body size, the mounting-hole spacing, and the output shaft's position and height. Community models are usually made by measuring a servo, so they can be slightly off.
4. **Upload the STEP files to your Fusion project, then insert them into the arm design:** SRV-001 (base, DS3218MG), SRV-002 (shoulder, DS3235) and SRV-003 (elbow, DS3218MG), matching `bom/bom.csv`.

If there's no good DS3235 model, copy the DS3218MG model and change its height to 38.5 mm, after checking that the hole positions match the DS3235 drawing. That takes a few minutes.
