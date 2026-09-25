# Topic 8 Solutions: Complex Analysis

## 1. Agricultural Engineering

**Question 1: groundwater flow under the drainage field**

φ_xx + φ_yy = 2 − 2 = 0, so φ is **harmonic**.

Find ψ from the Cauchy–Riemann equations:
- ψ_y = φ_x = 2x, so ψ = 2xy + g(x).
- ψ_x = −φ_y = 2y, so 2y + g′(x) = 2y and g is a constant.

So **ψ = 2xy** and **w = φ + iψ = (x + iy)² = z²**.

The streamlines xy = const are **rectangular hyperbolae**. This is flow into a corner. The complex velocity is dw/dz = 2z = 0 only at **z = 0**, which is the **stagnation point**.

**Question 2: impulse response of the greenhouse controller**

G has **no finite zeros** and **simple poles at s = −1, −2, −5**. The residues of e^{st}G(s) are:
- s = −1: 10e^{−t}/((1)(4)) = 2.5e^{−t}
- s = −2: 10e^{−2t}/((−1)(3)) = −(10/3)e^{−2t}
- s = −5: 10e^{−5t}/((−4)(−3)) = (5/6)e^{−5t}

**g(t) = 2.5e^{−t} − (10/3)e^{−2t} + (5/6)e^{−5t}** for t ≥ 0

Check: g(0) = 2.5 − 3.333 + 0.833 = 0 ✓, as expected for a third-order system.

## 2. Chemical Engineering

**Question 1: which functions are analytic**

- For f = z̄: u = x and v = −y, so u_x = 1 but v_y = −1. The first Cauchy–Riemann equation fails at **every** point, so z̄ is analytic nowhere.
- For f = eˣ(cos y + i sin y): u = eˣ cos y and v = eˣ sin y.
  - u_x = eˣ cos y = v_y ✓
  - u_y = −eˣ sin y = −v_x ✓

  The partial derivatives are continuous, so f is **analytic everywhere**. Writing e^{x+iy} = eˣe^{iy} shows that **f = e^z**.

Why it matters: if the concentration is c = Re f(z) with f analytic, then c automatically satisfies Laplace's equation, which is steady diffusion without reaction. The iso-concentration lines and flux lines (Im f) are then automatically orthogonal. If f is not analytic, none of this holds.

**Question 2: step response of the process**

C(s) = 1/(s(2s + 1)²) = (1/4)/(s(s + ½)²). It has a **simple pole at s = 0** and a **double pole at s = −½**, and no zeros.

- Residue at 0: e^{0}/(4(½)²) = 1.
- Residue at −½: d/ds[e^{st}/(4s)] at s = −½ = [te^{st}/(4s) − e^{st}/(4s²)] at s = −½ = −(t/2)e^{−t/2} − e^{−t/2}.

**c(t) = 1 − e^{−t/2} − (t/2)e^{−t/2} = 1 − (1 + t/2)e^{−t/2}** (t in minutes)

## 3. Computer Engineering

**Question 1: filter stability**

- **Zeros**: z² − 1 = 0, so **z = ±1**.
- **Poles**: z² − 0.5z + 0.06 = 0, so **z = 0.2 and z = 0.3**.

Both poles are inside |z| = 1, so the filter is **stable**. The zeros on the unit circle block DC (z = 1) and the Nyquist frequency (z = −1), so this is a band-pass filter.

```
import numpy as np
def is_stable(den):              # den = [a0, a1, ..., aN] of the z-polynomial
    poles = np.roots(den)
    return all(abs(p) < 1 for p in poles), poles
```

**Question 2: inverse z-transform**

X(z)z^{n−1} = zⁿ/((z − ½)(z − ¼)). For n ≥ 0, both poles are inside the contour |z| = R > ½.

- Res at ½: (½)ⁿ/(½ − ¼) = 4(½)ⁿ
- Res at ¼: (¼)ⁿ/(¼ − ½) = −4(¼)ⁿ

**x[n] = 4[(½)ⁿ − (¼)ⁿ]** for n ≥ 0, giving x = 0, 1, 0.75, 0.4375, …

## 4. Civil Engineering

**Question 1: seepage under the sheet pile**

Let z = b cosh w with w = φ + iψ:
- **x = b cosh φ cos ψ**
- **y = b sinh φ sin ψ**

- Holding φ fixed: x²/(b² cosh²φ) + y²/(b² sinh²φ) = 1. The equipotentials are **confocal ellipses**.
- Holding ψ fixed: x²/(b² cos²ψ) − y²/(b² sin²ψ) = 1. The streamlines are **confocal hyperbolae**.

Both families have their foci at z = ±b, which are the **branch points** of cosh⁻¹(z/b). There dz/dw = b sinh w = 0, so the inverse map is not analytic.

**Question 2: ∫_{−∞}^{∞} dx/(x² + 4)²**

f(z) = 1/(z² + 4)² has double poles at z = ±2i. Only 2i is in the upper half-plane.

Res at 2i: d/dz[1/(z + 2i)²] at z = 2i = −2/(4i)³ = −2/(−64i) = 1/(32i).

On the big semicircle, |f| ~ 1/R⁴, so that part of the integral → 0. Therefore

∫ = 2πi · 1/(32i) = **π/16 ≈ 0.196**

## 5. Electrical and Electronics Engineering

**Question 1: the Smith chart mapping**

Try w = (z − 1)/(z + 1):
- z = 0 → −1 ✓
- z = 1 → 0 ✓
- z = ∞ → 1 ✓

A bilinear transformation is fixed uniquely by three points, so **w = (z − 1)/(z + 1)**.

If Re z ≥ 0, then z is at least as close to 1 as to −1, so |z − 1| ≤ |z + 1| and **|w| ≤ 1**. The imaginary axis, |z − 1| = |z + 1|, maps to the unit circle |w| = 1.

With z = Z_L/Z₀ as the normalised impedance, w is the **reflection coefficient Γ = (Z_L − Z₀)/(Z_L + Z₀)**. Every passive load (Re z ≥ 0) plots inside the unit disc. The Smith chart is that disc with the circles of constant resistance and constant reactance drawn on it.

**Question 2: RLC impulse response**

s² + 2s + 5 = 0 gives **s = −1 ± 2i**, two **simple poles**.

h(t) = Σ Res[e^{st}H(s)] = e^{(−1+2i)t}/(4i) + e^{(−1−2i)t}/(−4i) = e^{−t}(e^{2it} − e^{−2it})/(4i)

**h(t) = ½ e^{−t} sin 2t**

This is an underdamped response that is stable, since the poles are in the left half-plane.

## 6. Food Engineering

**Question 1: steady slab temperature**

Let u = T − 20 = 5(x³ − 3xy²). Then u_xx = 30x and u_yy = −30x, so ∇²u = 0 and **T is harmonic**.

Find v from the Cauchy–Riemann equations:
- v_y = u_x = 15x² − 15y², so v = 15x²y − 5y³ + g(x).
- v_x = −u_y = 30xy, and 30xy + g′(x) = 30xy, so g is a constant.

**v = 5(3x²y − y³)**. Its level curves are the heat-flow lines.

**f(z) = u + iv = 5(x + iy)³ = 5z³**, so T = 20 + Re(5z³).

**Question 2: ∮ e^{2z}/(z − 1)³ dz on |z| = 2**

The point z = 1 is inside C. Use Cauchy's formula for derivatives, ∮ f(z)/(z − a)^{n+1} dz = 2πi f⁽ⁿ⁾(a)/n!, with f = e^{2z}, n = 2 and a = 1.

f″(z) = 4e^{2z}, so the integral is 2πi · 4e²/2! = **4πe² i ≈ 92.9i**

## 7. Mechanical Engineering

**Question 1: the Joukowski transformation**

- **Singularities**: a simple pole at z = 0, and z = ∞.
- **Critical points**: dw/dz = 1 − 1/z² = 0 gives **z = ±1**. The map is not conformal there, and these points become the sharp trailing edge of the aerofoil.

On |z| = 1, write z = e^{iθ}. Then w = e^{iθ} + e^{−iθ} = **2 cos θ**, which is real and runs over **[−2, 2]**, covered twice. The unit circle collapses onto a flat plate. Shifting the circle's centre off the origin, while keeping it through z = 1, produces a cambered, thick aerofoil.

**Question 2: ∫₀^{2π} dθ/(5 + 4 cos θ)**

Let z = e^{iθ}, so cos θ = (z + z⁻¹)/2 and dθ = dz/(iz):

∮_{|z|=1} dz / (iz(5 + 2z + 2/z)) = ∮ dz / (i(2z² + 5z + 2)) = ∮ dz / (2i(z + ½)(z + 2))

Only z = −½ is inside the circle. Res = 1/(2i · (3/2)) = 1/(3i).

**∫ = 2πi · 1/(3i) = 2π/3 ≈ 2.094**

## 8. Petroleum Engineering

**Question 1: injector–producer pair**

w has **logarithmic branch points at z = −a (source) and z = a (sink)**. These are not poles, because log is multivalued. The complex velocity dw/dz = (q/2π)[1/(z + a) − 1/(z − a)] has **simple poles** at ±a.

The equipotentials are φ = (q/2π) ln(|z + a|/|z − a|) = const, which means |z + a|/|z − a| = k. This is the locus of **Apollonius circles**, which have ±a as inverse points.

Stagnation points: dw/dz = (q/2π) · (−2a)/(z² − a²), which is never zero for finite z. So there are **no stagnation points** in the finite plane. All the fluid injected at −a goes to the producer at a.

**Question 2: mapping the off-centre well to the centre**

**w = R(z − z₀)/(R² − z̄₀z)**, where z̄₀ is the complex conjugate of z₀.

- At z = z₀, w = 0 ✓
- On |z| = R, z z̄ = R², so |R² − z̄₀z| = |z||z̄ − z̄₀| = R|z − z₀|. Hence **|w| = 1** ✓
- The point z = 0 maps to −z₀/R, which is inside the unit disc, so the inside maps to the inside.

The pressure for a *centred* well in a circular reservoir is known: p = p_w + (qμ/(2πkh)) ln(r/r_w). Because the map is conformal, Laplace's equation is preserved. Taking that solution in the w-plane and substituting w(z) gives the pressure field of the **off-centre well** directly. It also gives the well's effective shape factor for productivity calculations.
