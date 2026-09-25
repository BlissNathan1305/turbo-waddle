# Topic 2 Solutions: Matrices, Determinants and Inverses

## 1. Agricultural Engineering

**Question 1: revenue per hectare**

R = Y p = [[2.5, 12, 8], [3.0, 10, 9]] (150 000, 40 000, 60 000)ᵀ

- Season 1: 2.5(150 000) + 12(40 000) + 8(60 000) = 375 000 + 480 000 + 480 000 = **₦1 335 000 per ha**
- Season 2: 3(150 000) + 10(40 000) + 9(60 000) = 450 000 + 400 000 + 540 000 = **₦1 390 000 per ha**

**Question 2: the hitch linkage**

- det A = 2·3 − 1·1 = **5**.
- A⁻¹ = (1/5)[[3, −1], [−1, 2]] = **[[0.6, −0.2], [−0.2, 0.4]]**.

The determinant is the area scale factor. Any region of input motion is mapped to an output region **5 times larger**. Because det A > 0, orientation is kept.

## 2. Chemical Engineering

**Question 1: feed flow rates**

det C = **0.14**, so C is invertible, and

C⁻¹ = (1/14)[[29, −11, −1], [−19, 41, −9], [4, −16, 24]].

The feed rates are F = C⁻¹ (50, 40, 60)ᵀ:

**F₁ = 67.86 kg/h, F₂ = 10.71 kg/h, F₃ = 71.43 kg/h**

Check, component 1: 0.6(67.86) + 0.2(10.71) + 0.1(71.43) = 50.0 ✓

**Question 2: rows that sum to zero**

Let **1** = (1, 1, 1)ᵀ. If every row of K sums to zero, then K**1** = **0**. So K has a non-zero vector in its null space, its columns are dependent, and **det K = 0**.

Physically, the reactions only move mass between species. The total amount is conserved, so one combination of concentrations never changes and cannot be solved for independently. This also means there is always a non-trivial equilibrium (steady-state) composition.

## 3. Computer Engineering

**Question 1: Hill cipher key**

- det K = 3·5 − 3·2 = 9, and 9 mod 26 = **9**.
- gcd(9, 26) = 1, so K is **invertible mod 26**.
- The inverse of 9 mod 26 is 3, since 9·3 = 27 ≡ 1.
- K⁻¹ ≡ 3 · [[5, −3], [−2, 3]] = [[15, −9], [−6, 9]] ≡ **[[15, 17], [20, 9]] (mod 26)**.

Check: K K⁻¹ = [[105, 78], [130, 79]] ≡ [[1, 0], [0, 1]] (mod 26) ✓

**Question 2: translate then rotate in homogeneous coordinates**

- T = [[1, 0, 4], [0, 1, −2], [0, 0, 1]]
- R(90°) = [[0, −1, 0], [1, 0, 0], [0, 0, 1]]

**M = RT = [[0, −1, 2], [1, 0, 4], [0, 0, 1]]**, with **det M = 1**, and

**M⁻¹ = [[0, 1, −4], [−1, 0, 2], [0, 0, 1]]** (rotate by −90°, then translate by (−4, 2)).

The determinant is 1 because det R = 1 (a rotation) and det T = 1 (a translation). Neither changes area, so their product doesn't either.

## 4. Civil Engineering

**Question 1: flexibility matrix and displacements**

K = [[350, −150], [−150, 150]] kN/m, with det K = 52 500 − 22 500 = 30 000.

K⁻¹ = (1/30 000)[[150, 150], [150, 350]] = **[[1/200, 1/200], [1/200, 7/600]] m/kN**

u = K⁻¹F:
- u₁ = (10 + 5)/200 = **0.075 m (75 mm)**
- u₂ = 10/200 + 35/600 = **0.108 m (108 mm)**

**Question 2: the unsupported beam element**

The Euler–Bernoulli beam element stiffness matrix is

K = (EI/L³)[[12, 6L, −12, 6L], [6L, 4L², −6L, 2L²], [−12, −6L, 12, −6L], [6L, 2L², −6L, 4L²]]

- Row 1 + row 3 = **0**.
- Row 2 + row 4 = L × row 1.

So only two rows are independent: **rank K = 2 < 4**, and **det K = 0**.

The two missing ranks are the two rigid-body motions: translating and rotating the whole beam produces no strain and no force. With K singular, K u = F has no unique solution. Supports remove these rigid-body modes, which removes the matching rows and columns, and the reduced matrix is non-singular.

## 5. Electrical and Electronics Engineering

**Question 1: admittance matrix and port currents**

det Z = 60 − 16 = 44.

Y = Z⁻¹ = (1/44)[[6, −4], [−4, 10]] = **[[0.136, −0.091], [−0.091, 0.227]] S**

I = YV:
- I₁ = (6·20 − 4·12)/44 = 72/44 = **1.636 A**
- I₂ = (−4·20 + 10·12)/44 = 40/44 = **0.909 A**

**Question 2: determinant of the conductance matrix**

Expanding along the first row:

det G = 0.5(0.7·0.4 − 0.3·0.3) − (−0.2)(−0.2·0.4 − 0) + 0 = 0.5(0.19) + 0.2(−0.08) = 0.095 − 0.016 = **0.079 S³**

Since det G ≠ 0, the node voltages are **unique**.

## 6. Food Engineering

**Question 1: batches that use all the stock**

Rows are ingredients (flour, sugar, fat) and columns are products (bread, cake, biscuit). det A = **2.2**, and

A⁻¹ = [[5/22, 0, −5/11], [−1/11, 2, −20/11], [3/44, −3, 85/22]].

x = A⁻¹(80, 25, 18)ᵀ = **(10, 10, 0)**: 10 batches of bread, 10 batches of cake and no biscuits.

Check:
- Flour: 50 + 30 = 80 ✓
- Sugar: 5 + 20 = 25 ✓
- Fat: 3 + 15 = 18 ✓

**Question 2: the dryer heat-transfer matrix**

Hᵀ = H, since h₁₂ = h₂₁ = −1, h₂₃ = h₃₂ = −1 and h₁₃ = h₃₁ = 0. So H is symmetric.

det H = 4(16 − 1) − (−1)(−4 − 0) + 0 = 60 − 4 = **56**

H⁻¹ = (1/56)[[15, 4, 1], [4, 16, 4], [1, 4, 15]]

This is symmetric too: the inverse of a symmetric matrix is symmetric.

## 7. Mechanical Engineering

**Question 1: properties of the rotation matrix**

Let c = cos θ and s = sin θ.

RᵀR = [[c, s, 0], [−s, c, 0], [0, 0, 1]][[c, −s, 0], [s, c, 0], [0, 0, 1]] = [[c² + s², 0, 0], [0, s² + c², 0], [0, 0, 1]] = **I**

Expanding along the third row: det R = 1 · (c² + s²) = **1**.

From RᵀR = I we get R⁻¹ = Rᵀ = [[c, s, 0], [−s, c, 0], [0, 0, 1]]. Since cos(−θ) = c and sin(−θ) = −s, this is exactly **R(−θ)** ∎.

**Question 2: M⁻¹K**

M⁻¹ = diag(½, 1), so

**M⁻¹K = [[150, −50], [−100, 100]] s⁻²**

Its eigenvalues are ω² (see Topic 3).

## 8. Petroleum Engineering

**Question 1: block pressures**

det T = 2(3) − (−1)(−2) + 0 = 4, and

T⁻¹ = (1/4)[[3, 2, 1], [2, 4, 2], [1, 2, 3]].

**p** = T⁻¹(1500, 0, 1200)ᵀ = **(1425, 1350, 1275) psi**

The pressure falls steadily from the high-pressure boundary block towards the lower one, as expected for steady 1-D flow.

**Question 2: production-rate matrix**

Expanding along the first row:

det P = 500(120 000 − 10 000) − 200(90 000 − 20 000) + 50(30 000 − 80 000) = 55 000 000 − 14 000 000 − 2 500 000 = **3.85 × 10⁷ ≠ 0**

So each well's contribution can be recovered uniquely from the separator totals.

If det P = 0, at least one well's output would be a linear combination of the others. Infinitely many allocations would then fit the same totals, and the contributions could not be identified without extra measurements, such as individual well tests.
