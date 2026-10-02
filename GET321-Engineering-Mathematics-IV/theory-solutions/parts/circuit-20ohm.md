**The circuit equation.** By Kirchhoff's voltage law, with $I = dq/dt$,

$$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = E(t)$$

Here $R = 20\ \Omega$, $L = 1$ H and $C = 2000\ \mu\text{F} = 2\times 10^{-3}$ F, so $1/C = 500$:

$$\frac{d^2q}{dt^2} + 20\frac{dq}{dt} + 500q = E(t), \qquad q(0) = 0, \quad I(0) = q'(0) = 0$$

**Complementary function.** $r^2 + 20r + 500 = 0$ gives $r = -10 \pm \sqrt{100 - 500} = -10 \pm 20i$:

$$q_c = e^{-10t}\left(c_1\cos 20t + c_2\sin 20t\right)$$

### Case (i): 12 V battery, $E = 12$

**Particular integral.** Try a constant: $500q_p = 12$, so $q_p = \dfrac{12}{500} = 0.024$.

$$q = e^{-10t}\left(c_1\cos 20t + c_2\sin 20t\right) + 0.024$$

$q(0) = 0$: $\ c_1 + 0.024 = 0 \Rightarrow c_1 = -0.024$.

$q'(0) = 0$: $\ -10c_1 + 20c_2 = 0 \Rightarrow c_2 = \tfrac12 c_1 = -0.012$.

$$q(t) = 0.024 - e^{-10t}\left(0.024\cos 20t + 0.012\sin 20t\right) = \frac{3}{250}\left[2 - e^{-10t}\left(2\cos 20t + \sin 20t\right)\right]$$

**Current.** Differentiating,

$$I = \frac{dq}{dt} = 10e^{-10t}\left(0.024\cos 20t + 0.012\sin 20t\right) - e^{-10t}\left(-0.48\sin 20t + 0.24\cos 20t\right) = 0.6\,e^{-10t}\sin 20t$$

### Case (ii): generator, $E = 12\sin 10t$

**Particular integral.** Try $q_p = A\cos 10t + B\sin 10t$, so $q_p'' = -100q_p$:

$$(500 - 100)(A\cos 10t + B\sin 10t) + 20(-10A\sin 10t + 10B\cos 10t) = 12\sin 10t$$

$$\cos 10t: \ 400A + 200B = 0, \qquad \sin 10t: \ 400B - 200A = 12$$

From the first, $B = -2A$; then $-800A - 200A = 12$, so $A = -0.012$ and $B = 0.024$:

$$q_p = -0.012\cos 10t + 0.024\sin 10t$$

**Constants.** $q(0) = c_1 - 0.012 = 0 \Rightarrow c_1 = 0.012$.

$q'(0) = -10c_1 + 20c_2 + 10(0.024) = -0.12 + 20c_2 + 0.24 = 0 \Rightarrow c_2 = -0.006$.

$$q(t) = e^{-10t}\left(0.012\cos 20t - 0.006\sin 20t\right) - 0.012\cos 10t + 0.024\sin 10t$$

**Current.**

$$I = \frac{dq}{dt} = -e^{-10t}\left(0.24\cos 20t + 0.18\sin 20t\right) + 0.24\cos 10t + 0.12\sin 10t$$

Check: $I(0) = -0.24 + 0.24 = 0$. ✓ The $e^{-10t}$ terms are the transient, which dies away; the steady-state current is $0.24\cos 10t + 0.12\sin 10t$.

> **Answer.**
> (i) $q = 0.024 - e^{-10t}(0.024\cos 20t + 0.012\sin 20t)$ C and $I = 0.6\,e^{-10t}\sin 20t$ A.
> (ii) $q = e^{-10t}(0.012\cos 20t - 0.006\sin 20t) - 0.012\cos 10t + 0.024\sin 10t$ C and $I = -e^{-10t}(0.24\cos 20t + 0.18\sin 20t) + 0.24\cos 10t + 0.12\sin 10t$ A.
