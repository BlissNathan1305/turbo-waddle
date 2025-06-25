
from PIL import Image, ImageDraw
import random

def random_color():
    # Soft random pastel colors
    base = 100
    return tuple(random.randint(base, 255) for _ in range(3))

def generate_abstract_wallpaper(width=1920, height=1080, polygon_count=50):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Background gradient
    for y in range(height):
        t = y / height
        r = int(255 * (1 - t) + 50 * t)
        g = int(200 * (1 - t) + 50 * t)
        b = int(255 * (1 - t) + 100 * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Draw random polygons
    for _ in range(polygon_count):
        points = [(random.randint(0, width), random.randint(0, height)) for _ in range(random.randint(3, 6))]
        color = random_color()
        draw.polygon(points, fill=color + (random.randint(100, 200),) if img.mode == 'RGBA' else color)

    return img

def main():
    for i in range(1, 7):
        wallpaper = generate_abstract_wallpaper()
        wallpaper.save(f"abstract_wallpaper_{i}.png")
        print(f"Saved abstract_wallpaper_{i}.png")

if __name__ == "__main__":
    main()

