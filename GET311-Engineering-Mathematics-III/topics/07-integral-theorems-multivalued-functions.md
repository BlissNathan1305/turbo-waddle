# Topic 7: Gauss's, Green's and Stokes' Theorems and Applications; Single-Valued and Multivalued Functions

[← Back to course overview](../README.md)

## Introduction

### The integral theorems of vector calculus

These three theorems link an integral over a region to an integral over its boundary. They generalise the Fundamental Theorem of Calculus.

| Theorem | Statement | Relates |
|---------|-----------|---------|
| **Green's theorem** (plane) | ∮_C (P dx + Q dy) = ∬_R (∂Q/∂x − ∂P/∂y) dA | line integral ↔ double integral |
| **Stokes' theorem** | ∮_C **F** · d**r** = ∬_S (∇ × **F**) · **n** dS | circulation ↔ flux of the curl |
| **Gauss's (divergence) theorem** | ∯_S **F** · **n** dS = ∭_V ∇ · **F** dV | outward flux ↔ volume integral of divergence |

**Applications** include computing areas with line integrals (A = ½∮(x dy − y dx)), deriving the continuity equation and the heat-conduction equation, Gauss's and Ampère's laws in electromagnetism, and checking whether a field is conservative.

### Single-valued and multivalued functions

A **single-valued function** gives exactly one output for each input. Examples are polynomials and e^z. A **multivalued function** gives more than one output for some inputs:

- z^{1/2} has two values, and z^{1/n} has n values;
- log z = ln|z| + i(arg z + 2kπ) has infinitely many values;
- the inverse trigonometric functions are multivalued.

To work with them we choose a **principal branch**, place a **branch cut** (a curve across which the function jumps), and identify **branch points**, where going round a small circle changes the value. For example, z = 0 is a branch point of √z and of log z. Getting branches right is essential for the contour integration in Topic 8 and for physical problems with slits, cracks and flows around corners.

---

## Application Questions

### 1. Agricultural Engineering

1. A field boundary is traced by GPS as the ellipse x = 300 cos t, y = 200 sin t (m). Use Green's theorem (A = ½∮(x dy − y dx)) to find the field area. Explain how a GPS area-measuring device can use the same formula on a list of boundary points (the shoelace formula).
2. The groundwater flux under a farm is **q** = (x², y², z²) (m/day, scaled) in the cube 0 ≤ x, y, z ≤ 1. Check the divergence theorem by computing the net outward flux both as a surface integral and as a volume integral.

### 2. Chemical Engineering

1. Apply Gauss's divergence theorem to a fixed control volume V to derive the continuity equation ∂ρ/∂t + ∇ · (ρ**v**) = 0 from the integral mass balance.
2. The complex potential of flow in a corner-shaped mixing channel involves w = z^{2/3}. Find all values of w at z = 8i, give the principal value, and state the branch point. Suggest a suitable branch cut for a channel occupying the upper half-plane.

### 3. Computer Engineering

1. Polygon-area routines in computer graphics are based on Green's theorem. Derive the shoelace formula A = ½ Σ (xᵢyᵢ₊₁ − xᵢ₊₁yᵢ) from ½∮(x dy − y dx), and use it on the polygon with vertices (0, 0), (4, 0), (4, 3), (2, 5) and (0, 3). Write the algorithm in pseudocode.
2. A function atan2(y, x) returns the principal argument of z = x + iy in (−π, π]. Explain why arg z is multivalued. Show what happens to the computed angle as a point travels once round the origin, and describe how "phase unwrapping" algorithms fix the resulting jump.

### 4. Civil Engineering

1. Use Green's theorem to find the area and centroid of the plane region bounded by y = x² and y = 2x (in metres), which models a curved slab section. Check the answer with direct double integration.
2. Seepage under a dam has flux field **q** = (2x − y, x + 3y, −5z) (per unit time). Check whether the field is consistent with an incompressible soil (∇ · **q** = 0). Use the divergence theorem to find the net outflow from the unit cube.

### 5. Electrical and Electronics Engineering

1. Starting from Ampère's circuital law ∮_C **H** · d**r** = I_enc, use Stokes' theorem to derive the differential form ∇ × **H** = **J**. Apply it to find **H** inside a long straight conductor of radius a carrying a uniformly distributed current I.
2. The phase of an AC signal is found from the complex logarithm of the phasor. Find all values of log(−1 + i√3), give the principal value, and explain what the choice of branch means when measuring phase angles above 180°.

### 6. Food Engineering

1. A food can is heated in a retort. Heat flux into the can is **q** = −k∇T. Use the divergence theorem on the can volume to show that the total rate of heat entering through the surface equals ∭ ρc_p (∂T/∂t) dV (when there is no internal generation). This is the basis of the heat-conduction equation.
2. The stirring flow in a mixing bowl is approximated by **v** = (−y, x, 0) (rad/s units). Use Stokes' theorem to compute the circulation around the bowl rim (a circle of radius 0.15 m in the plane z = 0.1 m) through the flat disc it bounds. Check the answer against a direct line integral.

### 7. Mechanical Engineering

1. Compute the work done by the force **F** = (y + z, z + x, x + y) round the triangle with vertices (1, 0, 0), (0, 1, 0) and (0, 0, 1) using Stokes' theorem. Explain the result in terms of conservative forces.
2. The flow round a sharp re-entrant corner of angle 3π/2 in a duct is modelled by w = z^{2/3}. Identify the branch point, describe the branch cut, and find the two other values of w at z = 1 besides the principal value. Explain why the velocity becomes unbounded at the corner.

### 8. Petroleum Engineering

1. Use the divergence theorem to show that for steady incompressible flow in a reservoir with no wells (∇ · **u** = 0), the net volumetric flux through any closed surface is zero. Extend the argument to a region containing a producing well of rate q, and derive the resulting flux condition.
2. The complex potential for flow towards a well at the origin is w = (q/(2π)) log z. Show that the stream function ψ = Im w is multivalued, find its change on going once round the well, and relate this jump to the well's production rate.
