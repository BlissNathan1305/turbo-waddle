# Topic 3: Theory of Linear Equations; Eigenvalues and Eigenvectors

[← Back to course overview](../README.md)

## Introduction

**Systems of linear equations** Ax = b are the most common computational task in engineering. The theory answers three questions:

- **Existence and uniqueness (consistency):** by the Rouché–Capelli theorem, a system has a solution if and only if rank(A) = rank([A | b]). The solution is unique when that rank equals the number of unknowns. Otherwise there are infinitely many solutions.
- **Homogeneous systems:** Ax = 0 always has the trivial solution, and has non-trivial solutions exactly when det(A) = 0.
- **Solution methods:** Cramer's rule, Gaussian and Gauss–Jordan elimination, LU decomposition, and iterative methods (Jacobi, Gauss–Seidel) for large sparse systems.

**Eigenvalues and eigenvectors** describe directions that a matrix only stretches: Av = λv. The eigenvalues are the roots of the **characteristic equation** det(A − λI) = 0. Important results include:

- the sum of the eigenvalues is trace(A) and their product is det(A);
- a symmetric matrix has real eigenvalues and orthogonal eigenvectors;
- **diagonalisation** A = PDP⁻¹, which makes powers and exponentials of A easy to compute;
- the **Cayley–Hamilton theorem**: every square matrix satisfies its own characteristic equation.

Eigen-analysis gives natural frequencies and vibration modes, the stability of dynamic systems, principal stresses, the steady states of Markov processes and the principal components of data.

---

## Application Questions

### 1. Agricultural Engineering

1. An irrigation network has three canals with flows q₁, q₂, q₃ (m³/s) that satisfy q₁ + q₂ + q₃ = 12, 2q₁ − q₂ = 3 and q₂ − q₃ = 1. Use Gaussian elimination to find the flows, and check the result with Cramer's rule.
2. A livestock population has calves, yearlings and adults. It is modelled by the Leslie matrix L = [[0, 0, 0.8], [0.6, 0, 0], [0, 0.9, 0.9]]. Find the dominant eigenvalue and its eigenvector. What do they say about long-term herd growth and the herd's age structure?

### 2. Chemical Engineering

1. A system of three CSTRs in series with recycle gives the linear equations 5C₁ − C₃ = 20, −4C₁ + 5C₂ = 0 and −4C₂ + 5C₃ = 0 (concentrations in mol/L). Decide whether the system is consistent, then solve it using LU decomposition.
2. Two first-order reactions A ⇌ B are modelled by dx/dt = Kx with K = [[−3, 1], [3, −1]]. Find the eigenvalues and eigenvectors of K, and use them to write the general solution. Interpret the zero eigenvalue as the equilibrium composition.

### 3. Computer Engineering

1. Write an algorithm (pseudocode or Python) for Gauss–Seidel iteration, and use it for 3 iterations on 10x − y = 9, −x + 10y − 2z = 7, −2y + 10z = 6. State the convergence condition (diagonal dominance) and check it.
2. A simplified PageRank for 3 web pages uses the column-stochastic link matrix M = [[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]]. Show that λ = 1 is an eigenvalue, and find the normalised eigenvector that gives the page ranks.

### 4. Civil Engineering

1. The plane stress at a point is given by the tensor σ = [[80, 30], [30, 20]] MPa. Find the principal stresses (eigenvalues) and principal directions (eigenvectors), and give the angle of the principal plane.
2. A three-storey shear building has mass matrix M = mI and stiffness matrix K = k[[2, −1, 0], [−1, 2, −1], [0, −1, 1]]. Set up the eigenvalue problem (K − ω²M)φ = 0, and find the natural frequencies in terms of k/m.

### 5. Electrical and Electronics Engineering

1. Mesh analysis of a circuit gives 12I₁ − 4I₂ = 24, −4I₁ + 10I₂ − 2I₃ = 0 and −2I₂ + 8I₃ = −6. Solve for the mesh currents with Cramer's rule.
2. The state-space model of an RLC circuit is ẋ = Ax with A = [[0, 1], [−1/(LC), −R/L]]. For R = 4 Ω, L = 1 H and C = 0.25 F, find the eigenvalues of A. Classify the circuit as over-, critically or under-damped, and say whether it is stable.

### 6. Food Engineering

1. A juice blender mixes three concentrates to meet targets for sugar, acidity and vitamin C. This gives 0.1x + 0.2y + 0.15z = 15, 0.02x + 0.01y + 0.03z = 2 and 0.5x + 0.2y + 0.4z = 40. Decide using ranks whether the targets can be met exactly, and solve the system.
2. The moisture transfer between the surface, middle and core layers of a drying grain kernel is modelled by dM/dt = AM with A = [[−2, 1, 0], [1, −2, 1], [0, 1, −1]]. Find the eigenvalues of A and explain how the smallest eigenvalue in magnitude controls the drying time.

### 7. Mechanical Engineering

1. For the spring–mass system of Topic 2 (M = diag(2, 1), K = [[300, −100], [−100, 100]]), solve det(K − ω²M) = 0 to get the two natural frequencies, and find and sketch the corresponding mode shapes.
2. Use the Cayley–Hamilton theorem to find A⁻¹ and A³ for the inertia-like matrix A = [[4, 1], [2, 3]]. Check A⁻¹ by direct computation.

### 8. Petroleum Engineering

1. The material balance for three reservoir compartments linked by transmissibility gives 3p₁ − p₂ = 4000, −p₁ + 3p₂ − p₃ = 1000 and −p₂ + 2p₃ = 2500 (psi). Solve for the compartment pressures with Gauss–Jordan elimination.
2. The permeability tensor of an anisotropic formation is k = [[200, 50], [50, 100]] mD. Find the principal permeabilities and the directions of maximum and minimum permeability, and explain how these directions affect horizontal well placement.
