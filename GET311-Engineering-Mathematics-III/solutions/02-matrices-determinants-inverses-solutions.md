# Topic 2 Solutions: Matrices, Determinants and Inverses

## 1. Agricultural Engineering

### Question 1: Revenue per hectare

$$\mathbf{R} = Y\mathbf{p} = \begin{bmatrix} 2.5 & 12 & 8 \\ 3.0 & 10 & 9 \end{bmatrix}\begin{bmatrix} 150\,000 \\ 40\,000 \\ 60\,000 \end{bmatrix} = \begin{bmatrix} 375\,000 + 480\,000 + 480\,000 \\ 450\,000 + 400\,000 + 540\,000 \end{bmatrix} = \begin{bmatrix} 1\,335\,000 \\ 1\,390\,000 \end{bmatrix}$$

> **Answer.** Season 1: ₦1 335 000 per ha. Season 2: ₦1 390 000 per ha.

### Question 2: The hitch linkage

$$\det A = 2\cdot 3 - 1\cdot 1 = 5, \qquad A^{-1} = \frac{1}{5}\begin{bmatrix} 3 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.2 \\ -0.2 & 0.4 \end{bmatrix}$$

The determinant is the area scale factor. Any region of input motion is mapped to an output region **5 times larger**. Because $\det A > 0$, orientation is kept.

> **Answer.** $\det A = 5$; the linkage multiplies areas by 5.

## 2. Chemical Engineering

### Question 1: Feed flow rates

$\det C = 0.14 \ne 0$, so $C$ is invertible, and

$$C^{-1} = \frac{1}{14}\begin{bmatrix} 29 & -11 & -1 \\ -19 & 41 & -9 \\ 4 & -16 & 24 \end{bmatrix}, \qquad \mathbf{F} = C^{-1}\begin{bmatrix} 50 \\ 40 \\ 60 \end{bmatrix} = \begin{bmatrix} 67.86 \\ 10.71 \\ 71.43 \end{bmatrix}\ \text{kg/h}$$

Check, component 1: $0.6(67.86) + 0.2(10.71) + 0.1(71.43) = 50.0$ ✓

> **Answer.** $F_1 = 67.86$ kg/h, $F_2 = 10.71$ kg/h, $F_3 = 71.43$ kg/h.

### Question 2: Rows that sum to zero

Let $\mathbf{1} = (1, 1, 1)^{T}$. If every row of $K$ sums to zero, then

$$K\mathbf{1} = \mathbf{0}$$

so $K$ has a non-zero vector in its null space, its columns are dependent, and $\det K = 0$.

Physically, the reactions only move mass between species. The total amount is conserved, so one combination of concentrations never changes and cannot be solved for independently. This also means there is always a non-trivial equilibrium (steady-state) composition.

> **Answer.** $K\mathbf{1} = \mathbf{0}$ with $\mathbf{1} \ne \mathbf{0}$, so $\det K = 0$: conservation of mass removes one degree of freedom.

## 3. Computer Engineering

### Question 1: Hill cipher key

$\det K = 3\cdot 5 - 3\cdot 2 = 9$, and $\gcd(9, 26) = 1$, so $K$ is invertible mod 26. The inverse of 9 mod 26 is 3, since $9\cdot 3 = 27 \equiv 1$. Then

$$K^{-1} \equiv 3\begin{bmatrix} 5 & -3 \\ -2 & 3 \end{bmatrix} = \begin{bmatrix} 15 & -9 \\ -6 & 9 \end{bmatrix} \equiv \begin{bmatrix} 15 & 17 \\ 20 & 9 \end{bmatrix} \pmod{26}$$

Check: $KK^{-1} = \begin{bmatrix} 105 & 78 \\ 130 & 79 \end{bmatrix} \equiv \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \pmod{26}$ ✓

> **Answer.** $\det K \equiv 9 \pmod{26}$; $K^{-1} \equiv \begin{bmatrix} 15 & 17 \\ 20 & 9 \end{bmatrix} \pmod{26}$.

### Question 2: Translate then rotate in homogeneous coordinates

$$T = \begin{bmatrix} 1 & 0 & 4 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{bmatrix}, \qquad R(90^\circ) = \begin{bmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

$$M = RT = \begin{bmatrix} 0 & -1 & 2 \\ 1 & 0 & 4 \\ 0 & 0 & 1 \end{bmatrix}, \qquad M^{-1} = \begin{bmatrix} 0 & 1 & -4 \\ -1 & 0 & 2 \\ 0 & 0 & 1 \end{bmatrix}$$

$M^{-1}$ rotates by $-90^\circ$ and then translates by $(-4, 2)$. The determinant is 1 because $\det R = 1$ (a rotation) and $\det T = 1$ (a translation); neither changes area, so their product doesn't either.

> **Answer.** $\det M = 1$; $M^{-1}$ is given above.

## 4. Civil Engineering

### Question 1: Flexibility matrix and displacements

$$K = \begin{bmatrix} 350 & -150 \\ -150 & 150 \end{bmatrix}\ \text{kN/m}, \qquad \det K = 52\,500 - 22\,500 = 30\,000$$

$$K^{-1} = \frac{1}{30\,000}\begin{bmatrix} 150 & 150 \\ 150 & 350 \end{bmatrix} = \begin{bmatrix} 1/200 & 1/200 \\ 1/200 & 7/600 \end{bmatrix}\ \text{m/kN}$$

$$\mathbf{u} = K^{-1}\mathbf{F}: \qquad u_1 = \frac{10 + 5}{200} = 0.075\ \text{m}, \qquad u_2 = \frac{10}{200} + \frac{35}{600} = 0.108\ \text{m}$$

> **Answer.** $u_1 = 75$ mm and $u_2 = 108$ mm.

### Question 2: The unsupported beam element

The Euler–Bernoulli beam element stiffness matrix is

$$K = \frac{EI}{L^3}\begin{bmatrix} 12 & 6L & -12 & 6L \\ 6L & 4L^2 & -6L & 2L^2 \\ -12 & -6L & 12 & -6L \\ 6L & 2L^2 & -6L & 4L^2 \end{bmatrix}$$

$R_1 + R_3 = \mathbf{0}$ and $R_2 + R_4 = L\,R_1$, where $R_i$ is row $i$. So only two rows are independent: $\operatorname{rank} K = 2 < 4$ and $\det K = 0$.

The two missing ranks are the two rigid-body motions: translating and rotating the whole beam produces no strain and no force. With $K$ singular, $K\mathbf{u} = \mathbf{F}$ has no unique solution. Supports remove these rigid-body modes, which removes the matching rows and columns, and the reduced matrix is non-singular.

> **Answer.** $\operatorname{rank} K = 2$, so $\det K = 0$; supports must remove the two rigid-body modes.

## 5. Electrical and Electronics Engineering

### Question 1: Admittance matrix and port currents

$$\det Z = 60 - 16 = 44, \qquad Y = Z^{-1} = \frac{1}{44}\begin{bmatrix} 6 & -4 \\ -4 & 10 \end{bmatrix} = \begin{bmatrix} 0.136 & -0.091 \\ -0.091 & 0.227 \end{bmatrix}\ \text{S}$$

$$I_1 = \frac{6(20) - 4(12)}{44} = \frac{72}{44} = 1.636\ \text{A}, \qquad I_2 = \frac{-4(20) + 10(12)}{44} = \frac{40}{44} = 0.909\ \text{A}$$

> **Answer.** $I_1 = 1.636$ A and $I_2 = 0.909$ A.

### Question 2: Determinant of the conductance matrix

Expanding along the first row:

$$\det G = 0.5\left(0.7\cdot 0.4 - 0.3\cdot 0.3\right) + 0.2\left(-0.2\cdot 0.4 - 0\right) + 0 = 0.095 - 0.016 = 0.079\ \text{S}^3$$

> **Answer.** $\det G = 0.079 \ne 0$, so the node voltages are unique.

## 6. Food Engineering

### Question 1: Batches that use all the stock

Rows are ingredients (flour, sugar, fat) and columns are products (bread, cake, biscuit). $\det A = 2.2$ and

$$A^{-1} = \begin{bmatrix} 5/22 & 0 & -5/11 \\ -1/11 & 2 & -20/11 \\ 3/44 & -3 & 85/22 \end{bmatrix}, \qquad \mathbf{x} = A^{-1}\begin{bmatrix} 80 \\ 25 \\ 18 \end{bmatrix} = \begin{bmatrix} 10 \\ 10 \\ 0 \end{bmatrix}$$

Check: flour $50 + 30 = 80$ ✓, sugar $5 + 20 = 25$ ✓, fat $3 + 15 = 18$ ✓

> **Answer.** 10 batches of bread, 10 batches of cake and no biscuits.

### Question 2: The dryer heat-transfer matrix

$H^{T} = H$, since $h_{12} = h_{21} = -1$, $h_{23} = h_{32} = -1$ and $h_{13} = h_{31} = 0$, so $H$ is symmetric.

$$\det H = 4(16 - 1) + 1(-4 - 0) + 0 = 56, \qquad H^{-1} = \frac{1}{56}\begin{bmatrix} 15 & 4 & 1 \\ 4 & 16 & 4 \\ 1 & 4 & 15 \end{bmatrix}$$

The inverse is symmetric too: the inverse of a symmetric matrix is always symmetric.

> **Answer.** $\det H = 56$; $H^{-1}$ is given above.

## 7. Mechanical Engineering

### Question 1: Properties of the rotation matrix

Let $c = \cos\theta$ and $s = \sin\theta$. Then

$$R^{T}R = \begin{bmatrix} c & s & 0 \\ -s & c & 0 \\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} c & -s & 0 \\ s & c & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} c^2 + s^2 & 0 & 0 \\ 0 & s^2 + c^2 & 0 \\ 0 & 0 & 1 \end{bmatrix} = I$$

Expanding along the third row, $\det R = 1\cdot(c^2 + s^2) = 1$. From $R^{T}R = I$ we get $R^{-1} = R^{T}$. Since $\cos(-\theta) = c$ and $\sin(-\theta) = -s$, the transpose is exactly $R(-\theta)$. ∎

> **Answer.** $R^{T}R = I$, $\det R = 1$ and $R^{-1} = R^{T} = R(-\theta)$.

### Question 2: $M^{-1}K$

$$M^{-1} = \operatorname{diag}\left(\tfrac12, 1\right), \qquad M^{-1}K = \begin{bmatrix} 150 & -50 \\ -100 & 100 \end{bmatrix}\ \text{s}^{-2}$$

Its eigenvalues are the squared natural frequencies $\omega^2$ (see Topic 3).

> **Answer.** $M^{-1}K = \begin{bmatrix} 150 & -50 \\ -100 & 100 \end{bmatrix}$

## 8. Petroleum Engineering

### Question 1: Block pressures

$$\det T = 4, \qquad T^{-1} = \frac{1}{4}\begin{bmatrix} 3 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 3 \end{bmatrix}, \qquad \mathbf{p} = T^{-1}\begin{bmatrix} 1500 \\ 0 \\ 1200 \end{bmatrix} = \begin{bmatrix} 1425 \\ 1350 \\ 1275 \end{bmatrix}\ \text{psi}$$

The pressure falls steadily from the high-pressure boundary block towards the lower one, as expected for steady 1-D flow.

> **Answer.** $\mathbf{p} = (1425,\ 1350,\ 1275)$ psi

### Question 2: Production-rate matrix

$$\det P = 500(120\,000 - 10\,000) - 200(90\,000 - 20\,000) + 50(30\,000 - 80\,000) = 3.85 \times 10^{7}$$

Since $\det P \ne 0$, each well's contribution can be recovered uniquely from the separator totals. If $\det P = 0$, at least one well's output would be a linear combination of the others. Infinitely many allocations would then fit the same totals, and the contributions could not be identified without extra measurements, such as individual well tests.

> **Answer.** $\det P = 3.85 \times 10^{7} \ne 0$, so the allocation is unique.
