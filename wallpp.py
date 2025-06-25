import numpy as np
from PIL import Image, ImageDraw
import os

# Create output folder
os.makedirs("wallpapers", exist_ok=True)

WIDTH, HEIGHT = 1080, 1920

# Define 10 terrain styles with background + layer colors
terrains = [
    {"name": "Mountains at Sunset", "bg": "#ff9966", "layers": ["#663300", "#996633", "#cc9966"]},
    {"name": "Ocean Waves", "bg": "#3366cc", "layers": ["#003366", "#005599", "#0077bb"]},
    {"name": "Rolling Hills", "bg": "#99cc66", "layers": ["#336633", "#669933", "#99cc33"]},
    {"name": "Desert Dunes", "bg": "#ffcc99", "layers": ["#cc9966", "#e6b877", "#f2c888"]},
    {"name": "Forest Canopy", "bg": "#228822", "layers": ["#114411", "#226622", "#449944"]},
    {"name": "Snowy Peaks", "bg": "#dce3f0", "layers": ["#aabbee", "#ddeeff", "#ffffff"]},
    {"name": "River Valley", "bg": "#88ccee", "layers": ["#446688", "#6699aa", "#88bbcc"]},
    {"name": "Savannah Plains", "bg": "#ffe066", "layers": ["#cc9933", "#ffaa33", "#ffcc66"]},
    {"name": "Rocky Cliff", "bg": "#999999", "layers": ["#444444", "#666666", "#888888"]},
    {"name": "Rainy Jungle", "bg": "#335555", "layers": ["#113333", "#225544", "#337766"]},
]

def draw_layered_terrain(draw, layer_colors, height, layer_count=4):
    for i, color in enumerate(reversed(layer_colors)):
        y_offset = int(height * 0.3 * i / len(layer_colors))
        points = [(0, height), *generate_wavy_line(WIDTH, height - y_offset, amplitude=40 + i*10, frequency=0.005 * (i+1)), (WIDTH, height)]
        draw.polygon(points, fill=color)

def generate_wavy_line(width, y_base, amplitude=50, frequency=0.01):
    return [(x, y_base + np.sin(x * frequency) * amplitude) for x in range(0, width, 5)]

# Generate each wallpaper
for idx, terrain in enumerate(terrains, start=1):
    img = Image.new("RGB", (WIDTH, HEIGHT), terrain["bg"])
    draw = ImageDraw.Draw(img)

    # Add terrain layers
    draw_layered_terrain(draw, terrain["layers"], HEIGHT)

    # Optional: Add title
    # draw.text((40, 50), terrain["name"], fill="white")

    # Save
    filename = f"wallpapers/wallpaper_{idx:02d}_{terrain['name'].replace(' ', '_')}.png"
    img.save(filename)

print("✅ 10 terrain wallpapers generated in the 'wallpapers/' folder.")
