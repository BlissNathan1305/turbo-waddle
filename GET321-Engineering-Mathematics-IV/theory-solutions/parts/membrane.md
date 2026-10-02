We need the vectors $x$ for which $y = Ax$ is parallel to $x$, that is $Ax = \lambda x$. These are the eigenvectors of

$$A = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}$$

**Eigenvalues.**

$$\det(A - \lambda I) = (5 - \lambda)^2 - 9 = \lambda^2 - 10\lambda + 16 = (\lambda - 8)(\lambda - 2) = 0 \quad\Rightarrow\quad \lambda_1 = 8, \ \lambda_2 = 2$$

**Eigenvectors.**

For $\lambda_1 = 8$: $\ -3x_1 + 3x_2 = 0 \ \Rightarrow\ x_2 = x_1$, so $x^{(1)} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$, at $45^\circ$ to the $x_1$-axis.

For $\lambda_2 = 2$: $\ 3x_1 + 3x_2 = 0 \ \Rightarrow\ x_2 = -x_1$, so $x^{(2)} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$, at $135^\circ$ (or $-45^\circ$) to the $x_1$-axis.

Both eigenvalues are positive, so in each principal direction $y$ points the **same** way as $x$. The two directions are perpendicular because $A$ is symmetric.

**Interpretation.** Along the $45^\circ$ direction the membrane is stretched by a factor of 8, and along the $135^\circ$ direction by a factor of 2. With coordinates $u_1, u_2$ along these principal directions, the boundary circle $x_1^2 + x_2^2 = 1$ becomes the ellipse

$$\frac{u_1^2}{8^2} + \frac{u_2^2}{2^2} = 1$$

> **Answer.** The principal directions are $x_2 = x_1$ (at $45^\circ$, eigenvalue 8, stretch factor 8) and $x_2 = -x_1$ (at $135^\circ$, eigenvalue 2, stretch factor 2). The circle is deformed into an ellipse with semi-axes 8 and 2 along these directions.
