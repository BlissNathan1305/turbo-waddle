# Type 4

## Question 2: Differential Equations and Free Vibration

### (a) Non-homogeneous second-order ODE

::: {custom-style="Question Box"}
**Question 2(a).** An engineering problem is represented by the differential equation below. Give the solution to the problem. *(6 marks)*

$$\frac{d^2y}{dx^2} + 4\frac{dy}{dx} + 4y = x^2 + xe^{2x} + e^{-2x}\sin 2x$$
:::

**Complementary function.**

$$m^2 + 4m + 4 = (m + 2)^2 = 0 \quad\Rightarrow\quad m = -2 \ \text{(repeated)}, \qquad y_c = (A + Bx)e^{-2x}$$

**Particular integral.** $y_p = y_1 + y_2 + y_3$.

*For $x^2$.* Try $y_1 = ax^2 + bx + c$:

$$2a + 4(2ax + b) + 4(ax^2 + bx + c) = 4ax^2 + (8a + 4b)x + (2a + 4b + 4c) = x^2$$

$$a = \tfrac14, \quad b = -2a = -\tfrac12, \quad c = -\tfrac{2a + 4b}{4} = \tfrac38$$

*For $xe^{2x}$.* Put $y_2 = u\,e^{2x}$: $\ y_2'' + 4y_2' + 4y_2 = \left(u'' + 8u' + 16u\right)e^{2x} = xe^{2x}$. Try $u = px + q$: $\ 8p + 16(px + q) = x \Rightarrow p = \tfrac{1}{16}, \ q = -\tfrac{1}{32}$:

$$y_2 = \frac{2x - 1}{32}e^{2x}$$

*For $e^{-2x}\sin 2x$.* Put $y_3 = v\,e^{-2x}$. Because $-2$ is a double root of the auxiliary equation, the operator reduces to $v''$:

$$y_3'' + 4y_3' + 4y_3 = \left(v'' - 4v' + 4v + 4v' - 8v + 4v\right)e^{-2x} = v''e^{-2x} = e^{-2x}\sin 2x$$

So $v'' = \sin 2x$, $v = -\tfrac14\sin 2x$ and $y_3 = -\tfrac14 e^{-2x}\sin 2x$.

> **Answer.** $y = (A + Bx)e^{-2x} + \dfrac{x^2}{4} - \dfrac{x}{2} + \dfrac{3}{8} + \dfrac{2x - 1}{32}e^{2x} - \dfrac{1}{4}e^{-2x}\sin 2x$

### (b) Undamped spring–mass system

::: {custom-style="Question Box"}
**Question 2(b).** A spring with a mass of 2000 g has natural length of one-half a meter. A force of 25.6 N is required to maintain it stretched to a length of 700 mm. If the spring is stretched to a length of 700 mm and then released with initial velocity 0 m/s: (i) What will be the position of the mass at any time, $t$? (ii) What length of travel (in m) would the mass achieve in $t = \pi/24$ seconds? *(6 marks)*
:::

!include spring-undamped

## Question 3: Numerical Differentiation

### (a) Rate of population growth

::: {custom-style="Question Box"}
**Question 3(a).** The table below gives the census population (in millions) of a state for the years 1961 to 2001. Find the rate of growth of the population in the year 2001. *(6 marks)*

| Year ($x$) | 1961 | 1971 | 1981 | 1991 | 2001 |
|---|---|---|---|---|---|
| Population ($y$) | 19.96 | 36.65 | 58.81 | 77.21 | 94.61 |
:::

!include population

### (b) Derivatives from tabulated data

::: {custom-style="Question Box"}
**Question 3(b).** Given the following data points, determine $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$ at $x = 1.1$ and $x = 1.5$. *(6 marks)*

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
|---|---|---|---|---|---|---|---|
| $f(x)$ | 7.989 | 8.403 | 8.781 | 9.129 | 9.451 | 9.750 | 10.031 |
:::

!include numdiff-table
## Question 4: Series Solutions and Bessel's Equation

### (a) Power series solution

::: {custom-style="Question Box"}
**Question 4(a).** Find the power series solution of $4(y'' + y) = 0$. *(6 marks)*
:::

Dividing by the non-zero constant 4 leaves $y'' + y = 0$.

!include power-series

### (b) Bessel's equation

::: {custom-style="Question Box"}
**Question 4(b).** Find the general solution, in terms of Bessel functions, of the equation $\ xy'' + y' + \left(\dfrac{4}{8}\right)y = 0$. *(6 marks)*
:::

!include bessel

## Question 5: Eigenvalues and Eigenvectors

### (a) Eigenvalues and eigenvectors of a 3 × 3 matrix

::: {custom-style="Question Box"}
**Question 5(a).** Find the eigenvalues and eigenvectors of the matrix *(6 marks)*

$$A = \begin{bmatrix} 1 & 1 & -2 \\ -1 & 0 & 1 \\ -2 & 1 & 1 \end{bmatrix}$$
:::

**Characteristic equation.** Expanding $\det(A - \lambda I)$ along the first row,

$$(1 - \lambda)\left[-\lambda(1 - \lambda) - 1\right] - 1\left[-(1 - \lambda) + 2\right] - 2\left[-1 - 2\lambda\right]$$

$$= (1 - \lambda)(\lambda^2 - \lambda - 1) - (1 + \lambda) + 2 + 4\lambda = -\lambda^3 + 2\lambda^2 + 3\lambda = 0$$

$$\lambda(\lambda^2 - 2\lambda - 3) = \lambda(\lambda - 3)(\lambda + 1) = 0 \quad\Rightarrow\quad \lambda = -1, \ 0, \ 3$$

As a check, $-1 + 0 + 3 = 2 = 1 + 0 + 1$, the trace. ✓

**Eigenvectors.**

$\lambda = -1$: $\ \begin{bmatrix} 2 & 1 & -2 \\ -1 & 1 & 1 \\ -2 & 1 & 2 \end{bmatrix}x = 0$. Adding rows 1 and 3 gives $2x_2 = 0$, so $x_2 = 0$ and $x_1 = x_3$: $\ x = (1, 0, 1)^T$.

$\lambda = 0$: $\ \begin{bmatrix} 1 & 1 & -2 \\ -1 & 0 & 1 \\ -2 & 1 & 1 \end{bmatrix}x = 0$. Row 2 gives $x_1 = x_3$; row 1 then gives $x_2 = x_3$: $\ x = (1, 1, 1)^T$.

$\lambda = 3$: $\ \begin{bmatrix} -2 & 1 & -2 \\ -1 & -3 & 1 \\ -2 & 1 & -2 \end{bmatrix}x = 0$. Row 1 gives $x_2 = 2x_1 + 2x_3$; row 2 then gives $-x_1 - 6x_1 - 6x_3 + x_3 = 0$, so $7x_1 = -5x_3$. Taking $x_3 = -7$: $\ x = (5, -4, -7)^T$.

**Check** for $\lambda = 3$: $A(5, -4, -7)^T = (5 - 4 + 14, \ -5 - 7, \ -10 - 4 - 7)^T = (15, -12, -21)^T = 3(5, -4, -7)^T$ ✓

> **Answer.** $\lambda_1 = -1$ with $x_1 = k(1, 0, 1)^T$; $\ \lambda_2 = 0$ with $x_2 = k(1, 1, 1)^T$; $\ \lambda_3 = 3$ with $x_3 = k(5, -4, -7)^T$ ($k \neq 0$).

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

## Question 7: RLC Circuit

::: {custom-style="Question Box"}
**Question 7.** Consider an RLC circuit with a $\tfrac{17}{50}\ \Omega$ resistor, a $\tfrac{1}{100}$ H inductor and a $\tfrac{100}{93}$ F capacitor, driven by the voltage $E(t) = 0.06\sin 3t$ V. (a) Write the differential equation associated with this circuit in terms of the current $I$. *(6 marks)* (b) If the initial charge and initial current on the capacitor are both zero, find the current $I$ and the voltage across the resistor $E_R$ in terms of time $t$. *(6 marks)*
:::

### (a) Differential equation in terms of $I$

Kirchhoff's voltage law, with $q = \int I\,dt$, gives

$$L\frac{dI}{dt} + RI + \frac{1}{C}\int I\,dt = E(t)$$

Differentiating with respect to $t$ removes the integral:

$$L\frac{d^2I}{dt^2} + R\frac{dI}{dt} + \frac{1}{C}I = \frac{dE}{dt}$$

With $L = \tfrac{1}{100}$, $R = \tfrac{17}{50}$, $\tfrac1C = \tfrac{93}{100}$ and $\dfrac{dE}{dt} = 0.18\cos 3t$:

$$\frac{1}{100}\frac{d^2I}{dt^2} + \frac{17}{50}\frac{dI}{dt} + \frac{93}{100}I = 0.18\cos 3t$$

Multiplying by 100:

$$\frac{d^2I}{dt^2} + 34\frac{dI}{dt} + 93I = 18\cos 3t$$

### (b) Current and resistor voltage

**Initial conditions.** $I(0) = 0$. At $t = 0$ the circuit equation gives $L I'(0) = E(0) - RI(0) - q(0)/C = 0 - 0 - 0$, so $I'(0) = 0$.

**Complementary function.** $r^2 + 34r + 93 = 0$ gives $r = \dfrac{-34 \pm \sqrt{1156 - 372}}{2} = \dfrac{-34 \pm 28}{2}$, so $r = -3$ or $r = -31$:

$$I_c = c_1e^{-3t} + c_2e^{-31t}$$

**Particular integral.** Try $I_p = A\cos 3t + B\sin 3t$, with $I_p'' = -9I_p$:

$$(93 - 9)(A\cos 3t + B\sin 3t) + 34(-3A\sin 3t + 3B\cos 3t) = 18\cos 3t$$

$$\cos 3t: \ 84A + 102B = 18, \qquad \sin 3t: \ 84B - 102A = 0$$

The second gives $B = \tfrac{17}{14}A$. Substituting, $84A + \tfrac{1734}{14}A = 18$, so $\tfrac{2910}{14}A = 18$, giving $A = \tfrac{42}{485}$ and $B = \tfrac{51}{485}$.

**Constants.**

$$I(0) = c_1 + c_2 + \frac{42}{485} = 0, \qquad I'(0) = -3c_1 - 31c_2 + \frac{153}{485} = 0$$

Solving: $c_1 = -\tfrac{3}{28}$ and $c_2 = \tfrac{279}{13580}$.

**Current.**

$$I(t) = -\frac{3}{28}e^{-3t} + \frac{279}{13580}e^{-31t} + \frac{42\cos 3t + 51\sin 3t}{485}$$

$$I(t) \approx -0.1071e^{-3t} + 0.0205e^{-31t} + 0.0866\cos 3t + 0.1052\sin 3t \ \text{A}$$

**Voltage across the resistor.** $E_R = RI = \tfrac{17}{50}I$:

$$E_R(t) = -\frac{51}{1400}e^{-3t} + \frac{4743}{679000}e^{-31t} + \frac{357}{12125}\cos 3t + \frac{867}{24250}\sin 3t$$

$$E_R(t) \approx -0.0364e^{-3t} + 0.0070e^{-31t} + 0.0294\cos 3t + 0.0358\sin 3t \ \text{V}$$

> **Answer.** (a) $I'' + 34I' + 93I = 18\cos 3t$. (b) $I = -\tfrac{3}{28}e^{-3t} + \tfrac{279}{13580}e^{-31t} + \tfrac{1}{485}(42\cos 3t + 51\sin 3t)$ A, and $E_R = \tfrac{17}{50}I \approx -0.0364e^{-3t} + 0.0070e^{-31t} + 0.0294\cos 3t + 0.0358\sin 3t$ V.
