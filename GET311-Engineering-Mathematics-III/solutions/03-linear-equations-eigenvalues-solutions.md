# Topic 3 Solutions: Linear Equations, Eigenvalues and Eigenvectors

## 1. Agricultural Engineering

### Question 1: Canal flows

From $2q_1 - q_2 = 3$ we get $q_1 = (3 + q_2)/2$, and from $q_2 - q_3 = 1$ we get $q_3 = q_2 - 1$. Substituting into the first equation:

$$\frac{3 + q_2}{2} + q_2 + q_2 - 1 = 12 \quad\Rightarrow\quad 2.5\,q_2 = 11.5 \quad\Rightarrow\quad q_2 = 4.6$$

Then $q_1 = 3.8$ and $q_3 = 3.6$.

**Check with Cramer's rule.** With $D = \det\begin{bmatrix} 1 & 1 & 1 \\ 2 & -1 & 0 \\ 0 & 1 & -1 \end{bmatrix} = 5$:

$$q_1 = \frac{D_1}{D} = \frac{19}{5} = 3.8, \qquad q_2 = \frac{D_2}{D} = \frac{23}{5} = 4.6, \qquad q_3 = \frac{D_3}{D} = \frac{18}{5} = 3.6 \quad ✓$$

> **Answer.** $q_1 = 3.8$ m³/s, $q_2 = 4.6$ m³/s, $q_3 = 3.6$ m³/s.

### Question 2: Leslie matrix

Expanding along the first row:

$$\det(L - \lambda I) = -\lambda\left(\lambda^2 - 0.9\lambda\right) + 0.8(0.54) = -\lambda^3 + 0.9\lambda^2 + 0.432$$

Setting this to zero gives $\lambda^3 - 0.9\lambda^2 - 0.432 = 0$. Its real root is $\lambda_1 = 1.2$, since $1.728 - 1.296 - 0.432 = 0$. The other two roots are complex, $-0.15 \pm 0.58i$, with modulus $0.6 < 1.2$.

The eigenvector for $\lambda = 1.2$, normalised to sum to 1, is $\left(\tfrac13, \tfrac16, \tfrac12\right)$.

> **Answer.** $\lambda_1 = 1.2$: the herd grows by 20 % per time step, settling to about 33 % calves, 17 % yearlings and 50 % adults.

## 2. Computer Engineering

### Question 1: Gauss–Seidel

```
function gauss_seidel(A, b, x, iterations):
    n = length(b)
    repeat iterations times:
        for i = 1..n:
            s = b[i] - sum(A[i][j]*x[j] for j != i)
            x[i] = s / A[i][i]          # uses the newest values at once
    return x
```

The equations rearrange to $x = \dfrac{9 + y}{10}$, $y = \dfrac{7 + x + 2z}{10}$ and $z = \dfrac{6 + 2y}{10}$. Starting from $(0, 0, 0)$:

| Iteration | $x$ | $y$ | $z$ |
|---|---|---|---|
| 1 | 0.9000 | 0.7900 | 0.7580 |
| 2 | 0.9790 | 0.9495 | 0.7899 |
| 3 | 0.9950 | 0.9575 | 0.7915 |

The exact solution is $(0.9958,\ 0.9579,\ 0.7916)$. The matrix is **strictly diagonally dominant**, because $10 > 1$, $10 > 1 + 2$ and $10 > 2$ (in each row, the diagonal entry is larger than the sum of the absolute values of the other entries), so Gauss–Seidel is guaranteed to converge.

> **Answer.** After 3 iterations, $(x, y, z) = (0.9950,\ 0.9575,\ 0.7915)$.

### Question 2: PageRank

Every column of $M$ sums to 1, so $M^{T}\mathbf{1} = \mathbf{1}$ and $\lambda = 1$ is an eigenvalue of $M^{T}$. $M$ and $M^{T}$ have the same eigenvalues, so $\lambda = 1$ is an eigenvalue of $M$. (The eigenvalues are $1, -\tfrac12, -\tfrac12$.) Solving $(M - I)\mathbf{r} = \mathbf{0}$ gives $\mathbf{r} \propto (1, 1, 1)$.

> **Answer.** $\mathbf{r} = \left(\tfrac13, \tfrac13, \tfrac13\right)$: all three pages have equal rank.

## 3. Civil Engineering

### Question 1: Principal stresses

$$\det(\sigma - \lambda I) = (80 - \lambda)(20 - \lambda) - 900 = \lambda^2 - 100\lambda + 700 = 0 \quad\Rightarrow\quad \lambda = 50 \pm 30\sqrt{2}$$

$$\sigma_1 = 92.43\ \text{MPa}, \qquad \sigma_2 = 7.57\ \text{MPa}$$

The principal directions are $\mathbf{v}_1 = (1 + \sqrt2, 1)$, at $22.5^\circ$ to the $x$-axis, and $\mathbf{v}_2 = (1 - \sqrt2, 1)$, at $112.5^\circ$. As a check,

$$\tan 2\theta = \frac{2\tau_{xy}}{\sigma_x - \sigma_y} = \frac{60}{60} = 1 \quad\Rightarrow\quad \theta = 22.5^\circ \quad ✓$$

> **Answer.** $\sigma_1 = 92.43$ MPa at $22.5^\circ$; $\sigma_2 = 7.57$ MPa at $112.5^\circ$.

### Question 2: Three-storey shear building

With $M = mI$, the problem $(K - \omega^2 M)\boldsymbol{\phi} = \mathbf{0}$ becomes $\dfrac{K}{k}\boldsymbol{\phi} = \lambda\boldsymbol{\phi}$ with $\lambda = \dfrac{\omega^2 m}{k}$. The characteristic equation is

$$\det\begin{bmatrix} 11 - \lambda & -5 & 0 \\ -5 & 8 - \lambda & -3 \\ 0 & -3 & 3 - \lambda \end{bmatrix} = -\left(\lambda^3 - 22\lambda^2 + 111\lambda - 90\right) = -(\lambda - 1)(\lambda - 6)(\lambda - 15) = 0$$

As a check, the eigenvalues add to the trace, $1 + 6 + 15 = 22$, and multiply to the determinant, $1\times6\times15 = 90$. So

$$\omega_1 = \sqrt{k/m}, \qquad \omega_2 = \sqrt6\,\sqrt{k/m} \approx 2.449\sqrt{k/m}, \qquad \omega_3 = \sqrt{15}\,\sqrt{k/m} \approx 3.873\sqrt{k/m}$$

Solving $(K/k - \lambda I)\boldsymbol{\phi} = \mathbf{0}$ for each $\lambda$ gives the mode shapes (ground floor first):

$$\boldsymbol{\phi}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \qquad \boldsymbol{\phi}_2 = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}, \qquad \boldsymbol{\phi}_3 = \begin{bmatrix} 5 \\ -4 \\ 1 \end{bmatrix}$$

In the first mode all floors move the same way, with the largest movement at the top. The second mode has one change of direction and the third has two.

> **Answer.** $\omega = 1,\ \sqrt6,\ \sqrt{15}$ times $\sqrt{k/m}$, with mode shapes $(1, 2, 3)$, $(1, 1, -1)$ and $(5, -4, 1)$.

## 4. Electrical and Electronics Engineering

### Question 1: Mesh currents by Cramer's rule

$$D = \det\begin{bmatrix} 12 & -4 & 0 \\ -4 & 10 & -2 \\ 0 & -2 & 8 \end{bmatrix} = 12(76) + 4(-32) = 784$$

$$D_1 = \det\begin{bmatrix} 24 & -4 & 0 \\ 0 & 10 & -2 \\ -6 & -2 & 8 \end{bmatrix} = 1776, \quad D_2 = \det\begin{bmatrix} 12 & 24 & 0 \\ -4 & 0 & -2 \\ 0 & -6 & 8 \end{bmatrix} = 624, \quad D_3 = \det\begin{bmatrix} 12 & -4 & 24 \\ -4 & 10 & 0 \\ 0 & -2 & -6 \end{bmatrix} = -432$$

$$I_1 = \frac{1776}{784} = 2.265\ \text{A}, \qquad I_2 = \frac{624}{784} = 0.796\ \text{A}, \qquad I_3 = \frac{-432}{784} = -0.551\ \text{A}$$

The negative $I_3$ flows opposite to the assumed direction.

> **Answer.** $I_1 = 2.265$ A, $I_2 = 0.796$ A, $I_3 = -0.551$ A.

### Question 2: RLC circuit

$$A = \begin{bmatrix} 0 & 1 \\ -4 & -4 \end{bmatrix}, \qquad \det(A - \lambda I) = \lambda^2 + 4\lambda + 4 = (\lambda + 2)^2 = 0 \quad\Rightarrow\quad \lambda = -2$$

Repeated real eigenvalues mean the circuit is **critically damped**; as a check, $R = 4$ equals $2\sqrt{L/C} = 2\sqrt{4} = 4$. Both eigenvalues have negative real part, so the circuit is **stable**.

> **Answer.** $\lambda = -2$ (double): critically damped and stable.

## 5. Food Engineering

### Question 1: Juice blend

$\det A = 0.00105 \ne 0$, so $\operatorname{rank}A = \operatorname{rank}[A \mid \mathbf{b}] = 3$, the number of unknowns. The targets can be met exactly, with a unique blend:

$$x = 47.62, \qquad y = 33.33, \qquad z = 23.81$$

All three are positive, so the blend is physically possible.

> **Answer.** Unique blend: $x = 47.62$, $y = 33.33$, $z = 23.81$ units.

### Question 2: Drying model

The characteristic equation is

$$\det(A - \lambda I) = -\left(\lambda^3 + 2.2\lambda^2 + 1.11\lambda + 0.09\right) = -(\lambda + 0.1)(\lambda + 0.6)(\lambda + 1.5) = 0$$

so the eigenvalues are $-0.1$, $-0.6$ and $-1.5$ per hour. The solution is a sum of terms $c_i\mathbf{v}_i e^{\lambda_i t}$. The fast modes die out within a few hours. The mode with the smallest $\left|\lambda\right|$, $0.1$ per hour, decays most slowly and controls the drying time:

$$\tau = \frac{1}{0.1} = 10\ \text{h}, \qquad t_{1\%} \approx 4.6\,\tau \approx 46\ \text{h}$$

> **Answer.** $\lambda = -0.1,\ -0.6,\ -1.5$ per hour; the slowest mode ($\tau = 10$ h) sets the drying time, about 46 h to remove 99 % of the excess moisture.

## 6. Mechanical Engineering

### Question 1: Natural frequencies and mode shapes

$$\det(K - \omega^2 M) = (300 - 2\omega^2)(100 - \omega^2) - 10\,000 = 0 \quad\Rightarrow\quad \omega^4 - 250\omega^2 + 10\,000 = 0$$

This gives $\omega^2 = 50$ or $200$, so $\omega_1 = 7.07$ rad/s and $\omega_2 = 14.14$ rad/s.

- Mode 1: $(300 - 100)x_1 = 100x_2$, so $x_2 = 2x_1$ and $\boldsymbol{\phi}_1 = (1, 2)$. Both masses move in the same direction.
- Mode 2: $(300 - 400)x_1 = 100x_2$, so $x_2 = -x_1$ and $\boldsymbol{\phi}_2 = (1, -1)$. The masses move in opposite directions.

> **Answer.** $\omega_1 = 7.07$ rad/s with mode $(1, 2)$; $\omega_2 = 14.14$ rad/s with mode $(1, -1)$.

### Question 2: Cayley–Hamilton

The characteristic equation is $\lambda^2 - 7\lambda + 10 = 0$, so $A^2 - 7A + 10I = 0$. Multiplying by $A^{-1}$:

$$A^{-1} = \frac{7I - A}{10} = \begin{bmatrix} 0.3 & -0.1 \\ -0.2 & 0.4 \end{bmatrix}$$

Using $A^2 = 7A - 10I$:

$$A^3 = 7A^2 - 10A = 7(7A - 10I) - 10A = 39A - 70I = \begin{bmatrix} 86 & 39 \\ 78 & 47 \end{bmatrix}$$

Direct check: $\det A = 10$, so $A^{-1} = \frac{1}{10}\begin{bmatrix} 3 & -1 \\ -2 & 4 \end{bmatrix}$ ✓

> **Answer.** $A^{-1} = \begin{bmatrix} 0.3 & -0.1 \\ -0.2 & 0.4 \end{bmatrix}$ and $A^3 = \begin{bmatrix} 86 & 39 \\ 78 & 47 \end{bmatrix}$.
