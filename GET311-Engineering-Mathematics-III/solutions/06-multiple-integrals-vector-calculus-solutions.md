# Topic 6 Solutions: Multiple Integrals and Vector Calculus

## 1. Agricultural Engineering

**Question 1: rainfall over the catchment**

∬ (10 + 2x + y) dA = ∫₀³ ∫₀² (10 + 2x + y) dx dy = ∫₀³ (20 + 4 + 2y) dy = 72 + 9 = **81 mm·km²/h**

Converting units, with 1 mm = 10⁻³ m and 1 km² = 10⁶ m²: **Q = 81 000 m³/h**.

The area is 6 km², so the average intensity is 81/6 = **13.5 mm/h**.

**Question 2: soil water flux**

Ignoring the common factor 10⁻⁶:
- ∇ · **q** = −2 − 2 + 4 = **0**. The flow is **incompressible**.
- ∇ × **q** = (∂(4z)/∂y − ∂(−2y)/∂z, …) = **(0, 0, 0)**. Each component depends only on its own variable, so the flow is **irrotational**.

Since the curl is zero, a potential exists with **q** = ∇φ:

**φ = (−x² − y² + 2z²) × 10⁻⁶**

Check: ∇²φ = 0, so this is valid potential flow.

## 2. Chemical Engineering

**Question 1: catalyst mass**

m = ∫₀² ∫₀^{2π} ∫₀^{0.5} 800(1 − 0.3r²) r dr dθ dz = 800 · 2π · 2 · [r²/2 − 0.075r⁴]₀^{0.5}

= 3200π (0.125 − 0.00469) = **1209.5 kg**

**Question 2: Poiseuille flow rate**

Q = ∬ **v** · **k** dA = ∫₀^{2π} ∫₀^R v_max(1 − r²/R²) r dr dθ = 2πv_max [R²/2 − R²/4] = **πR²v_max/2**

The mean velocity is Q/(πR²) = **v_max/2** ∎

## 3. Computer Engineering

**Question 1: the drone's helical path**

- **v** = **r**′ = (−10 sin t, 10 cos t, 2)
- Speed |**v**| = √(100 + 4) = **√104 ≈ 10.20 m/s**
- **a** = (−10 cos t, −10 sin t, 0), with magnitude 10 m/s², pointing towards the axis

Length = ∫₀^{2π} √104 dt = 2π√104 = **64.08 m**

```
function arc_length(r_prime, a, b, n):
    h = (b - a) / n
    s = 0.5 * (|r_prime(a)| + |r_prime(b)|)
    for i = 1..n-1: s += |r_prime(a + i*h)|
    return h * s
```

Because the speed is constant, the trapezoidal rule gives **64.08 m exactly** for any n. For a non-uniform path the error falls as h².

**Question 2: heat generated in the heat sink**

Q = ∫₀¹ ∫₀² ∫₀² (5xy + z) dx dy dz = 5(2)(2)(1) + (2)(2)(½) = 20 + 2 = **22 W**

As a Riemann sum (midpoint rule):

```
Q = 0
for i in 0..n-1: for j in 0..n-1: for k in 0..n-1:
    x = (i+0.5)*dx; y = (j+0.5)*dy; z = (k+0.5)*dz
    Q += (5*x*y + z) * dx*dy*dz
```

The integrand is linear in each variable separately, so the midpoint rule gives exactly 22.

## 4. Civil Engineering

**Question 1: centroid and second moment of the T-section**

- Web area: 2 × 4 = 8, centroid at y = 2.
- Flange area: 6 × 1 = 6, centroid at y = 4.5.

ȳ = ∬ y dA / A = (8·2 + 6·4.5)/14 = 43/14 = **3.071** above the base.

I_x about the centroid = Σ[bh³/12 + A d²]:
- Web: 2·4³/12 + 8(2 − 3.071)² = 10.667 + 9.180
- Flange: 6·1³/12 + 6(4.5 − 3.071)² = 0.5 + 12.245

**I_x = 1369/42 ≈ 32.6 units⁴**

**Question 2: work done by the crane force**

Path 1, the straight line **r** = t(1, 2, 3):

W = ∫₀¹ [2t·2t·1 + (t² + 3t)·2 + 2t·3] dt = ∫₀¹ (6t² + 12t) dt = 2 + 6 = **8 kJ**

Path 2, broken line (0,0,0) → (1,0,0) → (1,2,0) → (1,2,3):
- Leg 1: F_x = 0 along y = 0, so the work is 0.
- Leg 2: ∫₀² (1 + 0) dy = 2.
- Leg 3: ∫₀³ 2 dz = 6.

Total **W = 8 kJ**, the same as path 1.

∇ × **F** = (1 − 1, 0 − 0, 2x − 2x) = **0**, so **F** is conservative. Its potential is **φ = x²y + yz**, and W = φ(1, 2, 3) − φ(0, 0, 0) = 2 + 6 = 8 ✓

## 5. Electrical and Electronics Engineering

**Question 1: flux through the cylinder**

- On the curved side, **E** is parallel to **n** and |**E**| = λ/(2πε₀a). The area is 2πaL, so the flux is (λ/(2πε₀a)) · 2πaL = λL/ε₀.
- On the two flat ends, **E** is perpendicular to **n**, so the flux is 0.

Total flux = **λL/ε₀**. This is the enclosed charge divided by ε₀, as Gauss's law requires ∎

**Question 2: circulation of B**

On r = a, **B** · d**r** = (μ₀I/(2πa)) a dθ, so ∮ = ∫₀^{2π} μ₀I/(2π) dθ = **μ₀I** (Ampère's law).

For r ≠ 0, the curl in cylindrical coordinates is (1/r) ∂(rB_θ)/∂r **k** = (1/r) ∂(μ₀I/2π)/∂r **k** = **0**.

So the field is irrotational everywhere except on the wire, yet the circulation around the wire is not zero. The two results are consistent: the region without the wire is **not simply connected**, and all of the curl is concentrated on the wire (∇ × **B** = μ₀**J**).

## 6. Food Engineering

**Question 1: average temperature in the dome cake**

T = 180 − 60(1 − ρ/10) = 120 + 6ρ.

T_avg = ∭ T dV / ∭ dV. The angular integrals ∫₀^{2π}∫₀^{π/2} sin φ dφ dθ = 2π cancel, leaving

T_avg = ∫₀¹⁰ (120 + 6ρ)ρ² dρ / ∫₀¹⁰ ρ² dρ = (40 000 + 15 000)/(1000/3) = **165 °C**

**Question 2: air and moisture flow through the dryer opening**

The opening lies in a plane y = const with normal **j**, so only v_y counts:

Q = ∫₀¹ ∫₀^{0.5} (2 + x − z) dz dx = ∫₀¹ (1 + 0.5x − 0.125) dx = 0.875 + 0.25 = **1.125 m³/s**

Moisture removal = 1.125 × 0.012 = **0.0135 kg/s ≈ 48.6 kg/h**

## 7. Mechanical Engineering

**Question 1: moment of inertia of a solid cone**

Put the apex at the origin, so the radius at height z is az/h.

I_z = ρ ∫₀^h ∫₀^{2π} ∫₀^{az/h} r² · r dr dθ dz = ρ · 2π ∫₀^h (a⁴z⁴)/(4h⁴) dz = πρa⁴h/10

The mass is m = ρπa²h/3, so **I_z = (3/10) m a²**.

**Question 2: rigid-body rotation**

- ∇ · **v** = 0 + 0 = **0**, so the flow is incompressible.
- ∇ × **v** = (0, 0, ∂(−x)/∂x − ∂y/∂y) = **(0, 0, −2)**.

This is **rigid-body rotation**, clockwise seen from above, with angular velocity ω = ½|curl| = 1 rad/s.

Circulation around the unit circle, taken counter-clockwise with **r** = (cos t, sin t):

∮ **v** · d**r** = ∫₀^{2π} (sin t)(−sin t) + (−cos t)(cos t) dt = **−2π**

This agrees with Stokes: (−2)(π · 1²) = −2π.

## 8. Petroleum Engineering

**Question 1: bulk volume and oil in place**

The thickness at radius r is 0.001r², so

V_bulk = ∫₀^{2π} ∫₀^{500} 0.001 r² · r dr dθ = 0.001 · 2π · 500⁴/4 = **9.82 × 10⁷ m³**

Oil in place = φ S_o V = 0.2 × 0.75 × 9.82 × 10⁷ = **1.47 × 10⁷ m³** (about 92.6 million barrels)

**Question 2: Darcy flux across the square**

∇p = (−x, −0.6y), so **u** = −0.01∇p = **(0.01x, 0.006y)**.

Flux through each side of the square (length 200 m):
- x = ±100: u · n = 0.01(100) = 1, so each side gives 1 × 200 = 200.
- y = ±100: u · n = 0.006(100) = 0.6, so each side gives 0.6 × 200 = 120.

Net outward flux = 2(200) + 2(120) = **640 (m²/unit time per unit thickness)**.

Check with the divergence theorem: ∇ · **u** = 0.016, and 0.016 × 200² = 640 ✓. The positive value means this pressure field implies a net source, such as injection, inside the square.
