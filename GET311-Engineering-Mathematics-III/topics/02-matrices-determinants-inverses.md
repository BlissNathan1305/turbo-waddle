# Topic 2: Elements of Matrices, Determinants and Inverses of Matrices

[← Back to course overview](../README.md)

## Introduction

A **matrix** is a rectangular array of numbers set out in rows and columns. It is a compact way to store data and to represent linear transformations. The key ideas are:

- **Types of matrices:** square, diagonal, identity, triangular, symmetric, skew-symmetric, orthogonal and singular.
- **Matrix algebra:** addition, scalar multiplication, matrix multiplication (associative but *not* commutative) and the transpose.
- **Determinant:** a scalar attached to a square matrix, found by cofactor expansion or row reduction. It measures how much the transformation scales volume. A matrix is invertible exactly when $\det A \ne 0$.
- **Properties of determinants:** the effect of row operations, $\det(AB) = \det A \det B$, and $\det A^{T} = \det A$.
- **Inverse of a matrix:** $A^{-1}$ satisfies $AA^{-1} = I$. It can be found with the adjoint formula $A^{-1} = \operatorname{adj}(A)/\det A$ or with Gauss–Jordan elimination.
- **Rank:** the number of linearly independent rows or columns.

Engineers use matrices to store stiffness, conductance, transition and input–output data, and use inverses and determinants to solve for unknowns, test stability and change coordinates.

---

## Application Questions

### 1. Agricultural Engineering

1. A farm makes three crops (maize, cassava, yam) over two seasons. The yield matrix $Y$ (tonnes/ha) is $2 \times 3$ and the price vector $\mathbf{p}$ (₦/tonne) is $3 \times 1$. With $Y = \begin{bmatrix} 2.5 & 12 & 8 \\ 3.0 & 10 & 9 \end{bmatrix}$ and $\mathbf{p} = (150\,000,\ 40\,000,\ 60\,000)^{T}$, compute the revenue per hectare for each season using matrix multiplication.
2. A tractor's hitch linkage gives the transformation matrix $A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$ between input and output displacements. Find $\det A$ and $A^{-1}$, and explain what $\det A$ says about how the linkage changes the area of the motion region.

### 2. Chemical Engineering

1. A mixer takes three feed streams, and the composition matrix $C$ (rows = components, columns = streams) is $C = \begin{bmatrix} 0.6 & 0.2 & 0.1 \\ 0.3 & 0.5 & 0.2 \\ 0.1 & 0.3 & 0.7 \end{bmatrix}$. Find $C^{-1}$ and use it to get the feed flow rates that give component product flows $(50, 40, 60)$ kg/h.
2. The rate constants of a reversible reaction network are placed in a $3 \times 3$ matrix $K$. Show that if the rows of $K$ add to zero (mass conservation), then $\det K = 0$. Explain why this makes $K$ singular in physical terms.

### 3. Computer Engineering

1. In a Hill cipher, a message is encrypted with the key matrix $K = \begin{bmatrix} 3 & 3 \\ 2 & 5 \end{bmatrix} \pmod{26}$. Find $\det K \bmod 26$, check that $K$ is invertible mod 26, and find the decryption matrix $K^{-1} \bmod 26$.
2. Homogeneous coordinates use $3 \times 3$ matrices for 2-D translation, rotation and scaling. Write the matrix that translates by $(4, -2)$ and then rotates by $90^\circ$. Find its determinant and inverse, and explain why the determinant is 1.

### 4. Civil Engineering

1. A two-member spring model of a structure has stiffness matrix $K = \begin{bmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 \end{bmatrix}$ with $k_1 = 200$ kN/m and $k_2 = 150$ kN/m. Find $K^{-1}$ (the flexibility matrix) and the displacements under loads $\mathbf{F} = (10, 5)^{T}$ kN.
2. Show that the stiffness matrix of an unsupported beam element has determinant zero. Explain, using rank, why supports (boundary conditions) must be applied before the system can be solved.

### 5. Electrical and Electronics Engineering

1. A two-port network has the impedance matrix $Z = \begin{bmatrix} 10 & 4 \\ 4 & 6 \end{bmatrix}\ \Omega$. Find the admittance matrix $Y = Z^{-1}$ and the port currents when $\mathbf{V} = (20, 12)^{T}$ V.
2. Nodal analysis of a three-node resistive circuit gives the conductance matrix $G = \begin{bmatrix} 0.5 & -0.2 & 0 \\ -0.2 & 0.7 & -0.3 \\ 0 & -0.3 & 0.4 \end{bmatrix}$ S. Compute $\det G$ by cofactor expansion and state whether a unique set of node voltages exists.

### 6. Food Engineering

1. A bakery makes bread, cake and biscuits. The ingredient-use matrix (kg of flour, sugar and fat per batch) is $A = \begin{bmatrix} 5 & 3 & 2 \\ 0.5 & 2 & 1 \\ 0.3 & 1.5 & 1 \end{bmatrix}$. With daily stock $(80, 25, 18)$ kg, find $A^{-1}$ and the number of batches that uses all the stock exactly.
2. The heat-transfer coefficients between three zones of a tunnel dryer form a symmetric matrix $H$. Given $H = \begin{bmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{bmatrix}$, show that $H$ is symmetric, compute $\det H$, and find $H^{-1}$.

### 7. Mechanical Engineering

1. The rotation matrix about the $z$-axis is $R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}$. Prove that $R$ is orthogonal ($R^{T}R = I$), that $\det R = 1$, and that $R^{-1} = R(-\theta)$.
2. A two-degree-of-freedom spring–mass system has mass matrix $M = \operatorname{diag}(2, 1)$ kg and stiffness matrix $K = \begin{bmatrix} 300 & -100 \\ -100 & 100 \end{bmatrix}$ N/m. Compute $M^{-1}K$, which is needed for the vibration analysis in Topic 3.

### 8. Petroleum Engineering

1. A finite-difference model of pressure in a 1-D reservoir with three blocks gives the transmissibility matrix $T = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}$. Find $T^{-1}$ and the block pressures when $T\mathbf{p} = (1500, 0, 1200)^{T}$ (suitably scaled).
2. Three wells produce oil, gas and water. The production-rate matrix is $P = \begin{bmatrix} 500 & 200 & 50 \\ 300 & 400 & 100 \\ 200 & 100 & 300 \end{bmatrix}$ (units/day). Find $\det P$ and explain what a zero determinant would mean for back-calculating each well's contribution from total separator readings.
