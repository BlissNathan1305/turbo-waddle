# Topic 8 Solutions: Complex Analysis

## 1. Agricultural Engineering

### Question 1: Groundwater flow under the drainage field

$\phi_{xx} + \phi_{yy} = 2 - 2 = 0$, so $\phi$ is harmonic. From the Cauchy–Riemann equations:

$$\psi_y = \phi_x = 2x \ \Rightarrow\ \psi = 2xy + g(x), \qquad \psi_x = -\phi_y = 2y \ \Rightarrow\ g'(x) = 0$$

So $\psi = 2xy$ and

$$w = \phi + i\psi = (x + iy)^2 = z^2$$

The streamlines $xy = \text{const}$ are rectangular hyperbolae: this is flow into a corner. The complex velocity $dw/dz = 2z$ vanishes only at $z = 0$.

> **Answer.** $\psi = 2xy$, $w = z^2$; the stagnation point is the origin.

### Question 2: Impulse response of the greenhouse controller

$G$ has no finite zeros and simple poles at $s = -1, -2, -5$. The residues of $e^{st}G(s)$ are

$$\operatorname*{Res}_{s=-1} = \frac{10e^{-t}}{(1)(4)} = 2.5e^{-t}, \qquad \operatorname*{Res}_{s=-2} = \frac{10e^{-2t}}{(-1)(3)} = -\frac{10}{3}e^{-2t}, \qquad \operatorname*{Res}_{s=-5} = \frac{10e^{-5t}}{(-4)(-3)} = \frac56e^{-5t}$$

Check: $g(0) = 2.5 - 3.333 + 0.833 = 0$ ✓, as expected for a third-order system.

> **Answer.** $g(t) = 2.5e^{-t} - \tfrac{10}{3}e^{-2t} + \tfrac56e^{-5t}$ for $t \ge 0$.

## 2. Computer Engineering

### Question 1: Filter stability

The zeros are the roots of $z^2 - 1 = 0$, so $z = \pm1$. The poles are the roots of $z^2 - 0.5z + 0.06 = 0$, so $z = 0.2$ and $z = 0.3$. Both poles lie inside the unit circle, so the filter is **stable**. The zeros on the unit circle block DC ($z = 1$) and the Nyquist frequency ($z = -1$), so this is a band-pass filter.

```
import numpy as np
def is_stable(den):   # den: denominator coefficients
    poles = np.roots(den)
    return all(abs(p) < 1 for p in poles), poles
```

> **Answer.** Zeros $\pm1$; poles $0.2$ and $0.3$; stable.

### Question 2: Inverse z-transform

$X(z)z^{n-1} = \dfrac{z^n}{(z - \tfrac12)(z - \tfrac14)}$. For $n \ge 0$ both poles lie inside the contour:

$$\operatorname*{Res}_{z=1/2} = \frac{(1/2)^n}{1/2 - 1/4} = 4\left(\tfrac12\right)^n, \qquad \operatorname*{Res}_{z=1/4} = \frac{(1/4)^n}{1/4 - 1/2} = -4\left(\tfrac14\right)^n$$

> **Answer.** $x[n] = 4\left[\left(\tfrac12\right)^n - \left(\tfrac14\right)^n\right]$ for $n \ge 0$, that is $0,\ 1,\ 0.75,\ 0.4375, \dots$

## 3. Civil Engineering

### Question 1: Seepage under the sheet pile

Let $z = b\cosh w$ with $w = \phi + i\psi$. Then

$$x = b\cosh\phi\cos\psi, \qquad y = b\sinh\phi\sin\psi$$

Holding $\phi$ fixed and eliminating $\psi$ gives the equipotentials, which are confocal ellipses:

$$\frac{x^2}{b^2\cosh^2\phi} + \frac{y^2}{b^2\sinh^2\phi} = 1$$

Holding $\psi$ fixed and eliminating $\phi$ gives the streamlines, which are confocal hyperbolae:

$$\frac{x^2}{b^2\cos^2\psi} - \frac{y^2}{b^2\sin^2\psi} = 1$$

Both families have their foci at $z = \pm b$, which are the branch points of $\cosh^{-1}(z/b)$. There $dz/dw = b\sinh w = 0$, so the inverse map is not analytic.

> **Answer.** Equipotentials are ellipses and streamlines are hyperbolae, all with foci at the branch points $z = \pm b$.

### Question 2: $\int_{-\infty}^{\infty} dx/(x^2 + 4)^2$

$f(z) = \dfrac{1}{(z^2 + 4)^2}$ has double poles at $z = \pm2i$; only $2i$ is in the upper half-plane.

$$\operatorname*{Res}_{z=2i} f = \frac{d}{dz}\left[\frac{1}{(z + 2i)^2}\right]_{z=2i} = \frac{-2}{(4i)^3} = \frac{1}{32i}$$

On the large semicircle $\left|f\right| \sim 1/R^4$, so that part of the integral tends to zero. Therefore

$$\int_{-\infty}^{\infty}\frac{dx}{(x^2 + 4)^2} = 2\pi i\cdot\frac{1}{32i} = \frac{\pi}{16}$$

> **Answer.** $\pi/16 \approx 0.196$

## 4. Electrical and Electronics Engineering

### Question 1: The Smith chart mapping

Try $w = \dfrac{z - 1}{z + 1}$: $z = 0 \mapsto -1$, $z = 1 \mapsto 0$ and $z = \infty \mapsto 1$ ✓. A bilinear transformation is fixed uniquely by three points, so this is the map.

If $\mathrm{Re}\, z \ge 0$, then $z$ is at least as close to 1 as to $-1$, so $\left|z - 1\right| \le \left|z + 1\right|$ and $\left|w\right| \le 1$. The imaginary axis maps to the unit circle.

With $z = Z_L/Z_0$ as the normalised impedance, $w$ is the reflection coefficient $\Gamma = \dfrac{Z_L - Z_0}{Z_L + Z_0}$. Every passive load ($\mathrm{Re}\, z \ge 0$) plots inside the unit disc; the Smith chart is that disc with the circles of constant resistance and constant reactance drawn on it.

> **Answer.** $w = \dfrac{z - 1}{z + 1}$, which maps $\mathrm{Re}\, z \ge 0$ onto the unit disc.

### Question 2: RLC impulse response

$s^2 + 2s + 5 = 0$ gives two simple poles, $s = -1 \pm 2i$. Then

$$h(t) = \frac{e^{(-1 + 2i)t}}{4i} + \frac{e^{(-1 - 2i)t}}{-4i} = e^{-t}\,\frac{e^{2it} - e^{-2it}}{4i} = \frac12e^{-t}\sin 2t$$

This is an underdamped response, and it is stable because the poles are in the left half-plane.

> **Answer.** $h(t) = \tfrac12 e^{-t}\sin 2t$

## 5. Food Engineering

### Question 1: Steady slab temperature

Let $u = T - 20 = 5(x^3 - 3xy^2)$. Then $u_{xx} = 30x$ and $u_{yy} = -30x$, so $\nabla^2 u = 0$ and $T$ is harmonic. From the Cauchy–Riemann equations:

$$v_y = u_x = 15x^2 - 15y^2 \ \Rightarrow\ v = 15x^2y - 5y^3 + g(x), \qquad v_x = -u_y = 30xy \ \Rightarrow\ g'(x) = 0$$

So $v = 5(3x^2y - y^3)$, whose level curves are the heat-flow lines, and

$$f(z) = u + iv = 5(x + iy)^3 = 5z^3$$

> **Answer.** $v = 5(3x^2y - y^3)$; $f(z) = 5z^3$, so $T = 20 + \mathrm{Re}\,(5z^3)$.

### Question 2: $\oint e^{2z}/(z - 1)^3\,dz$

The point $z = 1$ lies inside $C$. Using Cauchy's formula for derivatives, $\oint\dfrac{f(z)}{(z - a)^{n+1}}\,dz = \dfrac{2\pi i}{n!}f^{(n)}(a)$, with $f = e^{2z}$, $n = 2$ and $a = 1$, and $f''(z) = 4e^{2z}$:

$$\oint_C\frac{e^{2z}}{(z - 1)^3}\,dz = \frac{2\pi i}{2!}\cdot4e^{2} = 4\pi e^2\,i$$

> **Answer.** $4\pi e^2 i \approx 92.9i$

## 6. Mechanical Engineering

### Question 1: The Joukowski transformation

The singularities are a simple pole at $z = 0$ and $z = \infty$. The critical points satisfy

$$\frac{dw}{dz} = 1 - \frac{1}{z^2} = 0 \quad\Rightarrow\quad z = \pm1$$

The map is not conformal there; these points become the sharp trailing edge of the aerofoil. On the unit circle, $z = e^{i\theta}$ and

$$w = e^{i\theta} + e^{-i\theta} = 2\cos\theta \in [-2, 2]$$

so the circle collapses onto a flat plate, covered twice. Shifting the circle's centre off the origin, while keeping it through $z = 1$, produces a cambered, thick aerofoil.

> **Answer.** Pole at $z = 0$; critical points $z = \pm1$; the unit circle maps to $[-2, 2]$.

### Question 2: $\int_0^{2\pi} d\theta/(5 + 4\cos\theta)$

Let $z = e^{i\theta}$, so $\cos\theta = \tfrac12(z + z^{-1})$ and $d\theta = \dfrac{dz}{iz}$:

$$\int_0^{2\pi}\frac{d\theta}{5 + 4\cos\theta} = \oint_{\left|z\right| = 1}\frac{dz}{iz\left(5 + 2z + 2/z\right)} = \oint\frac{dz}{2i\left(z + \tfrac12\right)(z + 2)}$$

Only $z = -\tfrac12$ is inside the circle, with residue $\dfrac{1}{2i\cdot\tfrac32} = \dfrac{1}{3i}$. So the integral is $2\pi i\cdot\dfrac{1}{3i} = \dfrac{2\pi}{3}$.

> **Answer.** $2\pi/3 \approx 2.094$
