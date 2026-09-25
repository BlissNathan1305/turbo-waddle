# Topic 6 Solutions: Multiple Integrals and Vector Calculus

## 1. Agricultural Engineering

### Question 1: Rainfall over the catchment

$$\iint_R (10 + 2x + y)\,dA = \int_0^3\!\!\int_0^2 (10 + 2x + y)\,dx\,dy = \int_0^3 (24 + 2y)\,dy = 72 + 9 = 81\ \text{mm·km}^2/\text{h}$$

Since 1 mm is $10^{-3}$ m and 1 km² is $10^{6}$ m², this is $Q = 81\,000$ m³/h. The area is 6 km², so the average intensity is $81/6 = 13.5$ mm/h.

> **Answer.** $Q = 81\,000$ m³/h; average intensity 13.5 mm/h.

### Question 2: Soil water flux

Ignoring the common factor $10^{-6}$:

$$\nabla\cdot\mathbf{q} = -2 - 2 + 4 = 0, \qquad \nabla\times\mathbf{q} = \mathbf{0}$$

The curl is zero because each component depends only on its own variable. So the flow is **incompressible** and **irrotational**, and a potential exists with $\mathbf{q} = \nabla\phi$:

$$\phi = \left(-x^2 - y^2 + 2z^2\right)\times10^{-6}$$

Check: $\nabla^2\phi = 0$, so this is a valid potential flow.

> **Answer.** Incompressible and irrotational, with $\phi = (-x^2 - y^2 + 2z^2)\times10^{-6}$.

## 2. Chemical Engineering

### Question 1: Catalyst mass

$$m = \int_0^2\!\!\int_0^{2\pi}\!\!\int_0^{0.5} 800(1 - 0.3r^2)\,r\,dr\,d\theta\,dz = 3200\pi\left[\frac{r^2}{2} - 0.075r^4\right]_0^{0.5} = 3200\pi(0.125 - 0.00469) = 1209.5\ \text{kg}$$

> **Answer.** $m = 1209.5$ kg

### Question 2: Poiseuille flow rate

$$Q = \iint \mathbf{v}\cdot\mathbf{k}\,dA = \int_0^{2\pi}\!\!\int_0^R v_{\max}\left(1 - \frac{r^2}{R^2}\right)r\,dr\,d\theta = 2\pi v_{\max}\left[\frac{R^2}{2} - \frac{R^2}{4}\right] = \frac{\pi R^2 v_{\max}}{2}$$

The mean velocity is $\bar{v} = Q/(\pi R^2) = v_{\max}/2$. ∎

> **Answer.** $Q = \pi R^2 v_{\max}/2$ and $\bar{v} = v_{\max}/2$.

## 3. Computer Engineering

### Question 1: The drone's helical path

$$\mathbf{v} = (-10\sin t,\ 10\cos t,\ 2), \qquad \left\|\mathbf{v}\right\| = \sqrt{104} \approx 10.20\ \text{m/s}, \qquad \mathbf{a} = (-10\cos t,\ -10\sin t,\ 0)$$

The acceleration has magnitude 10 m/s² and points towards the axis. The path length is

$$s = \int_0^{2\pi}\sqrt{104}\,dt = 2\pi\sqrt{104} = 64.08\ \text{m}$$

```
function arc_length(r_prime, a, b, n):
    h = (b - a) / n
    s = 0.5 * (|r_prime(a)| + |r_prime(b)|)
    for i = 1..n-1: s += |r_prime(a + i*h)|
    return h * s
```

Because the speed is constant, the trapezoidal rule gives 64.08 m exactly for any $n$. For a non-uniform path the error falls as $h^2$.

> **Answer.** Speed $\sqrt{104} \approx 10.20$ m/s; length $2\pi\sqrt{104} = 64.08$ m.

### Question 2: Heat generated in the heat sink

$$Q = \int_0^1\!\!\int_0^2\!\!\int_0^2 (5xy + z)\,dx\,dy\,dz = 5(2)(2)(1) + (2)(2)\left(\tfrac12\right) = 20 + 2 = 22\ \text{W}$$

As a Riemann sum (midpoint rule):

```
Q = 0
for i in 0..n-1: for j in 0..n-1: for k in 0..n-1:
    x = (i+0.5)*dx; y = (j+0.5)*dy; z = (k+0.5)*dz
    Q += (5*x*y + z) * dx*dy*dz
```

The integrand is linear in each variable separately, so the midpoint rule gives exactly 22.

> **Answer.** $Q = 22$ W

## 4. Civil Engineering

### Question 1: Centroid and second moment of the T-section

The web has area 8 with centroid at $y = 2$; the flange has area 6 with centroid at $y = 4.5$.

$$\bar{y} = \frac{\iint y\,dA}{A} = \frac{8(2) + 6(4.5)}{14} = \frac{43}{14} = 3.071$$

$$I_x = \sum\left(\frac{bh^3}{12} + Ad^2\right) = \left[\frac{2\cdot4^3}{12} + 8(1.071)^2\right] + \left[\frac{6\cdot1^3}{12} + 6(1.429)^2\right] = \frac{1369}{42} \approx 32.6$$

> **Answer.** $\bar{y} = 3.071$ above the base; $I_x \approx 32.6$ units⁴.

### Question 2: Work done by the crane force

**Path 1**, the straight line $\mathbf{r} = t(1, 2, 3)$:

$$W = \int_0^1\left[(2t)(2t)(1) + (t^2 + 3t)(2) + (2t)(3)\right]dt = \int_0^1 (6t^2 + 12t)\,dt = 2 + 6 = 8\ \text{kJ}$$

**Path 2**, the broken line $(0,0,0) \to (1,0,0) \to (1,2,0) \to (1,2,3)$: the first leg gives 0 (since $F_x = 0$ on $y = 0$), the second $\int_0^2 1\,dy = 2$, and the third $\int_0^3 2\,dz = 6$. Total 8 kJ, the same as path 1.

$\nabla\times\mathbf{F} = (1 - 1,\ 0 - 0,\ 2x - 2x) = \mathbf{0}$, so $\mathbf{F}$ is conservative, with potential

$$\phi = x^2y + yz, \qquad W = \phi(1, 2, 3) - \phi(0, 0, 0) = 2 + 6 = 8 \quad ✓$$

> **Answer.** $W = 8$ kJ on both paths; $\mathbf{F}$ is conservative with $\phi = x^2y + yz$.

## 5. Electrical and Electronics Engineering

### Question 1: Flux through the cylinder

On the curved side, $\mathbf{E}$ is parallel to $\mathbf{n}$ with $\left\|\mathbf{E}\right\| = \dfrac{\lambda}{2\pi\varepsilon_0 a}$ over an area $2\pi aL$. On the two flat ends, $\mathbf{E}\perp\mathbf{n}$, so the flux there is 0. The total flux is

$$\Phi = \frac{\lambda}{2\pi\varepsilon_0 a}\cdot 2\pi aL = \frac{\lambda L}{\varepsilon_0}$$

This is the enclosed charge divided by $\varepsilon_0$, as Gauss's law requires. ∎

> **Answer.** $\Phi = \lambda L/\varepsilon_0$

### Question 2: Circulation of B

On $r = a$, $\mathbf{B}\cdot d\mathbf{r} = \dfrac{\mu_0 I}{2\pi a}\,a\,d\theta$, so

$$\oint\mathbf{B}\cdot d\mathbf{r} = \int_0^{2\pi}\frac{\mu_0 I}{2\pi}\,d\theta = \mu_0 I, \qquad \nabla\times\mathbf{B} = \frac{1}{r}\frac{\partial}{\partial r}\left(\frac{\mu_0 I}{2\pi}\right)\mathbf{k} = \mathbf{0}\quad (r \ne 0)$$

The field is irrotational everywhere except on the wire, yet the circulation around the wire is not zero. The two results are consistent: the region without the wire is **not simply connected**, and all of the curl is concentrated on the wire ($\nabla\times\mathbf{B} = \mu_0\mathbf{J}$).

> **Answer.** $\oint\mathbf{B}\cdot d\mathbf{r} = \mu_0 I$ (Ampère's law), and $\nabla\times\mathbf{B} = \mathbf{0}$ off the wire.

## 6. Food Engineering

### Question 1: Average temperature in the dome cake

$T = 180 - 60(1 - \rho/10) = 120 + 6\rho$. The angular integrals cancel between numerator and denominator, leaving

$$\bar{T} = \frac{\int_0^{10}(120 + 6\rho)\rho^2\,d\rho}{\int_0^{10}\rho^2\,d\rho} = \frac{40\,000 + 15\,000}{1000/3} = 165\ ^\circ\text{C}$$

> **Answer.** $\bar{T} = 165$ °C

### Question 2: Air and moisture flow through the dryer opening

The opening lies in a plane $y = \text{const}$ with normal $\mathbf{j}$, so only $v_y$ counts:

$$Q = \int_0^1\!\!\int_0^{0.5}(2 + x - z)\,dz\,dx = \int_0^1 (0.875 + 0.5x)\,dx = 1.125\ \text{m}^3/\text{s}$$

The moisture removal rate is $1.125\times0.012 = 0.0135$ kg/s ≈ 48.6 kg/h.

> **Answer.** $Q = 1.125$ m³/s; moisture removal 0.0135 kg/s (48.6 kg/h).

## 7. Mechanical Engineering

### Question 1: Moment of inertia of a solid cone

Put the apex at the origin, so the radius at height $z$ is $az/h$:

$$I_z = \rho\int_0^h\!\!\int_0^{2\pi}\!\!\int_0^{az/h} r^2\cdot r\,dr\,d\theta\,dz = 2\pi\rho\int_0^h\frac{a^4z^4}{4h^4}\,dz = \frac{\pi\rho a^4 h}{10}$$

With $m = \rho\pi a^2 h/3$, this is

$$I_z = \frac{3}{10}ma^2$$

> **Answer.** $I_z = \tfrac{3}{10}ma^2$

### Question 2: Rigid-body rotation

$$\nabla\cdot\mathbf{v} = 0 + 0 = 0, \qquad \nabla\times\mathbf{v} = \left(0,\ 0,\ \frac{\partial(-x)}{\partial x} - \frac{\partial y}{\partial y}\right) = (0, 0, -2)$$

This is **rigid-body rotation**, clockwise seen from above, with angular velocity $\omega = \tfrac12\left\|\nabla\times\mathbf{v}\right\| = 1$ rad/s. Around the unit circle, taken counter-clockwise with $\mathbf{r} = (\cos t, \sin t)$:

$$\oint\mathbf{v}\cdot d\mathbf{r} = \int_0^{2\pi}\left[(\sin t)(-\sin t) + (-\cos t)(\cos t)\right]dt = -2\pi$$

This agrees with Stokes' theorem: $(-2)(\pi\cdot1^2) = -2\pi$.

> **Answer.** $\nabla\cdot\mathbf{v} = 0$, $\nabla\times\mathbf{v} = (0, 0, -2)$; circulation $-2\pi$.

## 8. Petroleum Engineering

### Question 1: Bulk volume and oil in place

The thickness at radius $r$ is $0.001r^2$, so

$$V_{\text{bulk}} = \int_0^{2\pi}\!\!\int_0^{500} 0.001r^2\cdot r\,dr\,d\theta = 0.001\cdot2\pi\cdot\frac{500^4}{4} = 9.82\times10^{7}\ \text{m}^3$$

$$\text{OIP} = \phi\,S_o\,V_{\text{bulk}} = 0.2\times0.75\times9.82\times10^{7} = 1.47\times10^{7}\ \text{m}^3$$

> **Answer.** Bulk volume $9.82\times10^7$ m³; oil in place $1.47\times10^7$ m³ (about 92.6 million barrels).

### Question 2: Darcy flux across the square

$\nabla p = (-x,\ -0.6y)$, so $\mathbf{u} = -0.01\nabla p = (0.01x,\ 0.006y)$. On each side of the square (length 200 m):

- $x = \pm100$: $\mathbf{u}\cdot\mathbf{n} = 1$, giving $1\times200 = 200$ per side.
- $y = \pm100$: $\mathbf{u}\cdot\mathbf{n} = 0.6$, giving $0.6\times200 = 120$ per side.

The net outward flux is $2(200) + 2(120) = 640$. Check with the divergence theorem: $\nabla\cdot\mathbf{u} = 0.016$, and $0.016\times200^2 = 640$ ✓. The positive value means this pressure field implies a net source, such as injection, inside the square.

> **Answer.** $\mathbf{u} = (0.01x,\ 0.006y)$; net outward flux 640 (m² per unit time, per unit thickness).
