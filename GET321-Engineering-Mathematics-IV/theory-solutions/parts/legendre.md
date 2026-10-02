This is Legendre's equation $(1 - x^2)y'' - 2xy' + n(n+1)y = 0$ with $n(n+1) = 2$, that is $n = 1$.

**Power series.** Put $y = \sum_{m=0}^{\infty} a_m x^m$. Then

$$(1 - x^2)\sum_{m} m(m-1)a_m x^{m-2} - 2x\sum_{m} m a_m x^{m-1} + 2\sum_{m} a_m x^m = 0$$

Collecting the coefficient of $x^m$:

$$(m+2)(m+1)a_{m+2} - \left[m(m-1) + 2m - 2\right]a_m = 0$$

Since $m(m-1) + 2m - 2 = m^2 + m - 2 = (m+2)(m-1)$, the recurrence relation is

$$a_{m+2} = \frac{(m+2)(m-1)}{(m+2)(m+1)}\,a_m = \frac{m-1}{m+1}\,a_m$$

**Odd series** ($m = 1$): $a_3 = 0 \cdot a_1 = 0$, so $a_5 = a_7 = \cdots = 0$ and the series stops:

$$y_1 = a_1 x = a_1 P_1(x)$$

**Even series** (from $a_0$):

$$a_2 = -a_0, \qquad a_4 = \frac{1}{3}a_2 = -\frac{a_0}{3}, \qquad a_6 = \frac{3}{5}a_4 = -\frac{a_0}{5}, \qquad a_8 = -\frac{a_0}{7}, \ \ldots$$

$$y_2 = a_0\left(1 - x^2 - \frac{x^4}{3} - \frac{x^6}{5} - \frac{x^8}{7} - \cdots\right) = a_0\left(1 - \frac{x}{2}\ln\frac{1+x}{1-x}\right), \qquad \lvert x \rvert < 1$$

because $\dfrac12\ln\dfrac{1+x}{1-x} = x + \dfrac{x^3}{3} + \dfrac{x^5}{5} + \cdots$.

**Check** of $y_1 = x$: $\ (1 - x^2)(0) - 2x(1) + 2x = 0$. ✓

> **Answer.** $y = c_1 x + c_2\left(1 - x^2 - \dfrac{x^4}{3} - \dfrac{x^6}{5} - \cdots\right) = c_1 P_1(x) + c_2\left(1 - \dfrac{x}{2}\ln\dfrac{1+x}{1-x}\right)$ for $\left\lvert x \right\rvert < 1$. The polynomial solution is the Legendre polynomial $P_1(x) = x$.
