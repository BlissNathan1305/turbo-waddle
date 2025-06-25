
from PIL import Image, ImageDraw, ImageFont
import random

# === CONFIGURABLE SETTINGS ===
WIDTH, HEIGHT = 1080, 1920  # Standard Full HD wallpaper size
TEXT = "Jesus is Lord"
FONT_SIZE = 120
TEXT_COLOR = (255, 255, 255)
OUTPUT_FILE = "custom_wallpaper.jpg"
USE_RANDOM_COLORS = False  # Set True for random gradient colors

def create_gradient_background(width, height, start_color, end_color):
    """Create a vertical gradient from start_color to end_color"""
    img = Image.new("RGB", (width, height), start_color)
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * y / height)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * y / height)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def add_centered_text(img, text, font_path=None, font_size=100, color=(255, 255, 255)):
    """Add centered text to the image"""
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype(font_path or "arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Use textbbox instead of textsize for accurate measurement
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2
    draw.text((x, y), text, fill=color, font=font)

def main():
    # Generate random or fixed colors
    if USE_RANDOM_COLORS:
        start_color = tuple(random.randint(0, 255) for _ in range(3))
        end_color = tuple(random.randint(0, 255) for _ in range(3))
    else:
        start_color = (0, 0, 128)      # Navy Blue
        end_color = (255, 140, 0)      # Orange

    # Create image
    img = create_gradient_background(WIDTH, HEIGHT, start_color, end_color)
    
    # Add custom text
    add_centered_text(img, TEXT, font_size=FONT_SIZE, color=TEXT_COLOR)
    
    # Save wallpaper
    img.save(OUTPUT_FILE)
    print(f"Wallpaper saved as '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
