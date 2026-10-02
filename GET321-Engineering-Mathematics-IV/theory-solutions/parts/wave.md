The symbol $\delta$ in the question stands for the partial derivative $\partial$. The equation is

$$\frac{\partial^2 u}{\partial x^2} = \frac{1}{16}\frac{\partial^2 u}{\partial t^2} \quad\Leftrightarrow\quad \frac{\partial^2 u}{\partial t^2} = c^2\frac{\partial^2 u}{\partial x^2}, \qquad c^2 = 16, \ c = 4, \ L = 2$$

**Separation of variables.** Put $u = F(x)G(t)$:

$$\frac{F''}{F} = \frac{G''}{16\,G} = -p^2$$

so $F'' + p^2F = 0$ and $G'' + 16p^2G = 0$.

**Boundary conditions.** $u(0,t) = u(2,t) = 0$ need $F(0) = F(2) = 0$. With $F = A\cos px + B\sin px$, $F(0) = 0$ gives $A = 0$, and $\sin 2p = 0$ gives

$$p = \frac{n\pi}{2}, \qquad F_n(x) = \sin\frac{n\pi x}{2}, \qquad n = 1, 2, 3, \ldots$$

**Time part.** $G_n'' + \lambda_n^2 G_n = 0$ with $\lambda_n = \dfrac{cn\pi}{L} = \dfrac{4n\pi}{2} = 2n\pi$:

$$G_n(t) = B_n\cos 2n\pi t + B_n^*\sin 2n\pi t$$

so

$$u(x,t) = \sum_{n=1}^{\infty}\left(B_n\cos 2n\pi t + B_n^*\sin 2n\pi t\right)\sin\frac{n\pi x}{2}$$

**Initial velocity.** $\dfrac{\partial u}{\partial t}(x,0) = \sum 2n\pi B_n^*\sin\dfrac{n\pi x}{2} = 0$, so $B_n^* = 0$ for every $n$.

**Initial displacement.**

$$u(x,0) = \sum_{n=1}^{\infty} B_n\sin\frac{n\pi x}{2} = 6\sin\pi x - 3\sin 4\pi x$$

$\sin \pi x = \sin\dfrac{2\pi x}{2}$ is the $n = 2$ term and $\sin 4\pi x = \sin\dfrac{8\pi x}{2}$ is the $n = 8$ term. Comparing coefficients (no Fourier integrals are needed):

$$B_2 = 6, \qquad B_8 = -3, \qquad B_n = 0 \ \text{otherwise}$$

With $\lambda_2 = 4\pi$ and $\lambda_8 = 16\pi$:

> **Answer.** $u(x,t) = 6\sin\pi x\cos 4\pi t - 3\sin 4\pi x\cos 16\pi t$.

**Check.** $u(0,t) = u(2,t) = 0$ since $\sin 2\pi = \sin 8\pi = 0$; $u(x,0) = 6\sin\pi x - 3\sin 4\pi x$; $u_t(x,0) = 0$; and each term satisfies $u_{tt} = 16u_{xx}$, for example $(4\pi)^2 = 16\pi^2$. ✓
