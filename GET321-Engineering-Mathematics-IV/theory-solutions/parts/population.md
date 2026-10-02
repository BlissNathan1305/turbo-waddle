The year 2001 is at the **end** of the table, so we use Newton's backward difference formula with $h = 10$ years.

**Backward difference table.**

| Year $x$ | $y$ | $\nabla y$ | $\nabla^2 y$ | $\nabla^3 y$ | $\nabla^4 y$ |
|---|---|---|---|---|---|
| 1961 | 19.96 | | | | |
| 1971 | 36.65 | 16.69 | | | |
| 1981 | 58.81 | 22.16 | 5.47 | | |
| 1991 | 77.21 | 18.40 | −3.76 | −9.23 | |
| 2001 | 94.61 | **17.40** | **−1.00** | **2.76** | **11.99** |

**Derivative at the last point** $x_n = 2001$ (where $p = 0$):

$$\left(\frac{dy}{dx}\right)_{x_n} = \frac{1}{h}\left[\nabla y_n + \frac{1}{2}\nabla^2 y_n + \frac{1}{3}\nabla^3 y_n + \frac{1}{4}\nabla^4 y_n\right]$$

$$= \frac{1}{10}\left[17.40 + \frac{-1.00}{2} + \frac{2.76}{3} + \frac{11.99}{4}\right] = \frac{1}{10}\left[17.40 - 0.50 + 0.92 + 2.9975\right] = \frac{20.8175}{10} = 2.0818$$

> **Answer.** In 2001 the population was growing at about **2.08 million per year**.
