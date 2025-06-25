
from PIL import Image, ImageDraw
import random

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def draw_gradient(img, top_color, bottom_color):
    w, h = img.size
    for y in range(h):
        t = y / h
        color = lerp_color(top_color, bottom_color, t)
        ImageDraw.Draw(img).line([(0, y), (w, y)], fill=color)

def generate_terrain_layer(w, h, base_y, amplitude, color, roughness=0.005):
    points = []
    for x in range(w + 1):
        y = base_y + int(amplitude * random.uniform(-1, 1) * (random.random() ** roughness))
        points.append((x, y))
    points += [(w, h), (0, h)]
    return points, color

def main():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # Draw sky gradient
    draw_gradient(img, (135, 206, 250), (255, 223, 186))  # Light blue to soft orange

    # Draw terrain layers
    layers = [
        (h - 350, 80, (34, 139, 34)),    # Distant green hills
        (h - 250, 120, (60, 179, 113)),  # Mid green hills
        (h - 120, 160, (205, 133, 63)),  # Foreground brown hills
    ]
    for base_y, amplitude, color in layers:
        points, fill_color = generate_terrain_layer(w, h, base_y, amplitude, color)
        ImageDraw.Draw(img).polygon(points, fill=fill_color)

    img.save("terrain_wallpaper.png")
    print("Saved terrain_wallpaper.png")

if __name__ == "__main__":
    main()

