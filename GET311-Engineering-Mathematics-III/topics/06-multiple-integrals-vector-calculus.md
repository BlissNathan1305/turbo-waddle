# Topic 6: Ordinary Integrals; Double, Triple, Line and Surface Integrals; Vector Calculus

[← Back to course overview](../README.md)

## Introduction

This topic extends integration from a single variable to curves, regions, surfaces and volumes, and introduces the calculus of vector fields.

**Integrals**

- **Ordinary (single) integrals:** ∫ f(x) dx, reviewed along with improper integrals and differentiation under the integral sign.
- **Double integrals:** ∬_R f(x, y) dA, evaluated as iterated integrals, sometimes after changing the order of integration or converting to polar coordinates. They give area, mass, centroids and moments of inertia of plane laminae.
- **Triple integrals:** ∭_V f dV, evaluated in Cartesian, cylindrical or spherical coordinates, using the Jacobian for a change of variables. They give volume, mass and centre of gravity of solids.
- **Line integrals:** ∫_C f ds and ∫_C **F** · d**r** along a curve C. They give work done, circulation and path-dependence. A field is **conservative** (path-independent) when **F** = ∇φ.
- **Surface integrals:** ∬_S f dS and ∬_S **F** · **n** dS. The second is the **flux** of **F** through S.

**Vector calculus**

- **Derivatives and integrals of vectors:** d**r**/dt gives velocity and acceleration along a path. Vector functions are integrated component by component.
- **Gradient** ∇φ of a scalar field: the direction and rate of greatest increase, normal to level surfaces.
- **Divergence** ∇ · **F**: the net outflow (source strength) per unit volume.
- **Curl** ∇ × **F**: the local rotation (circulation per unit area). A field is **irrotational** when ∇ × **F** = 0.
- **Flux of a vector field:** the rate at which a quantity (fluid, heat, charge) crosses a surface.

These are the building blocks of the governing equations of fluid mechanics, heat transfer, electromagnetism and elasticity.

---

## Application Questions

### 1. Agricultural Engineering

1. The rainfall intensity over a rectangular catchment 0 ≤ x ≤ 2 km, 0 ≤ y ≤ 3 km is I(x, y) = 10 + 2x + y (mm/h). Use a double integral to find the total volumetric rainfall rate (m³/h) over the catchment and the average intensity.
2. Water flows through a soil profile with Darcy velocity field **q** = (−2x, −2y, 4z) × 10⁻⁶ m/s. Compute ∇ · **q** and ∇ × **q**. State whether the flow is incompressible and irrotational, and find a potential function if one exists.

### 2. Chemical Engineering

1. A cylindrical packed-bed reactor has radius 0.5 m and length 2 m. The catalyst density varies as ρ(r) = 800(1 − 0.3r²) kg/m³. Use a triple integral in cylindrical coordinates to find the total catalyst mass.
2. The velocity in a pipe of radius R is **v** = v_max(1 − r²/R²) **k** (laminar Poiseuille flow). Compute the volumetric flow rate as the flux of **v** through the pipe cross-section, and show that the mean velocity is v_max/2.

### 3. Computer Engineering

1. A drone flies along **r**(t) = (10 cos t, 10 sin t, 2t) m for 0 ≤ t ≤ 2π. Find its velocity, speed and acceleration, and the total path length. Write a short algorithm that approximates this arc length numerically with the trapezoidal rule, and compare the result with the exact value.
2. A heat sink on a processor chip occupies the region 0 ≤ x ≤ 2, 0 ≤ y ≤ 2, 0 ≤ z ≤ 1 (cm). The heat generation rate is q(x, y, z) = 5xy + z (W/cm³). Use a triple integral to find the total heat generated, and write it as a nested-loop numerical approximation (a Riemann sum).

### 4. Civil Engineering

1. A lamina shaped like a T-beam cross-section occupies the region between y = 0 and y = 4 for −1 ≤ x ≤ 1 (the web), plus the region 4 ≤ y ≤ 5 for −3 ≤ x ≤ 3 (the flange). Use double integrals to find the centroid ȳ and the second moment of area I_x about the centroidal axis.
2. A crane lifts a load along a path in the force field **F** = (2xy, x² + z, y) kN. Compute the work done ∫_C **F** · d**r** from (0, 0, 0) to (1, 2, 3) along two different paths. Decide whether **F** is conservative, and find its potential if it is.

### 5. Electrical and Electronics Engineering

1. The electric field of an infinite line charge is **E** = (λ/(2πε₀r)) **r̂**. Compute the flux of **E** through a closed cylinder of radius a and length L coaxial with the line. Show that it equals λL/ε₀, as Gauss's law requires.
2. The magnetic field around a long straight wire is **B** = (μ₀I/(2πr)) **θ̂**. Evaluate the line integral ∮ **B** · d**r** around a circle of radius a centred on the wire, and compute ∇ × **B** for r ≠ 0. Comment on the results.

### 6. Food Engineering

1. A hemispherical dome-shaped cake of radius 10 cm has a temperature during baking of T(ρ) = 180 − 60(1 − ρ/10) °C. Use a triple integral in spherical coordinates to find the volume-averaged temperature.
2. Air flows through a rectangular dryer opening 0 ≤ x ≤ 1 m, 0 ≤ z ≤ 0.5 m with velocity field **v** = (0, 2 + x − z, 0) m/s. Compute the volumetric air flow rate (the flux through the opening). If the air carries 0.012 kg of water per m³, find the rate of moisture removal.

### 7. Mechanical Engineering

1. Find the mass moment of inertia about the z-axis of a solid cone of height h, base radius a and uniform density ρ, using a triple integral in cylindrical coordinates.
2. A fluid velocity field is **v** = (y, −x, 0). Compute ∇ · **v** and ∇ × **v**, interpret the flow physically (rigid-body rotation), and evaluate the circulation around the unit circle in the xy-plane.

### 8. Petroleum Engineering

1. A reservoir occupies the region between the surfaces z = −2000 and z = −2000 − 0.001(x² + y²) for x² + y² ≤ 500² (m). Use a triple integral in cylindrical coordinates to find the bulk rock volume. With 20 % porosity and 75 % oil saturation, estimate the oil in place.
2. The pressure field in a reservoir is p(x, y) = 3000 − 0.5x² − 0.3y² (psi), and the Darcy velocity is **u** = −(k/μ)∇p. Find **u**, and compute the flux of **u** across the boundary of the square −100 ≤ x, y ≤ 100 m (per unit thickness) with k/μ = 0.01.
