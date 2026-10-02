Here $h = 0.1$. The point $x = 1.1$ is near the start of the table, so we use Newton's **forward** formula there; $x = 1.5$ is near the end, so we use the **backward** formula.

**Difference table** (row $x_i$ lists $\Delta^k f_i$, the forward differences starting at that row).

| $x$ | $f(x)$ | $\Delta$ | $\Delta^2$ | $\Delta^3$ | $\Delta^4$ | $\Delta^5$ | $\Delta^6$ |
|---|---|---|---|---|---|---|---|
| 1.0 | 7.989 | 0.414 | −0.036 | 0.006 | −0.002 | 0.001 | 0.002 |
| 1.1 | 8.403 | 0.378 | −0.030 | 0.004 | −0.001 | 0.003 | |
| 1.2 | 8.781 | 0.348 | −0.026 | 0.003 | 0.002 | | |
| 1.3 | 9.129 | 0.322 | −0.023 | 0.005 | | | |
| 1.4 | 9.451 | 0.299 | −0.018 | | | | |
| 1.5 | 9.750 | 0.281 | | | | | |
| 1.6 | 10.031 | | | | | | |

### At $x = 1.1$ (forward differences, $x_0 = 1.1$)

From the table, $\Delta y_0 = 0.378$, $\Delta^2 y_0 = -0.030$, $\Delta^3 y_0 = 0.004$, $\Delta^4 y_0 = -0.001$ and $\Delta^5 y_0 = 0.003$.

$$\left(\frac{dy}{dx}\right)_{x_0} = \frac{1}{h}\left[\Delta y_0 - \frac{1}{2}\Delta^2 y_0 + \frac{1}{3}\Delta^3 y_0 - \frac{1}{4}\Delta^4 y_0 + \frac{1}{5}\Delta^5 y_0\right]$$

$$= \frac{1}{0.1}\left[0.378 + \frac{0.030}{2} + \frac{0.004}{3} + \frac{0.001}{4} + \frac{0.003}{5}\right] = 10\left[0.378 + 0.015 + 0.00133 + 0.00025 + 0.0006\right] = 3.952$$

$$\left(\frac{d^2y}{dx^2}\right)_{x_0} = \frac{1}{h^2}\left[\Delta^2 y_0 - \Delta^3 y_0 + \frac{11}{12}\Delta^4 y_0 - \frac{5}{6}\Delta^5 y_0\right]$$

$$= 100\left[-0.030 - 0.004 + \frac{11}{12}(-0.001) - \frac{5}{6}(0.003)\right] = 100\left[-0.030 - 0.004 - 0.00092 - 0.0025\right] = -3.742$$

### At $x = 1.5$ (backward differences, $x_n = 1.5$)

From the table, $\nabla y_n = 0.299$, $\nabla^2 y_n = -0.023$, $\nabla^3 y_n = 0.003$, $\nabla^4 y_n = -0.001$ and $\nabla^5 y_n = 0.001$.

$$\left(\frac{dy}{dx}\right)_{x_n} = \frac{1}{h}\left[\nabla y_n + \frac{1}{2}\nabla^2 y_n + \frac{1}{3}\nabla^3 y_n + \frac{1}{4}\nabla^4 y_n + \frac{1}{5}\nabla^5 y_n\right]$$

$$= 10\left[0.299 - 0.0115 + 0.001 - 0.00025 + 0.0002\right] = 2.885$$

$$\left(\frac{d^2y}{dx^2}\right)_{x_n} = \frac{1}{h^2}\left[\nabla^2 y_n + \nabla^3 y_n + \frac{11}{12}\nabla^4 y_n + \frac{5}{6}\nabla^5 y_n\right]$$

$$= 100\left[-0.023 + 0.003 - 0.00092 + 0.00083\right] = -2.008$$

> **Answer.** At $x = 1.1$: $\dfrac{dy}{dx} \approx 3.952$ and $\dfrac{d^2y}{dx^2} \approx -3.742$. At $x = 1.5$: $\dfrac{dy}{dx} \approx 2.885$ and $\dfrac{d^2y}{dx^2} \approx -2.008$.
