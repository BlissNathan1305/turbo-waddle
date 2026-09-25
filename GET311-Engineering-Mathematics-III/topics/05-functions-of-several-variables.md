# Topic 5: Elements of Functions of Several Variables; Surface Variables

[← Back to course overview](../README.md)

## Introduction

Most engineering quantities depend on more than one variable. Temperature changes with position and time, and pressure depends on volume and temperature. A **function of several variables** $f(x, y, \dots)$ assigns one value to each point of its domain. The main tools are:

- **Level curves and surfaces:** $f(x, y) = c$ (contours) and $f(x, y, z) = c$ (level surfaces, such as isotherms).
- **Limits and continuity** in more than one dimension.
- **Partial derivatives:** $\partial f/\partial x$, $\partial f/\partial y$ and higher-order derivatives. Clairaut's theorem says $f_{xy} = f_{yx}$.
- **Total differential:** $df = f_x\,dx + f_y\,dy$, used for error and sensitivity analysis.
- **Chain rule and implicit differentiation** for composite and implicitly defined functions.
- **Directional derivative and gradient:** $D_{\mathbf{u}}f = \nabla f\cdot\mathbf{u}$. The gradient points in the direction of steepest increase.
- **Taylor expansion** in two variables, used for linearisation.
- **Extrema:** stationary points classified by the second-derivative test ($D = f_{xx}f_{yy} - f_{xy}^2$), and constrained optimisation with **Lagrange multipliers**.

**Surfaces and surface variables:** a surface can be written explicitly as $z = f(x, y)$, implicitly as $F(x, y, z) = 0$, or parametrically as $\mathbf{r}(u, v)$. The parameters $u$ and $v$ are the *surface variables*. The tangent plane and normal come from $\nabla F$ or from $\mathbf{r}_u\times\mathbf{r}_v$, and the element of surface area is $dS = \left\|\mathbf{r}_u\times\mathbf{r}_v\right\|du\,dv$. These are needed for the surface integrals in Topic 6.

---

## Application Questions

### 1. Agricultural Engineering

1. Crop yield (t/ha) is modelled by $Y(N, W) = 0.04N + 0.05W - 0.0001N^2 - 0.0002W^2 + 0.00005NW$, where $N$ is nitrogen (kg/ha) and $W$ is water (mm). Find the input levels that maximise yield, and confirm that the point is a maximum.
2. The evapotranspiration rate $E = kT^{0.5}R^{0.8}$ depends on temperature $T$ and radiation $R$. Use the total differential to estimate the percentage error in $E$ when $T$ is measured with 2 % error and $R$ with 3 % error.

### 2. Computer Engineering

1. Gradient descent minimises the loss $L(w_1, w_2) = (w_1 - 3)^2 + 2(w_2 + 1)^2 + w_1w_2$. Compute $\nabla L$, write the gradient-descent update rule, and carry out 3 iterations from $(0, 0)$ with learning rate $0.1$.
2. The brightness of a grayscale image is modelled as $I(x, y) = 100\,e^{-(x^2 + y^2)/50}$. Compute the image gradient at $(3, 4)$, its magnitude (the edge strength) and its direction, and explain how edge-detection algorithms use this.

### 3. Civil Engineering

1. The ground surface of a site is $z = 50 - 0.01x^2 - 0.02y^2$ (m). At the point $(10, 20)$, find the slope in the direction of the unit vector $\left(\tfrac35, \tfrac45\right)$, the direction of steepest descent (the drainage path), and the equation of the tangent plane.
2. A rectangular beam cut from a circular log of diameter $d$ is strongest in bending when $bh^2$ is largest. Use Lagrange multipliers to find $b$ and $h$ subject to $b^2 + h^2 = d^2$.

### 4. Electrical and Electronics Engineering

1. The power dissipated in a resistor is $P = V^2/R$. Given $V = 220 \pm 2$ V and $R = 50 \pm 0.5\ \Omega$, use partial derivatives and the total differential to estimate the maximum absolute and relative error in $P$.
2. The electric potential near a point charge is $V(x, y, z) = \dfrac{k}{\sqrt{x^2 + y^2 + z^2}}$. Show that $V$ satisfies Laplace's equation $\nabla^2 V = 0$ away from the origin, and find the equation of the equipotential surface through $(1, 2, 2)$.

### 5. Food Engineering

1. During drying, the moisture content is $M(t, T) = M_0\,e^{-k(T)t}$ with $k(T) = 0.01\,e^{0.05(T - 60)}$. Find $\partial M/\partial t$ and $\partial M/\partial T$, and use the chain rule to find $dM/dt$ when the dryer temperature rises as $T = 60 + 0.5t$.
2. A rectangular box for packaging cereal must hold 3000 cm³. The top and bottom cost twice as much per cm² as the sides. Use Lagrange multipliers to find the dimensions that give the cheapest box.

### 6. Mechanical Engineering

1. The temperature distribution in a plate is $T(x, y) = 100 - x^2 - 2y^2$ (°C). A heat-seeking sensor at $(2, 1)$ moves in the direction of fastest heating. Find that direction and the rate of temperature change in it, and find the path of the sensor.
2. The surface of a turbine blade is given parametrically by $\mathbf{r}(u, v) = \left(u\cos v,\ u\sin v,\ 0.5v\right)$ for $1 \le u \le 2$ and $0 \le v \le \pi/2$ (a helicoid). Find $\mathbf{r}_u\times\mathbf{r}_v$, the unit normal and the element of surface area $dS$.
