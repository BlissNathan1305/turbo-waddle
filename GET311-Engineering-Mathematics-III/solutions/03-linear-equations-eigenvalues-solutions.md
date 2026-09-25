# Topic 3 Solutions: Linear Equations, Eigenvalues and Eigenvectors

## 1. Agricultural Engineering

**Question 1: canal flows**

From 2q₁ − q₂ = 3 we get q₁ = (3 + q₂)/2. From q₂ − q₃ = 1 we get q₃ = q₂ − 1. Substituting into q₁ + q₂ + q₃ = 12:

(3 + q₂)/2 + q₂ + q₂ − 1 = 12 ⇒ 2.5q₂ = 11.5 ⇒ **q₂ = 4.6 m³/s**

Then **q₁ = 3.8 m³/s** and **q₃ = 3.6 m³/s**.

Check with Cramer's rule. D = det [[1, 1, 1], [2, −1, 0], [0, 1, −1]] = 5.
- D₁ = det [[12, 1, 1], [3, −1, 0], [1, 1, −1]] = 19, so q₁ = 19/5 = 3.8 ✓
- D₂ = 23, so q₂ = 23/5 = 4.6 ✓
- D₃ = 18, so q₃ = 18/5 = 3.6 ✓

**Question 2: Leslie matrix**

Expanding along the first row, det(L − λI) = −λ(λ² − 0.9λ) + 0.8(0.54) = −λ³ + 0.9λ² + 0.432. Setting this to zero gives λ³ − 0.9λ² − 0.432 = 0. Its real root is **λ₁ = 1.2**, since 1.728 − 1.296 − 0.432 = 0. The other two roots are complex, −0.15 ± 0.58i, with modulus 0.6 < 1.2.

The eigenvector for λ = 1.2, normalised to sum to 1, is **(1/3, 1/6, 1/2)**.

Interpretation: in the long run the herd **grows by 20 % per time step**. It settles into a stable age structure of about 33 % calves, 17 % yearlings and 50 % adults, whatever the starting mix.

## 2. Chemical Engineering

**Question 1: CSTRs with recycle**

det A = 5(25) − 0 + (−1)(16) = 109 ≠ 0, so the system is **consistent with a unique solution**.

LU decomposition:
- L = [[1, 0, 0], [−0.8, 1, 0], [0, −0.8, 1]]
- U = [[5, 0, −1], [0, 5, −0.8], [0, 0, 4.36]]

Forward substitution in Ly = b gives y = (20, 16, 12.8). Back substitution in Ux = y then gives:
- **C₃ = 12.8/4.36 = 2.936 mol/L**
- **C₂ = (16 + 0.8·2.936)/5 = 3.670 mol/L**
- **C₁ = (20 + 2.936)/5 = 4.587 mol/L**

**Question 2: A ⇌ B kinetics**

det(K − λI) = (−3 − λ)(−1 − λ) − 3 = λ² + 4λ = 0, so **λ₁ = 0** and **λ₂ = −4**.

- For λ₁ = 0: 3x₁ = x₂, so **v₁ = (1, 3)**.
- For λ₂ = −4: x₁ + x₂ = 0, so **v₂ = (−1, 1)**.

General solution: **x(t) = c₁(1, 3)ᵀ + c₂e^{−4t}(−1, 1)ᵀ**

As t → ∞, x → c₁(1, 3). This is the **equilibrium, with [B]/[A] = 3 = k₁/k₋₁**. The zero eigenvalue means the total A + B is conserved. The −4 eigenvalue sets how fast equilibrium is approached, with time constant 1/4.

## 3. Computer Engineering

**Question 1: Gauss–Seidel**

```
function gauss_seidel(A, b, x, iterations):
    n = length(b)
    repeat iterations times:
        for i = 1..n:
            s = b[i] - sum(A[i][j]*x[j] for j != i)
            x[i] = s / A[i][i]          # uses the newest values at once
    return x
```

The equations rearrange to x = (9 + y)/10, y = (7 + x + 2z)/10 and z = (6 + 2y)/10. Starting from (0, 0, 0):

| Iteration | x | y | z |
|---|---|---|---|
| 1 | 0.9000 | 0.7900 | 0.7580 |
| 2 | 0.9790 | 0.9495 | 0.7899 |
| 3 | 0.9950 | 0.9575 | 0.7915 |

The exact solution is (0.9958, 0.9579, 0.7916).

Convergence: the matrix is **strictly diagonally dominant**, because |10| > 1, |10| > 1 + 2 and |10| > 2. So Gauss–Seidel is guaranteed to converge.

**Question 2: PageRank**

Every column of M sums to 1, so the rows of Mᵀ sum to 1. That means Mᵀ(1, 1, 1)ᵀ = (1, 1, 1)ᵀ, so λ = 1 is an eigenvalue of Mᵀ. M and Mᵀ have the same eigenvalues, so **λ = 1 is an eigenvalue of M**. The eigenvalues are 1, −½, −½.

Solving (M − I)**r** = 0 gives **r** ∝ (1, 1, 1). Normalised, **r = (1/3, 1/3, 1/3)**. All three pages have equal rank, as the symmetry of the links suggests.

## 4. Civil Engineering

**Question 1: principal stresses**

det(σ − λI) = (80 − λ)(20 − λ) − 900 = λ² − 100λ + 700 = 0, so λ = 50 ± 30√2.

**σ₁ = 92.43 MPa and σ₂ = 7.57 MPa.**

The principal directions are v₁ = (1 + √2, 1), at **22.5°** to the x-axis, and v₂ = (1 − √2, 1), at 112.5°. They are perpendicular.

Check: tan 2θ = 2τ/(σₓ − σᵧ) = 60/60 = 1, so θ = 22.5° ✓

**Question 2: three-storey shear building**

With M = mI, the problem becomes (K/k) φ = (ω²m/k) φ. The eigenvalues of [[2, −1, 0], [−1, 2, −1], [0, −1, 1]] are 0.198, 1.555 and 3.247. So:

**ω₁ = 0.445√(k/m), ω₂ = 1.247√(k/m), ω₃ = 1.802√(k/m)**

The first mode has all floors moving the same way, with the largest movement at the top.

## 5. Electrical and Electronics Engineering

**Question 1: mesh currents by Cramer's rule**

- D = det [[12, −4, 0], [−4, 10, −2], [0, −2, 8]] = 12(76) + 4(−32) = **784**
- D₁ = det [[24, −4, 0], [0, 10, −2], [−6, −2, 8]] = 1776, so **I₁ = 2.265 A**
- D₂ = det [[12, 24, 0], [−4, 0, −2], [0, −6, 8]] = 624, so **I₂ = 0.796 A**
- D₃ = det [[12, −4, 24], [−4, 10, 0], [0, −2, −6]] = −432, so **I₃ = −0.551 A** (it flows opposite to the assumed direction)

**Question 2: RLC circuit**

A = [[0, 1], [−4, −4]], so det(A − λI) = λ² + 4λ + 4 = (λ + 2)² = 0, giving **λ = −2 (repeated)**.

Repeated real eigenvalues mean the circuit is **critically damped**. As a check, R = 4 equals 2√(L/C) = 2√4 = 4. Both eigenvalues have negative real part, so the circuit is **stable**.

## 6. Food Engineering

**Question 1: juice blend**

det A = 0.00105 ≠ 0, so rank A = rank [A | b] = 3 = number of unknowns. The targets can be met **exactly, with a unique blend**:

**x = 47.62, y = 33.33, z = 23.81** (units of each concentrate)

All three are positive, so the blend is physically possible.

**Question 2: drying model**

The eigenvalues of A are **−0.198, −1.555 and −3.247**. The solution is a sum of terms cᵢvᵢe^{λᵢt}.

The fast modes (−3.247 and −1.555) die out quickly. The mode with the **smallest |λ|, 0.198**, decays most slowly and controls how long drying takes. Its time constant is τ = 1/0.198 ≈ 5.05 time units, so reaching about 1 % of the initial excess moisture takes around 4.6τ ≈ 23 time units.

## 7. Mechanical Engineering

**Question 1: natural frequencies and mode shapes**

det(K − ω²M) = (300 − 2ω²)(100 − ω²) − 10 000 = 2ω⁴ − 500ω² + 20 000 = 0, so ω⁴ − 250ω² + 10 000 = 0.

This gives ω² = 50 or 200:
- **ω₁ = 7.07 rad/s**
- **ω₂ = 14.14 rad/s**

Mode shapes:
- Mode 1: (300 − 100)x₁ = 100x₂, so **x₂ = 2x₁**, giving φ₁ = (1, 2). Both masses move in the same direction.
- Mode 2: (300 − 400)x₁ = 100x₂, so **x₂ = −x₁**, giving φ₂ = (1, −1). The masses move in opposite directions.

**Question 2: Cayley–Hamilton**

The characteristic equation is λ² − 7λ + 10 = 0, so by Cayley–Hamilton A² − 7A + 10I = 0.

- **A⁻¹**: multiply by A⁻¹ to get A − 7I + 10A⁻¹ = 0, so A⁻¹ = (7I − A)/10 = **[[0.3, −0.1], [−0.2, 0.4]]**.
- **A³**: A² = 7A − 10I, so A³ = 7A² − 10A = 7(7A − 10I) − 10A = 39A − 70I = **[[86, 39], [78, 47]]**.

Direct check: A⁻¹ = (1/10)[[3, −1], [−2, 4]], since det A = 10 ✓

## 8. Petroleum Engineering

**Question 1: compartment pressures**

Gauss–Jordan elimination on [[3, −1, 0 | 4000], [−1, 3, −1 | 1000], [0, −1, 2 | 2500]]:

1. R₂ → 3R₂ + R₁ gives [0, 8, −3 | 7000].
2. R₃ → 8R₃ + R₂ gives [0, 0, 13 | 27 000], so p₃ = 2076.9.
3. Back substitution gives the rest.

**p₁ = 1884.6 psi, p₂ = 1653.8 psi, p₃ = 2076.9 psi**

**Question 2: principal permeabilities**

det(k − λI) = λ² − 300λ + 17 500 = 0, so λ = 150 ± 50√2:
- **k_max = 220.7 mD**, along (1 + √2, 1), which is **22.5°** from the x-axis.
- **k_min = 79.3 mD**, at **112.5°**.

Fluid moves most easily along the k_max direction. To get the most flow into the wellbore, a horizontal well should be drilled **perpendicular to k_max**, that is, along 112.5°. The well then cuts across the high-permeability direction. Hydraulic fractures, by contrast, tend to follow the stress field, not permeability.
