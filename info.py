
from PIL import Image, ImageDraw, ImageFont

# Set wallpaper size (mobile-friendly)
WIDTH, HEIGHT = 1080, 1920
BACKGROUND_COLOR = "#1e1e2f"
TEXT_COLOR = "white"
BAR_COLOR = "#4CAF50"

# Sample data for the infographic (labels and values)
data = {
    "Python": 90,
    "JavaScript": 75,
    "C++": 60,
    "Java": 55,
    "Go": 40,
}

# Create image
img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(img)

# Load fonts
try:
    font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 80)
    font_label = ImageFont.truetype("DejaVuSans.ttf", 50)
except:
    font_title = font_label = ImageFont.load_default()

# Draw title
title = "Programming Language Popularity"
bbox = font_title.getbbox(title)
title_w = bbox[2] - bbox[0]
title_h = bbox[3] - bbox[1]
draw.text(((WIDTH - title_w) // 2, 100), title, fill=TEXT_COLOR, font=font_title)

# Draw bars
start_y = 300
bar_height = 80
bar_spacing = 50
max_value = max(data.values())

for i, (label, value) in enumerate(data.items()):
    y = start_y + i * (bar_height + bar_spacing)

    # Draw label
    draw.text((100, y), label, fill=TEXT_COLOR, font=font_label)

    # Calculate bar width
    bar_width = int((value / max_value) * 700)
    draw.rectangle(
        [(300, y), (300 + bar_width, y + bar_height)],
        fill=BAR_COLOR
    )

    # Draw value
    value_text = f"{value}%"
    value_bbox = font_label.getbbox(value_text)
    value_w = value_bbox[2] - value_bbox[0]
    draw.text((320 + bar_width, y), value_text, fill=TEXT_COLOR, font=font_label)

# Save and confirm
img.save("infographic_wallpaper.png")
print("✅ Wallpaper saved as infographic_wallpaper.png")
