# Topic 7 Solutions: Integral Theorems and Multivalued Functions

## 1. Agricultural Engineering

**Question 1: field area by Green's theorem**

With x = 300 cos t and y = 200 sin t:
- dx = −300 sin t dt
- dy = 200 cos t dt

A = ½∮(x dy − y dx) = ½∫₀^{2π} [60 000 cos²t + 60 000 sin²t] dt = ½(60 000)(2π) = **60 000π ≈ 188 496 m² (18.85 ha)**

For GPS points (x₁, y₁), …, (xₙ, yₙ), treat the boundary as straight segments. The same line integral then becomes the **shoelace formula** A = ½|Σ(xᵢyᵢ₊₁ − xᵢ₊₁yᵢ)|, which is what handheld area meters compute.

**Question 2: checking the divergence theorem**

Volume integral: ∇ · **q** = 2x + 2y + 2z, so ∭(2x + 2y + 2z) dV = 1 + 1 + 1 = **3**.

Surface integral:
- On x = 1, q · n = 1² = 1, which integrates to 1.
- On x = 0, q · n = −0 = 0.
- The y and z faces work the same way.

The total is 1 + 1 + 1 = **3** ✓

## 2. Chemical Engineering

**Question 1: deriving the continuity equation**

Mass balance on a fixed control volume V: the rate of increase of mass equals the net inflow.

d/dt ∭_V ρ dV = −∯_S ρv · n dS

By the divergence theorem, ∯_S ρv · n dS = ∭_V ∇ · (ρv) dV. Since V is fixed:

∭_V [∂ρ/∂t + ∇ · (ρv)] dV = 0

This holds for *every* V, so the integrand must be zero everywhere:

**∂ρ/∂t + ∇ · (ρv) = 0** ∎

**Question 2: values of z^{2/3} at 8i**

z = 8i = 8e^{i(π/2 + 2kπ)}, so w = 8^{2/3} e^{i(2/3)(π/2 + 2kπ)} = 4e^{i(π/3 + 4kπ/3)}:
- k = 0: 4e^{iπ/3} = **2 + 2√3 i** (the principal value)
- k = 1: 4e^{i5π/3} = **2 − 2√3 i**
- k = 2: 4e^{i3π} = **−4**

The **branch point is z = 0** (and z = ∞).

For a channel in the upper half-plane, place the **branch cut along the negative imaginary axis**, taking −π/2 < arg z < 3π/2. The whole flow region then has no cut in it, and w is single-valued and continuous there.

## 3. Computer Engineering

**Question 1: the shoelace formula**

On the straight edge from (xᵢ, yᵢ) to (xᵢ₊₁, yᵢ₊₁), parametrise x = xᵢ + tΔx and y = yᵢ + tΔy for 0 ≤ t ≤ 1. Then

∫(x dy − y dx) = ∫₀¹ [(xᵢ + tΔx)Δy − (yᵢ + tΔy)Δx] dt = xᵢΔy − yᵢΔx = xᵢyᵢ₊₁ − xᵢ₊₁yᵢ.

Summing over the edges gives **A = ½ Σ (xᵢyᵢ₊₁ − xᵢ₊₁yᵢ)** ∎

For the vertices (0,0), (4,0), (4,3), (2,5), (0,3), the terms are 0, 12, 14, 6 and 0, so the sum is 32 and **A = 16 square units**.

```
function polygon_area(xs, ys):
    n = len(xs); s = 0
    for i in 0..n-1:
        j = (i + 1) mod n
        s += xs[i]*ys[j] - xs[j]*ys[i]
    return abs(s) / 2
```

**Question 2: atan2 and phase unwrapping**

arg z = θ + 2kπ for any integer k, so it has infinitely many values. atan2 always returns the principal value in (−π, π].

As a point goes once round the origin counter-clockwise, the true angle rises steadily from 0 to 2π. atan2, however, rises to π and then **jumps to −π** when the point crosses the negative real axis, which is the branch cut.

**Phase unwrapping** removes these jumps. If two consecutive samples differ by more than π, add or subtract 2π from every later sample:

```
for i = 1..n-1:
    d = phase[i] - phase[i-1]
    if d >  π: offset -= 2π
    if d < -π: offset += 2π
    unwrapped[i] = phase[i] + offset
```

## 4. Civil Engineering

**Question 1: area and centroid of the slab section**

The curves meet at x = 0 and x = 2. Going round counter-clockwise, along y = x² from (0, 0) to (2, 4) and back along y = 2x:

- A = ½∮(x dy − y dx) = ½[∫₀² (2x² − x²) dx + ∫₂⁰ (2x − 2x) dx] = ½(8/3) = **4/3 m²**
- x̄ = (1/A)∮ ½x² dy = **1 m**
- ȳ = (1/A)∮ (−½y²) dx = **8/5 = 1.6 m**

Direct check: A = ∫₀² (2x − x²) dx = 4 − 8/3 = 4/3 ✓, and x̄ = (1/A)∫₀² x(2x − x²) dx = (4/3)/(4/3) = 1 ✓

**Question 2: seepage under the dam**

∇ · **q** = 2 + 3 − 5 = **0**. The field is consistent with an incompressible soil and no sources or sinks.

By the divergence theorem, the net outflow from the unit cube is ∭ 0 dV = **0**. Whatever flows in, flows out.

## 5. Electrical and Electronics Engineering

**Question 1: Ampère's law in differential form**

∮_C **H** · d**r** = I_enc = ∬_S **J** · **n** dS. By Stokes' theorem the left side equals ∬_S (∇ × **H**) · **n** dS.

So ∬_S (∇ × **H** − **J**) · **n** dS = 0 for every surface S. Hence **∇ × H = J** ∎

Inside the conductor (r < a), the current density is uniform. A circle of radius r encloses I r²/a². Then H · 2πr = I r²/a², so

**H = Ir/(2πa²)** in the θ̂ direction. It rises linearly to I/(2πa) at the surface.

**Question 2: log(−1 + i√3)**

|z| = 2 and arg z = 2π/3 + 2kπ, so **log z = ln 2 + i(2π/3 + 2kπ)** for k = 0, ±1, …

Principal value: **Log z = 0.693 + 2.094i**.

The principal branch gives phase angles only in (−180°, 180°]. A phase of 240° is reported as −120°. When a phase is tracked continuously, for example in a PLL or when measuring the phase shift through a filter, you must stay on one branch and unwrap, not rely on the principal value.

## 6. Food Engineering

**Question 1: heat balance for the can**

Energy balance on the can volume V with surface S:

∭_V ρc_p ∂T/∂t dV = rate of heat in = −∯_S **q** · **n** dS = ∯_S k∇T · **n** dS

By the divergence theorem, the right side is ∭_V ∇ · (k∇T) dV. So

∭_V [ρc_p ∂T/∂t − ∇ · (k∇T)] dV = 0

This holds for any sub-volume, so ρc_p ∂T/∂t = ∇ · (k∇T). For constant k this is the heat equation, **∂T/∂t = α∇²T** ∎

**Question 2: circulation round the bowl rim**

∇ × **v** = (0, 0, 2). On the flat disc with **n** = **k**:

∬ (∇ × **v**) · **k** dS = 2 × π(0.15)² = **0.045π ≈ 0.141 m²/s**

Direct check: **r** = (0.15 cos t, 0.15 sin t, 0.1), so **v** · d**r** = (0.15)²(sin²t + cos²t) dt. Then ∮ = 0.0225 × 2π = 0.045π ✓

## 7. Mechanical Engineering

**Question 1: work round the triangle**

∇ × **F** = (∂(x + y)/∂y − ∂(z + x)/∂z, ∂(y + z)/∂z − ∂(x + y)/∂x, ∂(z + x)/∂x − ∂(y + z)/∂y) = (0, 0, 0)

By Stokes' theorem, W = ∬ (∇ × **F**) · **n** dS = **0**.

**F** is conservative, with φ = xy + yz + zx. The work done round *any* closed path is zero, and the work between two points does not depend on the path.

**Question 2: flow round the re-entrant corner**

- **Branch point: z = 0**, the corner. The other branch point is at infinity.
- **Branch cut**: along the ray bisecting the solid wall region outside the 3π/2 flow sector, so the flow domain contains no cut.

At z = 1 = e^{i2kπ}, the values are w = e^{i4kπ/3}:
- k = 0: **1** (principal)
- k = 1: **e^{i4π/3} = −½ − (√3/2)i**
- k = 2: **e^{i2π/3} = −½ + (√3/2)i**

The velocity is dw/dz = (2/3)z^{−1/3}, with |dw/dz| = (2/3)|z|^{−1/3} → ∞ as z → 0. The flow cannot turn a sharp convex corner smoothly, so the velocity becomes infinite there. In a real fluid, viscosity produces **flow separation** at such corners.

## 8. Petroleum Engineering

**Question 1: flux with and without a well**

With no wells, ∇ · **u** = 0 everywhere in V. By the divergence theorem, ∯_S **u** · **n** dS = ∭_V ∇ · **u** dV = **0**. The net flux through any closed surface is zero.

With a producing well of rate q inside V, the well is a point (or line) sink, and ∇ · **u** = −q δ(**r** − **r**_w). Then

∯_S **u** · **n** dS = −q

The net *inflow* through any closed surface around the well equals the production rate q, whatever the shape of the surface. This is the basis of the well boundary condition 2πr h u_r = −q at r = r_w.

**Question 2: the multivalued stream function**

w = (q/2π)(ln r + iθ), so ψ = Im w = **(q/2π)θ**.

θ increases by 2π on each circuit, so **ψ increases by q** each time round the well. ψ is therefore multivalued, with its branch point at the well.

The difference in ψ between two streamlines equals the volumetric flow between them. A jump of exactly q on going once round means the **total flow crossing any closed curve around the well equals the well's production rate q** (per unit thickness).
