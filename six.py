
from PIL import Image, ImageDraw
import random

def random_pastel_color():
    base = 150
    return tuple(random.randint(base, 255) for _ in range(3))

def generate_abstract_wallpaper(width=1080, height=1920, polygon_count=60):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Create vertical gradient background (blue to pinkish)
    for y in range(height):
        t = y / height
        r = int(255 * t + 100 * (1 - t))
        g = int(100 * (1 - t))
        b = int(255 * (1 - t) + 150 * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Draw random polygons with pastel colors
    for _ in range(polygon_count):
        points = [(random.randint(0, width), random.randint(0, height)) for _ in range(random.randint(3, 6))]
        color = random_pastel_color()
        draw.polygon(points, fill=color)

    return img

def main():
    for i in range(1, 7):
        wallpaper = generate_abstract_wallpaper()
        wallpaper.save(f"abstract_mobile_wallpaper_{i}.png")
        print(f"Saved abstract_mobile_wallpaper_{i}.png")

if __name__ == "__main__":
    main()

