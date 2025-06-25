
from PIL import Image, ImageDraw
import random
import math
import os

# Set up dimensions
width, height = 1080, 1920
output_dir = "wallpapers"
os.makedirs(output_dir, exist_ok=True)

def save_wallpaper(image, index):
    filename = f"{output_dir}/wallpaper_{index + 1}.png"
    image.save(filename)
    print(f"Saved: {filename}")

# 1. Radial Gradient Dream
def radial_gradient():
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)
    for _ in range(6):
        center = (random.randint(0, width), random.randint(0, height))
        max_radius = random.randint(300, 800)
        for r in range(max_radius, 0, -1):
            color = (
                int(255 * r / max_radius),
                int(128 + 127 * math.sin(r / 20.0)),
                int(255 * (1 - r / max_radius))
            )
            draw.ellipse([
                (center[0] - r, center[1] - r),
                (center[0] + r, center[1] + r)
            ], fill=color)
    return image

# 2. Pastel Stripes
def pastel_stripes():
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    for y in range(0, height, 100):
        color = tuple(random.randint(150, 255) for _ in range(3))
        draw.rectangle([0, y, width, y + 100], fill=color)
    return image

# 3. Geometric Mosaic
def geometric_mosaic():
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    for _ in range(500):
        size = random.randint(50, 150)
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = tuple(random.randint(50, 255) for _ in range(3))
        draw.polygon([
            (x, y),
            (x + size, y),
            (x + size // 2, y + size)
        ], fill=color)
    return image

# 4. Diagonal Blend
def diagonal_blend():
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = int(255 - ((x + y) / (width + height)) * 255)
            pixels[x, y] = (r, g, b)
    return image

# 5. Soft Circles
def soft_circles():
    image = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(image)
    for _ in range(100):
        radius = random.randint(30, 100)
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = tuple(random.randint(100, 255) for _ in range(3))
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)
    return image

# Generate and save all five
wallpapers = [radial_gradient, pastel_stripes, geometric_mosaic, diagonal_blend, soft_circles]
for idx, generator in enumerate(wallpapers):
    save_wallpaper(generator(), idx)
