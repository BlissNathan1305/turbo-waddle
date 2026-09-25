# Topic 3: Theory of Linear Equations; Eigenvalues and Eigenvectors

[← Back to course overview](../README.md)

## Introduction

**Systems of linear equations** $A\mathbf{x} = \mathbf{b}$ are the most common computational task in engineering. The theory answers three questions:

- **Existence and uniqueness (consistency):** by the Rouché–Capelli theorem, a system has a solution if and only if $\operatorname{rank}A = \operatorname{rank}[A \mid \mathbf{b}]$. The solution is unique when that rank equals the number of unknowns. Otherwise there are infinitely many solutions.
- **Homogeneous systems:** $A\mathbf{x} = \mathbf{0}$ always has the trivial solution, and has non-trivial solutions exactly when $\det A = 0$.
- **Solution methods:** Cramer's rule, Gaussian and Gauss–Jordan elimination, LU decomposition, and iterative methods (Jacobi, Gauss–Seidel) for large sparse systems.

**Eigenvalues and eigenvectors** describe directions that a matrix only stretches: $A\mathbf{v} = \lambda\mathbf{v}$. The eigenvalues are the roots of the **characteristic equation** $\det(A - \lambda I) = 0$. Important results include:

- the sum of the eigenvalues is $\operatorname{tr}A$ and their product is $\det A$;
- a symmetric matrix has real eigenvalues and orthogonal eigenvectors;
- **diagonalisation** $A = PDP^{-1}$, which makes powers and exponentials of $A$ easy to compute;
- the **Cayley–Hamilton theorem**: every square matrix satisfies its own characteristic equation.

Eigen-analysis gives natural frequencies and vibration modes, the stability of dynamic systems, principal stresses, the steady states of Markov processes and the principal components of data.

---

## Application Questions

### 1. Agricultural Engineering

1. An irrigation network has three canals with flows $q_1, q_2, q_3$ (m³/s) that satisfy $q_1 + q_2 + q_3 = 12$, $2q_1 - q_2 = 3$ and $q_2 - q_3 = 1$. Use Gaussian elimination to find the flows, and check the result with Cramer's rule.
2. A livestock population has calves, yearlings and adults. It is modelled by the Leslie matrix $L = \begin{bmatrix} 0 & 0 & 0.8 \\ 0.6 & 0 & 0 \\ 0 & 0.9 & 0.9 \end{bmatrix}$. Find the dominant eigenvalue and its eigenvector. What do they say about long-term herd growth and the herd's age structure?

### 2. Chemical Engineering

1. A system of three CSTRs in series with recycle gives the linear equations $5C_1 - C_3 = 20$, $-4C_1 + 5C_2 = 0$ and $-4C_2 + 5C_3 = 0$ (concentrations in mol/L). Decide whether the system is consistent, then solve it using LU decomposition.
2. Two first-order reactions A ⇌ B are modelled by $\dfrac{d\mathbf{x}}{dt} = K\mathbf{x}$ with $K = \begin{bmatrix} -3 & 1 \\ 3 & -1 \end{bmatrix}$. Find the eigenvalues and eigenvectors of $K$, and use them to write the general solution. Interpret the zero eigenvalue as the equilibrium composition.

### 3. Computer Engineering

1. Write an algorithm (pseudocode or Python) for Gauss–Seidel iteration, and use it for 3 iterations on $10x - y = 9$, $-x + 10y - 2z = 7$, $-2y + 10z = 6$. State the convergence condition (diagonal dominance) and check it.
2. A simplified PageRank for 3 web pages uses the column-stochastic link matrix $M = \begin{bmatrix} 0 & 0.5 & 0.5 \\ 0.5 & 0 & 0.5 \\ 0.5 & 0.5 & 0 \end{bmatrix}$. Show that $\lambda = 1$ is an eigenvalue, and find the normalised eigenvector that gives the page ranks.

### 4. Civil Engineering

1. The plane stress at a point is given by the tensor $\sigma = \begin{bmatrix} 80 & 30 \\ 30 & 20 \end{bmatrix}$ MPa. Find the principal stresses (eigenvalues) and principal directions (eigenvectors), and give the angle of the principal plane.
2. A three-storey shear building has mass matrix $M = mI$ and stiffness matrix $K = k\begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}$. Set up the eigenvalue problem $(K - \omega^2 M)\boldsymbol{\phi} = \mathbf{0}$, and find the natural frequencies in terms of $k/m$.

### 5. Electrical and Electronics Engineering

1. Mesh analysis of a circuit gives $12I_1 - 4I_2 = 24$, $-4I_1 + 10I_2 - 2I_3 = 0$ and $-2I_2 + 8I_3 = -6$. Solve for the mesh currents with Cramer's rule.
2. The state-space model of an RLC circuit is $\dot{\mathbf{x}} = A\mathbf{x}$ with $A = \begin{bmatrix} 0 & 1 \\ -1/(LC) & -R/L \end{bmatrix}$. For $R = 4\ \Omega$, $L = 1$ H and $C = 0.25$ F, find the eigenvalues of $A$. Classify the circuit as over-, critically or under-damped, and say whether it is stable.

### 6. Food Engineering

1. A juice blender mixes three concentrates to meet targets for sugar, acidity and vitamin C. This gives $0.1x + 0.2y + 0.15z = 15$, $0.02x + 0.01y + 0.03z = 2$ and $0.5x + 0.2y + 0.4z = 40$. Decide using ranks whether the targets can be met exactly, and solve the system.
2. The moisture transfer between the surface, middle and core layers of a drying grain kernel is modelled by $\dfrac{d\mathbf{M}}{dt} = A\mathbf{M}$ with $A = \begin{bmatrix} -2 & 1 & 0 \\ 1 & -2 & 1 \\ 0 & 1 & -1 \end{bmatrix}$. Find the eigenvalues of $A$ and explain how the smallest eigenvalue in magnitude controls the drying time.

### 7. Mechanical Engineering

1. For the spring–mass system of Topic 2 ($M = \operatorname{diag}(2, 1)$, $K = \begin{bmatrix} 300 & -100 \\ -100 & 100 \end{bmatrix}$), solve $\det(K - \omega^2 M) = 0$ to get the two natural frequencies, and find and sketch the corresponding mode shapes.
2. Use the Cayley–Hamilton theorem to find $A^{-1}$ and $A^3$ for the inertia-like matrix $A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$. Check $A^{-1}$ by direct computation.

### 8. Petroleum Engineering

1. The material balance for three reservoir compartments linked by transmissibility gives $3p_1 - p_2 = 4000$, $-p_1 + 3p_2 - p_3 = 1000$ and $-p_2 + 2p_3 = 2500$ (psi). Solve for the compartment pressures with Gauss–Jordan elimination.
2. The permeability tensor of an anisotropic formation is $\mathbf{k} = \begin{bmatrix} 200 & 50 \\ 50 & 100 \end{bmatrix}$ mD. Find the principal permeabilities and the directions of maximum and minimum permeability, and explain how these directions affect horizontal well placement.
