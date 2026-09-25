# Topic 6: Ordinary Integrals; Double, Triple, Line and Surface Integrals; Vector Calculus

[← Back to course overview](../README.md)

## Introduction

This topic extends integration from a single variable to curves, regions, surfaces and volumes, and introduces the calculus of vector fields.

**Integrals**

- **Ordinary (single) integrals:** $\int f(x)\,dx$, reviewed along with improper integrals and differentiation under the integral sign.
- **Double integrals:** $\iint_R f(x, y)\,dA$, evaluated as iterated integrals, sometimes after changing the order of integration or converting to polar coordinates. They give area, mass, centroids and moments of inertia of plane laminae.
- **Triple integrals:** $\iiint_V f\,dV$, evaluated in Cartesian, cylindrical or spherical coordinates, using the Jacobian for a change of variables. They give volume, mass and centre of gravity of solids.
- **Line integrals:** $\int_C f\,ds$ and $\int_C \mathbf{F}\cdot d\mathbf{r}$ along a curve $C$. They give work done, circulation and path-dependence. A field is **conservative** (path-independent) when $\mathbf{F} = \nabla\phi$.
- **Surface integrals:** $\iint_S f\,dS$ and $\iint_S \mathbf{F}\cdot\mathbf{n}\,dS$. The second is the **flux** of $\mathbf{F}$ through $S$.

**Vector calculus**

- **Derivatives and integrals of vectors:** $d\mathbf{r}/dt$ gives velocity and acceleration along a path. Vector functions are integrated component by component.
- **Gradient** $\nabla\phi$ of a scalar field: the direction and rate of greatest increase, normal to level surfaces.
- **Divergence** $\nabla\cdot\mathbf{F}$: the net outflow (source strength) per unit volume.
- **Curl** $\nabla\times\mathbf{F}$: the local rotation (circulation per unit area). A field is **irrotational** when $\nabla\times\mathbf{F} = \mathbf{0}$.
- **Flux of a vector field:** the rate at which a quantity (fluid, heat, charge) crosses a surface.

These are the building blocks of the governing equations of fluid mechanics, heat transfer, electromagnetism and elasticity.

---

## Application Questions

### 1. Agricultural Engineering

1. The rainfall intensity over a rectangular catchment $0 \le x \le 2$ km, $0 \le y \le 3$ km is $I(x, y) = 10 + 2x + y$ (mm/h). Use a double integral to find the total volumetric rainfall rate (m³/h) over the catchment and the average intensity.
2. Water flows through a soil profile with Darcy velocity field $\mathbf{q} = (-2x,\ -2y,\ 4z)\times10^{-6}$ m/s. Compute $\nabla\cdot\mathbf{q}$ and $\nabla\times\mathbf{q}$. State whether the flow is incompressible and irrotational, and find a potential function if one exists.

### 2. Chemical Engineering

1. A cylindrical packed-bed reactor has radius 0.5 m and length 2 m. The catalyst density varies as $\rho(r) = 800(1 - 0.3r^2)$ kg/m³. Use a triple integral in cylindrical coordinates to find the total catalyst mass.
2. The velocity in a pipe of radius $R$ is $\mathbf{v} = v_{\max}\left(1 - \dfrac{r^2}{R^2}\right)\mathbf{k}$ (laminar Poiseuille flow). Compute the volumetric flow rate as the flux of $\mathbf{v}$ through the pipe cross-section, and show that the mean velocity is $v_{\max}/2$.

### 3. Computer Engineering

1. A drone flies along $\mathbf{r}(t) = (10\cos t,\ 10\sin t,\ 2t)$ m for $0 \le t \le 2\pi$. Find its velocity, speed and acceleration, and the total path length. Write a short algorithm that approximates this arc length numerically with the trapezoidal rule, and compare the result with the exact value.
2. A heat sink on a processor chip occupies the region $0 \le x \le 2$, $0 \le y \le 2$, $0 \le z \le 1$ (cm). The heat generation rate is $q(x, y, z) = 5xy + z$ (W/cm³). Use a triple integral to find the total heat generated, and write it as a nested-loop numerical approximation (a Riemann sum).

### 4. Civil Engineering

1. A lamina shaped like a T-beam cross-section occupies the region between $y = 0$ and $y = 4$ for $-1 \le x \le 1$ (the web), plus the region $4 \le y \le 5$ for $-3 \le x \le 3$ (the flange). Use double integrals to find the centroid $\bar{y}$ and the second moment of area $I_x$ about the centroidal axis.
2. A crane lifts a load along a path in the force field $\mathbf{F} = (2xy,\ x^2 + z,\ y)$ kN. Compute the work done $\int_C \mathbf{F}\cdot d\mathbf{r}$ from $(0, 0, 0)$ to $(1, 2, 3)$ along two different paths. Decide whether $\mathbf{F}$ is conservative, and find its potential if it is.

### 5. Electrical and Electronics Engineering

1. The electric field of an infinite line charge is $\mathbf{E} = \dfrac{\lambda}{2\pi\varepsilon_0 r}\,\hat{\mathbf{r}}$. Compute the flux of $\mathbf{E}$ through a closed cylinder of radius $a$ and length $L$ coaxial with the line. Show that it equals $\lambda L/\varepsilon_0$, as Gauss's law requires.
2. The magnetic field around a long straight wire is $\mathbf{B} = \dfrac{\mu_0 I}{2\pi r}\,\hat{\boldsymbol{\theta}}$. Evaluate the line integral $\oint \mathbf{B}\cdot d\mathbf{r}$ around a circle of radius $a$ centred on the wire, and compute $\nabla\times\mathbf{B}$ for $r \ne 0$. Comment on the results.

### 6. Food Engineering

1. A hemispherical dome-shaped cake of radius 10 cm has a temperature during baking of $T(\rho) = 180 - 60\left(1 - \dfrac{\rho}{10}\right)$ °C. Use a triple integral in spherical coordinates to find the volume-averaged temperature.
2. Air flows through a rectangular dryer opening $0 \le x \le 1$ m, $0 \le z \le 0.5$ m with velocity field $\mathbf{v} = (0,\ 2 + x - z,\ 0)$ m/s. Compute the volumetric air flow rate (the flux through the opening). If the air carries 0.012 kg of water per m³, find the rate of moisture removal.

### 7. Mechanical Engineering

1. Find the mass moment of inertia about the $z$-axis of a solid cone of height $h$, base radius $a$ and uniform density $\rho$, using a triple integral in cylindrical coordinates.
2. A fluid velocity field is $\mathbf{v} = (y,\ -x,\ 0)$. Compute $\nabla\cdot\mathbf{v}$ and $\nabla\times\mathbf{v}$, interpret the flow physically (rigid-body rotation), and evaluate the circulation around the unit circle in the $xy$-plane.

### 8. Petroleum Engineering

1. A reservoir occupies the region between the surfaces $z = -2000$ and $z = -2000 - 0.001(x^2 + y^2)$ for $x^2 + y^2 \le 500^2$ (m). Use a triple integral in cylindrical coordinates to find the bulk rock volume. With 20 % porosity and 75 % oil saturation, estimate the oil in place.
2. The pressure field in a reservoir is $p(x, y) = 3000 - 0.5x^2 - 0.3y^2$ (psi), and the Darcy velocity is $\mathbf{u} = -\dfrac{k}{\mu}\nabla p$. Find $\mathbf{u}$, and compute the flux of $\mathbf{u}$ across the boundary of the square $-100 \le x, y \le 100$ m (per unit thickness) with $k/\mu = 0.01$.
