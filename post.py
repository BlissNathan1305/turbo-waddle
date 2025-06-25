
from PIL import Image, ImageDraw
import random
import math

# Define dimensions for mobile wallpapers
width, height = 1080, 1920

# Function to create a gradient
def create_gradient(draw, color1, color2):
    for y in range(height):
        # Calculate the interpolation factor
        factor = y / height
        # Interpolate between the two colors
        r = int(color1[0] + factor * (color2[0] - color1[0]))
        g = int(color1[1] + factor * (color2[1] - color1[1]))
        b = int(color1[2] + factor * (color2[2] - color1[2]))
        # Draw horizontal line with interpolated color
        draw.line([(0, y), (width, y)], fill=(r, g, b))

# Function to create circular patterns
def create_circles(draw, base_color, accent_color):
    num_circles = random.randint(5, 15)
    for _ in range(num_circles):
        radius = random.randint(50, 200)
        x = random.randint(radius, width - radius)
        y = random.randint(radius, height - radius)
        draw.ellipse(
            [(x - radius, y - radius), (x + radius, y + radius)],
            outline=accent_color,
            width=random.randint(2, 8)
        )
        # Draw smaller accent circles
        for _ in range(random.randint(1, 3)):
            inner_radius = random.randint(10, radius//2)
            inner_x = x + random.randint(-radius//3, radius//3)
            inner_y = y + random.randint(-radius//3, radius//3)
            draw.ellipse(
                [(inner_x - inner_radius, inner_y - inner_radius), 
                 (inner_x + inner_radius, inner_y + inner_radius)],
                fill=accent_color
            )

# Function to create diagonal lines
def create_diagonal_lines(draw, color):
    line_spacing = random.randint(30, 60)
    line_width = random.randint(3, 8)
    for y in range(0, height, line_spacing):
        start_x = random.randint(-50, 50)
        end_x = start_x + width + random.randint(-50, 50)
        draw.line(
            [(start_x, y), (end_x, y + height)],
            fill=color,
            width=line_width
        )

# Function to create geometric patterns
def create_geometric_shapes(draw, base_color, accent_color):
    num_shapes = random.randint(5, 15)
    for _ in range(num_shapes):
        size = random.randint(50, 200)
        x = random.randint(size, width - size)
        y = random.randint(size, height - size)
        
        # Randomly choose shape type
        if random.random() > 0.5:
            # Triangle
            draw.polygon(
                [(x, y - size), (x - size, y + size), (x + size, y + size)],
                outline=accent_color,
                width=random.randint(2, 6)
            )
        else:
            # Square/Diamond
            draw.polygon(
                [(x, y - size), (x + size, y), (x, y + size), (x - size, y)],
                outline=accent_color,
                width=random.randint(2, 6)
            )

# Generate 10 wallpapers
for i in range(10):
    # Create a new image
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Choose random colors
    base_color = (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255)
    )
    accent_color = (
        random.randint(0, 150),
        random.randint(0, 150),
        random.randint(0, 150)
    )
    gradient_color = (
        random.randint(50, 200),
        random.randint(50, 200),
        random.randint(50, 200)
    )
    
    # Randomly choose a pattern type
    pattern_type = random.randint(0, 3)
    
    if pattern_type == 0:
        # Gradient background with circles
        create_gradient(draw, base_color, gradient_color)
        create_circles(draw, base_color, accent_color)
    elif pattern_type == 1:
        # Solid background with diagonal lines and shapes
        draw.rectangle([(0, 0), (width, height)], fill=base_color)
        create_diagonal_lines(draw, accent_color)
        create_geometric_shapes(draw, base_color, accent_color)
    elif pattern_type == 2:
        # Gradient background with geometric shapes
        create_gradient(draw, base_color, gradient_color)
        create_geometric_shapes(draw, base_color, accent_color)
    else:
        # Solid background with circles and diagonal lines
        draw.rectangle([(0, 0), (width, height)], fill=base_color)
        create_circles(draw, base_color, accent_color)
        create_diagonal_lines(draw, accent_color)
    
    # Save the wallpaper
    image.save(f'beautiful_wallpaper_{i + 1}.png', 'PNG')
