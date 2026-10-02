The fraction in the equation reduces to $\tfrac12$, so the equation is

$$x y'' + y' + \tfrac12\, y = 0$$

**Change of variable.** Equations of the form $xy'' + y' + \lambda y = 0$ become Bessel's equation under $z = 2\sqrt{\lambda x}$. Here $\lambda = \tfrac12$, so put

$$z = 2\sqrt{\tfrac{x}{2}} = \sqrt{2x}, \qquad z^2 = 2x, \qquad \frac{dz}{dx} = \frac{1}{z}$$

Then

$$\frac{dy}{dx} = \frac{1}{z}\frac{dy}{dz}, \qquad \frac{d^2y}{dx^2} = \frac{1}{z}\frac{d}{dz}\left(\frac{1}{z}\frac{dy}{dz}\right) = \frac{1}{z^2}\frac{d^2y}{dz^2} - \frac{1}{z^3}\frac{dy}{dz}$$

With $x = z^2/2$:

$$x\frac{d^2y}{dx^2} + \frac{dy}{dx} + \frac12 y = \frac12\frac{d^2y}{dz^2} - \frac{1}{2z}\frac{dy}{dz} + \frac{1}{z}\frac{dy}{dz} + \frac12 y = \frac12\left(\frac{d^2y}{dz^2} + \frac{1}{z}\frac{dy}{dz} + y\right) = 0$$

Multiplying by $2z^2$:

$$z^2\frac{d^2y}{dz^2} + z\frac{dy}{dz} + (z^2 - \nu^2)y = 0 \quad \text{with} \quad \nu = 0$$

This is **Bessel's equation of order $\nu = 0$**.

**General solution.** For order $\nu = 0$ the two independent solutions are $J_0(z)$ and the Bessel function of the second kind, $Y_0(z)$:

$$y = c_1 J_0(z) + c_2 Y_0(z) = c_1 J_0\!\left(\sqrt{2x}\right) + c_2 Y_0\!\left(\sqrt{2x}\right)$$

In series form, the first solution is

$$J_0\!\left(\sqrt{2x}\right) = \sum_{m=0}^{\infty} \frac{(-1)^m}{(m!)^2}\left(\frac{x}{2}\right)^m = 1 - \frac{x}{2} + \frac{x^2}{16} - \frac{x^3}{288} + \cdots$$

> **Answer.** $y = c_1 J_0\!\left(\sqrt{2x}\right) + c_2 Y_0\!\left(\sqrt{2x}\right)$.
