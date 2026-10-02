Here $h = 0.1$. The point $x = 1.1$ is near the start of the table, so we use Newton's **forward** formula there; $x = 1.5$ is near the end, so we use the **backward** formula.

**Difference table** (row $x_i$ lists $\Delta^k f_i$, the forward differences starting at that row).

| $x$ | $f(x)$ | $\Delta$ | $\Delta^2$ | $\Delta^3$ | $\Delta^4$ | $\Delta^5$ | $\Delta^6$ |
|---|---|---|---|---|---|---|---|
| 1.0 | 7.991 | 0.412 | −0.034 | 0.004 | 0.000 | −0.001 | 0.604 |
| 1.1 | 8.403 | 0.378 | −0.030 | 0.004 | −0.001 | 0.603 | |
| 1.2 | 8.781 | 0.348 | −0.026 | 0.003 | 0.602 | | |
| 1.3 | 9.129 | 0.322 | −0.023 | 0.605 | | | |
| 1.4 | 9.451 | 0.299 | 0.582 | | | | |
| 1.5 | 9.750 | 0.881 | | | | | |
| 1.6 | 10.631 | | | | | | |

**A note on the data.** The first differences fall steadily (0.412, 0.378, 0.348, 0.322, 0.299) until the last one jumps to 0.881. Every difference that uses $f(1.6)$ is then about 0.6, while the third and fourth differences elsewhere are practically zero. So $f(1.6) = 10.631$ is out of line with the rest of the table, most likely a misprint of 10.031 (the value in the standard version of this table). The working below uses the five points $x = 1.1, \ldots, 1.5$ (differences up to fourth order). Both formulas need only these points, so neither $f(1.6)$ nor $f(1.0)$ affects the answers.

### At $x = 1.1$ (forward differences, $x_0 = 1.1$)

$$\left(\frac{dy}{dx}\right)_{x_0} = \frac{1}{h}\left[\Delta y_0 - \frac{1}{2}\Delta^2 y_0 + \frac{1}{3}\Delta^3 y_0 - \frac{1}{4}\Delta^4 y_0\right]$$

$$= \frac{1}{0.1}\left[0.378 + \frac{0.030}{2} + \frac{0.004}{3} + \frac{0.001}{4}\right] = 10\left[0.378 + 0.015 + 0.00133 + 0.00025\right] = 3.946$$

$$\left(\frac{d^2y}{dx^2}\right)_{x_0} = \frac{1}{h^2}\left[\Delta^2 y_0 - \Delta^3 y_0 + \frac{11}{12}\Delta^4 y_0\right] = 100\left[-0.030 - 0.004 + \frac{11}{12}(-0.001)\right] = -3.492$$

### At $x = 1.5$ (backward differences, $x_n = 1.5$)

From the table, $\nabla y_n = 0.299$, $\nabla^2 y_n = -0.023$, $\nabla^3 y_n = 0.003$ and $\nabla^4 y_n = -0.001$.

$$\left(\frac{dy}{dx}\right)_{x_n} = \frac{1}{h}\left[\nabla y_n + \frac{1}{2}\nabla^2 y_n + \frac{1}{3}\nabla^3 y_n + \frac{1}{4}\nabla^4 y_n\right] = 10\left[0.299 - 0.0115 + 0.001 - 0.00025\right] = 2.883$$

$$\left(\frac{d^2y}{dx^2}\right)_{x_n} = \frac{1}{h^2}\left[\nabla^2 y_n + \nabla^3 y_n + \frac{11}{12}\nabla^4 y_n\right] = 100\left[-0.023 + 0.003 + \frac{11}{12}(-0.001)\right] = -2.092$$

> **Answer.** At $x = 1.1$: $\dfrac{dy}{dx} \approx 3.946$ and $\dfrac{d^2y}{dx^2} \approx -3.492$. At $x = 1.5$: $\dfrac{dy}{dx} \approx 2.883$ and $\dfrac{d^2y}{dx^2} \approx -2.092$.

**If students include $f(1.6)$.** Carrying the forward formula at 1.1 to fifth differences with the printed $f(1.6) = 10.631$ gives $dy/dx \approx 5.15$ and $d^2y/dx^2 \approx -53.7$, which are clearly wrong. With the corrected value $f(1.6) = 10.031$ the fifth-order results are $dy/dx = 3.952$ and $d^2y/dx^2 = -3.742$, close to the answers above.
