# Topic 1 Solutions: Linear Algebra

## 1. Agricultural Engineering

**Question 1: independence and span of the fertilizer vectors**

Put **a**, **b** and **c** as the columns of a matrix and take its determinant:

det [[20, 0, 10], [10, 20, 0], [10, 20, 30]] = 20(20·30 − 0·20) − 0 + 10(10·20 − 20·10) = 12 000 − 0 + 0 = 12 000.

Since the determinant is not zero, the three vectors are **linearly independent**. Three independent vectors in ℝ³ form a basis, so they **span ℝ³**. Mathematically, any composition (N, P, K) can be written as α**a** + β**b** + γ**c**.

In practice a blend needs α, β, γ ≥ 0, since you cannot add a negative amount of fertilizer. The compositions you can actually make are only those with non-negative coefficients, which form a cone inside ℝ³.

**Question 2: distances and angle between soil samples**

- **s₁** − **r** = (2, 0.3, 0.2), so |**s₁** − **r**| = √(4 + 0.09 + 0.04) = **2.03**.
- **s₂** − **r** = (−2, −0.4, −0.2), so |**s₂** − **r**| = √(4 + 0.16 + 0.04) = **2.05**.
- **s₁** · **s₂** = 22·18 + 3.1·2.4 + 6.2·5.8 = 396 + 7.44 + 35.96 = 439.4.
- |**s₁**| = 23.07 and |**s₂**| = 19.07, so cos θ = 439.4 / (23.07 × 19.07) = 0.9993 and **θ ≈ 2.2°**.

Both samples are about the same distance from the reference, on opposite sides of it. The very small angle means they have almost the same *proportions* and differ mainly in overall size, which here is driven by moisture. Note that the distance is dominated by moisture because it has the largest numbers. In practice each variable should be scaled (normalised) before comparing.

## 2. Chemical Engineering

**Question 1: balancing CH₄ + O₂ → CO₂ + H₂O**

Let the coefficients be x₁, x₂, x₃, x₄. Moving the products to the left gives x₁(1, 4, 0) + x₂(0, 0, 2) − x₃(1, 0, 2) − x₄(0, 2, 1) = **0**, where each vector is (C, H, O):

- C: x₁ − x₃ = 0
- H: 4x₁ − 2x₄ = 0
- O: 2x₂ − 2x₃ − x₄ = 0

The null space is spanned by (1/2, 1, 1/2, 1). Multiplying by 2 gives the smallest integers (1, 2, 1, 2):

**CH₄ + 2O₂ → CO₂ + 2H₂O**

**Question 2: the stream compositions form a basis**

With the stream vectors as columns, det [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]] = **0.07 ≠ 0**. So the three vectors are independent and form a basis of ℝ³.

Solve α**x_A** + β**x_B** + γ**x_C** = (0.35, 0.35, 0.30) by Gaussian elimination:

**α = 3/7 ≈ 0.429, β = 5/14 ≈ 0.357, γ = 3/14 ≈ 0.214.**

Check: α + β + γ = 1, as it must be when mixing streams whose fractions each add to 1. The product is 42.9 % stream A, 35.7 % stream B and 21.4 % stream C.

## 3. Computer Engineering

**Question 1: rotation followed by scaling**

- R(30°) = [[cos 30°, −sin 30°], [sin 30°, cos 30°]] = [[0.866, −0.5], [0.5, 0.866]]
- S = [[2, 0], [0, 1]]

The rotation is applied first, so the combined matrix is **M = SR = [[√3, −1], [0.5, 0.866]] ≈ [[1.732, −1], [0.5, 0.866]]**.

Unit square vertices:
- (0, 0) → (0, 0)
- (1, 0) → (1.732, 0.5)
- (1, 1) → (0.732, 1.366)
- (0, 1) → (−1, 0.866)

det M = 2 × 1 = 2, so the image is a parallelogram of area 2.

**Question 2: cosine similarity**

**d₁** · **d₂** = 3 + 0 + 0 + 4 = 7, |**d₁**| = √14 and |**d₂**| = √6.

cos θ = 7 / √84 = **0.764**

Algorithm:

```
function most_similar(q, docs):
    best, best_score = None, -1
    for each d in docs:
        score = dot(q, d) / (norm(q) * norm(d))
        if score > best_score: best, best_score = d, score
    return best
```

## 4. Civil Engineering

**Question 1: equilibrium at the truss joint**

For equilibrium, **F₁** + **F₂** + **F₃** = **0**, so **F₃** = −(10 − 5, 0 + 8) = **(−5, −8) kN**, with magnitude 9.43 kN.

**F₁** and **F₂** are linearly independent, since det [[10, −5], [0, 8]] = 80 ≠ 0. So they span the plane, and any applied load at the joint can be resolved uniquely into components along the two members. This is what makes the joint statically determinate.

**Question 2: survey vectors**

- **AC** = **AB** + **BC** = **(90, 125, 1) m**.
- |**AC**| = √(8100 + 15 625 + 1) = **154.03 m**.
- The unit vector along **AC** is **(0.584, 0.812, 0.0065)**.
- **BC** · **AB** = −3600 + 3600 − 2 = −2, and |**AB**| = 128.18 m.
- The scalar projection of **BC** on **AB** is −2 / 128.18 = **−0.0156 m**. The vector projection is (−2 / 16 429)**AB** ≈ (−0.015, −0.005, −0.0002) m.

So BC is almost exactly perpendicular to AB.

## 5. Electrical and Electronics Engineering

**Question 1: the three-phase phasors**

In components:
- V∠0° = V(1, 0)
- V∠−120° = V(−½, −√3/2)
- V∠120° = V(−½, √3/2)

Their sum is V(1 − ½ − ½, 0 − √3/2 + √3/2) = **(0, 0)**.

Since 1·**v₁** + 1·**v₂** + 1·**v₃** = **0** with coefficients that are not all zero, the set is **linearly dependent**. (Any three vectors in ℝ² are dependent anyway.) This is why a balanced three-phase system has zero neutral current.

**Question 2: Haar-type expansion**

Every pair of basis vectors has a zero dot product. For example, **h₁** · **h₂** = 1 + 1 − 1 − 1 = 0, and **h₃** · **h₄** = 0. So the basis is orthogonal.

The coefficients are cᵢ = (**x** · **hᵢ**) / (**hᵢ** · **hᵢ**):
- c₁ = 8/4 = **2**
- c₂ = 4/4 = **1**
- c₃ = 2/2 = **1**
- c₄ = −2/2 = **−1**

Check: 2(1, 1, 1, 1) + (1, 1, −1, −1) + (1, −1, 0, 0) − (0, 0, 1, −1) = (4, 2, 0, 2) ✓

## 6. Food Engineering

**Question 1: ingredient masses**

The composition vectors (12, 2, 70), (25, 15, 5) and (1, 0, 95) are independent (det ≠ 0), so together they span ℝ³.

Let x, y, z be the masses in units of 100 g. Then:
- 12x + 25y + z = 10
- 2x + 15y = 3
- 70x + 5y + 95z = 75

Solving gives x = 0.532, y = 0.129 and z = 0.391, so you need **53.2 g, 12.9 g and 39.1 g** of the three ingredients (105.2 g in total).

**Question 2: colour difference**

**e** = batch − target = (−3, 4, −3).

**ΔE = √(9 + 16 + 9) = √34 ≈ 5.83**

The unit error direction is (−0.514, 0.686, −0.514). The batch is darker (lower L*), redder (higher a*) and less yellow (lower b*) than the target. A ΔE above about 2–3 is visible to the eye.

## 7. Mechanical Engineering

**Question 1: moment of the force**

**M** = **r** × **F** = |**i** **j** **k**; 1 2 0; 3 −2 5| = (2·5 − 0, 0·3 − 1·5, 1·(−2) − 2·3) = **(10, −5, −8) N·m**

Checks:
- **M** · **r** = 10 − 10 + 0 = 0 ✓
- **M** · **F** = 30 + 10 − 40 = 0 ✓

So **M** is orthogonal to both **r** and **F**, as it must be.

**Question 2: the deformation map**

T = [[1, 0.02], [0.01, 1]].

- T(1, 0) = (1, 0.01)
- T(0, 1) = (0.02, 1)

det T = 1 − 0.0002 = **0.9998 ≠ 0**, so T is **invertible**. The area changes by −0.02 %, so the deformation is nearly area-preserving.

## 8. Petroleum Engineering

**Question 1: the blend**

**x** = 0.4**w₁** + 0.6**w₂** = **(0.640, 0.138, 0.092, 0.130)**, which adds to 1 ✓.

The distance between the wells is |**w₁** − **w₂**| = √(0.01 + 0.0009 + 0.0004 + 0.0025) = **0.117**.

**Question 2: the well path**

- The total displacement is **d₁** + **d₂** + **d₃** = **(450, 300, −1100) m**.
- The horizontal departure is √(450² + 300²) = **540.8 m**.
- det [**d₁** **d₂** **d₃**] = 0, so the vectors are **linearly dependent**. In fact **d₃** = 2**d₂** − 1.2**d₁**.

This means the three survey legs lie in a single vertical plane, the one with azimuth tan⁻¹(450/300) ≈ 56.3° from north if y points north.
