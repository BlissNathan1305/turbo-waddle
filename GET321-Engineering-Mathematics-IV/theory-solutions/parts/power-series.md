Assume a power series solution about $x = 0$:

$$y = \sum_{n=0}^{\infty} a_n x^n, \qquad y'' = \sum_{n=2}^{\infty} n(n-1)a_n x^{n-2} = \sum_{n=0}^{\infty} (n+2)(n+1)a_{n+2}\, x^{n}$$

Substituting into $y'' + y = 0$:

$$\sum_{n=0}^{\infty}\left[(n+2)(n+1)a_{n+2} + a_n\right]x^n = 0$$

Every coefficient must vanish, which gives the **recurrence relation**

$$a_{n+2} = -\frac{a_n}{(n+2)(n+1)}, \qquad n = 0, 1, 2, \ldots$$

**Even coefficients** (in terms of $a_0$):

$$a_2 = -\frac{a_0}{2!}, \qquad a_4 = -\frac{a_2}{4\cdot 3} = \frac{a_0}{4!}, \qquad a_6 = -\frac{a_4}{6\cdot 5} = -\frac{a_0}{6!}, \ \ldots$$

**Odd coefficients** (in terms of $a_1$):

$$a_3 = -\frac{a_1}{3!}, \qquad a_5 = -\frac{a_3}{5\cdot 4} = \frac{a_1}{5!}, \qquad a_7 = -\frac{a_1}{7!}, \ \ldots$$

Hence

$$y = a_0\left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots\right) + a_1\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots\right)$$

The two series are the Maclaurin series of $\cos x$ and $\sin x$, and both converge for all $x$.

> **Answer.** $y = a_0\left(1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \cdots\right) + a_1\left(x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots\right) = a_0\cos x + a_1\sin x$, where $a_0$ and $a_1$ are arbitrary constants.
