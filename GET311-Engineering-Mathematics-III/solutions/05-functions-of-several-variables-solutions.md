# Topic 5 Solutions: Functions of Several Variables

## 1. Agricultural Engineering

**Question 1: maximum crop yield**

Set both partial derivatives to zero:
- Y_N = 0.04 − 0.0002N + 0.00005W = 0
- Y_W = 0.05 − 0.0004W + 0.00005N = 0

Solving gives **N = 238.7 kg/ha and W = 154.8 mm**, with Y_max = **8.65 t/ha**.

Second-derivative test: Y_NN = −0.0002, Y_WW = −0.0004 and Y_NW = 0.00005.

D = (−0.0002)(−0.0004) − (0.00005)² = 7.75 × 10⁻⁸ > 0, and Y_NN < 0. So the point is a **maximum**.

**Question 2: error in evapotranspiration**

Take logarithms: ln E = ln k + 0.5 ln T + 0.8 ln R. Differentiating:

dE/E = 0.5 dT/T + 0.8 dR/R

In the worst case the errors add: 0.5(2 %) + 0.8(3 %) = **3.4 %**.

## 2. Chemical Engineering

**Question 1: van der Waals partial derivatives**

Write P = RT/(V − b) − a/V². Then:
- **(∂P/∂V)_T = −RT/(V − b)² + 2a/V³**
- **(∂P/∂T)_V = R/(V − b)**

Now treat F(P, V, T) = 0. Implicit differentiation gives:
- (∂V/∂T)_P = −(∂P/∂T)_V / (∂P/∂V)_T
- (∂T/∂P)_V = 1 / (∂P/∂T)_V

Multiply the three:

(∂P/∂V)_T · [−(∂P/∂T)_V/(∂P/∂V)_T] · [1/(∂P/∂T)_V] = **−1** ∎

**Question 2: least surface area for a fixed volume**

Minimise A = 2πr² + 2πrh subject to πr²h = 10. The Lagrange conditions are:
- 4πr + 2πh = λ·2πrh
- 2πr = λπr²

The second gives λ = 2/r. Substituting into the first gives 4r + 2h = 4h, so **h = 2r**. The height equals the diameter.

Then 2πr³ = 10, so **r = (5/π)^{1/3} = 1.168 m, h = 2.335 m**, and A_min = **25.7 m²**.

## 3. Computer Engineering

**Question 1: gradient descent**

∇L = (2(w₁ − 3) + w₂, 4(w₂ + 1) + w₁)

Update rule: **w ← w − η∇L(w)**, with η = 0.1.

| k | w₁ | w₂ | L |
|---|---|---|---|
| 0 | 0 | 0 | 11.00 |
| 1 | 0.600 | −0.400 | 6.24 |
| 2 | 1.120 | −0.700 | 2.93 |
| 3 | 1.566 | −0.932 | 0.61 |

The iterates are heading towards the true minimum at ∇L = 0, which is **(4, −2)** with L = −4.

**Question 2: image gradient**

I(3, 4) = 100e^{−25/50} = 60.65.

∇I = −(2/50)(x, y) I, so ∇I(3, 4) = −0.04(3, 4)(60.65) = **(−7.28, −9.70)**.

- Magnitude = **12.13**. This is the edge strength.
- Direction = **(−0.6, −0.8)**, pointing towards the bright centre.

Edge detectors (Sobel, Canny) estimate ∇I with finite differences at each pixel. They mark as edges the pixels where |∇I| is a local maximum across the gradient direction and above a threshold. The edge itself runs perpendicular to ∇I.

## 4. Civil Engineering

**Question 1: slope and drainage at (10, 20)**

z(10, 20) = 50 − 1 − 8 = 41 m, and ∇z = (−0.02x, −0.04y) = **(−0.2, −0.8)**.

- **Directional derivative** along (3/5, 4/5): −0.12 − 0.64 = **−0.76**. The ground falls 0.76 m per metre in that direction.
- **Steepest descent (drainage)**: along −∇z = (0.2, 0.8), or (0.243, 0.970) as a unit vector. The slope there is |∇z| = 0.825.
- **Tangent plane**: z = 41 − 0.2(x − 10) − 0.8(y − 20), which simplifies to **0.2x + 0.8y + z = 59**.

**Question 2: strongest beam from a log**

Maximise S = bh² subject to b² + h² = d². The Lagrange conditions are:
- h² = 2λb
- 2bh = 2λh, so λ = b

Then h² = 2b², so **h = √2 b**. Substituting into the constraint gives 3b² = d², so:

**b = d/√3 ≈ 0.577d and h = d√(2/3) ≈ 0.816d** (depth : breadth = √2 : 1)

## 5. Electrical and Electronics Engineering

**Question 1: error in dissipated power**

P = V²/R = 48 400/50 = **968 W**.

dP = (2V/R)dV − (V²/R²)dR = 8.8 dV − 19.36 dR.

The worst case has the errors in the directions that add:

|dP| ≤ 8.8(2) + 19.36(0.5) = 17.6 + 9.68 = **27.3 W**

Relative error = 2(2/220) + 0.5/50 = 0.0182 + 0.0100 = **2.8 %**.

**Question 2: the point-charge potential**

Let r² = x² + y² + z², so V = k/r.

- V_x = −kx/r³
- V_xx = −k/r³ + 3kx²/r⁵
- V_yy and V_zz have the same form.

Adding: ∇²V = −3k/r³ + 3k(x² + y² + z²)/r⁵ = −3k/r³ + 3k/r³ = **0** for r ≠ 0 ∎

At (1, 2, 2), r = 3 and V = k/3. The equipotential through that point is the **sphere x² + y² + z² = 9**.

## 6. Food Engineering

**Question 1: moisture during drying**

- ∂M/∂t = **−k(T) M**
- ∂M/∂T = −M₀ t k′(T) e^{−kt} = **−0.05 k(T) t M**, since k′ = 0.05k

With T = 60 + 0.5t, dT/dt = 0.5. The chain rule gives:

dM/dt = ∂M/∂t + (∂M/∂T)(dT/dt) = −kM − 0.025ktM = **−k(T) M (1 + 0.025t)**, where k = 0.01e^{0.025t}.

The rising temperature speeds up drying in two ways: k grows, and the extra (1 + 0.025t) factor appears.

**Question 2: cheapest cereal box**

Let the base be a × b and the height c. Cost is proportional to C = 2(2ab) + 2ac + 2bc, subject to abc = 3000.

The Lagrange conditions give a = b (by symmetry) and **c = 2a**. Then 2a³ = 3000, so:

**a = b = 11.45 cm and c = 22.89 cm**

The box is twice as tall as it is wide because its top and bottom cost more.

## 7. Mechanical Engineering

**Question 1: path of fastest heating**

∇T = (−2x, −4y), so ∇T(2, 1) = (−4, −4).

- **Direction** = (−1, −1)/√2, towards the hotter centre.
- **Rate** = |∇T| = **4√2 ≈ 5.66 °C per unit length**.

The path follows the gradient: dx/dt = −2x and dy/dt = −4y. So x = 2e^{−2t} and y = e^{−4t}, which gives **y = x²/4**. The sensor moves along a parabola towards the hottest point (0, 0).

**Question 2: the helicoid blade surface**

- **r**_u = (cos v, sin v, 0)
- **r**_v = (−u sin v, u cos v, ½)

**r**_u × **r**_v = **(½ sin v, −½ cos v, u)**, with |**r**_u × **r**_v| = **√(u² + ¼)**.

Unit normal: **n** = (½ sin v, −½ cos v, u)/√(u² + ¼).

Surface element: **dS = √(u² + ¼) du dv**.

## 8. Petroleum Engineering

**Question 1: the pressure field around the well**

Let c = qμ/(4πkh) and r² = x² + y². Then p = pₑ − c ln(r²/rₑ²), and

**∇p = −2c(x, y)/r² = −(qμ/(2πkh)) r̂/r**

This is purely radial, with magnitude falling off as 1/r. So the flow, along −∇p, is **radial**, and the Darcy velocity is u = (k/μ)(q/(2πkh))/r, which gives the familiar q/(2πrh).

Note on the sign: with the formula exactly as written, p *increases* towards the well, so −∇p points **outward**. That describes an injector. For a **producing** well, the pressure must be lowest at the well: p = pₑ + c ln(r²/rₑ²). Then ∇p points outward and the flow −∇p points **radially inward, towards the well** ✓. Students should spot and correct the sign.

**Question 2: linearising Bₒ**

Bₒ is already linear in p and T, so its first-order Taylor expansion about (3000, 150) is the function itself:

Bₒ ≈ 1.2 + 0.0001(T − 150) − 0.00002(p − 3000)

At (2800 psi, 160 °F): Bₒ = 1.2 + 0.0001(10) − 0.00002(−200) = 1.2 + 0.001 + 0.004 = **1.205 rb/stb**
