#!/usr/bin/env python3
"""
Color Chip Generator for Cyberbotanical Collection
Generates PNG color palette chips for each pattern theme
"""

import json
from PIL import Image, ImageDraw, ImageFont
import os

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_color_chip(palette_data, pattern_name, output_path):
    """Create a color chip image for a given palette"""
    
    # Image dimensions
    chip_width = 100
    chip_height = 100
    chips_per_row = 5
    margin = 20
    text_height = 40
    
    # Calculate total image size
    total_colors = len(palette_data['palette']['secondary']) + 1  # +1 for primary
    rows = (total_colors + chips_per_row - 1) // chips_per_row
    
    img_width = chips_per_row * chip_width + (chips_per_row + 1) * margin
    img_height = rows * (chip_height + text_height) + (rows + 1) * margin + 60  # +60 for title
    
    # Create image with white background
    img = Image.new('RGB', (img_width, img_height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        title_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 16)
        label_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
    
    # Draw title
    title = f"{pattern_name} - Color Palette"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((img_width - title_width) // 2, 10), title, fill='black', font=title_font)
    
    # Collect all colors
    colors = [palette_data['palette']['primary']] + palette_data['palette']['secondary']
    color_names = ['Primary'] + [f'Secondary {i+1}' for i in range(len(palette_data['palette']['secondary']))]
    
    # Draw color chips
    y_offset = 50
    for i, (color_hex, color_name) in enumerate(zip(colors, color_names)):
        row = i // chips_per_row
        col = i % chips_per_row
        
        x = margin + col * (chip_width + margin)
        y = y_offset + row * (chip_height + text_height + margin)
        
        # Draw color chip
        color_rgb = hex_to_rgb(color_hex)
        draw.rectangle([x, y, x + chip_width, y + chip_height], fill=color_rgb, outline='black', width=2)
        
        # Draw hex code
        hex_bbox = draw.textbbox((0, 0), color_hex, font=label_font)
        hex_width = hex_bbox[2] - hex_bbox[0]
        draw.text((x + (chip_width - hex_width) // 2, y + chip_height + 5), color_hex, fill='black', font=label_font)
        
        # Draw color name
        name_bbox = draw.textbbox((0, 0), color_name, font=label_font)
        name_width = name_bbox[2] - name_bbox[0]
        draw.text((x + (chip_width - name_width) // 2, y + chip_height + 20), color_name, fill='gray', font=label_font)
    
    # Save image
    img.save(output_path, 'PNG')
    print(f"Created color chip: {output_path}")

def generate_all_color_chips():
    """Generate color chip images for all patterns"""
    
    # Load color strategy
    with open('/home/runner/work/music-video-workflow/music-video-workflow/print-16702775433/color-strategy.json', 'r') as f:
        color_data = json.load(f)
    
    # Ensure colors directory exists
    colors_dir = '/home/runner/work/music-video-workflow/music-video-workflow/print-16702775433/colors'
    os.makedirs(colors_dir, exist_ok=True)
    
    # Generate chips for each pattern
    for pattern_key, pattern_data in color_data['color_palettes'].items():
        pattern_name = pattern_data['name']
        safe_name = pattern_name.lower().replace(' ', '-').replace(':', '')
        output_path = os.path.join(colors_dir, f"{pattern_key}-{safe_name}.png")
        
        create_color_chip(pattern_data, pattern_name, output_path)

if __name__ == "__main__":
    generate_all_color_chips()
    print("All color chip images generated successfully!")