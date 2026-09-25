# Topic 1: Linear Algebra

[← Back to course overview](../README.md)

## Introduction

Linear algebra studies **vectors**, **vector spaces** and **linear transformations**. A vector space is a set of objects that can be added together and multiplied by scalars under a fixed set of rules (axioms). Examples are $\mathbb{R}^n$, the set of polynomials and the set of solutions of a linear differential equation. The main ideas are:

- **Linear combination and span:** the set of all vectors you can build from a given set by scaling and adding.
- **Linear independence:** no vector in the set can be written as a combination of the others.
- **Basis and dimension:** a basis is a minimal spanning set, and the number of vectors in it is the dimension of the space.
- **Linear transformations:** maps $T$ with $T(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$. Every such map between finite-dimensional spaces can be written as a matrix.
- **Inner product, norm and orthogonality:** tools for measuring length and angle, projecting and finding least-squares approximations.

Engineering uses linear algebra constantly. Structural analysis, circuit networks, signal processing, computer graphics, process mass balances and reservoir simulation all reduce to linear models, which makes this topic the base for the rest of the course.

---

## Application Questions

### 1. Agricultural Engineering

1. A fertilizer blend is made from three stock fertilizers with N-P-K compositions $\mathbf{a} = (20, 10, 10)$, $\mathbf{b} = (0, 20, 20)$ and $\mathbf{c} = (10, 0, 30)$ (percent by mass). Decide whether these three vectors are linearly independent. Can any target composition in $\mathbb{R}^3$ be reached by blending them? Explain using the idea of span.
2. Soil samples from a farm are described by the vector (moisture %, organic matter %, pH). Given $\mathbf{s}_1 = (22, 3.1, 6.2)$, $\mathbf{s}_2 = (18, 2.4, 5.8)$ and a reference sample $\mathbf{r} = (20, 2.8, 6.0)$, find the Euclidean distance of each sample from the reference and the angle between $\mathbf{s}_1$ and $\mathbf{s}_2$. Comment on how alike the samples are.

### 2. Computer Engineering

1. A 2-D graphics engine rotates every point by $\theta = 30^\circ$ and then scales it by 2 in the $x$-direction. Write each step as a linear transformation matrix, find the combined matrix, and apply it to the vertices of the unit square.
2. In a basic document-search system, each document is a term-frequency vector. With $\mathbf{d}_1 = (3, 0, 1, 2)$ and $\mathbf{d}_2 = (1, 1, 0, 2)$, compute the cosine similarity between them. Write a short algorithm (pseudocode) that returns the document most similar to a query vector $\mathbf{q}$.

### 3. Civil Engineering

1. Three forces act at a truss joint: $\mathbf{F}_1 = (10, 0)$ kN, $\mathbf{F}_2 = (-5, 8)$ kN and $\mathbf{F}_3 = (a, b)$ kN. Use vector addition to find $\mathbf{F}_3$ so the joint is in equilibrium. Are $\mathbf{F}_1$ and $\mathbf{F}_2$ linearly independent? What does that mean for the joint?
2. A surveyor records displacement vectors between control points: $\overrightarrow{AB} = (120, 45, 2)$ m and $\overrightarrow{BC} = (-30, 80, -1)$ m. Find $\overrightarrow{AC}$, its length, and the unit vector along $\overrightarrow{AC}$. Find the projection of $\overrightarrow{BC}$ on $\overrightarrow{AB}$.

### 4. Electrical and Electronics Engineering

1. A three-phase balanced voltage set can be written as vectors in $\mathbb{R}^2$ (phasor components). Show that the phasors $V\angle 0^\circ$, $V\angle -120^\circ$ and $V\angle 120^\circ$ are linearly dependent, and that their sum is the zero vector.
2. A discrete signal of 4 samples, $\mathbf{x} = (4, 2, 0, 2)$, is expanded in the orthogonal basis $\mathbf{h}_1 = (1, 1, 1, 1)$, $\mathbf{h}_2 = (1, 1, -1, -1)$, $\mathbf{h}_3 = (1, -1, 0, 0)$, $\mathbf{h}_4 = (0, 0, 1, -1)$ (a Haar-type basis). Check that the basis is orthogonal, then find the coefficients of $\mathbf{x}$ using inner products.

### 5. Food Engineering

1. A food product is formulated from three ingredients whose (protein, fat, carbohydrate) contents in g per 100 g are $(12, 2, 70)$, $(25, 15, 5)$ and $(1, 0, 95)$. Decide whether any nutritional profile can be made by mixing them (span). Find the mass of each ingredient needed to supply exactly $(10, 3, 75)$ g of protein, fat and carbohydrate.
2. The colour of a juice is measured in (L\*, a\*, b\*) colour space. The target is $(45, 20, 30)$ and a batch measures $(42, 24, 27)$. Compute the colour difference $\Delta E$ as a Euclidean norm, and the unit vector giving the direction of the colour error.

### 6. Mechanical Engineering

1. A force $\mathbf{F} = (3, -2, 5)$ N acts at the point $\mathbf{r} = (1, 2, 0)$ m. Compute the moment $\mathbf{M} = \mathbf{r} \times \mathbf{F}$ about the origin, and check that $\mathbf{M}$ is orthogonal to both $\mathbf{r}$ and $\mathbf{F}$ using the dot product.
2. The displacement field of a deformed plate is modelled by a linear map $T(x, y) = (x + 0.02y,\ 0.01x + y)$. Write the matrix of $T$, find the image of the unit vectors, and decide whether $T$ is invertible.
