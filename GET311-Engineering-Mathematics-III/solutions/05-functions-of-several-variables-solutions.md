# Topic 5 Solutions: Functions of Several Variables

## 1. Agricultural Engineering

### Question 1: Maximum crop yield

Set both partial derivatives to zero:

$$Y_N = 0.04 - 0.0002N + 0.00005W = 0, \qquad Y_W = 0.05 - 0.0004W + 0.00005N = 0$$

Solving gives $N = 238.7$ kg/ha and $W = 154.8$ mm, with $Y_{\max} = 8.65$ t/ha. For the second-derivative test, $Y_{NN} = -0.0002$, $Y_{WW} = -0.0004$ and $Y_{NW} = 0.00005$:

$$D = (-0.0002)(-0.0004) - (0.00005)^2 = 7.75\times10^{-8} > 0, \qquad Y_{NN} < 0$$

so the point is a **maximum**.

> **Answer.** $N = 238.7$ kg/ha, $W = 154.8$ mm, $Y_{\max} = 8.65$ t/ha.

### Question 2: Error in evapotranspiration

Taking logarithms, $\ln E = \ln k + 0.5\ln T + 0.8\ln R$. Differentiating,

$$\frac{dE}{E} = 0.5\frac{dT}{T} + 0.8\frac{dR}{R}$$

In the worst case the errors add: $0.5(2\%) + 0.8(3\%) = 3.4\%$.

> **Answer.** The maximum error in $E$ is 3.4 %.

## 2. Chemical Engineering

### Question 1: Van der Waals partial derivatives

Write $P = \dfrac{RT}{V - b} - \dfrac{a}{V^2}$. Then

$$\left(\frac{\partial P}{\partial V}\right)_T = -\frac{RT}{(V - b)^2} + \frac{2a}{V^3}, \qquad \left(\frac{\partial P}{\partial T}\right)_V = \frac{R}{V - b}$$

Treating $F(P, V, T) = 0$ implicitly, $\left(\dfrac{\partial V}{\partial T}\right)_P = -\dfrac{(\partial P/\partial T)_V}{(\partial P/\partial V)_T}$ and $\left(\dfrac{\partial T}{\partial P}\right)_V = \dfrac{1}{(\partial P/\partial T)_V}$. Multiplying the three:

$$\left(\frac{\partial P}{\partial V}\right)_T\cdot\left(-\frac{(\partial P/\partial T)_V}{(\partial P/\partial V)_T}\right)\cdot\frac{1}{(\partial P/\partial T)_V} = -1 \qquad ∎$$

> **Answer.** The two partial derivatives are given above, and their cyclic product is $-1$.

### Question 2: Least surface area for a fixed volume

Minimise $A = 2\pi r^2 + 2\pi rh$ subject to $\pi r^2 h = 10$. The Lagrange conditions are

$$4\pi r + 2\pi h = \lambda\cdot 2\pi rh, \qquad 2\pi r = \lambda\pi r^2$$

The second gives $\lambda = 2/r$; substituting into the first gives $4r + 2h = 4h$, so $h = 2r$ (the height equals the diameter). Then $2\pi r^3 = 10$, so

$$r = \left(\frac{5}{\pi}\right)^{1/3} = 1.168\ \text{m}, \qquad h = 2.335\ \text{m}, \qquad A_{\min} = 25.7\ \text{m}^2$$

> **Answer.** $r = 1.168$ m and $h = 2.335$ m (height = diameter).

## 3. Computer Engineering

### Question 1: Gradient descent

$$\nabla L = \left(2(w_1 - 3) + w_2,\ \ 4(w_2 + 1) + w_1\right), \qquad \mathbf{w} \leftarrow \mathbf{w} - \eta\,\nabla L(\mathbf{w}),\ \ \eta = 0.1$$

| $k$ | $w_1$ | $w_2$ | $L$ |
|---|---|---|---|
| 0 | 0 | 0 | 11.00 |
| 1 | 0.600 | −0.400 | 6.24 |
| 2 | 1.120 | −0.700 | 2.93 |
| 3 | 1.566 | −0.932 | 0.61 |

The iterates are heading towards the true minimum, where $\nabla L = \mathbf{0}$: $(4, -2)$ with $L = -4$.

> **Answer.** After 3 steps, $\mathbf{w} = (1.566,\ -0.932)$.

### Question 2: Image gradient

$I(3, 4) = 100\,e^{-25/50} = 60.65$, and $\nabla I = -\dfrac{2}{50}(x, y)\,I$, so

$$\nabla I(3, 4) = -0.04\,(3, 4)(60.65) = (-7.28,\ -9.70), \qquad \left\|\nabla I\right\| = 12.13$$

The gradient direction is $(-0.6, -0.8)$, pointing towards the bright centre. Edge detectors (Sobel, Canny) estimate $\nabla I$ with finite differences at each pixel and mark as edges the pixels where $\left\|\nabla I\right\|$ is a local maximum across the gradient direction and above a threshold. The edge itself runs perpendicular to $\nabla I$.

> **Answer.** $\nabla I = (-7.28,\ -9.70)$; edge strength $12.13$; direction $(-0.6,\ -0.8)$.

## 4. Civil Engineering

### Question 1: Slope and drainage at (10, 20)

$z(10, 20) = 50 - 1 - 8 = 41$ m and $\nabla z = (-0.02x,\ -0.04y) = (-0.2,\ -0.8)$.

$$D_{\mathbf{u}}z = \nabla z\cdot\left(\tfrac35, \tfrac45\right) = -0.12 - 0.64 = -0.76$$

The ground falls 0.76 m per metre in that direction. Water drains along $-\nabla z = (0.2, 0.8)$, or $(0.243, 0.970)$ as a unit vector, where the slope is $\left\|\nabla z\right\| = 0.825$. The tangent plane is

$$z = 41 - 0.2(x - 10) - 0.8(y - 20) \quad\Longleftrightarrow\quad 0.2x + 0.8y + z = 59$$

> **Answer.** Slope $-0.76$; drainage along $(0.243,\ 0.970)$; tangent plane $0.2x + 0.8y + z = 59$.

### Question 2: Strongest beam from a log

Maximise $S = bh^2$ subject to $b^2 + h^2 = d^2$. The Lagrange conditions are $h^2 = 2\lambda b$ and $2bh = 2\lambda h$, so $\lambda = b$ and $h^2 = 2b^2$. Substituting into the constraint gives $3b^2 = d^2$:

$$b = \frac{d}{\sqrt3} \approx 0.577d, \qquad h = d\sqrt{\frac23} \approx 0.816d$$

> **Answer.** $b = d/\sqrt3$ and $h = d\sqrt{2/3}$ (so $h : b = \sqrt2 : 1$).

## 5. Electrical and Electronics Engineering

### Question 1: Error in dissipated power

$P = V^2/R = 48\,400/50 = 968$ W, and

$$dP = \frac{2V}{R}\,dV - \frac{V^2}{R^2}\,dR = 8.8\,dV - 19.36\,dR$$

In the worst case the errors add: $\left|dP\right| \le 8.8(2) + 19.36(0.5) = 17.6 + 9.68 = 27.3$ W. The relative error is

$$\frac{\left|dP\right|}{P} \le 2\cdot\frac{2}{220} + \frac{0.5}{50} = 0.0182 + 0.0100 = 2.8\%$$

> **Answer.** $P = 968 \pm 27.3$ W, a relative error of 2.8 %.

### Question 2: The point-charge potential

Let $r^2 = x^2 + y^2 + z^2$, so $V = k/r$. Then $V_x = -kx/r^3$ and $V_{xx} = -k/r^3 + 3kx^2/r^5$, with $V_{yy}$ and $V_{zz}$ of the same form. Adding,

$$\nabla^2 V = -\frac{3k}{r^3} + \frac{3k(x^2 + y^2 + z^2)}{r^5} = -\frac{3k}{r^3} + \frac{3k}{r^3} = 0 \qquad (r \ne 0)$$

At $(1, 2, 2)$, $r = 3$ and $V = k/3$.

> **Answer.** $\nabla^2 V = 0$; the equipotential through $(1, 2, 2)$ is the sphere $x^2 + y^2 + z^2 = 9$.

## 6. Food Engineering

### Question 1: Moisture during drying

$$\frac{\partial M}{\partial t} = -k(T)\,M, \qquad \frac{\partial M}{\partial T} = -M_0\,t\,k'(T)\,e^{-kt} = -0.05\,k(T)\,t\,M$$

since $k' = 0.05k$. With $T = 60 + 0.5t$, $dT/dt = 0.5$, and the chain rule gives

$$\frac{dM}{dt} = \frac{\partial M}{\partial t} + \frac{\partial M}{\partial T}\frac{dT}{dt} = -k(T)\,M\,(1 + 0.025t), \qquad k = 0.01\,e^{0.025t}$$

The rising temperature speeds up drying in two ways: $k$ grows, and the extra factor $(1 + 0.025t)$ appears.

> **Answer.** $\dfrac{dM}{dt} = -0.01\,e^{0.025t}\,M\,(1 + 0.025t)$

### Question 2: Cheapest cereal box

Let the base be $a\times b$ and the height $c$. The cost is proportional to $C = 2(2ab) + 2ac + 2bc$, subject to $abc = 3000$. The Lagrange conditions give $a = b$ (by symmetry) and $c = 2a$. Then $2a^3 = 3000$:

$$a = b = 11.45\ \text{cm}, \qquad c = 22.89\ \text{cm}$$

The box is twice as tall as it is wide because its top and bottom cost more.

> **Answer.** Base 11.45 cm × 11.45 cm; height 22.89 cm.

## 7. Mechanical Engineering

### Question 1: Path of fastest heating

$\nabla T = (-2x, -4y)$, so $\nabla T(2, 1) = (-4, -4)$. The sensor moves along $\dfrac{(-1, -1)}{\sqrt2}$, towards the hotter centre, at the rate $\left\|\nabla T\right\| = 4\sqrt2 \approx 5.66$ °C per unit length.

The path follows the gradient: $\dot{x} = -2x$ and $\dot{y} = -4y$, so $x = 2e^{-2t}$ and $y = e^{-4t}$. Eliminating $t$:

$$y = \frac{x^2}{4}$$

> **Answer.** Direction $(-1, -1)/\sqrt2$; rate $4\sqrt2 \approx 5.66$ °C/unit; path $y = x^2/4$ towards $(0, 0)$.

### Question 2: The helicoid blade surface

$$\mathbf{r}_u = (\cos v,\ \sin v,\ 0), \qquad \mathbf{r}_v = (-u\sin v,\ u\cos v,\ \tfrac12)$$

$$\mathbf{r}_u\times\mathbf{r}_v = \left(\tfrac12\sin v,\ -\tfrac12\cos v,\ u\right), \qquad \left\|\mathbf{r}_u\times\mathbf{r}_v\right\| = \sqrt{u^2 + \tfrac14}$$

> **Answer.** $\mathbf{n} = \dfrac{\left(\tfrac12\sin v,\ -\tfrac12\cos v,\ u\right)}{\sqrt{u^2 + 1/4}}$ and $dS = \sqrt{u^2 + \tfrac14}\,du\,dv$.

## 8. Petroleum Engineering

### Question 1: The pressure field around the well

Let $c = \dfrac{q\mu}{4\pi kh}$ and $r^2 = x^2 + y^2$. Then $p = p_e - c\ln(r^2/r_e^2)$, and

$$\nabla p = -\frac{2c\,(x, y)}{r^2} = -\frac{q\mu}{2\pi kh}\,\frac{\hat{\mathbf{r}}}{r}$$

This is purely radial, with magnitude falling off as $1/r$. So the flow along $-\nabla p$ is radial, and the Darcy velocity is $u = \dfrac{k}{\mu}\cdot\dfrac{q\mu}{2\pi kh\,r} = \dfrac{q}{2\pi rh}$.

**Note on the sign.** With the formula exactly as written, $p$ *increases* towards the well, so $-\nabla p$ points **outward**: that describes an injector. For a **producing** well the pressure must be lowest at the well, $p = p_e + c\ln(r^2/r_e^2)$. Then $\nabla p$ points outward and the flow $-\nabla p$ points radially **inward**, towards the well ✓. Students should spot and correct the sign.

> **Answer.** $\nabla p$ is radial with magnitude $\dfrac{q\mu}{2\pi kh\,r}$; with the corrected sign the flow is radially into the well.

### Question 2: Linearising $B_o$

$B_o$ is already linear in $p$ and $T$, so its first-order Taylor expansion about $(3000, 150)$ is the function itself. At (2800 psi, 160 °F):

$$B_o = 1.2 + 0.0001(10) - 0.00002(-200) = 1.2 + 0.001 + 0.004 = 1.205$$

> **Answer.** $B_o = 1.205$ rb/stb
