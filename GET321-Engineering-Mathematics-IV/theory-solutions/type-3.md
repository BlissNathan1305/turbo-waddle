# Type 3

## Question 2: Numerical Differentiation

### (a) Rate of population growth

::: {custom-style="Question Box"}
**Question 2(a).** The table below gives the census population (in millions) of a state for the years 1961 to 2001. Find the rate of growth of the population in the year 2001. *(6 marks)*

| Year ($x$) | 1961 | 1971 | 1981 | 1991 | 2001 |
|---|---|---|---|---|---|
| Population ($y$) | 19.96 | 36.65 | 58.81 | 77.21 | 94.61 |
:::

!include population

### (b) Derivatives from tabulated data

::: {custom-style="Question Box"}
**Question 2(b).** Given a polynomial with the following data points, determine $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$ at $x = 1.1$ and $x = 1.5$. *(6 marks)*

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
|---|---|---|---|---|---|---|---|
| $f(x)$ | 7.991 | 8.403 | 8.781 | 9.129 | 9.451 | 9.750 | 10.631 |
:::

!include numdiff-table
## Question 3: RLC Circuit

::: {custom-style="Question Box"}
**Question 3.** Consider a series RLC circuit consisting of a 20 Ω resistor, a 1 H inductor and a 2000 μF capacitor. The circuit starts with zero initial charge and zero initial current. (a) Determine the expression for the charge on the capacitor at time $t$ (i) when the circuit is connected to a constant 12 V DC source, and (ii) when the circuit is driven by an AC source with voltage $E(t) = 12\sin 10t$. *(6 marks)* (b) For each case in part (a), also find the corresponding current in the circuit as a function of time. *(6 marks)*
:::

!include circuit-20ohm

## Question 4: Series Solutions and Bessel's Equation

### (a) Power series solution

::: {custom-style="Question Box"}
**Question 4(a).** Find the power series solution of $3(y'' + y) = 0$. *(6 marks)*
:::

Dividing by the non-zero constant 3 leaves $y'' + y = 0$.

!include power-series

### (b) Bessel's equation

::: {custom-style="Question Box"}
**Question 4(b).** Find the general solutions in terms of $J_\nu(x)$ and $J_{-\nu}(x)$ of the following Bessel function equation: $\ xy'' + y' + \left(\dfrac{3}{6}\right)y = 0$. *(6 marks)*
:::

!include bessel

## Question 5: Legendre's Equation and the Wave Equation

### (a) Legendre's equation

::: {custom-style="Question Box"}
**Question 5(a).** Solve this special Legendre equation, $(1 - x^2)y'' - 2xy' + 2y = 0$, which occurs in models exhibiting spherical symmetry. *(6 marks)*
:::

!include legendre

### (b) One-dimensional wave equation

::: {custom-style="Question Box"}
**Question 5(b).** Find the solution to this one-dimensional wave equation: $\ \dfrac{\partial^2 u}{\partial x^2} = \dfrac{1}{16}\dfrac{\partial^2 u}{\partial t^2}$ for $0 < x < 2$, $t > 0$. The boundary conditions are $u(0,t) = u(2,t) = 0$. The initial conditions are (i) $u(x,0) = 6\sin\pi x - 3\sin 4\pi x$ and (ii) $\dfrac{\partial u}{\partial t}(x,0) = 0$. *(6 marks)*
:::

!include wave

## Question 6: Eigenvalues and Eigenvectors

### (a) Eigenvalues and eigenvectors of a 3 × 3 matrix

::: {custom-style="Question Box"}
**Question 6(a).** Find the eigenvalues and eigenvectors of the matrix *(6 marks)*

$$A = \begin{bmatrix} 8 & -6 & 2 \\ -6 & 7 & -4 \\ 2 & -4 & 3 \end{bmatrix}$$
:::

**Characteristic equation.** Expanding $\det(A - \lambda I)$ along the first row,

$$(8 - \lambda)\left[(7 - \lambda)(3 - \lambda) - 16\right] + 6\left[-6(3 - \lambda) + 8\right] + 2\left[24 - 2(7 - \lambda)\right] = 0$$

$$(8 - \lambda)(\lambda^2 - 10\lambda + 5) + 6(6\lambda - 10) + 2(2\lambda + 10) = -\lambda^3 + 18\lambda^2 - 45\lambda = 0$$

$$\lambda(\lambda^2 - 18\lambda + 45) = \lambda(\lambda - 3)(\lambda - 15) = 0 \quad\Rightarrow\quad \lambda = 0, \ 3, \ 15$$

As a check, the eigenvalues add up to the trace: $0 + 3 + 15 = 8 + 7 + 3 = 18$. ✓

**Eigenvectors.**

$\lambda = 0$: $\ \begin{bmatrix} 8 & -6 & 2 \\ -6 & 7 & -4 \\ 2 & -4 & 3 \end{bmatrix}x = 0$. The cross product of the first two rows, $(8, -6, 2)\times(-6, 7, -4) = (10, 20, 20)$, gives $x = (1, 2, 2)^T$.

$\lambda = 3$: $\ \begin{bmatrix} 5 & -6 & 2 \\ -6 & 4 & -4 \\ 2 & -4 & 0 \end{bmatrix}x = 0$. The third row gives $x_1 = 2x_2$; then the first gives $10x_2 - 6x_2 + 2x_3 = 0$, so $x_3 = -2x_2$ and $x = (2, 1, -2)^T$.

$\lambda = 15$: $\ \begin{bmatrix} -7 & -6 & 2 \\ -6 & -8 & -4 \\ 2 & -4 & -12 \end{bmatrix}x = 0$. The cross product of the first two rows, $(-7, -6, 2)\times(-6, -8, -4) = (40, -40, 20)$, gives $x = (2, -2, 1)^T$.

**Check** for $\lambda = 15$: $A(2, -2, 1)^T = (16 + 12 + 2, \ -12 - 14 - 4, \ 4 + 8 + 3)^T = (30, -30, 15)^T = 15(2, -2, 1)^T$ ✓. The matrix is symmetric, so the eigenvectors are mutually orthogonal.

> **Answer.** $\lambda_1 = 0$ with $x_1 = k(1, 2, 2)^T$; $\ \lambda_2 = 3$ with $x_2 = k(2, 1, -2)^T$; $\ \lambda_3 = 15$ with $x_3 = k(2, -2, 1)^T$ ($k \neq 0$).

### (b) Principal directions of a stretched membrane

::: {custom-style="Question Box"}
**Question 6(b).** An elastic membrane in the $x_1x_2$-plane with boundary circle $x_1^2 + x_2^2 = 1$ is stretched so that a point $P: (x_1, x_2)$ goes over into the point $Q: (y_1, y_2)$ given by

$$y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = Ax = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

Find the principal directions, that is, the directions of the position vector $x$ of $P$ for which the direction of the position vector $y$ of $Q$ is the same or exactly opposite. *(7 marks)*
:::

!include membrane

## Question 7: Differential Equations and Free Vibration

### (a) Non-homogeneous second-order ODE

::: {custom-style="Question Box"}
**Question 7(a).** Find the solution to the engineering problem represented by the differential equation below.

$$\frac{d^2y}{dx^2} + 2\frac{dy}{dx} + 5y = x^2 + xe^{2x} + e^{-x}\sin 2x$$
:::

**Complementary function.**

$$m^2 + 2m + 5 = 0 \quad\Rightarrow\quad m = -1 \pm 2i, \qquad y_c = e^{-x}\left(A\cos 2x + B\sin 2x\right)$$

**Particular integral.** $y_p = y_1 + y_2 + y_3$.

*For $x^2$.* Try $y_1 = ax^2 + bx + c$:

$$2a + 2(2ax + b) + 5(ax^2 + bx + c) = 5ax^2 + (4a + 5b)x + (2a + 2b + 5c) = x^2$$

$$a = \tfrac15, \quad b = -\tfrac{4a}{5} = -\tfrac{4}{25}, \quad c = -\tfrac{2a + 2b}{5} = -\tfrac{2}{125}$$

*For $xe^{2x}$.* Put $y_2 = u\,e^{2x}$: $\ y_2'' + 2y_2' + 5y_2 = \left(u'' + 6u' + 13u\right)e^{2x} = xe^{2x}$. Try $u = px + q$: $\ 6p + 13(px + q) = x \Rightarrow p = \tfrac{1}{13}, \ q = -\tfrac{6}{169}$:

$$y_2 = \frac{13x - 6}{169}e^{2x}$$

*For $e^{-x}\sin 2x$.* This term has the same form as $y_c$ (since $-1 \pm 2i$ are the roots), so an extra factor of $x$ is needed. Put $y_3 = v\,e^{-x}$; then $y_3' = (v' - v)e^{-x}$, $y_3'' = (v'' - 2v' + v)e^{-x}$ and

$$y_3'' + 2y_3' + 5y_3 = \left(v'' - 2v' + v + 2v' - 2v + 5v\right)e^{-x} = \left(v'' + 4v\right)e^{-x} = e^{-x}\sin 2x$$

Try $v = x(C\cos 2x + D\sin 2x)$. Then $v'' + 4v = 2\dfrac{d}{dx}(C\cos 2x + D\sin 2x) = -4C\sin 2x + 4D\cos 2x = \sin 2x$, so $C = -\tfrac14$, $D = 0$:

$$y_3 = -\frac{x}{4}e^{-x}\cos 2x$$

> **Answer.** $y = e^{-x}\left(A\cos 2x + B\sin 2x\right) + \dfrac{x^2}{5} - \dfrac{4x}{25} - \dfrac{2}{125} + \dfrac{13x - 6}{169}e^{2x} - \dfrac{x}{4}e^{-x}\cos 2x$

### (b) Undamped spring–mass system

::: {custom-style="Question Box"}
**Question 7(b).** A spring with a mass of 2000 g has natural length of one-half a meter. A force of 25.6 N is required to maintain it stretched to a length of 700 mm. If the spring is stretched to a length of 700 mm and then released with initial velocity 0 m/s: (i) What will be the position of the mass at any time, $t$? (ii) What length of travel (in m) would the mass achieve in $t = \pi/24$ seconds?
:::

!include spring-undamped
