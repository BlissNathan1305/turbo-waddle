
from PIL import Image, ImageDraw
import random

# Set the dimensions of the wallpaper
width, height = 1080, 1920

# Define a list of colors
colors = [
    (255, 105, 97),  # Pastel pink
    (135, 206, 235),  # Sky blue
    (245, 222, 179),  # Light beige
    (255, 182, 193),  # Pastel peach
    (173, 255, 47),  # Pastel green
    (240, 230, 140),  # Light yellow
    (176, 196, 222),  # Soft blue
    (255, 160, 122),  # Pastel orange
    (218, 165, 32),  # Golden brown
    (135, 135, 206),  # Soft purple
]

# Generate 10 wallpapers
for i in range(10):
    # Create a new image
    img = Image.new('RGB', (width, height), colors[i])

    # Add some shapes to the image
    draw = ImageDraw.Draw(img)
    for _ in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(10, 100)
        shape_type = random.randint(1, 3)
        if shape_type == 1:
            draw.ellipse([(x, y), (x + size, y + size)], fill=(255, 255, 255, 128))
        elif shape_type == 2:
            draw.rectangle([(x, y), (x + size, y + size)], fill=(255, 255, 255, 128))
        else:
            draw.polygon([(x, y), (x + size, y), (x + size / 2, y + size)], fill=(255, 255, 255, 128))

    # Save the image
    img.save(f'wallpaper_{i+1}.png')
