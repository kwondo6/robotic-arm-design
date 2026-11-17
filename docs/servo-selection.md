# Servo selection

**Choice: DSSERVO DS3218MG (270° version) at all three joints.** Using one model keeps the CAD simple: one model to import, and one mount design reused at every joint.

## Key specs

| Spec | Value |
| --- | --- |
| Stall torque | 18–19 kg·cm at 5 V (sellers' listings vary), 21.5 kg·cm at 6.8 V |
| Speed | 0.16 s/60° at 5 V |
| Mass | 60 g |
| Body size | 40 × 20 × 40.5 mm |
| Output spline | 25T |
| Control range | 270° (a 180° version also exists) |

The calculations use **18 kg·cm**, the lowest figure quoted at 5 V.

## Torque check (R3)

The worst case for the shoulder is the arm stretched out horizontally with the full payload. Every mass beyond the shoulder adds its weight × horizontal distance:

T_shoulder = g × (m_payload·(L1+L2) + m_end·(L1+L2) + m_forearm·(L1 + L2/2) + m_elbow_servo·L1 + m_upperarm·L1/2)

T_elbow = g × (m_payload·L2 + m_end·L2 + m_forearm·L2/2)

| Quantity | Value used |
| --- | --- |
| L1, L2 | 140 mm each |
| Payload | 100 g |
| End plate | 30 g (placeholder) |
| Forearm | 45 g (estimate for 3 mm aluminium) |
| Elbow servo | 60 g (DS3218MG) |
| Upper arm | 56 g (estimate for 3 mm aluminium) |

| Joint | Static torque | DS3218MG margin (18 ÷ static) | R3 (≥ 2×) |
| --- | --- | --- | --- |
| Shoulder | 0.57 N·m ≈ 5.8 kg·cm | 3.1× | Pass on paper |
| Elbow | 0.21 N·m ≈ 2.1 kg·cm | 8.4× | Pass on paper |
| Base | No gravity load, only inertia and friction | n/a | Carry the arm on the turntable bearing, not the servo shaft |

Conversion: 1 kg·cm = 0.0981 N·m. In Week 4, replace the estimated masses with Fusion's numbers and check the shoulder torque across the whole workspace in Python.

## CAD model: download it, don't model it

1. **Get DSSERVO's installation drawing** (PDF) for the DS3218MG. It is linked on product pages such as [this one](https://aifitlab.com/collections/dsservo-motor/products/dsservo-ds3218-mg-servo-motor) and gives the mounting-hole positions and the output shaft location.
2. **Download a STEP model** of the DS3218MG from [GrabCAD](https://grabcad.com/library) (search "DS3218MG"; several exist).
3. **Check it against the drawing** before designing any mounts: body 40 × 20 × 40.5 mm, the mounting-hole spacing, and the output shaft's position and height. Community models are usually made by measuring a servo, so they can be slightly off.
4. **Upload the STEP file to your Fusion project, then insert it into the arm design** three times, naming the copies SRV-001 to SRV-003 to match `bom/bom.csv`.

If no model matches the drawing, build a simplified one from the drawing instead: the body block, the mounting tabs with their holes, and the output shaft. That is all the mounts need, and it takes about 30 minutes.
