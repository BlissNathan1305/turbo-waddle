# Topic 1 Solutions: Linear Algebra

## 1. Agricultural Engineering

### Question 1: Independence and span of the fertilizer vectors

Put $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$ as the columns of a matrix and take its determinant:

$$\det\begin{bmatrix} 20 & 0 & 10 \\ 10 & 20 & 0 \\ 10 & 20 & 30 \end{bmatrix} = 20(600 - 0) - 0 + 10(200 - 200) = 12\,000$$

Since the determinant is not zero, the three vectors are **linearly independent**. Three independent vectors in $\mathbb{R}^3$ form a basis, so they **span** $\mathbb{R}^3$: any composition $(N, P, K)$ can be written as $\alpha\mathbf{a} + \beta\mathbf{b} + \gamma\mathbf{c}$.

In practice a blend needs $\alpha, \beta, \gamma \ge 0$, since you cannot add a negative amount of fertilizer. The compositions you can actually make are only those with non-negative coefficients, which form a cone inside $\mathbb{R}^3$.

> **Answer.** $\det = 12\,000 \ne 0$, so the vectors are independent and span $\mathbb{R}^3$. Only non-negative combinations are physically possible.

### Question 2: Distances and angle between soil samples

$$\left\|\mathbf{s}_1 - \mathbf{r}\right\| = \left\|(2,\ 0.3,\ 0.2)\right\| = \sqrt{4 + 0.09 + 0.04} = 2.03$$

$$\left\|\mathbf{s}_2 - \mathbf{r}\right\| = \left\|(-2,\ -0.4,\ -0.2)\right\| = \sqrt{4 + 0.16 + 0.04} = 2.05$$

$$\cos\theta = \frac{\mathbf{s}_1\cdot\mathbf{s}_2}{\left\|\mathbf{s}_1\right\|\left\|\mathbf{s}_2\right\|} = \frac{396 + 7.44 + 35.96}{(23.07)(19.07)} = \frac{439.4}{439.9} = 0.9993 \quad\Rightarrow\quad \theta \approx 2.2^\circ$$

Both samples are about the same distance from the reference, on opposite sides of it. The very small angle means they have almost the same *proportions* and differ mainly in overall size, which here is driven by moisture. The distance is dominated by moisture because it has the largest numbers, so in practice each variable should be scaled (normalised) before comparing.

> **Answer.** Distances $2.03$ and $2.05$; angle $\theta \approx 2.2^\circ$. The samples are very alike.

## 2. Chemical Engineering

### Question 1: Balancing CH₄ + O₂ → CO₂ + H₂O

Let the coefficients be $x_1, x_2, x_3, x_4$ and write each species as a (C, H, O) vector:

$$x_1\begin{bmatrix}1\\4\\0\end{bmatrix} + x_2\begin{bmatrix}0\\0\\2\end{bmatrix} - x_3\begin{bmatrix}1\\0\\2\end{bmatrix} - x_4\begin{bmatrix}0\\2\\1\end{bmatrix} = \mathbf{0}$$

This gives $x_1 - x_3 = 0$, $4x_1 - 2x_4 = 0$ and $2x_2 - 2x_3 - x_4 = 0$. The null space is spanned by $\left(\tfrac12, 1, \tfrac12, 1\right)$. Multiplying by 2 gives the smallest integers $(1, 2, 1, 2)$.

> **Answer.** CH₄ + 2O₂ → CO₂ + 2H₂O

### Question 2: The stream compositions form a basis

$$\det\begin{bmatrix} 0.5 & 0.2 & 0.3 \\ 0.3 & 0.5 & 0.2 \\ 0.2 & 0.3 & 0.5 \end{bmatrix} = 0.07 \ne 0$$

so the three vectors are independent and form a basis of $\mathbb{R}^3$. Solving $\alpha\mathbf{x}_A + \beta\mathbf{x}_B + \gamma\mathbf{x}_C = (0.35, 0.35, 0.30)$ by Gaussian elimination gives

$$\alpha = \frac{3}{7} \approx 0.429, \qquad \beta = \frac{5}{14} \approx 0.357, \qquad \gamma = \frac{3}{14} \approx 0.214$$

As a check, $\alpha + \beta + \gamma = 1$, as it must be when mixing streams whose fractions each add to 1.

> **Answer.** $\mathbf{x}_P = \tfrac{3}{7}\mathbf{x}_A + \tfrac{5}{14}\mathbf{x}_B + \tfrac{3}{14}\mathbf{x}_C$, that is 42.9 % A, 35.7 % B and 21.4 % C.

## 3. Computer Engineering

### Question 1: Rotation followed by scaling

$$R(30^\circ) = \begin{bmatrix} \cos 30^\circ & -\sin 30^\circ \\ \sin 30^\circ & \cos 30^\circ \end{bmatrix} = \begin{bmatrix} 0.866 & -0.5 \\ 0.5 & 0.866 \end{bmatrix}, \qquad S = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$$

The rotation is applied first, so the combined matrix is

$$M = SR = \begin{bmatrix} \sqrt{3} & -1 \\ 0.5 & 0.866 \end{bmatrix} \approx \begin{bmatrix} 1.732 & -1 \\ 0.5 & 0.866 \end{bmatrix}$$

Applying $M$ to the vertices of the unit square:

| Vertex | Image |
|---|---|
| $(0, 0)$ | $(0, 0)$ |
| $(1, 0)$ | $(1.732,\ 0.5)$ |
| $(1, 1)$ | $(0.732,\ 1.366)$ |
| $(0, 1)$ | $(-1,\ 0.866)$ |

Since $\det M = 2 \times 1 = 2$, the image is a parallelogram of area 2.

> **Answer.** $M = \begin{bmatrix} \sqrt{3} & -1 \\ 0.5 & 0.866 \end{bmatrix}$; the square becomes a parallelogram of area 2.

### Question 2: Cosine similarity

$$\cos\theta = \frac{\mathbf{d}_1\cdot\mathbf{d}_2}{\left\|\mathbf{d}_1\right\|\left\|\mathbf{d}_2\right\|} = \frac{3 + 0 + 0 + 4}{\sqrt{14}\,\sqrt{6}} = \frac{7}{\sqrt{84}} = 0.764$$

```
function most_similar(q, docs):
    best, best_score = None, -1
    for each d in docs:
        score = dot(q, d) / (norm(q) * norm(d))
        if score > best_score: best, best_score = d, score
    return best
```

> **Answer.** The cosine similarity is $0.764$.

## 4. Civil Engineering

### Question 1: Equilibrium at the truss joint

For equilibrium, $\mathbf{F}_1 + \mathbf{F}_2 + \mathbf{F}_3 = \mathbf{0}$, so

$$\mathbf{F}_3 = -\left(10 - 5,\ 0 + 8\right) = (-5, -8)\ \text{kN}, \qquad \left\|\mathbf{F}_3\right\| = 9.43\ \text{kN}$$

$\mathbf{F}_1$ and $\mathbf{F}_2$ are linearly independent because $\det\begin{bmatrix} 10 & -5 \\ 0 & 8 \end{bmatrix} = 80 \ne 0$. They span the plane, so any load at the joint can be resolved uniquely into components along the two members. This is what makes the joint statically determinate.

> **Answer.** $\mathbf{F}_3 = (-5, -8)$ kN. $\mathbf{F}_1$ and $\mathbf{F}_2$ are independent, so the member forces are unique.

### Question 2: Survey vectors

$$\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC} = (90, 125, 1)\ \text{m}, \qquad \left\|\overrightarrow{AC}\right\| = \sqrt{8100 + 15\,625 + 1} = 154.03\ \text{m}$$

The unit vector along $\overrightarrow{AC}$ is $\hat{\mathbf{u}} = (0.584,\ 0.812,\ 0.0065)$.

$$\overrightarrow{BC}\cdot\overrightarrow{AB} = -3600 + 3600 - 2 = -2, \qquad \operatorname{comp}_{AB}\overrightarrow{BC} = \frac{-2}{128.18} = -0.0156\ \text{m}$$

The vector projection is $\frac{-2}{16\,429}\overrightarrow{AB} \approx (-0.015,\ -0.005,\ -0.0002)$ m, so BC is almost exactly perpendicular to AB.

> **Answer.** $\overrightarrow{AC} = (90, 125, 1)$ m, length 154.03 m; projection of BC on AB is $-0.0156$ m.

## 5. Electrical and Electronics Engineering

### Question 1: The three-phase phasors

In components, $V\angle 0^\circ = V(1, 0)$, $V\angle -120^\circ = V\left(-\tfrac12, -\tfrac{\sqrt3}{2}\right)$ and $V\angle 120^\circ = V\left(-\tfrac12, \tfrac{\sqrt3}{2}\right)$. Their sum is

$$V\left(1 - \tfrac12 - \tfrac12,\ 0 - \tfrac{\sqrt3}{2} + \tfrac{\sqrt3}{2}\right) = (0, 0)$$

Since $1\cdot\mathbf{v}_1 + 1\cdot\mathbf{v}_2 + 1\cdot\mathbf{v}_3 = \mathbf{0}$ with coefficients that are not all zero, the set is **linearly dependent**. (Any three vectors in $\mathbb{R}^2$ are dependent anyway.) This is why a balanced three-phase system has zero neutral current.

> **Answer.** The phasors sum to $\mathbf{0}$, so they are linearly dependent.

### Question 2: Haar-type expansion

Every pair of basis vectors has zero dot product, for example $\mathbf{h}_1\cdot\mathbf{h}_2 = 1 + 1 - 1 - 1 = 0$, so the basis is orthogonal. The coefficients are

$$c_i = \frac{\mathbf{x}\cdot\mathbf{h}_i}{\mathbf{h}_i\cdot\mathbf{h}_i}: \qquad c_1 = \frac{8}{4} = 2, \quad c_2 = \frac{4}{4} = 1, \quad c_3 = \frac{2}{2} = 1, \quad c_4 = \frac{-2}{2} = -1$$

Check: $2(1,1,1,1) + (1,1,-1,-1) + (1,-1,0,0) - (0,0,1,-1) = (4, 2, 0, 2)$ ✓

> **Answer.** $\mathbf{x} = 2\mathbf{h}_1 + \mathbf{h}_2 + \mathbf{h}_3 - \mathbf{h}_4$

## 6. Food Engineering

### Question 1: Ingredient masses

The three composition vectors are independent ($\det \ne 0$), so together they span $\mathbb{R}^3$. Let $x, y, z$ be the masses in units of 100 g:

$$\begin{bmatrix} 12 & 25 & 1 \\ 2 & 15 & 0 \\ 70 & 5 & 95 \end{bmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 10 \\ 3 \\ 75 \end{bmatrix} \quad\Rightarrow\quad x = 0.532,\ y = 0.129,\ z = 0.391$$

> **Answer.** 53.2 g, 12.9 g and 39.1 g of the three ingredients (105.2 g in total).

### Question 2: Colour difference

$$\mathbf{e} = \text{batch} - \text{target} = (-3, 4, -3), \qquad \Delta E = \sqrt{9 + 16 + 9} = \sqrt{34} \approx 5.83$$

The unit error direction is $\hat{\mathbf{e}} = (-0.514,\ 0.686,\ -0.514)$. The batch is darker (lower L\*), redder (higher a\*) and less yellow (lower b\*) than the target. A $\Delta E$ above about 2–3 is visible to the eye.

> **Answer.** $\Delta E = 5.83$; direction $(-0.514,\ 0.686,\ -0.514)$.

## 7. Mechanical Engineering

### Question 1: Moment of the force

$$\mathbf{M} = \mathbf{r}\times\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & 0 \\ 3 & -2 & 5 \end{vmatrix} = (10 - 0)\,\mathbf{i} - (5 - 0)\,\mathbf{j} + (-2 - 6)\,\mathbf{k} = (10, -5, -8)\ \text{N·m}$$

Checks: $\mathbf{M}\cdot\mathbf{r} = 10 - 10 + 0 = 0$ ✓ and $\mathbf{M}\cdot\mathbf{F} = 30 + 10 - 40 = 0$ ✓, so $\mathbf{M}$ is orthogonal to both $\mathbf{r}$ and $\mathbf{F}$.

> **Answer.** $\mathbf{M} = (10, -5, -8)$ N·m

### Question 2: The deformation map

$$T = \begin{bmatrix} 1 & 0.02 \\ 0.01 & 1 \end{bmatrix}, \qquad T\begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}1\\0.01\end{bmatrix}, \qquad T\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}0.02\\1\end{bmatrix}$$

$\det T = 1 - 0.0002 = 0.9998 \ne 0$, so $T$ is **invertible**. Area changes by only −0.02 %, so the deformation is nearly area-preserving.

> **Answer.** $\det T = 0.9998$, so $T$ is invertible.

## 8. Petroleum Engineering

### Question 1: The blend

$$\mathbf{x} = 0.4\,\mathbf{w}_1 + 0.6\,\mathbf{w}_2 = (0.640,\ 0.138,\ 0.092,\ 0.130)$$

which sums to 1 ✓. The distance between the wells is

$$\left\|\mathbf{w}_1 - \mathbf{w}_2\right\| = \sqrt{0.01 + 0.0009 + 0.0004 + 0.0025} = 0.117$$

> **Answer.** Blend $(0.640,\ 0.138,\ 0.092,\ 0.130)$; distance $0.117$.

### Question 2: The well path

$$\mathbf{d}_1 + \mathbf{d}_2 + \mathbf{d}_3 = (450, 300, -1100)\ \text{m}, \qquad \text{horizontal departure} = \sqrt{450^2 + 300^2} = 540.8\ \text{m}$$

$\det\left[\mathbf{d}_1\ \mathbf{d}_2\ \mathbf{d}_3\right] = 0$, so the vectors are **linearly dependent**; in fact $\mathbf{d}_3 = 2\mathbf{d}_2 - 1.2\,\mathbf{d}_1$. The three survey legs lie in a single vertical plane, with azimuth $\tan^{-1}(450/300) \approx 56.3^\circ$ from north if $y$ points north.

> **Answer.** Total displacement $(450, 300, -1100)$ m; departure 540.8 m; the vectors are dependent.
