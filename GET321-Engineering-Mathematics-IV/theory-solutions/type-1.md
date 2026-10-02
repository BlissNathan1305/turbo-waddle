# Type 1

## Question 2: Differential Equations and Free Vibration

### (a) Non-homogeneous second-order ODE

::: {custom-style="Question Box"}
**Question 2(a).** Find the solution to the engineering problem represented by the differential equation below. *(6 marks)*

$$\frac{d^2y}{dx^2} - 4\frac{dy}{dx} + 4y = x^2 + x^3e^{2x} + \sin 2x$$
:::

**Complementary function.** The auxiliary equation is

$$m^2 - 4m + 4 = (m - 2)^2 = 0 \quad\Rightarrow\quad m = 2 \ \text{(repeated)}$$

$$y_c = (A + Bx)e^{2x}$$

**Particular integral.** Treat each term on the right separately: $y_p = y_1 + y_2 + y_3$.

*For $x^2$.* Try $y_1 = ax^2 + bx + c$, so $y_1' = 2ax + b$ and $y_1'' = 2a$:

$$2a - 4(2ax + b) + 4(ax^2 + bx + c) = 4ax^2 + (4b - 8a)x + (2a - 4b + 4c) = x^2$$

$$4a = 1, \quad 4b - 8a = 0, \quad 2a - 4b + 4c = 0 \quad\Rightarrow\quad a = \tfrac14, \ b = \tfrac12, \ c = \tfrac38$$

*For $x^3e^{2x}$.* Here $e^{2x}$ is part of $y_c$ (twice over), so put $y_2 = u(x)e^{2x}$. Then $y_2' = (u' + 2u)e^{2x}$, $y_2'' = (u'' + 4u' + 4u)e^{2x}$ and

$$y_2'' - 4y_2' + 4y_2 = \left[u'' + 4u' + 4u - 4u' - 8u + 4u\right]e^{2x} = u''e^{2x}$$

So $u'' = x^3$, giving $u = \dfrac{x^5}{20}$ and $y_2 = \dfrac{x^5}{20}e^{2x}$.

*For $\sin 2x$.* Try $y_3 = C\cos 2x + D\sin 2x$, so $y_3'' = -4y_3$:

$$-4y_3 - 4y_3' + 4y_3 = -4(-2C\sin 2x + 2D\cos 2x) = 8C\sin 2x - 8D\cos 2x = \sin 2x$$

so $C = \tfrac18$, $D = 0$ and $y_3 = \tfrac18\cos 2x$.

> **Answer.** $y = (A + Bx)e^{2x} + \dfrac{x^5}{20}e^{2x} + \dfrac{x^2}{4} + \dfrac{x}{2} + \dfrac{3}{8} + \dfrac{1}{8}\cos 2x$

### (b) Undamped spring–mass system

::: {custom-style="Question Box"}
**Question 2(b).** A spring with a mass of 2000 g has natural length of one-half a meter. A force of 25.6 N is required to maintain it stretched to a length of 700 mm. If the spring is stretched to a length of 700 mm and then released with initial velocity 0 m/s: (i) What will be the position of the mass at any time, $t$? (ii) What length of travel (in m) would the mass achieve in $t = \pi/24$ seconds? *(6 marks)*
:::

!include spring-undamped

## Question 3: RLC Circuit

::: {custom-style="Question Box"}
**Question 3.** A series circuit comprises a resistor of value 20 Ω with a 1 H inductor and a capacitor whose capacitance is 2000 μF. If the initial charge and current are both zero, find the charge at time $t$ in these two cases: (i) the circuit is connected to a 12-volt battery; (ii) the circuit is connected to a generator producing a voltage of $E(t) = 12\sin 10t$. *(6 marks)* Find also the current in each case in (i) and (ii). *(6 marks)*
:::

!include circuit-20ohm

## Question 4: Series Solutions and Bessel's Equation

### (a) Power series solution

::: {custom-style="Question Box"}
**Question 4(a).** Find the power series solution of $y'' + y = 0$. *(6 marks)*
:::

!include power-series

### (b) Bessel's equation

::: {custom-style="Question Box"}
**Question 4(b).** Find the general solution, in terms of Bessel functions, of the equation $\ xy'' + y' + \left(\dfrac{1}{2}\right)y = 0$. *(6 marks)*
:::

!include bessel

## Question 5: Eigenvalues and Eigenvectors

### (a) Eigenvalues and eigenvectors of a 3 × 3 matrix

::: {custom-style="Question Box"}
**Question 5(a).** Find the eigenvalues and eigenvectors of the matrix *(6 marks)*

$$A = \begin{bmatrix} 3 & 1 & 4 \\ 0 & 2 & 6 \\ 0 & 0 & 5 \end{bmatrix}$$
:::

**Eigenvalues.** $A$ is upper triangular, so $\det(A - \lambda I)$ is the product of the diagonal entries:

$$\det(A - \lambda I) = (3 - \lambda)(2 - \lambda)(5 - \lambda) = 0 \quad\Rightarrow\quad \lambda = 2, \ 3, \ 5$$

(Expanded, the characteristic equation is $\lambda^3 - 10\lambda^2 + 31\lambda - 30 = 0$.)

**Eigenvectors.** Solve $(A - \lambda I)x = 0$ for each eigenvalue.

$\lambda = 2$: $\ \begin{bmatrix} 1 & 1 & 4 \\ 0 & 0 & 6 \\ 0 & 0 & 3 \end{bmatrix}x = 0 \ \Rightarrow\ x_3 = 0, \ x_1 + x_2 = 0 \ \Rightarrow\ x = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$

$\lambda = 3$: $\ \begin{bmatrix} 0 & 1 & 4 \\ 0 & -1 & 6 \\ 0 & 0 & 2 \end{bmatrix}x = 0 \ \Rightarrow\ x_3 = 0, \ x_2 = 0, \ x_1 \text{ free} \ \Rightarrow\ x = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$

$\lambda = 5$: $\ \begin{bmatrix} -2 & 1 & 4 \\ 0 & -3 & 6 \\ 0 & 0 & 0 \end{bmatrix}x = 0 \ \Rightarrow\ x_2 = 2x_3, \ -2x_1 + 2x_3 + 4x_3 = 0 \Rightarrow x_1 = 3x_3 \ \Rightarrow\ x = \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix}$

**Check** for $\lambda = 5$: $A\begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 9 + 2 + 4 \\ 4 + 6 \\ 5 \end{bmatrix} = \begin{bmatrix} 15 \\ 10 \\ 5 \end{bmatrix} = 5\begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix}$ ✓

> **Answer.** $\lambda_1 = 2$ with $x_1 = k(1, -1, 0)^T$; $\ \lambda_2 = 3$ with $x_2 = k(1, 0, 0)^T$; $\ \lambda_3 = 5$ with $x_3 = k(3, 2, 1)^T$ ($k \neq 0$).

### (b) Principal directions of a stretched membrane

::: {custom-style="Question Box"}
**Question 5(b).** An elastic membrane in the $x_1x_2$-plane with boundary circle $x_1^2 + x_2^2 = 1$ is stretched so that a point $P: (x_1, x_2)$ goes over into the point $Q: (y_1, y_2)$ given by

$$y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = Ax = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

Find the principal directions, that is, the directions of the position vector $x$ of $P$ for which the direction of the position vector $y$ of $Q$ is the same or exactly opposite. *(6 marks)*
:::

!include membrane

## Question 6: Legendre's Equation and the Wave Equation

### (a) Legendre's equation

::: {custom-style="Question Box"}
**Question 6(a).** Solve this special Legendre equation, $(1 - x^2)y'' - 2xy' + 2y = 0$, which occurs in models exhibiting spherical symmetry. *(6 marks)*
:::

!include legendre

### (b) One-dimensional wave equation

::: {custom-style="Question Box"}
**Question 6(b).** Find the solution to this one-dimensional wave equation: $\ \dfrac{\partial^2 u}{\partial x^2} = \dfrac{1}{16}\dfrac{\partial^2 u}{\partial t^2}$ for $0 < x < 2$, $t > 0$. The boundary conditions are $u(0,t) = u(2,t) = 0$. The initial conditions are (i) $u(x,0) = 6\sin\pi x - 3\sin 4\pi x$ and (ii) $\dfrac{\partial u}{\partial t}(x,0) = 0$. *(6 marks)*
:::

!include wave

## Question 7: Numerical Differentiation

### (a) Rate of population growth

::: {custom-style="Question Box"}
**Question 7(a).** The table below gives the census population (in millions) of a state for the years 1961 to 2001. Find the rate of growth of the population in the year 2001. *(6 marks)*

| Year ($x$) | 1961 | 1971 | 1981 | 1991 | 2001 |
|---|---|---|---|---|---|
| Population ($y$) | 19.96 | 36.65 | 58.81 | 77.21 | 94.61 |
:::

!include population

### (b) Derivatives from tabulated data

::: {custom-style="Question Box"}
**Question 7(b).** Given the following data points, determine $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$ at $x = 1.1$ and $x = 1.5$. *(6 marks)*

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
|---|---|---|---|---|---|---|---|
| $f(x)$ | 7.989 | 8.403 | 8.781 | 9.129 | 9.451 | 9.750 | 10.031 |
:::

!include numdiff-table
