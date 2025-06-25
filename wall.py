
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
import math
import colorsys

# Common mobile resolutions
MOBILE_RESOLUTIONS = {
    'iphone_14': (1179, 2556),
    'iphone_se': (750, 1334),
    'android_fhd': (1080, 1920),
    'android_qhd': (1440, 2560),
    'generic_tall': (1080, 2340)
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient_wallpaper(width, height, colors, filename="gradient_wallpaper.png"):
    """Create a smooth gradient wallpaper using PIL"""
    img = Image.new('RGB', (width, height))
    pixels = []
    
    # Convert hex colors to RGB
    rgb_colors = [hex_to_rgb(color) for color in colors]
    
    for y in range(height):
        # Calculate position in gradient (0 to 1)
        position = y / height
        
        # Determine which two colors to interpolate between
        if len(rgb_colors) == 2:
            color1, color2 = rgb_colors[0], rgb_colors[1]
            weight = position
        else:
            # For multiple colors, find the segment
            segment_size = 1.0 / (len(rgb_colors) - 1)
            segment = int(position / segment_size)
            if segment >= len(rgb_colors) - 1:
                segment = len(rgb_colors) - 2
            
            color1 = rgb_colors[segment]
            color2 = rgb_colors[segment + 1]
            weight = (position - segment * segment_size) / segment_size
        
        # Interpolate between colors
        r = int(color1[0] * (1 - weight) + color2[0] * weight)
        g = int(color1[1] * (1 - weight) + color2[1] * weight)
        b = int(color1[2] * (1 - weight) + color2[2] * weight)
        
        # Create row of pixels
        row = [(r, g, b) for _ in range(width)]
        pixels.extend(row)
    
    img.putdata(pixels)
    img.save(filename, quality=95)
    print(f"Gradient wallpaper saved as {filename}")

def create_geometric_wallpaper(width, height, filename="geometric_wallpaper.png"):
    """Create a geometric pattern wallpaper using PIL"""
    img = Image.new('RGB', (width, height), color='#1a1a2e')
    
    colors = ['#16213e', '#0f3460', '#533483', '#7209b7', '#a663cc', '#4cc9f0']
    
    # Draw circles with transparency
    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(20, 150)
        color = random.choice(colors)
        
        # Create overlay for transparency
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        rgb_color = hex_to_rgb(color)
        overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                           fill=(*rgb_color, 60))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Draw triangles
    for _ in range(30):
        points = [(random.randint(0, width), random.randint(0, height)) for _ in range(3)]
        color = random.choice(colors)
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        rgb_color = hex_to_rgb(color)
        overlay_draw.polygon(points, fill=(*rgb_color, 40))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Apply slight blur
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    img.save(filename, quality=95)
    print(f"Geometric wallpaper saved as {filename}")

def create_wave_wallpaper(width, height, filename="wave_wallpaper.png"):
    """Create a wave pattern wallpaper using mathematical functions"""
    img = Image.new('RGB', (width, height))
    pixels = []
    
    colors = ['#0d1b2a', '#415a77', '#778da9', '#e0e1dd']
    rgb_colors = [hex_to_rgb(color) for color in colors]
    
    for y in range(height):
        row = []
        for x in range(width):
            # Create wave pattern
            wave1 = math.sin(x * 0.01) * math.cos(y * 0.005)
            wave2 = math.cos(x * 0.005) * math.sin(y * 0.008)
            combined = (wave1 + wave2 + 2) / 4  # Normalize to 0-1
            
            # Map to color
            color_index = combined * (len(rgb_colors) - 1)
            index1 = int(color_index)
            index2 = min(index1 + 1, len(rgb_colors) - 1)
            weight = color_index - index1
            
            # Interpolate colors
            color1 = rgb_colors[index1]
            color2 = rgb_colors[index2]
            
            r = int(color1[0] * (1 - weight) + color2[0] * weight)
            g = int(color1[1] * (1 - weight) + color2[1] * weight)
            b = int(color1[2] * (1 - weight) + color2[2] * weight)
            
            row.append((r, g, b))
        pixels.extend(row)
    
    img.putdata(pixels)
    img.save(filename, quality=95)
    print(f"Wave wallpaper saved as {filename}")

def create_particle_wallpaper(width, height, filename="particle_wallpaper.png"):
    """Create a particle/star field wallpaper"""
    img = Image.new('RGB', (width, height), color='#0a0a0a')
    
    # Create particles
    particles = []
    for _ in range(200):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 4)
        
        # Create color variation in blue-purple range
        hue = random.uniform(0.6, 1.0)
        saturation = random.uniform(0.3, 1.0)
        value = random.uniform(0.5, 1.0)
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        color = tuple(int(c * 255) for c in rgb)
        
        particles.append((x, y, size, color))
        
        # Draw particle with glow effect
        for glow in range(size, 0, -1):
            alpha = int(255 / (glow + 1))
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            overlay_draw.ellipse([x-glow, y-glow, x+glow, y+glow], 
                               fill=(*color, alpha//2))
            img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Add connecting lines between nearby particles
    connection_particles = random.sample(particles, min(50, len(particles)))
    
    for i, (x1, y1, _, _) in enumerate(connection_particles):
        for j, (x2, y2, _, _) in enumerate(connection_particles[i+1:], i+1):
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if distance < 200:
                alpha = int(255 * (1 - distance/200))
                overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
                overlay_draw = ImageDraw.Draw(overlay)
                overlay_draw.line([(x1, y1), (x2, y2)], 
                                fill=(100, 150, 255, alpha//3), width=1)
                img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    img.save(filename, quality=95)
    print(f"Particle wallpaper saved as {filename}")

def create_abstract_art_wallpaper(width, height, filename="abstract_wallpaper.png"):
    """Create an abstract art wallpaper using random patterns"""
    img = Image.new('RGB', (width, height), color='#2d3436')
    
    # Create random color patches
    colors = ['#74b9ff', '#0984e3', '#6c5ce7', '#a29bfe', '#fd79a8', '#e84393']
    
    for _ in range(100):
        # Random blob position and size
        x = random.randint(-100, width + 100)
        y = random.randint(-100, height + 100)
        size = random.randint(50, 300)
        color = random.choice(colors)
        
        # Create blob with random shape
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        rgb_color = hex_to_rgb(color)
        
        # Draw irregular shape using multiple overlapping circles
        for _ in range(5):
            offset_x = random.randint(-size//3, size//3)
            offset_y = random.randint(-size//3, size//3)
            blob_size = size + random.randint(-size//4, size//4)
            overlay_draw.ellipse([x+offset_x-blob_size//2, y+offset_y-blob_size//2, 
                                x+offset_x+blob_size//2, y+offset_y+blob_size//2], 
                               fill=(*rgb_color, 30))
        
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    
    # Apply blur for smooth abstract look
    img = img.filter(ImageFilter.GaussianBlur(radius=3))
    
    # Add some sharp lines
    draw = ImageDraw.Draw(img)
    for _ in range(10):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = x1 + random.randint(-200, 200), y1 + random.randint(-200, 200)
        color = random.choice(colors)
        rgb_color = hex_to_rgb(color)
        draw.line([(x1, y1), (x2, y2)], fill=rgb_color, width=random.randint(2, 8))
    
    img.save(filename, quality=95)
    print(f"Abstract wallpaper saved as {filename}")

def create_minimalist_wallpaper(width, height, filename="minimalist_wallpaper.png"):
    """Create a clean minimalist wallpaper"""
    bg_color = '#f8f9fa'
    accent_color = '#6c757d'
    
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = width // 2, height // 2
    accent_rgb = hex_to_rgb(accent_color)
    
    # Draw concentric circles
    for i in range(3):
        radius = 100 + i * 50
        draw.ellipse([center_x - radius, center_y - radius, 
                     center_x + radius, center_y + radius], 
                    outline=accent_rgb, width=2)
    
    # Add minimal lines
    for i in range(5):
        y_pos = height // 6 * (i + 1)
        draw.line([(width//4, y_pos), (3*width//4, y_pos)], 
                 fill=accent_rgb, width=1)
    
    img.save(filename, quality=95)
    print(f"Minimalist wallpaper saved as {filename}")

def create_radial_gradient_wallpaper(width, height, center_color, edge_color, filename="radial_wallpaper.png"):
    """Create a radial gradient wallpaper"""
    img = Image.new('RGB', (width, height))
    pixels = []
    
    center_rgb = hex_to_rgb(center_color)
    edge_rgb = hex_to_rgb(edge_color)
    
    center_x, center_y = width // 2, height // 2
    max_distance = math.sqrt(center_x**2 + center_y**2)
    
    for y in range(height):
        row = []
        for x in range(width):
            # Calculate distance from center
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            weight = min(distance / max_distance, 1.0)
            
            # Interpolate colors
            r = int(center_rgb[0] * (1 - weight) + edge_rgb[0] * weight)
            g = int(center_rgb[1] * (1 - weight) + edge_rgb[1] * weight)
            b = int(center_rgb[2] * (1 - weight) + edge_rgb[2] * weight)
            
            row.append((r, g, b))
        pixels.extend(row)
    
    img.putdata(pixels)
    img.save(filename, quality=95)
    print(f"Radial gradient wallpaper saved as {filename}")

# Example usage
if __name__ == "__main__":
    # Choose resolution
    resolution = MOBILE_RESOLUTIONS['android_fhd']  # 1080x1920
    width, height = resolution
    
    print(f"Creating wallpapers at {width}x{height} resolution...")
    print("This version uses only PIL/Pillow - no NumPy or Matplotlib required!")
    
    # Create different types of wallpapers
    create_gradient_wallpaper(width, height, 
                            ['#ff006e', '#8338ec', '#3a86ff'], 
                            "gradient_mobile.png")
    
    create_geometric_wallpaper(width, height, "geometric_mobile.png")
    
    create_wave_wallpaper(width, height, "wave_mobile.png")
    
    create_particle_wallpaper(width, height, "particle_mobile.png")
    
    create_abstract_art_wallpaper(width, height, "abstract_mobile.png")
    
    create_minimalist_wallpaper(width, height, "minimalist_mobile.png")
    
    create_radial_gradient_wallpaper(width, height, '#ff6b6b', '#4ecdc4', "radial_mobile.png")
    
    print("\nAll wallpapers created successfully!")
    print("Only requires: pip install pillow")
