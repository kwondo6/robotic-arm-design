# Servo selection

Goal for Week 1: choose a real servo for each joint from its datasheet, with enough torque margin to meet R3 (rated torque ≥ 2 × worst-case static torque).

## 1. First torque estimate (hand calculation)

The worst case for the shoulder is the arm stretched out horizontally, holding the full payload. Every mass beyond the shoulder adds weight × horizontal distance:

T_shoulder = g × (m_payload·(L1+L2) + m_tool·(L1+L2) + m_forearm·(L1 + L2/2) + m_elbow_servo·L1 + m_upperarm·L1/2)

T_elbow = g × (m_payload·L2 + m_tool·L2 + m_forearm·L2/2)

The masses below are **placeholder guesses**. Replace them with your own numbers, then with Fusion's numbers once the parts exist.

| Quantity | Value used |
| --- | --- |
| L1 (upper arm) | 125 mm |
| L2 (forearm to tool point) | 125 mm |
| Payload | 100 g |
| Gripper or end plate | 30 g |
| Forearm | 40 g |
| Elbow servo (standard size) | 55 g |
| Upper arm | 50 g |

| Joint | Static torque | × 2 margin (minimum rating) |
| --- | --- | --- |
| Shoulder | 0.49 N·m ≈ 5.0 kg·cm | ≈ 10 kg·cm |
| Elbow | 0.18 N·m ≈ 1.9 kg·cm | ≈ 3.8 kg·cm |
| Base | No gravity load, only inertia and friction | Any standard servo; support the arm on a bearing, not the servo shaft |

Conversion: 1 kg·cm = 0.0981 N·m.

**Takeaway:** the shoulder is the joint that limits the design. A shoulder servo rated near 10 kg·cm has no spare margin left, so look at the 15–20 kg·cm class. Week 4's Python torque sweep replaces this estimate across the whole workspace.

## 2. Candidates

Compare at least two shoulder options on real datasheets. Good places to start are standard-size metal-gear servos (MG996R class) and 20 kg·cm-class servos (DS3218 class). Check each datasheet yourself: ratings vary between sellers, and most hobby servos quote stall torque.

| Servo | Joint | Rated torque (kg·cm @ V) | Stall or continuous? | Speed (s/60°) | Mass (g) | Size (mm) | Price (NZ$) | Datasheet / supplier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | Shoulder | | | | | | | |
| | Shoulder | | | | | | | |
| | Elbow | | | | | | | |
| | Base | | | | | | | |

## 3. Decision

- Shoulder: ___ because ___
- Elbow: ___
- Base: ___
- Gripper (if any): ___

Record the chosen servos in `bom/bom.csv`, and model their real dimensions in Fusion (or download the manufacturer's CAD model if one is available).
