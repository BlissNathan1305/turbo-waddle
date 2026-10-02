# Type 2

## Question 2: Differential Equations and Damped Vibration

### (a) Non-homogeneous second-order ODE

::: {custom-style="Question Box"}
**Question 2(a).** An engineering problem is represented by the differential equation below. Give the solution to the problem. *(6 marks)*

$$\frac{d^2y}{dx^2} + \frac{dy}{dx} + y = x^2 + xe^{2x} + e^{x}\cos 2x$$
:::

**Complementary function.** The auxiliary equation is

$$m^2 + m + 1 = 0 \quad\Rightarrow\quad m = \frac{-1 \pm \sqrt{1 - 4}}{2} = -\frac12 \pm \frac{\sqrt3}{2}i$$

$$y_c = e^{-x/2}\left(A\cos\frac{\sqrt3}{2}x + B\sin\frac{\sqrt3}{2}x\right)$$

**Particular integral.** $y_p = y_1 + y_2 + y_3$, one part for each term on the right. None of the terms appears in $y_c$.

*For $x^2$.* Try $y_1 = ax^2 + bx + c$:

$$2a + (2ax + b) + (ax^2 + bx + c) = ax^2 + (2a + b)x + (2a + b + c) = x^2$$

$$a = 1, \quad 2a + b = 0 \Rightarrow b = -2, \quad 2a + b + c = 0 \Rightarrow c = 0 \quad\Rightarrow\quad y_1 = x^2 - 2x$$

*For $xe^{2x}$.* Put $y_2 = u\,e^{2x}$. Then $y_2' = (u' + 2u)e^{2x}$, $y_2'' = (u'' + 4u' + 4u)e^{2x}$ and

$$y_2'' + y_2' + y_2 = \left(u'' + 5u' + 7u\right)e^{2x} = xe^{2x}$$

Try $u = px + q$: $\ 5p + 7(px + q) = x \Rightarrow p = \tfrac17, \ q = -\tfrac{5}{49}$, so

$$y_2 = \frac{7x - 5}{49}e^{2x}$$

*For $e^{x}\cos 2x$.* Put $y_3 = v\,e^{x}$. Then $y_3' = (v' + v)e^x$, $y_3'' = (v'' + 2v' + v)e^x$ and

$$y_3'' + y_3' + y_3 = \left(v'' + 3v' + 3v\right)e^x = e^x\cos 2x$$

Try $v = C\cos 2x + D\sin 2x$, with $v'' = -4v$:

$$(-C + 6D)\cos 2x + (-D - 6C)\sin 2x = \cos 2x \quad\Rightarrow\quad -C + 6D = 1, \quad D = -6C$$

so $-37C = 1$, $C = -\tfrac{1}{37}$, $D = \tfrac{6}{37}$, and

$$y_3 = \frac{e^x}{37}\left(6\sin 2x - \cos 2x\right)$$

> **Answer.** $y = e^{-x/2}\left(A\cos\dfrac{\sqrt3}{2}x + B\sin\dfrac{\sqrt3}{2}x\right) + x^2 - 2x + \dfrac{7x - 5}{49}e^{2x} + \dfrac{e^x}{37}\left(6\sin 2x - \cos 2x\right)$

### (b) Damped spring–mass system

::: {custom-style="Question Box"}
**Question 2(b).** A spring with a 2000-g mass has a natural length 0.5 m, and a 25.6-newton force is required to maintain it stretched to a length of 0.7 m. If the spring is immersed in a fluid with damping constant $\beta = 40$, and stretched to a length of 0.7 m and then released from the equilibrium position with initial velocity 0.6 m/s: (i) characterize the damped spring–mass system with reason(s); (ii) find the position of the mass at any time $t$. *(6 marks)*
:::

**Data.** $m = 2$ kg. From Hooke's law, $k(0.7 - 0.5) = 25.6$, so $k = 128$ N/m. The damping constant is $\beta = 40$.

**Equation of motion.**

$$m\frac{d^2x}{dt^2} + \beta\frac{dx}{dt} + kx = 0 \quad\Rightarrow\quad 2x'' + 40x' + 128x = 0 \quad\Rightarrow\quad x'' + 20x' + 64x = 0$$

**(i) Characterisation.** The type of motion depends on the sign of $\beta^2 - 4mk$:

$$\beta^2 - 4mk = 40^2 - 4(2)(128) = 1600 - 1024 = 576 > 0$$

The auxiliary equation has two distinct real roots,

$$r^2 + 20r + 64 = (r + 4)(r + 16) = 0 \quad\Rightarrow\quad r = -4, \ -16$$

so the system is **overdamped**: the damping is strong enough that the mass does not oscillate, and it returns to equilibrium without passing through it more than once.

**(ii) Position.**

$$x(t) = c_1e^{-4t} + c_2e^{-16t}$$

The question says both "stretched to 0.7 m" and "released from the equilibrium position". We follow the second phrase, which matches the standard form of this problem: the mass starts at equilibrium and is given a push, so $x(0) = 0$ and $x'(0) = 0.6$.

$$c_1 + c_2 = 0, \qquad -4c_1 - 16c_2 = 0.6 \quad\Rightarrow\quad 12c_1 = 0.6, \ c_1 = 0.05, \ c_2 = -0.05$$

> **Answer.** (i) Overdamped, because $\beta^2 - 4mk = 576 > 0$ (real roots $-4$ and $-16$, no oscillation). (ii) $x(t) = 0.05\left(e^{-4t} - e^{-16t}\right)$ m.

**If the mass starts from the stretched position.** Taking $x(0) = 0.2$ m with $x'(0) = 0.6$ m/s instead gives $c_1 + c_2 = 0.2$ and $-4c_1 - 16c_2 = 0.6$, so $c_1 = \tfrac{19}{60}$, $c_2 = -\tfrac{7}{60}$ and

$$x(t) = \frac{1}{60}\left(19e^{-4t} - 7e^{-16t}\right) \text{ m}$$

The system is overdamped either way.

## Question 3: RLC Circuit

::: {custom-style="Question Box"}
**Question 3.** Find (a) the charge *(6 marks)* and (b) the current *(6 marks)* at time $t$ in a circuit with $R = 40\ \Omega$, $L = 1$ H, $C = 16\times 10^{-4}$ F and $E(t) = 50\cos 5t$. The initial charge and current are both 0.
:::

**The circuit equation.** With $1/C = 1/(16\times 10^{-4}) = 625$,

$$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = E(t) \quad\Rightarrow\quad \frac{d^2q}{dt^2} + 40\frac{dq}{dt} + 625q = 50\cos 5t$$

with $q(0) = 0$ and $q'(0) = I(0) = 0$.

**Complementary function.** $r^2 + 40r + 625 = 0$ gives $r = -20 \pm \sqrt{400 - 625} = -20 \pm 15i$:

$$q_c = e^{-20t}\left(c_1\cos 15t + c_2\sin 15t\right)$$

**Particular integral.** Try $q_p = A\cos 5t + B\sin 5t$, with $q_p'' = -25q_p$:

$$(625 - 25)(A\cos 5t + B\sin 5t) + 40(-5A\sin 5t + 5B\cos 5t) = 50\cos 5t$$

$$\cos 5t: \ 600A + 200B = 50, \qquad \sin 5t: \ 600B - 200A = 0$$

The second gives $A = 3B$; then $1800B + 200B = 50$, so $B = \tfrac{1}{40}$ and $A = \tfrac{3}{40}$:

$$q_p = \frac{1}{40}\left(3\cos 5t + \sin 5t\right)$$

**Constants.** $q(0) = c_1 + \tfrac{3}{40} = 0 \Rightarrow c_1 = -\tfrac{3}{40}$.

$q'(0) = -20c_1 + 15c_2 + 5\cdot\tfrac{1}{40} = \tfrac32 + 15c_2 + \tfrac18 = 0 \Rightarrow c_2 = -\tfrac{13}{120}$.

**(a) Charge.**

$$q(t) = -e^{-20t}\left(\frac{3}{40}\cos 15t + \frac{13}{120}\sin 15t\right) + \frac{1}{40}\left(3\cos 5t + \sin 5t\right)$$

**(b) Current.** Differentiating,

$$I(t) = \frac{dq}{dt} = e^{-20t}\left(\frac{79}{24}\sin 15t - \frac{1}{8}\cos 15t\right) + \frac18\left(\cos 5t - 3\sin 5t\right)$$

Check: $I(0) = -\tfrac18 + \tfrac18 = 0$. ✓

> **Answer.** (a) $q = -e^{-20t}\left(0.075\cos 15t + 0.1083\sin 15t\right) + 0.075\cos 5t + 0.025\sin 5t$ C. (b) $I = e^{-20t}\left(3.2917\sin 15t - 0.125\cos 15t\right) + 0.125\cos 5t - 0.375\sin 5t$ A. The $e^{-20t}$ terms are the transient; the steady-state current is $\tfrac18(\cos 5t - 3\sin 5t)$.

## Question 4: Series Solutions and Bessel's Equation

### (a) Power series solution

::: {custom-style="Question Box"}
**Question 4(a).** Find the power series solution of $2(y'' + 2y) = 0$. *(6 marks)*
:::

Dividing by 2, the equation is $y'' + 2y = 0$. Assume $y = \sum_{n=0}^{\infty} a_n x^n$, so $y'' = \sum_{n=0}^{\infty}(n+2)(n+1)a_{n+2}x^n$. Substituting:

$$\sum_{n=0}^{\infty}\left[(n+2)(n+1)a_{n+2} + 2a_n\right]x^n = 0 \quad\Rightarrow\quad a_{n+2} = -\frac{2a_n}{(n+2)(n+1)}$$

**Even coefficients:**

$$a_2 = -\frac{2a_0}{2!}, \qquad a_4 = -\frac{2a_2}{4\cdot 3} = \frac{2^2a_0}{4!}, \qquad a_6 = -\frac{2^3a_0}{6!}, \ \ldots$$

**Odd coefficients:**

$$a_3 = -\frac{2a_1}{3!}, \qquad a_5 = \frac{2^2a_1}{5!}, \qquad a_7 = -\frac{2^3a_1}{7!}, \ \ldots$$

Hence

$$y = a_0\left(1 - \frac{2x^2}{2!} + \frac{4x^4}{4!} - \frac{8x^6}{6!} + \cdots\right) + a_1\left(x - \frac{2x^3}{3!} + \frac{4x^5}{5!} - \frac{8x^7}{7!} + \cdots\right)$$

Since $2^k x^{2k} = (\sqrt2 x)^{2k}$, the first series is $\cos\sqrt2 x$ and the second is $\dfrac{1}{\sqrt2}\sin\sqrt2 x$.

> **Answer.** $y = a_0\left(1 - x^2 + \dfrac{x^4}{6} - \cdots\right) + a_1\left(x - \dfrac{x^3}{3} + \dfrac{x^5}{30} - \cdots\right) = a_0\cos\sqrt2 x + \dfrac{a_1}{\sqrt2}\sin\sqrt2 x$

### (b) Bessel's equation

::: {custom-style="Question Box"}
**Question 4(b).** Find the general solutions in terms of $J_\nu(x)$ and $J_{-\nu}(x)$ of the following Bessel function equation: $\ xy'' + y' + \left(\dfrac{2}{4}\right)y = 0$. *(6 marks)*
:::

!include bessel

## Question 5: Eigenvalues and Eigenvectors

### (a) Eigenvalues and eigenvectors of a 3 × 3 matrix

::: {custom-style="Question Box"}
**Question 5(a).** Find the eigenvalues and eigenvectors of the matrix *(6 marks)*

$$A = \begin{bmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{bmatrix}$$
:::

**Characteristic equation.** Expanding along the first row,

$$\det(A - \lambda I) = (1 - \lambda)\left[(2 - \lambda)(1 - \lambda) - 1\right] + 1\cdot\left[-(1 - \lambda)\right] = (1 - \lambda)\left[(2 - \lambda)(1 - \lambda) - 2\right]$$

$$= (1 - \lambda)(\lambda^2 - 3\lambda) = -\lambda(\lambda - 1)(\lambda - 3) = 0$$

so $\lambda = 0, \ 1, \ 3$. (Expanded: $\lambda^3 - 4\lambda^2 + 3\lambda = 0$.)

**Eigenvectors.**

$\lambda = 0$: $\ x_1 - x_2 = 0$ and $-x_2 + x_3 = 0 \ \Rightarrow\ x = (1, 1, 1)^T$

$\lambda = 1$: $\ \begin{bmatrix} 0 & -1 & 0 \\ -1 & 1 & -1 \\ 0 & -1 & 0 \end{bmatrix}x = 0 \ \Rightarrow\ x_2 = 0, \ x_1 = -x_3 \ \Rightarrow\ x = (1, 0, -1)^T$

$\lambda = 3$: $\ \begin{bmatrix} -2 & -1 & 0 \\ -1 & -1 & -1 \\ 0 & -1 & -2 \end{bmatrix}x = 0 \ \Rightarrow\ x_2 = -2x_1, \ x_2 = -2x_3 \ \Rightarrow\ x = (1, -2, 1)^T$

**Check** for $\lambda = 3$: $A(1, -2, 1)^T = (1 + 2, \ -1 - 4 - 1, \ 2 + 1)^T = (3, -6, 3)^T = 3(1, -2, 1)^T$ ✓. The matrix is symmetric, so the three eigenvectors are mutually orthogonal.

> **Answer.** $\lambda_1 = 0$ with $x_1 = k(1, 1, 1)^T$; $\ \lambda_2 = 1$ with $x_2 = k(1, 0, -1)^T$; $\ \lambda_3 = 3$ with $x_3 = k(1, -2, 1)^T$ ($k \neq 0$).

### (b) Principal directions of a stretched membrane

::: {custom-style="Question Box"}
**Question 5(b).** An elastic membrane in the $x_1x_2$-plane with boundary circle $x_1^2 + x_2^2 = 1$ is stretched so that a point $P: (x_1, x_2)$ goes over into the point $Q: (y_1, y_2)$ given by

$$y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = Ax = \begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

Find the principal directions, that is, the directions of the position vector $x$ of $P$ for which the direction of the position vector $y$ of $Q$ is the same or exactly opposite. *(6 marks)*
:::

!include membrane

## Question 6: Numerical Differentiation

### (a) Rate of population growth

::: {custom-style="Question Box"}
**Question 6(a).** The table below gives the census population (in millions) of a state for the years 1961 to 2001. Find the rate of growth of the population in the year 2001. *(6 marks)*

| Year ($x$) | 1961 | 1971 | 1981 | 1991 | 2001 |
|---|---|---|---|---|---|
| Population ($y$) | 19.96 | 36.65 | 58.81 | 77.21 | 94.61 |
:::

!include population

### (b) Derivatives from tabulated data

::: {custom-style="Question Box"}
**Question 6(b).** Given a polynomial with the following data points, determine $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$ at $x = 1.1$ and $x = 1.5$. *(6 marks)*

| $x$ | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 |
|---|---|---|---|---|---|---|---|
| $f(x)$ | 7.991 | 8.403 | 8.781 | 9.129 | 9.451 | 9.750 | 10.631 |
:::

!include numdiff-table

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
