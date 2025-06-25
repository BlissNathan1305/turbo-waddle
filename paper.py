
from PIL import Image, ImageDraw
import random

def pastel_color():
    base = 200
    return tuple(random.randint(base, 255) for _ in range(3))

def draw_diagonal_lines(img, line_count=400):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for _ in range(line_count):
        color = pastel_color()
        # Random start and end points for diagonal lines
        x0 = random.randint(0, w)
        y0 = random.randint(0, h)
        # Diagonal direction
        x1 = x0 + random.randint(200, 600)
        y1 = y0 + random.randint(200, 600)
        draw.line((x0, y0, x1, y1), fill=color, width=1)

def generate_wallpapers(num=3, size=(1920, 1080)):
    for i in range(1, num + 1):
        img = Image.new("RGB", size, "white")
        draw_diagonal_lines(img, line_count=600)
        img.save(f"wallpaper_{i}.png")
        print(f"Saved wallpaper_{i}.png")

if __name__ == "__main__":
    generate_wallpapers(num=3)

