**Spring constant.** Hooke's law, $F = kx$, with the extension $x = 0.7 - 0.5 = 0.2$ m:

$$k(0.2) = 25.6 \quad\Rightarrow\quad k = 128 \text{ N/m}$$

The mass is $m = 2000 \text{ g} = 2$ kg. Let $x(t)$ be the displacement of the mass from equilibrium (the natural length, 0.5 m), positive in the direction of stretching.

**Equation of motion.** There is no damping, so

$$m\frac{d^2x}{dt^2} + kx = 0 \quad\Rightarrow\quad 2\frac{d^2x}{dt^2} + 128x = 0 \quad\Rightarrow\quad \frac{d^2x}{dt^2} + 64x = 0$$

The auxiliary equation $r^2 + 64 = 0$ gives $r = \pm 8i$, so

$$x(t) = c_1\cos 8t + c_2\sin 8t$$

**Initial conditions.** The spring starts stretched to 0.7 m, so $x(0) = 0.2$, and it is released from rest, so $x'(0) = 0$.

$$x(0) = c_1 = 0.2, \qquad x'(0) = 8c_2 = 0 \quad\Rightarrow\quad c_2 = 0$$

**(i) Position at any time.**

$$x(t) = 0.2\cos 8t \ \text{m}$$

The mass oscillates about the equilibrium position with amplitude 0.2 m, angular frequency $\omega = 8$ rad/s and period $T = 2\pi/8 = \pi/4$ s.

**(ii) At $t = \pi/24$ s.**

$$x\left(\frac{\pi}{24}\right) = 0.2\cos\left(\frac{8\pi}{24}\right) = 0.2\cos\frac{\pi}{3} = 0.2 \times 0.5 = 0.1 \text{ m}$$

The velocity $x'(t) = -1.6\sin 8t$ stays negative for $0 < t < \pi/8$, and $\pi/24 < \pi/8$, so the mass moves steadily back towards equilibrium without turning. The distance travelled from the start is therefore

$$0.2 - 0.1 = 0.1 \text{ m}$$

and the spring's length at that moment is $0.5 + 0.1 = 0.6$ m.

> **Answer.** (i) $x(t) = 0.2\cos 8t$ m. (ii) At $t = \pi/24$ s the mass is 0.1 m from equilibrium, having travelled 0.1 m from its starting point (spring length 0.6 m).
