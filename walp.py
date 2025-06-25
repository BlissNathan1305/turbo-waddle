
from PIL import Image, ImageDraw, ImageFilter
import random
import math

def get_random_color():
    """Generates a random vibrant RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def interpolate_color(color1, color2, factor):
    """Interpolates between two RGB colors."""
    r = int(color1[0] + (color2[0] - color1[0]) * factor)
    g = int(color1[1] + (color2[1] - color1[1]) * factor)
    b = int(color1[2] + (color2[2] - color1[2]) * factor)
    return (r, g, b)

def draw_gradient_wave(draw, width, height, colors):
    """Draws an abstract gradient wave pattern."""
    for y in range(height):
        # Calculate wave offset
        wave_offset = int(20 * math.sin(y * 0.05 + random.random() * math.pi))
        for x in range(width):
            # Calculate color based on x position and wave offset
            factor_x = (x + wave_offset) / width
            # Ensure factor_x is within [0, 1]
            factor_x = max(0, min(1, factor_x))
            # Create a simple two-point gradient
            color = interpolate_color(colors[0], colors[1], factor_x)
            draw.point((x, y), fill=color)

def draw_geometric_shapes(draw, width, height, colors):
    """Draws a pattern of random geometric shapes (triangles and rectangles)."""
    for _ in range(150): # Draw 150 shapes
        shape_type = random.choice(['rectangle', 'triangle'])
        fill_color = random.choice(colors)
        alpha = random.randint(100, 255) # Add some transparency
        fill_color_with_alpha = fill_color + (alpha,)

        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        size_w = random.randint(50, 300)
        size_h = random.randint(50, 300)

        if shape_type == 'rectangle':
            x2 = min(x1 + size_w, width)
            y2 = min(y1 + size_h, height)
            draw.rectangle([x1, y1, x2, y2], fill=fill_color_with_alpha)
        else: # triangle
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            x3 = random.randint(0, width)
            y3 = random.randint(0, height)
            draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=fill_color_with_alpha)

def draw_concentric_circles(draw, width, height, colors):
    """Draws concentric circles with varying colors."""
    center_x, center_y = width // 2, height // 2
    max_radius = max(width, height) // 2
    
    # Sort colors for a smoother transition, or keep them random
    # colors.sort() 
    
    num_circles = 30
    for i in range(num_circles, 0, -1):
        radius = int(max_radius * (i / num_circles))
        
        # Ensure index is within bounds for colors list
        color_index = i % len(colors) 
        fill_color = colors[color_index]
        
        # Add slight transparency to outer circles
        alpha = int(255 * (i / num_circles)) 
        fill_color_with_alpha = fill_color + (alpha,)

        bbox = [center_x - radius, center_y - radius, center_x + radius, center_y + radius]
        draw.ellipse(bbox, fill=fill_color_with_alpha)

def draw_swirling_lines(draw, width, height, colors):
    """Draws organic, swirling lines."""
    num_lines = 20
    for i in range(num_lines):
        start_x = random.randint(0, width)
        start_y = random.randint(0, height)
        end_x = random.randint(0, width)
        end_y = random.randint(0, height)
        control_x1 = random.randint(0, width)
        control_y1 = random.randint(0, height)
        control_x2 = random.randint(0, width)
        control_y2 = random.randint(0, height)

        # Using a Bezier curve to create swirling effect
        points = []
        steps = 100
        for t in range(steps + 1):
            t /= steps
            x = (1-t)**3 * start_x + 3*(1-t)**2*t * control_x1 + 3*(1-t)*t**2 * control_x2 + t**3 * end_x
            y = (1-t)**3 * start_y + 3*(1-t)**2*t * control_y1 + 3*(1-t)*t**2 * control_y2 + t**3 * end_y
            points.append((x, y))

        line_color = random.choice(colors)
        draw.line(points, fill=line_color, width=random.randint(5, 20))

def draw_polka_dots(draw, width, height, colors):
    """Draws various sizes and colors of polka dots/bubbles."""
    num_dots = 500
    for _ in range(num_dots):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(5, 50)
        fill_color = random.choice(colors)
        alpha = random.randint(150, 255)
        fill_color_with_alpha = fill_color + (alpha,)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=fill_color_with_alpha)

def draw_diagonal_stripes(draw, width, height, colors):
    """Draws colorful diagonal stripes."""
    stripe_width = random.randint(50, 150)
    angle_rad = math.radians(random.choice([-45, 45, -60, 60])) # Diagonal angles

    # Calculate the range for the diagonal lines
    # The lines need to cover the entire canvas, so they extend beyond its bounds
    start_x = -height * abs(math.tan(angle_rad))
    end_x = width + height * abs(math.tan(angle_rad))

    num_stripes = int(abs(end_x - start_x) / stripe_width) + 2

    for i in range(num_stripes):
        fill_color = random.choice(colors)
        
        # Calculate the position for each stripe
        if angle_rad > 0: # Positive slope (bottom-left to top-right)
            x_offset = start_x + i * stripe_width
            draw.polygon([
                (x_offset, height),
                (x_offset + stripe_width, height),
                (x_offset + stripe_width + height * math.tan(angle_rad), 0),
                (x_offset + height * math.tan(angle_rad), 0)
            ], fill=fill_color)
        else: # Negative slope (top-left to bottom-right)
            x_offset = start_x + i * stripe_width
            draw.polygon([
                (x_offset, 0),
                (x_offset + stripe_width, 0),
                (x_offset + stripe_width + height * math.tan(angle_rad), height),
                (x_offset + height * math.tan(angle_rad), height)
            ], fill=fill_color)


def draw_chessboard_grid(draw, width, height, colors):
    """Draws a chessboard-like grid with varying colors."""
    cell_size = random.randint(50, 150)
    for i in range(0, width, cell_size):
        for j in range(0, height, cell_size):
            fill_color = random.choice(colors)
            draw.rectangle([i, j, i + cell_size, j + cell_size], fill=fill_color)

def draw_stained_glass(draw, width, height, colors):
    """Draws a pattern resembling stained glass with polygonal shapes."""
    num_polygons = 100
    for _ in range(num_polygons):
        num_points = random.randint(3, 8) # 3 to 8 sided polygons
        points = []
        for _ in range(num_points):
            points.append((random.randint(0, width), random.randint(0, height)))
        
        fill_color = random.choice(colors)
        draw.polygon(points, fill=fill_color, outline=(0, 0, 0), width=random.randint(1, 3)) # Black outline

def draw_pixel_art_abstract(draw, width, height, colors):
    """Creates a pixel art style abstract pattern."""
    pixel_size = random.randint(10, 30)
    for x in range(0, width, pixel_size):
        for y in range(0, height, pixel_size):
            fill_color = random.choice(colors)
            draw.rectangle([x, y, x + pixel_size, y + pixel_size], fill=fill_color)

def draw_radial_burst(draw, width, height, colors):
    """Draws colors radiating from a central point."""
    center_x, center_y = width // 2, height // 2
    max_dist = math.sqrt((width/2)**2 + (height/2)**2)

    # Create a gradient for the burst effect
    for y in range(height):
        for x in range(width):
            dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            factor = dist / max_dist
            
            # Ensure factor is within [0, 1]
            factor = max(0, min(1, factor))

            # Use more colors for a richer radial gradient
            color_index = int(factor * (len(colors) - 1))
            
            # Interpolate between colors for smoother transition
            if color_index + 1 < len(colors):
                interp_factor = (factor * (len(colors) - 1)) - color_index
                color = interpolate_color(colors[color_index], colors[color_index + 1], interp_factor)
            else:
                color = colors[color_index] # Use the last color if at the end

            draw.point((x, y), fill=color)

def generate_wallpapers(num_wallpapers=10, width=1080, height=1920):
    """Generates a specified number of unique mobile wallpapers."""
    design_functions = [
        draw_gradient_wave,
        draw_geometric_shapes,
        draw_concentric_circles,
        draw_swirling_lines,
        draw_polka_dots,
        draw_diagonal_stripes,
        draw_chessboard_grid,
        draw_stained_glass,
        draw_pixel_art_abstract,
        draw_radial_burst
    ]

    for i in range(num_wallpapers):
        print(f"Generating wallpaper {i + 1}...")
        image = Image.new('RGB', (width, height), color='black')
        draw = ImageDraw.Draw(image)

        # Generate a distinct set of 3-5 vibrant colors for each wallpaper
        num_colors = random.randint(3, 5)
        current_colors = [get_random_color() for _ in range(num_colors)]

        # Apply a random filter or enhance some wallpapers
        if random.random() < 0.3: # 30% chance to apply a filter
            filter_type = random.choice([ImageFilter.BLUR, ImageFilter.SMOOTH, ImageFilter.SHARPEN])
            print(f"  Applying filter: {filter_type} for wallpaper {i + 1}")
            image = image.filter(filter_type)
            draw = ImageDraw.Draw(image) # Redraw the image after filter for continued drawing

        # Select a design function and apply it
        design_func = design_functions[i % len(design_functions)] # Cycle through designs
        design_func(draw, width, height, current_colors)

        # Enhance with some random elements if desired (e.g., subtle noise, more shapes)
        if random.random() < 0.2: # 20% chance to add subtle elements
            for _ in range(50):
                x = random.randint(0, width)
                y = random.randint(0, height)
                radius = random.randint(1, 3)
                color = random.choice(current_colors) + (random.randint(50, 150),) # Semi-transparent
                draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)


        filename = f'mobile_wallpaper_{i + 1}.png'
        image.save(filename)
        print(f"Saved {filename}")

if __name__ == "__main__":
    generate_wallpapers()

