# Topic 4: Analytical Geometry, Coordinate Transformation, Solid Geometry, and Polar, Cylindrical and Spherical Coordinates

[← Back to course overview](../README.md)

## Introduction

**Analytical geometry** describes geometric objects with algebraic equations. In the plane this means straight lines, circles and the conic sections (parabola, ellipse, hyperbola), which all come from the general second-degree equation ax² + 2hxy + by² + 2gx + 2fy + c = 0.

**Coordinate transformation** changes the reference frame:

- *translation* moves the origin: x = X + h, y = Y + k;
- *rotation* turns the axes through θ: x = X cos θ − Y sin θ, y = X sin θ + Y cos θ. Choosing tan 2θ = 2h/(a − b) removes the xy term, which reduces a conic to standard form.

**Solid (3-D) geometry** covers direction cosines and ratios, the equations of lines and planes, the angle between planes, the distance from a point to a plane, and quadric surfaces (sphere, cylinder, cone, ellipsoid, paraboloid, hyperboloid).

**Curvilinear coordinate systems** make problems with symmetry much simpler:

| System | Coordinates | Relation to Cartesian | Volume element |
|--------|-------------|-----------------------|----------------|
| Polar (2-D) | (r, θ) | x = r cos θ, y = r sin θ | dA = r dr dθ |
| Cylindrical | (r, θ, z) | x = r cos θ, y = r sin θ, z = z | dV = r dr dθ dz |
| Spherical | (ρ, θ, φ) | x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ | dV = ρ² sin φ dρ dθ dφ |

Cylindrical coordinates suit pipes, shafts and wells. Spherical coordinates suit tanks, antennas and radial flow.

---

## Application Questions

### 1. Agricultural Engineering

1. A centre-pivot irrigation system covers a circle of radius 400 m centred at (500, 300) m in the farm's coordinate grid. Write the equation of the irrigated boundary, convert it to polar coordinates centred at the pivot, and find the irrigated area.
2. A grain silo is a cylinder of radius 3 m and height 10 m with a conical roof of height 2 m. Write the equations of both surfaces in cylindrical coordinates, and find the total storage volume.

### 2. Chemical Engineering

1. A spherical catalyst pellet of radius R = 5 mm has a reactant concentration C(ρ) that depends only on the radial distance. Write the position of a point on the pellet surface in spherical coordinates, and explain why spherical coordinates reduce the 3-D diffusion problem to one variable.
2. The cross-section of an elliptical storage tank is 9x² + 4y² − 36x + 24y + 36 = 0. Use a translation of axes to reduce it to standard form, and find the centre, semi-axes and cross-sectional area.

### 3. Computer Engineering

1. A robot arm's end-effector is located by (r, θ, z) = (0.8 m, 60°, 0.5 m) in cylindrical coordinates. Convert this to Cartesian coordinates, and write a function (pseudocode) that converts between Cartesian, cylindrical and spherical coordinates in both directions.
2. A lidar sensor reports a point at range ρ = 20 m, azimuth θ = 45° and elevation angle 30° (so the polar angle is φ = 60°). Convert it to Cartesian coordinates, then find the distance from the point to the ground plane z = 0 and to the plane x + y + z = 10.

### 4. Civil Engineering

1. A road designer needs the equation of the plane that contains the points A(0, 0, 100), B(200, 0, 104) and C(0, 150, 97) (metres) on a graded embankment. Find the plane equation, the direction cosines of its normal, and the angle it makes with the horizontal.
2. The profile of a parabolic arch bridge passes through (−30, 0), (30, 0) and (0, 15) m. Find its equation. Rotate the axes by 10° to model an inclined abutment, and write the transformed equation.

### 5. Electrical and Electronics Engineering

1. The radiation pattern of a dipole antenna is proportional to sin φ in spherical coordinates. Convert the pattern surface ρ = sin φ to Cartesian form, identify it, and sketch it.
2. A coaxial cable has an inner conductor of radius a = 1 mm and an outer conductor of radius b = 4 mm. Describe the dielectric region with inequalities in cylindrical coordinates, and find the cross-sectional area of the dielectric using polar coordinates.

### 6. Food Engineering

1. A cylindrical can with radius 4 cm and height 11 cm is heated during sterilisation. The slowest-heating point is on the axis at mid-height. Give its cylindrical coordinates relative to the centre of the base, and find its distance from the rim edge.
2. An egg is approximated by the ellipsoid x²/4 + y²/4 + z²/9 = 1 (cm). Find its volume, and use a coordinate transformation (stretching) to map it onto a unit sphere. Explain why this simplifies heat-transfer analysis.

### 7. Mechanical Engineering

1. A cam profile is given in polar form by r = 40 + 10 cos θ (mm). Convert it to Cartesian form, find the maximum and minimum radius (the follower lift), and find the area enclosed by the profile.
2. Two machine members lie along the lines (x − 1)/2 = (y + 1)/3 = z/6 and (x − 2)/3 = (y − 1)/(−2) = (z + 1)/6. Find the angle between them and the shortest distance between the lines.

### 8. Petroleum Engineering

1. Radial flow into a vertical well is analysed in cylindrical coordinates. The drainage area is a circle of radius rₑ = 300 m around a well of radius r_w = 0.1 m. Write the flow domain in cylindrical coordinates, and find the volume of a reservoir 20 m thick with 25 % porosity.
2. A directional well leaves the surface at (0, 0, 0) and reaches a target at (600, 800, −2500) m. Find the equation of the straight well path, its inclination from the vertical, and its azimuth. Express the target in spherical coordinates.
