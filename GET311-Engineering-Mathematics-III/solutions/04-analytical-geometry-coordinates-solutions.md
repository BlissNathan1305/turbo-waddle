# Topic 4 Solutions: Analytical Geometry and Coordinate Systems

## 1. Agricultural Engineering

### Question 1: Centre-pivot boundary

In Cartesian coordinates the boundary is

$$(x - 500)^2 + (y - 300)^2 = 400^2$$

Translate the origin to the pivot with $X = x - 500$, $Y = y - 300$, so $X^2 + Y^2 = 160\,000$. In polar coordinates about the pivot ($X = r\cos\theta$, $Y = r\sin\theta$) this becomes $r = 400$. Then

$$A = \int_0^{2\pi}\!\!\int_0^{400} r\,dr\,d\theta = \pi(400)^2 = 502\,655\ \text{m}^2$$

> **Answer.** $r = 400$ about the pivot; area $502\,655$ m² ≈ 50.3 ha.

### Question 2: The silo

In cylindrical coordinates $(r, \theta, z)$:

- Cylinder wall: $r = 3$, $0 \le z \le 10$.
- Conical roof: it rises from $z = 10$ at $r = 3$ to $z = 12$ at $r = 0$, so $z = 12 - \tfrac{2}{3}r$, $0 \le r \le 3$.

$$V = \pi r^2 h + \tfrac13\pi r^2 h_c = \pi(9)(10) + \tfrac13\pi(9)(2) = 90\pi + 6\pi = 96\pi \approx 301.6\ \text{m}^3$$

> **Answer.** Wall $r = 3$; roof $z = 12 - \tfrac23 r$; volume $96\pi \approx 301.6$ m³.

## 2. Chemical Engineering

### Question 1: The spherical catalyst pellet

A point on the surface is $(\rho, \theta, \phi) = (5\ \text{mm}, \theta, \phi)$ for any $0 \le \theta < 2\pi$ and $0 \le \phi \le \pi$, that is $x = 5\sin\phi\cos\theta$, $y = 5\sin\phi\sin\theta$, $z = 5\cos\phi$.

If $C$ depends only on $\rho$, then $\partial C/\partial\theta = \partial C/\partial\phi = 0$ and the Laplacian reduces to

$$\nabla^2 C = \frac{1}{\rho^2}\frac{d}{d\rho}\left(\rho^2\frac{dC}{d\rho}\right)$$

So the 3-D diffusion–reaction PDE becomes **one ordinary differential equation in $\rho$**, where Cartesian coordinates would need all three variables together.

> **Answer.** Surface: $\rho = 5$ mm. Spherical symmetry removes $\theta$ and $\phi$, leaving an ODE in $\rho$.

### Question 2: The elliptical tank

Complete the squares:

$$9(x^2 - 4x) + 4(y^2 + 6y) + 36 = 0 \quad\Rightarrow\quad 9(x - 2)^2 + 4(y + 3)^2 = 36$$

Translating with $X = x - 2$ and $Y = y + 3$ gives the standard form

$$\frac{X^2}{4} + \frac{Y^2}{9} = 1$$

> **Answer.** Centre $(2, -3)$; semi-axes $a = 2$ (along $x$) and $b = 3$ (along $y$); area $\pi ab = 6\pi \approx 18.85$.

## 3. Computer Engineering

### Question 1: Robot arm position

$$x = 0.8\cos 60^\circ = 0.400\ \text{m}, \qquad y = 0.8\sin 60^\circ = 0.693\ \text{m}, \qquad z = 0.5\ \text{m}$$

```
cart_to_cyl(x,y,z):  return (sqrt(x²+y²), atan2(y,x), z)
cyl_to_cart(r,θ,z):  return (r cos θ, r sin θ, z)
cart_to_sph(x,y,z):  ρ = sqrt(x²+y²+z²)
                     return (ρ, atan2(y,x), acos(z/ρ))
sph_to_cart(ρ,θ,φ):  return (ρ sin φ cos θ, ρ sin φ sin θ, ρ cos φ)
cyl_to_sph(r,θ,z):   return (sqrt(r²+z²), θ, atan2(r, z))
sph_to_cyl(ρ,θ,φ):   return (ρ sin φ, θ, ρ cos φ)
```

Use atan2, not atan, so that the angle ends up in the correct quadrant.

> **Answer.** $(x, y, z) = (0.400,\ 0.693,\ 0.5)$ m.

### Question 2: The lidar point

With $\rho = 20$, $\theta = 45^\circ$ and $\phi = 60^\circ$:

$$x = 20\sin 60^\circ\cos 45^\circ = 12.25, \qquad y = 12.25, \qquad z = 20\cos 60^\circ = 10$$

(all in metres).

The distance to $z = 0$ is 10 m. The distance to the plane $x + y + z = 10$ is

$$d = \frac{\left|12.25 + 12.25 + 10 - 10\right|}{\sqrt3} = \frac{24.49}{\sqrt3} = 14.14\ \text{m}$$

> **Answer.** Point $(12.25,\ 12.25,\ 10)$ m; 10 m above the ground; 14.14 m from the plane.

## 4. Civil Engineering

### Question 1: The embankment plane

$\overrightarrow{AB} = (200, 0, 4)$ and $\overrightarrow{AC} = (0, 150, -3)$, so the normal is

$$\mathbf{n} = \overrightarrow{AB}\times\overrightarrow{AC} = (-600,\ 600,\ 30\,000) \parallel (-1,\ 1,\ 50)$$

The plane through $A$ is $-x + y + 50z = 5000$, or

$$z = 100 + \frac{x - y}{50}$$

The direction cosines of the normal are $\dfrac{(-1, 1, 50)}{\sqrt{2502}} = (-0.0200,\ 0.0200,\ 0.9996)$. The angle with the horizontal equals the angle between the normal and the $z$-axis: $\cos^{-1}(0.9996) = 1.62^\circ$.

> **Answer.** $z = 100 + (x - y)/50$; direction cosines $(-0.020,\ 0.020,\ 0.9996)$; slope angle $1.62^\circ$.

### Question 2: The parabolic arch

The arch is symmetric with vertex $(0, 15)$, so $y = 15 - kx^2$. At $(30, 0)$, $0 = 15 - 900k$, so $k = 1/60$:

$$y = 15 - \frac{x^2}{60}$$

Rotate the axes by $\alpha = 10^\circ$ using $x = X\cos\alpha - Y\sin\alpha$ and $y = X\sin\alpha + Y\cos\alpha$, with $\cos 10^\circ = 0.9848$ and $\sin 10^\circ = 0.1736$:

$$0.1736X + 0.9848Y = 15 - \frac{(0.9848X - 0.1736Y)^2}{60}$$

Expanded, this contains an $XY$ term. That is expected: in the rotated frame the parabola's axis is no longer parallel to a coordinate axis.

> **Answer.** $y = 15 - x^2/60$; the rotated form is given above.

## 5. Electrical and Electronics Engineering

### Question 1: The dipole pattern surface

Multiply $\rho = \sin\phi$ by $\rho$ to get $\rho^2 = \rho\sin\phi$. Since $\rho\sin\phi = \sqrt{x^2 + y^2}$:

$$x^2 + y^2 + z^2 = \sqrt{x^2 + y^2}$$

In any plane through the $z$-axis, with $r = \sqrt{x^2 + y^2}$, this is $\left(r - \tfrac12\right)^2 + z^2 = \tfrac14$: a circle of radius $\tfrac12$ centred at $r = \tfrac12$ that touches the axis. Revolving it about the $z$-axis gives a **horn torus**, a doughnut with no hole. The dipole radiates most strongly broadside ($\phi = 90^\circ$) and not at all along its own axis.

> **Answer.** $x^2 + y^2 + z^2 = \sqrt{x^2 + y^2}$, a horn torus.

### Question 2: The coaxial dielectric

The dielectric region is $1\ \text{mm} \le r \le 4\ \text{mm}$, $0 \le \theta < 2\pi$, with $z$ unrestricted along the cable.

$$A = \int_0^{2\pi}\!\!\int_1^4 r\,dr\,d\theta = 2\pi\cdot\frac{16 - 1}{2} = 15\pi \approx 47.1\ \text{mm}^2$$

> **Answer.** $1 \le r \le 4$ mm; area $15\pi \approx 47.1$ mm².

## 6. Food Engineering

### Question 1: Slowest-heating point in the can

On the axis at mid-height means $(r, \theta, z) = (0,\ \text{any }\theta,\ 5.5\ \text{cm})$; the angle is undefined on the axis. The rim edges are at $r = 4$ and $z = 0$ or $11$, so the distance is

$$d = \sqrt{4^2 + 5.5^2} = \sqrt{46.25} = 6.80\ \text{cm}$$

> **Answer.** $(0, \theta, 5.5)$ cm; 6.80 cm from the rim.

### Question 2: The egg

With semi-axes $a = b = 2$ cm and $c = 3$ cm,

$$V = \frac43\pi abc = \frac43\pi(2)(2)(3) = 16\pi \approx 50.3\ \text{cm}^3$$

The stretching $X = x/2$, $Y = y/2$, $Z = z/3$ maps the ellipsoid onto the unit sphere $X^2 + Y^2 + Z^2 = 1$. The Jacobian is $abc = 12$, so $V = 12\times\tfrac43\pi$ ✓.

On a sphere, heat conduction with uniform surface conditions depends only on the radius. The PDE reduces to a 1-D problem with standard series solutions, which can be mapped back, or used as a shape-factor approximation, for the egg.

> **Answer.** $V = 16\pi \approx 50.3$ cm³; $X = x/2$, $Y = y/2$, $Z = z/3$ gives the unit sphere.

## 7. Mechanical Engineering

### Question 1: The cam profile

Multiply $r = 40 + 10\cos\theta$ by $r$ to get $r^2 = 40r + 10r\cos\theta$, that is

$$x^2 + y^2 = 40\sqrt{x^2 + y^2} + 10x$$

This curve is a limaçon.

$r_{\max} = 50$ mm at $\theta = 0$ and $r_{\min} = 30$ mm at $\theta = \pi$, so the follower lift is 20 mm.

$$A = \frac12\int_0^{2\pi}(40 + 10\cos\theta)^2\,d\theta = \frac12\left[1600(2\pi) + 0 + 100\pi\right] = 1650\pi \approx 5184\ \text{mm}^2$$

> **Answer.** Lift 20 mm; area $1650\pi \approx 5184$ mm².

### Question 2: The two machine members

The directions are $\mathbf{d}_1 = (2, 3, 6)$ and $\mathbf{d}_2 = (3, -2, 6)$, both of length 7:

$$\cos\alpha = \frac{6 - 6 + 36}{49} = \frac{36}{49} \quad\Rightarrow\quad \alpha = 42.7^\circ$$

For the shortest distance, take $P_1 = (1, -1, 0)$ and $P_2 = (2, 1, -1)$, so $\overrightarrow{P_1P_2} = (1, 2, -1)$, and $\mathbf{n} = \mathbf{d}_1\times\mathbf{d}_2 = (30, 6, -13)$ with $\left\|\mathbf{n}\right\| = \sqrt{1105} = 33.24$:

$$d = \frac{\left|\overrightarrow{P_1P_2}\cdot\mathbf{n}\right|}{\left\|\mathbf{n}\right\|} = \frac{\left|30 + 12 + 13\right|}{33.24} = 1.65$$

> **Answer.** Angle $42.7^\circ$; shortest distance 1.65 units.

## 8. Petroleum Engineering

### Question 1: The drainage volume

The flow domain is $0.1 \le r \le 300$ m, $0 \le \theta < 2\pi$, $0 \le z \le 20$ m.

$$V_{\text{bulk}} = \pi\left(300^2 - 0.1^2\right)(20) = 5.65\times 10^{6}\ \text{m}^3, \qquad V_{\text{pore}} = 0.25\,V_{\text{bulk}} = 1.41\times 10^{6}\ \text{m}^3$$

> **Answer.** Bulk volume $5.65\times10^6$ m³; pore volume $1.41\times10^6$ m³.

### Question 2: The directional well

The path is $\mathbf{r}(s) = s\,(600, 800, -2500)$ for $0 \le s \le 1$, or $\dfrac{x}{600} = \dfrac{y}{800} = \dfrac{z}{-2500}$.

$$L = \sqrt{600^2 + 800^2 + 2500^2} = 2692.6\ \text{m}, \qquad \text{inclination} = \tan^{-1}\frac{1000}{2500} = 21.8^\circ$$

Taking $y$ as north and $x$ as east, the azimuth is $\tan^{-1}(600/800) = 36.9^\circ$ (N36.9°E). In spherical coordinates ($\phi$ measured from the positive $z$-axis):

$$\rho = 2692.6\ \text{m}, \qquad \theta = \tan^{-1}\frac{800}{600} = 53.1^\circ, \qquad \phi = \cos^{-1}\frac{-2500}{2692.6} = 158.2^\circ$$

> **Answer.** Length 2692.6 m; inclination $21.8^\circ$; azimuth N36.9°E; $(\rho, \theta, \phi) = (2692.6\ \text{m},\ 53.1^\circ,\ 158.2^\circ)$.
