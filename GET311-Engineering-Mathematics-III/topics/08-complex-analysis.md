# Topic 8: Analytic Functions, Cauchy–Riemann Equations, Singularities and Zeros, Contour Integration and Bilinear Transformation

[← Back to course overview](../README.md)

## Introduction

**Complex analysis** studies functions $f(z) = u(x, y) + i\,v(x, y)$ of the complex variable $z = x + iy$.

- **Analytic (holomorphic) functions:** $f$ is analytic at $z_0$ if it is differentiable in a neighbourhood of $z_0$. Analytic functions are very well behaved. They are infinitely differentiable and can be expanded in power series.
- **Cauchy–Riemann equations:** a necessary condition for analyticity is $u_x = v_y$ and $u_y = -v_x$. If the partial derivatives are also continuous, the condition is sufficient too. As a result, $u$ and $v$ are **harmonic** ($\nabla^2 u = \nabla^2 v = 0$), and $v$ is the *harmonic conjugate* of $u$. This is why complex analysis can model 2-D potential flow, electrostatics and steady heat conduction.
- **Zeros and singularities:** $z_0$ is a zero of order $m$ if $f(z_0) = \dots = f^{(m-1)}(z_0) = 0$ but $f^{(m)}(z_0) \ne 0$. **Singularities** are points where $f$ is not analytic. They are classified, using the Laurent series, as *removable*, *poles* (of order $m$) or *essential*.
- **Contour integration:**
  - *Cauchy's integral theorem:* $\oint_C f(z)\,dz = 0$ if $f$ is analytic on and inside the closed curve $C$.
  - *Cauchy's integral formula:* $f(z_0) = \dfrac{1}{2\pi i}\oint_C\dfrac{f(z)}{z - z_0}\,dz$, and its extension to derivatives.
  - *Residue theorem:* $\oint_C f(z)\,dz = 2\pi i\sum_k\operatorname{Res}(f, z_k)$. This is used to evaluate real integrals and inverse Laplace transforms.
- **Bilinear (Möbius) transformation:** $w = \dfrac{az + b}{cz + d}$ with $ad - bc \ne 0$. It is conformal (it preserves angles), maps circles and lines to circles and lines, and is fixed uniquely by three point correspondences. It is used to map awkward domains onto simple ones, and underlies the Smith chart.

Complex analysis is essential in control-system stability (Nyquist criterion), AC circuit analysis, signal processing (the z-transform), aerodynamics (the Joukowski aerofoil) and potential-flow problems.

---

## Application Questions

### 1. Agricultural Engineering

1. Steady groundwater flow under a drainage field is modelled by the potential $\phi(x, y) = x^2 - y^2$. Check that $\phi$ is harmonic. Use the Cauchy–Riemann equations to find the stream function $\psi$ and the complex potential $w = \phi + i\psi$, and sketch the flow lines. Where is the stagnation point?
2. The transfer function of a greenhouse temperature controller is $G(s) = \dfrac{10}{(s + 1)(s + 2)(s + 5)}$. Find its poles and zeros, and use the residue theorem to find the impulse response $g(t)$, the inverse Laplace transform, as $\dfrac{1}{2\pi i}\oint e^{st}G(s)\,ds$.

### 2. Computer Engineering

1. A digital filter has transfer function $H(z) = \dfrac{z^2 - 1}{z^2 - 0.5z + 0.06}$. Find its zeros and poles, and state whether the filter is stable (all poles inside the unit circle). Write a program sketch that computes the poles and tests stability for any given denominator coefficients.
2. The inverse z-transform is $x[n] = \dfrac{1}{2\pi i}\oint X(z)\,z^{n-1}\,dz$. Use the residue theorem to find $x[n]$ for $X(z) = \dfrac{z}{(z - 0.5)(z - 0.25)}$ in the region outside the circle of radius $0.5$.

### 3. Civil Engineering

1. Seepage under a sheet pile is modelled by the complex potential $w = \cosh^{-1}(z/b)$. Rewrite it as $z = b\cosh w$, separate the real and imaginary parts, and show that the equipotential lines are ellipses and the streamlines are hyperbolae. Identify the branch points at $z = \pm b$.
2. Evaluate the real integral $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{(x^2 + 4)^2}$ by contour integration over a semicircle in the upper half-plane. The integral appears in the deflection of a beam on an elastic foundation under a distributed load.

### 4. Electrical and Electronics Engineering

1. Find the bilinear transformation that maps $z = 0, 1, \infty$ to $w = -1, 0, 1$. Show that the normalised load-impedance plane ($\mathrm{Re}\, z \ge 0$) is mapped onto the unit disc, and explain how this gives the Smith chart reflection coefficient $\Gamma = \dfrac{z - 1}{z + 1}$.
2. An RLC circuit has transfer function $H(s) = \dfrac{1}{s^2 + 2s + 5}$. Find its poles, and classify them as simple or of higher order. Use Cauchy's integral formula or residues to find the impulse response $h(t)$.

### 5. Food Engineering

1. The temperature in a long rectangular food slab in steady state is $T(x, y) = 20 + 5(x^3 - 3xy^2)$. Show that $T$ is harmonic, and find the harmonic conjugate that gives the heat-flow lines. Write the analytic function $f(z)$ whose real part is $T - 20$.
2. Evaluate $\displaystyle\oint_C\frac{e^{2z}}{(z - 1)^3}\,dz$ where $C$ is the circle of radius 2 centred at the origin, using Cauchy's integral formula for derivatives. Such integrals arise in inverting Laplace-domain models of thermal processing with repeated time constants.

### 6. Mechanical Engineering

1. The Joukowski transformation $w = z + \dfrac{1}{z}$ maps circles in the $z$-plane to aerofoil-like shapes. Find the singularities and the critical points (where $dw/dz = 0$) of the transformation, and show that the unit circle maps to the segment $[-2, 2]$ on the real axis.
2. Evaluate $\displaystyle\int_0^{2\pi}\frac{d\theta}{5 + 4\cos\theta}$ by contour integration round the unit circle. This type of integral appears in the analysis of rotating machinery with eccentric loading.
