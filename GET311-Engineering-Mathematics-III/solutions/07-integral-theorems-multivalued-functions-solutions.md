# Topic 7 Solutions: Integral Theorems and Multivalued Functions

## 1. Agricultural Engineering

### Question 1: Field area by Green's theorem

With $x = 300\cos t$ and $y = 200\sin t$, we have $dx = -300\sin t\,dt$ and $dy = 200\cos t\,dt$, so

$$A = \frac12\oint(x\,dy - y\,dx) = \frac12\int_0^{2\pi}\left(60\,000\cos^2 t + 60\,000\sin^2 t\right)dt = \frac12(60\,000)(2\pi) = 60\,000\pi$$

For GPS points $(x_1, y_1), \dots, (x_n, y_n)$, treat the boundary as straight segments. The same line integral then becomes the **shoelace formula**, which is what handheld area meters compute:

$$A = \frac12\left|\sum_{i=1}^{n}\left(x_iy_{i+1} - x_{i+1}y_i\right)\right|$$

> **Answer.** $A = 60\,000\pi \approx 188\,496$ m² (18.85 ha).

### Question 2: Checking the divergence theorem

**Volume integral.** $\nabla\cdot\mathbf{q} = 2x + 2y + 2z$, so

$$\iiint_V (2x + 2y + 2z)\,dV = 1 + 1 + 1 = 3$$

**Surface integral.** On the face $x = 1$, $\mathbf{q}\cdot\mathbf{n} = 1^2 = 1$, which integrates to 1. On $x = 0$, $\mathbf{q}\cdot\mathbf{n} = -0^2 = 0$. The $y$ and $z$ faces work the same way, so the total is $1 + 1 + 1 = 3$ ✓.

> **Answer.** Both integrals equal 3.

## 2. Computer Engineering

### Question 1: The shoelace formula

On the straight edge from $(x_i, y_i)$ to $(x_{i+1}, y_{i+1})$, parametrise $x = x_i + t\,\Delta x$, $y = y_i + t\,\Delta y$ for $0 \le t \le 1$. Then

$$\int(x\,dy - y\,dx) = \int_0^1\left[(x_i + t\Delta x)\Delta y - (y_i + t\Delta y)\Delta x\right]dt = x_i\Delta y - y_i\Delta x = x_iy_{i+1} - x_{i+1}y_i$$

Summing over the edges gives $A = \tfrac12\sum_i(x_iy_{i+1} - x_{i+1}y_i)$. ∎ For the given vertices the terms are 0, 12, 14, 6 and 0, so the sum is 32 and $A = 16$.

```
function polygon_area(xs, ys):
    n = len(xs); s = 0
    for i in 0..n-1:
        j = (i + 1) mod n
        s += xs[i]*ys[j] - xs[j]*ys[i]
    return abs(s) / 2
```

> **Answer.** $A = 16$ square units.

### Question 2: atan2 and phase unwrapping

$\arg z = \theta + 2k\pi$ for any integer $k$, so it has infinitely many values; atan2 always returns the principal value, with $-\pi < \theta \le \pi$. As a point goes once round the origin counter-clockwise, the true angle rises steadily from 0 to $2\pi$. atan2, however, rises to $\pi$ and then **jumps to $-\pi$** when the point crosses the negative real axis, which is the branch cut.

**Phase unwrapping** removes these jumps: if two consecutive samples differ by more than $\pi$, add or subtract $2\pi$ from every later sample.

```
for i = 1..n-1:
    d = phase[i] - phase[i-1]
    if d >  π: offset -= 2π
    if d < -π: offset += 2π
    unwrapped[i] = phase[i] + offset
```

> **Answer.** atan2 jumps by $2\pi$ at the negative real axis; unwrapping adds back multiples of $2\pi$.

## 3. Civil Engineering

### Question 1: Area and centroid of the slab section

The curves meet at $x = 0$ and $x = 2$. Going round counter-clockwise, along $y = x^2$ from $(0, 0)$ to $(2, 4)$ and back along $y = 2x$:

$$A = \frac12\oint(x\,dy - y\,dx) = \frac12\left[\int_0^2(2x^2 - x^2)\,dx + \int_2^0(2x - 2x)\,dx\right] = \frac12\cdot\frac83 = \frac43$$

$$\bar{x} = \frac{1}{A}\oint\frac{x^2}{2}\,dy = 1, \qquad \bar{y} = -\frac{1}{A}\oint\frac{y^2}{2}\,dx = \frac85$$

Direct check: $A = \int_0^2(2x - x^2)\,dx = 4 - \tfrac83 = \tfrac43$ ✓ and $\bar{x} = \dfrac{1}{A}\int_0^2 x(2x - x^2)\,dx = 1$ ✓.

> **Answer.** $A = \tfrac43$ m²; centroid $(1,\ 1.6)$ m.

### Question 2: Seepage under the dam

$$\nabla\cdot\mathbf{q} = 2 + 3 - 5 = 0$$

The field is consistent with an incompressible soil and no sources or sinks. By the divergence theorem, the net outflow from the unit cube is $\iiint 0\,dV = 0$: whatever flows in, flows out.

> **Answer.** $\nabla\cdot\mathbf{q} = 0$; the net outflow is zero.

## 4. Electrical and Electronics Engineering

### Question 1: Ampère's law in differential form

$\oint_C\mathbf{H}\cdot d\mathbf{r} = I_{\text{enc}} = \iint_S\mathbf{J}\cdot\mathbf{n}\,dS$, and by Stokes' theorem the left side equals $\iint_S(\nabla\times\mathbf{H})\cdot\mathbf{n}\,dS$. So

$$\iint_S\left(\nabla\times\mathbf{H} - \mathbf{J}\right)\cdot\mathbf{n}\,dS = 0$$

for every surface $S$, hence $\nabla\times\mathbf{H} = \mathbf{J}$. ∎

Inside the conductor ($r < a$) the current density is uniform, so a circle of radius $r$ encloses $I r^2/a^2$. Then $H\cdot 2\pi r = I r^2/a^2$, giving

$$H = \frac{Ir}{2\pi a^2}\,\hat{\boldsymbol{\theta}}$$

which rises linearly to $I/(2\pi a)$ at the surface.

> **Answer.** $\nabla\times\mathbf{H} = \mathbf{J}$; inside the conductor $H = Ir/(2\pi a^2)$.

### Question 2: $\log(-1 + i\sqrt3)$

$\left|z\right| = 2$ and $\arg z = \tfrac{2\pi}{3} + 2k\pi$, so

$$\log z = \ln 2 + i\left(\frac{2\pi}{3} + 2k\pi\right), \qquad k = 0, \pm1, \pm2, \dots$$

The principal value is $\operatorname{Log} z = 0.693 + 2.094i$.

The principal branch gives phase angles only in the range $-180^\circ < \theta \le 180^\circ$, so a phase of $240^\circ$ is reported as $-120^\circ$. When a phase is tracked continuously, for example in a PLL or when measuring the phase shift through a filter, you must stay on one branch and unwrap, not rely on the principal value.

> **Answer.** $\log z = \ln 2 + i(2\pi/3 + 2k\pi)$; principal value $0.693 + 2.094i$.

## 5. Food Engineering

### Question 1: Heat balance for the can

The energy balance on the can volume $V$ with surface $S$ is

$$\iiint_V\rho c_p\frac{\partial T}{\partial t}\,dV = -\oiint_S\mathbf{q}\cdot\mathbf{n}\,dS = \oiint_S k\nabla T\cdot\mathbf{n}\,dS = \iiint_V\nabla\cdot(k\nabla T)\,dV$$

using the divergence theorem in the last step. So $\iiint_V\left[\rho c_p\,\partial T/\partial t - \nabla\cdot(k\nabla T)\right]dV = 0$ for any sub-volume, which gives $\rho c_p\,\partial T/\partial t = \nabla\cdot(k\nabla T)$. ∎

> **Answer.** For constant $k$ this is the heat equation $\dfrac{\partial T}{\partial t} = \alpha\nabla^2 T$.

### Question 2: Circulation round the bowl rim

$\nabla\times\mathbf{v} = (0, 0, 2)$. On the flat disc with $\mathbf{n} = \mathbf{k}$:

$$\iint(\nabla\times\mathbf{v})\cdot\mathbf{k}\,dS = 2\times\pi(0.15)^2 = 0.045\pi \approx 0.141\ \text{m}^2/\text{s}$$

Direct check: with $\mathbf{r} = (0.15\cos t,\ 0.15\sin t,\ 0.1)$, $\mathbf{v}\cdot d\mathbf{r} = (0.15)^2(\sin^2 t + \cos^2 t)\,dt$, so $\oint = 0.0225\times2\pi = 0.045\pi$ ✓.

> **Answer.** Circulation $0.045\pi \approx 0.141$ m²/s.

## 6. Mechanical Engineering

### Question 1: Work round the triangle

$$\nabla\times\mathbf{F} = \left(\frac{\partial(x + y)}{\partial y} - \frac{\partial(z + x)}{\partial z},\ \frac{\partial(y + z)}{\partial z} - \frac{\partial(x + y)}{\partial x},\ \frac{\partial(z + x)}{\partial x} - \frac{\partial(y + z)}{\partial y}\right) = (0, 0, 0)$$

By Stokes' theorem, $W = \iint(\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS = 0$. $\mathbf{F}$ is conservative, with $\phi = xy + yz + zx$: the work round *any* closed path is zero, and the work between two points does not depend on the path.

> **Answer.** $W = 0$; $\mathbf{F} = \nabla(xy + yz + zx)$ is conservative.

### Question 2: Flow round the re-entrant corner

The branch point is $z = 0$, the corner (the other is at infinity). Place the branch cut along a ray inside the solid wall, outside the $3\pi/2$ flow sector, so the flow domain contains no cut.

At $z = 1 = e^{i2k\pi}$, the values are $w = e^{i4k\pi/3}$:

- $k = 0$: $1$ (principal)
- $k = 1$: $e^{i4\pi/3} = -\tfrac12 - \tfrac{\sqrt3}{2}i$
- $k = 2$: $e^{i2\pi/3} = -\tfrac12 + \tfrac{\sqrt3}{2}i$

The velocity is

$$\frac{dw}{dz} = \frac23 z^{-1/3}, \qquad \left|\frac{dw}{dz}\right| = \frac23\left|z\right|^{-1/3} \to \infty \ \text{ as } z \to 0$$

The flow cannot turn a sharp convex corner smoothly, so the velocity becomes infinite there. In a real fluid, viscosity produces **flow separation** at such corners.

> **Answer.** Branch point $z = 0$; other values $-\tfrac12 \mp \tfrac{\sqrt3}{2}i$; $\left|dw/dz\right| \propto \left|z\right|^{-1/3}$ is unbounded at the corner.
