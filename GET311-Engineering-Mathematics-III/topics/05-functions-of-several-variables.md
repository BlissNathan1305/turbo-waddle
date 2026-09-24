# Topic 5: Elements of Functions of Several Variables; Surface Variables

[← Back to course overview](../README.md)

## Introduction

Most engineering quantities depend on more than one variable. Temperature changes with position and time, and pressure depends on volume and temperature. A **function of several variables** f(x, y, …) assigns one value to each point of its domain. The main tools are:

- **Level curves and surfaces:** f(x, y) = c (contours) and f(x, y, z) = c (level surfaces, such as isotherms).
- **Limits and continuity** in more than one dimension.
- **Partial derivatives:** ∂f/∂x, ∂f/∂y and higher-order derivatives. Clairaut's theorem says f_xy = f_yx.
- **Total differential:** df = f_x dx + f_y dy, used for error and sensitivity analysis.
- **Chain rule and implicit differentiation** for composite and implicitly defined functions.
- **Directional derivative and gradient:** D_u f = ∇f · u. The gradient points in the direction of steepest increase.
- **Taylor expansion** in two variables, used for linearisation.
- **Extrema:** stationary points classified by the second-derivative test (D = f_xx f_yy − f_xy²), and constrained optimisation with **Lagrange multipliers**.

**Surfaces and surface variables:** a surface can be written explicitly as z = f(x, y), implicitly as F(x, y, z) = 0, or parametrically as **r**(u, v). The parameters u and v are the *surface variables*. The tangent plane and normal come from ∇F or from **r**_u × **r**_v, and the element of surface area is dS = |**r**_u × **r**_v| du dv. These are needed for the surface integrals in Topic 6.

---

## Application Questions

### 1. Agricultural Engineering

1. Crop yield (t/ha) is modelled by Y(N, W) = 0.04N + 0.05W − 0.0001N² − 0.0002W² + 0.00005NW, where N is nitrogen (kg/ha) and W is water (mm). Find the input levels that maximise yield, and confirm that the point is a maximum.
2. The evapotranspiration rate E = kT^0.5 R^0.8 depends on temperature T and radiation R. Use the total differential to estimate the percentage error in E when T is measured with 2 % error and R with 3 % error.

### 2. Chemical Engineering

1. For a van der Waals gas, (P + a/V²)(V − b) = RT. Find ∂P/∂V at constant T and ∂P/∂T at constant V. Verify the cyclic relation (∂P/∂V)_T(∂V/∂T)_P(∂T/∂P)_V = −1.
2. A cylindrical reactor of fixed volume 10 m³ is to be built with the least surface area (and so the least material cost). Use Lagrange multipliers to find the best radius and height.

### 3. Computer Engineering

1. Gradient descent minimises the loss L(w₁, w₂) = (w₁ − 3)² + 2(w₂ + 1)² + w₁w₂. Compute ∇L, write the gradient-descent update rule, and carry out 3 iterations from (0, 0) with learning rate 0.1.
2. The brightness of a grayscale image is modelled as I(x, y) = 100 e^{−(x² + y²)/50}. Compute the image gradient at (3, 4), its magnitude (the edge strength) and its direction, and explain how edge-detection algorithms use this.

### 4. Civil Engineering

1. The ground surface of a site is z = 50 − 0.01x² − 0.02y² (m). At the point (10, 20), find the slope in the direction of the unit vector (3/5, 4/5), the direction of steepest descent (the drainage path), and the equation of the tangent plane.
2. A rectangular beam cut from a circular log of diameter d is strongest in bending when bh² is largest. Use Lagrange multipliers to find b and h subject to b² + h² = d².

### 5. Electrical and Electronics Engineering

1. The power dissipated in a resistor is P = V²/R. Given V = 220 ± 2 V and R = 50 ± 0.5 Ω, use partial derivatives and the total differential to estimate the maximum absolute and relative error in P.
2. The electric potential near a point charge is V(x, y, z) = k/√(x² + y² + z²). Show that V satisfies Laplace's equation ∇²V = 0 away from the origin, and find the equation of the equipotential surface through (1, 2, 2).

### 6. Food Engineering

1. During drying, the moisture content is M(t, T) = M₀ e^{−k(T)t} with k(T) = 0.01 e^{0.05(T − 60)}. Find ∂M/∂t and ∂M/∂T, and use the chain rule to find dM/dt when the dryer temperature rises as T = 60 + 0.5t.
2. A rectangular box for packaging cereal must hold 3000 cm³. The top and bottom cost twice as much per cm² as the sides. Use Lagrange multipliers to find the dimensions that give the cheapest box.

### 7. Mechanical Engineering

1. The temperature distribution in a plate is T(x, y) = 100 − x² − 2y² (°C). A heat-seeking sensor at (2, 1) moves in the direction of fastest heating. Find that direction and the rate of temperature change in it, and find the path of the sensor.
2. The surface of a turbine blade is given parametrically by **r**(u, v) = (u cos v, u sin v, 0.5v) for 1 ≤ u ≤ 2 and 0 ≤ v ≤ π/2 (a helicoid). Find **r**_u × **r**_v, the unit normal and the element of surface area dS.

### 8. Petroleum Engineering

1. The pressure distribution around a producing well is p(x, y) = pₑ − (qμ/(4πkh)) ln[(x² + y²)/rₑ²]. Find ∇p, and show that the flow (along −∇p) is directed radially towards the well.
2. The oil formation volume factor Bₒ(p, T) is approximated by Bₒ = 1.2 + 0.0001(T − 150) − 0.00002(p − 3000). Find the linear (Taylor) approximation of Bₒ about (p, T) = (3000, 150), and estimate Bₒ at (2800 psi, 160 °F).
