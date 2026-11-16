"""
Week 1 starter: plot a 2-link arm at one pose.

This is the side view of the shoulder and elbow, the two joints that lift the
payload. The base rotation just turns this whole picture around a vertical axis.

Run it from the repo root:
    python python\\arm_2link_pose.py

New to Python? Comments marked "C++:" compare each idea with something you
already know from C++.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np  # C++: like #include, but you give the module a short name

# ---- Arm geometry (mm). Match these to docs/design-spec.md ----
L1 = 125.0  # upper arm: shoulder axis to elbow axis
L2 = 125.0  # forearm: elbow axis to tool point
# C++: no type declarations. Python works out that these are floats.

# ---- The pose to draw (degrees) ----
shoulder_deg = 45.0  # measured up from horizontal
elbow_deg = -60.0  # measured from the upper arm's direction; negative bends down


def forward_kinematics(theta1_deg, theta2_deg, l1=L1, l2=L2):
    """Return the (x, z) positions of the shoulder, elbow and tool point.

    theta1 is the shoulder angle from horizontal, and theta2 is the elbow
    angle relative to the upper arm. Both are in degrees.
    """
    # C++: a function with default arguments. The indented block is the body:
    # Python uses indentation where C++ uses braces.
    t1 = np.radians(theta1_deg)
    t2 = np.radians(theta2_deg)

    shoulder = np.array([0.0, 0.0])
    elbow = shoulder + l1 * np.array([np.cos(t1), np.sin(t1)])
    tool = elbow + l2 * np.array([np.cos(t1 + t2), np.sin(t1 + t2)])
    # numpy arrays add element by element, so each 2D point takes one line.

    return shoulder, elbow, tool  # Python can return several values at once


def plot_arm(ax, shoulder, elbow, tool, label=None):
    """Draw the arm on a matplotlib axes: links as thick lines, joints as dots."""
    points = np.vstack([shoulder, elbow, tool])  # a 3x2 array, one row per point
    xs = points[:, 0]  # every row, column 0: the x coordinates
    zs = points[:, 1]  # every row, column 1: the z coordinates
    ax.plot(xs, zs, "-o", linewidth=4, markersize=10, label=label)


def main():
    shoulder, elbow, tool = forward_kinematics(shoulder_deg, elbow_deg)

    # f-strings fill each {} with a value; :6.1f works like printf's "%6.1f".
    print(f"Elbow at      x = {elbow[0]:6.1f} mm, z = {elbow[1]:6.1f} mm")
    print(f"Tool point at x = {tool[0]:6.1f} mm, z = {tool[1]:6.1f} mm")
    print(f"Shoulder to tool point: {np.linalg.norm(tool - shoulder):.1f} mm")

    fig, ax = plt.subplots(figsize=(7, 6))

    # Maximum reach: a dashed circle of radius L1 + L2 around the shoulder.
    angles = np.linspace(0, 2 * np.pi, 200)  # 200 evenly spaced angles
    reach = L1 + L2
    ax.plot(
        reach * np.cos(angles),
        reach * np.sin(angles),
        "--",
        color="grey",
        label=f"Max reach {reach:.0f} mm",
    )

    plot_arm(
        ax,
        shoulder,
        elbow,
        tool,
        label=f"Shoulder {shoulder_deg:.0f}°, elbow {elbow_deg:.0f}°",
    )
    ax.annotate(
        f"Tool ({tool[0]:.0f}, {tool[1]:.0f}) mm",
        xy=tool,
        xytext=(10, 10),
        textcoords="offset points",
    )

    ax.axhline(0, color="black", linewidth=0.8)  # shoulder height
    ax.set_aspect("equal")  # 1 mm across looks the same as 1 mm up
    ax.set_xlabel("x: forward from shoulder (mm)")
    ax.set_ylabel("z: up from shoulder (mm)")
    ax.set_title("2-link arm, side view")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="lower left")

    # Save the plot into media/ (found relative to this file), then show it.
    out_path = Path(__file__).resolve().parent.parent / "media" / "week1_arm_pose.png"
    out_path.parent.mkdir(exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"Saved {out_path}")
    plt.show()


# C++: this works like int main(). The code below runs only when you run this
# file directly, not when another script imports its functions.
if __name__ == "__main__":
    main()


# -----------------------------------------------------------------------------
# Try this (each exercise adds one Python idea)
#
# 1. Change shoulder_deg and elbow_deg and rerun. Which angles put the tool
#    point at x = 200 mm, z = 50 mm? Use trial and error for now; inverse
#    kinematics solves it properly in Week 4.
# 2. Lists and for-loops: draw three poses on the same plot.
#        poses = [(30, -45), (60, -90), (90, -120)]
#        for s, e in poses:
#            ...
# 3. Change L1 and L2 to your own link lengths from docs/design-spec.md.
# 4. if / else: check each pose against the joint ranges in R5, and print a
#    warning instead of plotting a pose that is out of range.
# 5. Week 4 preview: loop over many shoulder and elbow angles, keep every tool
#    point in a list, and plot them all as small dots. That cloud of points is
#    the arm's workspace.
# -----------------------------------------------------------------------------
