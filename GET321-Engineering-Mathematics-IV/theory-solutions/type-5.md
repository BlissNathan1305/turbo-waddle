# Type 5

## Question 2: Differential Equations and Free Vibration

### (a) Non-homogeneous second-order ODE

::: {custom-style="Question Box"}
**Question 2(a).** Find the solution to the engineering problem represented by the differential equation below. *(6 marks)*

$$\frac{d^2y}{dx^2} + 2\frac{dy}{dx} + 5y = x^2 + xe^{2x} + e^{-x}\cos 2x$$
:::

**Complementary function.**

$$m^2 + 2m + 5 = 0 \quad\Rightarrow\quad m = -1 \pm 2i, \qquad y_c = e^{-x}\left(A\cos 2x + B\sin 2x\right)$$

**Particular integral.** $y_p = y_1 + y_2 + y_3$.

*For $x^2$.* Try $y_1 = ax^2 + bx + c$:

$$5ax^2 + (4a + 5b)x + (2a + 2b + 5c) = x^2 \quad\Rightarrow\quad a = \tfrac15, \quad b = -\tfrac{4}{25}, \quad c = -\tfrac{2}{125}$$

*For $xe^{2x}$.* Put $y_2 = u\,e^{2x}$: $\ \left(u'' + 6u' + 13u\right)e^{2x} = xe^{2x}$. Try $u = px + q$: $\ 6p + 13(px + q) = x \Rightarrow p = \tfrac{1}{13}, \ q = -\tfrac{6}{169}$:

$$y_2 = \frac{13x - 6}{169}e^{2x}$$

*For $e^{-x}\cos 2x$.* This term has the same form as $y_c$, so an extra factor of $x$ is needed. Put $y_3 = v\,e^{-x}$; then

$$y_3'' + 2y_3' + 5y_3 = \left(v'' - 2v' + v + 2v' - 2v + 5v\right)e^{-x} = \left(v'' + 4v\right)e^{-x} = e^{-x}\cos 2x$$

Try $v = x(C\cos 2x + D\sin 2x)$. Then $v'' + 4v = 2\dfrac{d}{dx}(C\cos 2x + D\sin 2x) = -4C\sin 2x + 4D\cos 2x = \cos 2x$, so $C = 0$, $D = \tfrac14$:

$$y_3 = \frac{x}{4}e^{-x}\sin 2x$$

> **Answer.** $y = e^{-x}\left(A\cos 2x + B\sin 2x\right) + \dfrac{x^2}{5} - \dfrac{4x}{25} - \dfrac{2}{125} + \dfrac{13x - 6}{169}e^{2x} + \dfrac{x}{4}e^{-x}\sin 2x$

### (b) Undamped spring–mass system

::: {custom-style="Question Box"}
**Question 2(b).** A spring with a mass of 2000 g has natural length of one-half a meter. A force of 25.6 N is required to maintain it stretched to a length of 700 mm. If the spring is stretched to a length of 700 mm and then released with initial velocity 0 m/s: (i) What will be the position of the mass at any time, $t$? (ii) What length of travel (in m) would the mass achieve in $t = \pi/24$ seconds? *(6 marks)*
:::

!include spring-undamped

## Question 3: RLC Circuit

::: {custom-style="Question Box"}
**Question 3.** A series RLC circuit consists of a 5 Ω resistor, a 0.1 H inductor and a 1000 μF capacitor. The circuit starts with zero charge on the capacitor and zero current through the inductor. (a) Find the charge on the capacitor as a function of time (i) when the circuit is connected to a 6 V DC source, and (ii) when the circuit is driven by an AC source given by $E(t) = 6\sin 2t$. *(6 marks)* (b) For each case in part (a), determine the corresponding current in the circuit. *(6 marks)*
:::

**The circuit equation.** With $C = 1000\ \mu\text{F} = 10^{-3}$ F, so $1/C = 1000$:

$$0.1\frac{d^2q}{dt^2} + 5\frac{dq}{dt} + 1000q = E(t) \quad\Rightarrow\quad \frac{d^2q}{dt^2} + 50\frac{dq}{dt} + 10000q = 10E(t)$$

with $q(0) = 0$ and $q'(0) = I(0) = 0$.

**Complementary function.** $r^2 + 50r + 10000 = 0$ gives

$$r = -25 \pm \sqrt{625 - 10000} = -25 \pm i\sqrt{9375} = -25 \pm 25\sqrt{15}\,i$$

Write $\omega = 25\sqrt{15} \approx 96.82$ rad/s. Then

$$q_c = e^{-25t}\left(c_1\cos\omega t + c_2\sin\omega t\right)$$

### Case (i): 6 V DC source

**Particular integral.** $10000q_p = 60$, so $q_p = 0.006$.

**Constants.** $q(0) = c_1 + 0.006 = 0 \Rightarrow c_1 = -0.006$. $\ q'(0) = -25c_1 + \omega c_2 = 0 \Rightarrow c_2 = \dfrac{25c_1}{\omega} = -\dfrac{0.006}{\sqrt{15}} = -\dfrac{\sqrt{15}}{2500} \approx -0.001549$.

$$q(t) = 0.006\left[1 - e^{-25t}\left(\cos\omega t + \frac{1}{\sqrt{15}}\sin\omega t\right)\right]$$

**Current.** Differentiating (the cosine terms cancel),

$$I(t) = 0.006\left(\omega + \frac{625}{\omega}\right)e^{-25t}\sin\omega t = \frac{60}{\omega}e^{-25t}\sin\omega t = \frac{4\sqrt{15}}{25}e^{-25t}\sin\omega t \approx 0.6197\,e^{-25t}\sin(96.82t)$$

### Case (ii): AC source, $E = 6\sin 2t$

The right-hand side is $10E = 60\sin 2t$.

**Particular integral.** Try $q_p = A\cos 2t + B\sin 2t$, with $q_p'' = -4q_p$:

$$\cos 2t: \ 9996A + 100B = 0, \qquad \sin 2t: \ 9996B - 100A = 60$$

Solving,

$$B = \frac{60 \times 9996}{9996^2 + 100^2} = \frac{37485}{6245626} \approx 6.0018\times 10^{-3}, \qquad A = -\frac{100B}{9996} = -\frac{375}{6245626} \approx -6.004\times 10^{-5}$$

**Constants.** $q(0) = c_1 + A = 0 \Rightarrow c_1 = 6.004\times 10^{-5}$. $\ q'(0) = -25c_1 + \omega c_2 + 2B = 0 \Rightarrow c_2 = \dfrac{25c_1 - 2B}{\omega} \approx -1.0847\times 10^{-4}$.

$$q(t) \approx e^{-25t}\left(6.004\times 10^{-5}\cos\omega t - 1.0847\times 10^{-4}\sin\omega t\right) + 6.0018\times 10^{-3}\sin 2t - 6.004\times 10^{-5}\cos 2t$$

**Current.**

$$I(t) \approx -e^{-25t}\left(0.012004\cos\omega t + 0.003102\sin\omega t\right) + 0.012004\cos 2t + 0.000120\sin 2t$$

Check: $I(0) = -0.012004 + 0.012004 = 0$. ✓ The transient dies away within about 0.2 s (since $e^{-25t}$ is then below 1 %), leaving the steady-state current $\approx 0.0120\cos 2t$ A.

> **Answer.**
> (i) $q = 0.006\left[1 - e^{-25t}\left(\cos 25\sqrt{15}\,t + \tfrac{1}{\sqrt{15}}\sin 25\sqrt{15}\,t\right)\right]$ C and $I = \tfrac{4\sqrt{15}}{25}e^{-25t}\sin 25\sqrt{15}\,t \approx 0.620\,e^{-25t}\sin 96.82t$ A.
> (ii) $q \approx e^{-25t}\left(6.00\times 10^{-5}\cos 96.82t - 1.08\times 10^{-4}\sin 96.82t\right) + 6.00\times 10^{-3}\sin 2t - 6.00\times 10^{-5}\cos 2t$ C and $I \approx -e^{-25t}\left(0.0120\cos 96.82t + 0.0031\sin 96.82t\right) + 0.0120\cos 2t + 0.00012\sin 2t$ A.

## Question 4: Numerical Differentiation

### (a) Rate of population growth

::: {custom-style="Question Box"}
**Question 4(a).** The table below gives the census population (in millions) of a state for the years 1961 to 2001. Find the rate of growth of the population in the year 2001. *(6 marks)*

| Year ($x$) | 1961 | 1971 | 1981 | 1991 | 2001 |
|---|---|---|---|---|---|
| Population ($y$) | 19.96 | 36.65 | 58.81 | 77.21 | 94.61 |
:::

!include population

### (b) Derivatives from tabulated data

::: {custom-style="Question Box"}
**Question 4(b).** Given a polynomial with the following data points, determine $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$ at $x = 1.1$ and $x = 1.5$. *(6 marks)*

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
|---|---|---|---|---|---|---|---|
| $f(x)$ | 7.991 | 8.403 | 8.781 | 9.129 | 9.451 | 9.750 | 10.631 |
:::

!include numdiff-table
## Question 5: Eigenvalues and Eigenvectors

### (a) Eigenvalues and eigenvectors of a 3 × 3 matrix

::: {custom-style="Question Box"}
**Question 5(a).** Find the eigenvalues and eigenvectors of the matrix *(6 marks)*

$$A = \begin{bmatrix} 4 & -4 & 3 \\ 0 & -1 & 9 \\ 0 & 0 & 1 \end{bmatrix}$$
:::

**Eigenvalues.** $A$ is upper triangular, so

$$\det(A - \lambda I) = (4 - \lambda)(-1 - \lambda)(1 - \lambda) = 0 \quad\Rightarrow\quad \lambda = 4, \ -1, \ 1$$

(Expanded: $\lambda^3 - 4\lambda^2 - \lambda + 4 = 0$.)

**Eigenvectors.**

$\lambda = 4$: $\ \begin{bmatrix} 0 & -4 & 3 \\ 0 & -5 & 9 \\ 0 & 0 & -3 \end{bmatrix}x = 0 \ \Rightarrow\ x_3 = 0, \ x_2 = 0, \ x_1 \text{ free} \ \Rightarrow\ x = (1, 0, 0)^T$

$\lambda = -1$: $\ \begin{bmatrix} 5 & -4 & 3 \\ 0 & 0 & 9 \\ 0 & 0 & 2 \end{bmatrix}x = 0 \ \Rightarrow\ x_3 = 0, \ 5x_1 = 4x_2 \ \Rightarrow\ x = (4, 5, 0)^T$

$\lambda = 1$: $\ \begin{bmatrix} 3 & -4 & 3 \\ 0 & -2 & 9 \\ 0 & 0 & 0 \end{bmatrix}x = 0 \ \Rightarrow\ x_2 = \tfrac92 x_3, \ 3x_1 = 4x_2 - 3x_3 = 15x_3 \Rightarrow x_1 = 5x_3$. Taking $x_3 = 2$: $\ x = (10, 9, 2)^T$

**Check** for $\lambda = 1$: $A(10, 9, 2)^T = (40 - 36 + 6, \ -9 + 18, \ 2)^T = (10, 9, 2)^T$ ✓

> **Answer.** $\lambda_1 = 4$ with $x_1 = k(1, 0, 0)^T$; $\ \lambda_2 = -1$ with $x_2 = k(4, 5, 0)^T$; $\ \lambda_3 = 1$ with $x_3 = k(10, 9, 2)^T$ ($k \neq 0$).

### (b) Principal directions of a stretched membrane

::: {custom-style="Question Box"}
**Question 5(b).** An elastic membrane in the $x_1x_2$-plane with boundary circle $x_1^2 + x_2^2 = 1$ is stretched so that a point $P: (x_1, x_2)$ goes over into the point $Q: (y_1, y_2)$ given by

$$y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = Ax = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

Find the principal directions, that is, the directions of the position vector $x$ of $P$ for which the direction of the position vector $y$ of $Q$ is the same or exactly opposite. *(6 marks)*
:::

!include membrane

## Question 6: Series Solutions and Bessel's Equation

### (a) Power series solution

::: {custom-style="Question Box"}
**Question 6(a).** Find the power series solution of $5(y'' + y) = 0$. *(6 marks)*
:::

Dividing by the non-zero constant 5 leaves $y'' + y = 0$.

!include power-series

### (b) Bessel's equation

::: {custom-style="Question Box"}
**Question 6(b).** Find the general solutions in terms of $J_\nu(x)$ and $J_{-\nu}(x)$ of the following Bessel function equation: $\ xy'' + y' + \left(\dfrac{5}{10}\right)y = 0$. *(6 marks)*
:::

!include bessel

## Question 7: Legendre's Equation and the Wave Equation

### (a) Legendre's equation

::: {custom-style="Question Box"}
**Question 7(a).** Solve this special Legendre equation, $(1 - x^2)y'' - 2xy' + 2y = 0$, which occurs in models exhibiting spherical symmetry. *(6 marks)*
:::

!include legendre

### (b) One-dimensional wave equation

::: {custom-style="Question Box"}
**Question 7(b).** Find the solution to this one-dimensional wave equation: $\ \dfrac{\partial^2 u}{\partial x^2} = \dfrac{1}{16}\dfrac{\partial^2 u}{\partial t^2}$ for $0 < x < 2$, $t > 0$. The boundary conditions are $u(0,t) = u(2,t) = 0$. The initial conditions are (i) $u(x,0) = 6\sin\pi x - 3\sin 4\pi x$ and (ii) $\dfrac{\partial u}{\partial t}(x,0) = 0$. *(6 marks)*
:::

!include wave
