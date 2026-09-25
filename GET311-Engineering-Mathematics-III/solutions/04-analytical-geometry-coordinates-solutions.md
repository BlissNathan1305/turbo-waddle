# Topic 4 Solutions: Analytical Geometry and Coordinate Systems

## 1. Agricultural Engineering

**Question 1: centre-pivot boundary**

- Cartesian: **(x − 500)² + (y − 300)² = 400²**.
- Translate the origin to the pivot: X = x − 500, Y = y − 300, so X² + Y² = 160 000.
- In polar coordinates about the pivot (X = r cos θ, Y = r sin θ) this becomes **r = 400**.

Area = ∫₀^{2π}∫₀^{400} r dr dθ = π(400)² = **502 655 m² ≈ 50.3 ha**

**Question 2: the silo**

In cylindrical coordinates (r, θ, z):
- Cylinder wall: **r = 3, 0 ≤ z ≤ 10**.
- Conical roof: it rises from z = 10 at r = 3 to z = 12 at r = 0, so **z = 12 − (2/3)r, 0 ≤ r ≤ 3**.

Volume = πr²h (cylinder) + ⅓πr²h (cone) = π(9)(10) + ⅓π(9)(2) = 90π + 6π = **96π ≈ 301.6 m³**

## 2. Chemical Engineering

**Question 1: the spherical catalyst pellet**

A point on the surface is (ρ, θ, φ) = (5 mm, θ, φ), for any 0 ≤ θ < 2π and 0 ≤ φ ≤ π. In Cartesian form that is x = 5 sin φ cos θ, y = 5 sin φ sin θ, z = 5 cos φ.

If C depends only on ρ, then ∂C/∂θ = ∂C/∂φ = 0. The Laplacian in spherical coordinates then reduces to

∇²C = (1/ρ²) d/dρ (ρ² dC/dρ).

So the 3-D diffusion–reaction PDE becomes **one ordinary differential equation in ρ**. In Cartesian coordinates the same problem would need all three variables together.

**Question 2: the elliptical tank**

Complete the squares:

9(x² − 4x) + 4(y² + 6y) + 36 = 0 ⇒ 9(x − 2)² − 36 + 4(y + 3)² − 36 + 36 = 0 ⇒ 9(x − 2)² + 4(y + 3)² = 36

Translate with X = x − 2 and Y = y + 3:

**X²/4 + Y²/9 = 1**

- **Centre: (2, −3).**
- **Semi-axes: a = 2 (along x) and b = 3 (along y).**
- **Area = πab = 6π ≈ 18.85 square units.**

## 3. Computer Engineering

**Question 1: robot arm position**

- x = 0.8 cos 60° = **0.400 m**
- y = 0.8 sin 60° = **0.693 m**
- z = **0.5 m**

```
cart_to_cyl(x,y,z):  return (sqrt(x²+y²), atan2(y,x), z)
cyl_to_cart(r,θ,z):  return (r cos θ, r sin θ, z)
cart_to_sph(x,y,z):  ρ = sqrt(x²+y²+z²); return (ρ, atan2(y,x), acos(z/ρ))
sph_to_cart(ρ,θ,φ):  return (ρ sin φ cos θ, ρ sin φ sin θ, ρ cos φ)
cyl_to_sph(r,θ,z):   return (sqrt(r²+z²), θ, atan2(r, z))
sph_to_cyl(ρ,θ,φ):   return (ρ sin φ, θ, ρ cos φ)
```

Use atan2, not atan, so that the angle ends up in the correct quadrant.

**Question 2: the lidar point**

With ρ = 20, θ = 45° and φ = 60°:
- x = 20 sin 60° cos 45° = **12.25 m**
- y = **12.25 m**
- z = 20 cos 60° = **10 m**

Distances:
- To the plane z = 0: **10 m**.
- To the plane x + y + z = 10: |12.25 + 12.25 + 10 − 10|/√3 = 24.49/√3 = **14.14 m**.

## 4. Civil Engineering

**Question 1: the embankment plane**

- **AB** = (200, 0, 4) and **AC** = (0, 150, −3).
- The normal is **n** = **AB** × **AC** = (0·(−3) − 4·150, 4·0 − 200·(−3), 200·150) = (−600, 600, 30 000). Dividing by 600 gives (−1, 1, 50).

Plane: −x + y + 50z = 5000, or **z = 100 + (x − y)/50**. It passes through A, B and C.

Direction cosines of the normal: (−1, 1, 50)/√2502 = **(−0.0200, 0.0200, 0.9996)**.

The angle with the horizontal equals the angle between the normal and the z-axis: cos⁻¹(0.9996) = **1.62°**.

**Question 2: the parabolic arch**

The arch is symmetric with its vertex at (0, 15), so y = 15 − kx². At (30, 0): 0 = 15 − 900k, so k = 1/60.

**y = 15 − x²/60**

Rotate the axes by α = 10° using x = X cos α − Y sin α and y = X sin α + Y cos α, with cos 10° = 0.9848 and sin 10° = 0.1736:

**0.1736X + 0.9848Y = 15 − (0.9848X − 0.1736Y)²/60**

Expanded, this contains an XY term. That is expected: in the rotated frame the parabola's axis is no longer parallel to a coordinate axis.

## 5. Electrical and Electronics Engineering

**Question 1: the dipole pattern surface**

Multiply ρ = sin φ by ρ to get ρ² = ρ sin φ. Since ρ sin φ = √(x² + y²):

**x² + y² + z² = √(x² + y²)**

In any plane through the z-axis, with r = √(x² + y²), this is (r − ½)² + z² = ¼. That is a circle of radius ½ centred at r = ½, touching the axis. Revolving it about the z-axis gives a **horn torus**, a doughnut with no hole. It shows that a dipole radiates most strongly broadside (φ = 90°) and not at all along its own axis.

**Question 2: the coaxial dielectric**

The dielectric region is **1 mm ≤ r ≤ 4 mm, 0 ≤ θ < 2π, with z unrestricted** (along the cable).

Area = ∫₀^{2π}∫₁⁴ r dr dθ = 2π · (16 − 1)/2 = **15π ≈ 47.1 mm²**

## 6. Food Engineering

**Question 1: slowest-heating point in the can**

On the axis at mid-height means **(r, θ, z) = (0, any θ, 5.5 cm)**. The angle is undefined on the axis.

The rim edges are at r = 4 and z = 0 or 11. The distance is √(4² + 5.5²) = √46.25 = **6.80 cm**.

**Question 2: the egg**

Semi-axes are a = b = 2 cm and c = 3 cm.

V = (4/3)πabc = (4/3)π(2)(2)(3) = **16π ≈ 50.3 cm³**

The stretching X = x/2, Y = y/2, Z = z/3 maps the ellipsoid onto the **unit sphere X² + Y² + Z² = 1**. The Jacobian is abc = 12, so V = 12 × (4/3)π ✓.

Why this helps: on a sphere, heat conduction with uniform surface conditions depends only on the radius. The PDE reduces to a 1-D problem with standard series solutions. Those can then be mapped back, or used as a shape-factor approximation, for the egg.

## 7. Mechanical Engineering

**Question 1: the cam profile**

Multiply r = 40 + 10 cos θ by r to get r² = 40r + 10r cos θ. In Cartesian form:

**x² + y² = 40√(x² + y²) + 10x** (a limaçon)

- r_max = 50 mm at θ = 0, and r_min = 30 mm at θ = π.
- The **follower lift is 20 mm**.

Area = ½∫₀^{2π} (40 + 10 cos θ)² dθ = ½[1600(2π) + 0 + 100π] = **1650π ≈ 5184 mm²**

**Question 2: the two machine members**

- Directions: **d₁** = (2, 3, 6) and **d₂** = (3, −2, 6). Both have length 7.
- cos α = (6 − 6 + 36)/49 = 36/49, so **α = 42.7°**.

Shortest distance:
- Points on the lines: P₁ = (1, −1, 0) and P₂ = (2, 1, −1), so **P₁P₂** = (1, 2, −1).
- **n** = **d₁** × **d₂** = (30, 6, −13), with |**n**| = √1105 = 33.24.
- Distance = |**P₁P₂** · **n**|/|**n**| = |30 + 12 + 13|/33.24 = **1.65 units**.

## 8. Petroleum Engineering

**Question 1: the drainage volume**

The flow domain is **0.1 m ≤ r ≤ 300 m, 0 ≤ θ < 2π, 0 ≤ z ≤ 20 m**.

- Bulk volume = π(300² − 0.1²)(20) = **5.65 × 10⁶ m³**.
- Pore volume = 0.25 × 5.65 × 10⁶ = **1.41 × 10⁶ m³**.

**Question 2: the directional well**

The path is **r**(s) = s(600, 800, −2500) for 0 ≤ s ≤ 1, or equivalently x/600 = y/800 = z/(−2500).

- Measured length = √(600² + 800² + 2500²) = **2692.6 m**.
- The horizontal displacement is 1000 m, so the **inclination from vertical** is tan⁻¹(1000/2500) = **21.8°**.
- Taking y as north and x as east, the **azimuth** is tan⁻¹(600/800) = **36.9°** (N36.9°E).

In spherical coordinates (φ measured from +z): **ρ = 2692.6 m, θ = tan⁻¹(800/600) = 53.1° from the +x-axis, φ = cos⁻¹(−2500/2692.6) = 158.2°**.
