# Topic 1: Linear Algebra

[← Back to course overview](../README.md)

## Introduction

Linear algebra studies **vectors**, **vector spaces** and **linear transformations**. A vector space is a set of objects that can be added together and multiplied by scalars under a fixed set of rules (axioms). Examples are ℝⁿ, the set of polynomials and the set of solutions of a linear differential equation. The main ideas are:

- **Linear combination and span:** the set of all vectors you can build from a given set by scaling and adding.
- **Linear independence:** no vector in the set can be written as a combination of the others.
- **Basis and dimension:** a basis is a minimal spanning set, and the number of vectors in it is the dimension of the space.
- **Linear transformations:** maps T with T(αu + βv) = αT(u) + βT(v). Every such map between finite-dimensional spaces can be written as a matrix.
- **Inner product, norm and orthogonality:** tools for measuring length and angle, projecting and finding least-squares approximations.

Engineering uses linear algebra constantly. Structural analysis, circuit networks, signal processing, computer graphics, process mass balances and reservoir simulation all reduce to linear models, which makes this topic the base for the rest of the course.

---

## Application Questions

### 1. Agricultural Engineering

1. A fertilizer blend is made from three stock fertilizers with N-P-K compositions **a** = (20, 10, 10), **b** = (0, 20, 20) and **c** = (10, 0, 30) (percent by mass). Decide whether these three vectors are linearly independent. Can any target composition in ℝ³ be reached by blending them? Explain using the idea of span.
2. Soil samples from a farm are described by the vector (moisture %, organic matter %, pH). Given **s₁** = (22, 3.1, 6.2), **s₂** = (18, 2.4, 5.8) and a reference sample **r** = (20, 2.8, 6.0), find the Euclidean distance of each sample from the reference and the angle between **s₁** and **s₂**. Comment on how alike the samples are.

### 2. Chemical Engineering

1. The combustion of methane, CH₄ + O₂ → CO₂ + H₂O, can be balanced by writing the atom counts (C, H, O) of each species as vectors and finding a non-trivial vector in the null space of the resulting matrix. Set up the vector equation and find the smallest integer stoichiometric coefficients.
2. In a three-component mixture, the composition vectors of streams A, B and C are **x_A** = (0.5, 0.3, 0.2), **x_B** = (0.2, 0.5, 0.3) and **x_C** = (0.3, 0.2, 0.5). Show that the set {**x_A**, **x_B**, **x_C**} is a basis of ℝ³, and express a product stream **x_P** = (0.35, 0.35, 0.30) as a linear combination of them.

### 3. Computer Engineering

1. A 2-D graphics engine rotates every point by θ = 30° and then scales it by 2 in the x-direction. Write each step as a linear transformation matrix, find the combined matrix, and apply it to the vertices of the unit square.
2. In a basic document-search system, each document is a term-frequency vector. With **d₁** = (3, 0, 1, 2) and **d₂** = (1, 1, 0, 2), compute the cosine similarity between them. Write a short algorithm (pseudocode) that returns the document most similar to a query vector **q**.

### 4. Civil Engineering

1. Three forces act at a truss joint: **F₁** = (10, 0) kN, **F₂** = (−5, 8) kN and **F₃** = (a, b) kN. Use vector addition to find **F₃** so the joint is in equilibrium. Are **F₁** and **F₂** linearly independent? What does that mean for the joint?
2. A surveyor records displacement vectors between control points: **AB** = (120, 45, 2) m and **BC** = (−30, 80, −1) m. Find **AC**, its length, and the unit vector along **AC**. Find the projection of **BC** on **AB**.

### 5. Electrical and Electronics Engineering

1. A three-phase balanced voltage set can be written as vectors in ℝ² (phasor components). Show that the phasors V∠0°, V∠−120° and V∠120° are linearly dependent, and that their sum is the zero vector.
2. A discrete signal of 4 samples, **x** = (4, 2, 0, 2), is expanded in the orthogonal basis **h₁** = (1, 1, 1, 1), **h₂** = (1, 1, −1, −1), **h₃** = (1, −1, 0, 0), **h₄** = (0, 0, 1, −1) (a Haar-type basis). Check that the basis is orthogonal, then find the coefficients of **x** using inner products.

### 6. Food Engineering

1. A food product is formulated from three ingredients whose (protein, fat, carbohydrate) contents in g per 100 g are (12, 2, 70), (25, 15, 5) and (1, 0, 95). Decide whether any nutritional profile can be made by mixing them (span). Find the mass of each ingredient needed to supply exactly (10, 3, 75) g of protein, fat and carbohydrate.
2. The colour of a juice is measured in (L*, a*, b*) colour space. The target is (45, 20, 30) and a batch measures (42, 24, 27). Compute the colour difference ΔE as a Euclidean norm, and the unit vector giving the direction of the colour error.

### 7. Mechanical Engineering

1. A force **F** = (3, −2, 5) N acts at the point **r** = (1, 2, 0) m. Compute the moment **M** = **r** × **F** about the origin, and check that **M** is orthogonal to both **r** and **F** using the dot product.
2. The displacement field of a deformed plate is modelled by a linear map T(x, y) = (x + 0.02y, 0.01x + y). Write the matrix of T, find the image of the unit vectors, and decide whether T is invertible.

### 8. Petroleum Engineering

1. The composition of a reservoir fluid is recorded as mole fractions of (C₁, C₂, C₃, C₄₊). Samples from wells W₁ and W₂ are (0.70, 0.12, 0.08, 0.10) and (0.60, 0.15, 0.10, 0.15). Find the composition of a blend with 40 % of W₁ and 60 % of W₂, and the Euclidean distance between the two well compositions.
2. A deviated well path is given by survey displacement vectors **d₁** = (0, 0, −500) m, **d₂** = (150, 100, −400) m and **d₃** = (300, 200, −200) m. Find the total displacement vector to the target and the horizontal departure. Decide whether the three vectors are linearly independent.
