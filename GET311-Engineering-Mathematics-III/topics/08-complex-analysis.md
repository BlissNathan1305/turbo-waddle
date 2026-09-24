# Topic 8: Analytic Functions, Cauchy–Riemann Equations, Singularities and Zeros, Contour Integration and Bilinear Transformation

[← Back to course overview](../README.md)

## Introduction

**Complex analysis** studies functions f(z) = u(x, y) + i v(x, y) of the complex variable z = x + iy.

- **Analytic (holomorphic) functions:** f is analytic at z₀ if it is differentiable in a neighbourhood of z₀. Analytic functions are very well behaved. They are infinitely differentiable and can be expanded in power series.
- **Cauchy–Riemann equations:** a necessary condition for analyticity is u_x = v_y and u_y = −v_x. If the partial derivatives are also continuous, the condition is sufficient too. As a result, u and v are **harmonic** (∇²u = ∇²v = 0), and v is the *harmonic conjugate* of u. This is why complex analysis can model 2-D potential flow, electrostatics and steady heat conduction.
- **Zeros and singularities:** z₀ is a zero of order m if f(z₀) = … = f^{(m−1)}(z₀) = 0 but f^{(m)}(z₀) ≠ 0. **Singularities** are points where f is not analytic. They are classified, using the Laurent series, as *removable*, *poles* (of order m) or *essential*.
- **Contour integration:**
  - *Cauchy's integral theorem:* ∮_C f(z) dz = 0 if f is analytic on and inside the closed curve C.
  - *Cauchy's integral formula:* f(z₀) = (1/2πi)∮_C f(z)/(z − z₀) dz, and its extension to derivatives.
  - *Residue theorem:* ∮_C f(z) dz = 2πi Σ Res(f, zₖ). This is used to evaluate real integrals and inverse Laplace transforms.
- **Bilinear (Möbius) transformation:** w = (az + b)/(cz + d) with ad − bc ≠ 0. It is conformal (it preserves angles), maps circles and lines to circles and lines, and is fixed uniquely by three point correspondences. It is used to map awkward domains onto simple ones, and underlies the Smith chart.

Complex analysis is essential in control-system stability (Nyquist criterion), AC circuit analysis, signal processing (the z-transform), aerodynamics (the Joukowski aerofoil) and potential-flow problems.

---

## Application Questions

### 1. Agricultural Engineering

1. Steady groundwater flow under a drainage field is modelled by the potential φ(x, y) = x² − y². Check that φ is harmonic. Use the Cauchy–Riemann equations to find the stream function ψ and the complex potential w = φ + iψ, and sketch the flow lines. Where is the stagnation point?
2. The transfer function of a greenhouse temperature controller is G(s) = 10/((s + 1)(s + 2)(s + 5)). Find its poles and zeros, and use the residue theorem to find the impulse response g(t), the inverse Laplace transform, as (1/2πi)∮ e^{st}G(s) ds.

### 2. Chemical Engineering

1. Use the Cauchy–Riemann equations to show that f(z) = z̄ = x − iy is *not* analytic anywhere, while f(z) = e^{x}(cos y + i sin y) *is* analytic everywhere. Identify the second function as e^z. Explain why analyticity is needed when the concentration field in a thin 2-D film is modelled as the real part of an analytic function.
2. The response of a first-order-plus-lag process is C(s) = 1/(s(τs + 1)²). Classify its singularities, and use residues to find c(t) for τ = 2 min.

### 3. Computer Engineering

1. A digital filter has transfer function H(z) = (z² − 1)/(z² − 0.5z + 0.06). Find its zeros and poles, and state whether the filter is stable (all poles inside |z| = 1). Write a program sketch that computes the poles and tests stability for any given denominator coefficients.
2. The inverse z-transform is x[n] = (1/2πi)∮ X(z) z^{n−1} dz. Use the residue theorem to find x[n] for X(z) = z/((z − 0.5)(z − 0.25)) with |z| > 0.5.

### 4. Civil Engineering

1. Seepage under a sheet pile is modelled by the complex potential w = cosh⁻¹(z/b). Rewrite it as z = b cosh w, separate the real and imaginary parts, and show that the equipotential lines are ellipses and the streamlines are hyperbolae. Identify the branch points at z = ±b.
2. Evaluate the real integral ∫_{−∞}^{∞} dx/(x² + 4)² by contour integration over a semicircle in the upper half-plane. The integral appears in the deflection of a beam on an elastic foundation under a distributed load.

### 5. Electrical and Electronics Engineering

1. Find the bilinear transformation that maps z = 0, 1, ∞ to w = −1, 0, 1. Show that the normalised load-impedance plane (Re z ≥ 0) is mapped onto the unit disc |w| ≤ 1, and explain how this gives the Smith chart reflection coefficient Γ = (z − 1)/(z + 1).
2. An RLC circuit has transfer function H(s) = 1/(s² + 2s + 5). Find its poles, and classify them as simple or of higher order. Use Cauchy's integral formula / residues to find the impulse response h(t).

### 6. Food Engineering

1. The temperature in a long rectangular food slab in steady state is T(x, y) = 20 + 5(x³ − 3xy²). Show that T is harmonic, and find the harmonic conjugate that gives the heat-flow lines. Write the analytic function f(z) whose real part is T − 20.
2. Evaluate ∮_C (e^{2z}/(z − 1)³) dz where C is |z| = 2, using Cauchy's integral formula for derivatives. Such integrals arise in inverting Laplace-domain models of thermal processing with repeated time constants.

### 7. Mechanical Engineering

1. The Joukowski transformation w = z + 1/z maps circles in the z-plane to aerofoil-like shapes. Find the singularities and the critical points (where dw/dz = 0) of the transformation, and show that the circle |z| = 1 maps to the segment [−2, 2] on the real axis.
2. Evaluate ∫₀^{2π} dθ/(5 + 4 cos θ) by contour integration round the unit circle. This type of integral appears in the analysis of rotating machinery with eccentric loading.

### 8. Petroleum Engineering

1. A source (injector) at z = −a and a sink (producer) at z = a give the complex potential w = (q/2π)[log(z + a) − log(z − a)]. Find the singularities of w and their type, and show that the equipotentials are circles (Apollonius circles). Find the stagnation points, if there are any.
2. Find the bilinear transformation that maps the circle |z| = R (the reservoir boundary) to the unit circle, with an off-centre well at z = z₀ going to the centre w = 0. Explain how this lets the known solution for a centred well be used for an off-centre well.
