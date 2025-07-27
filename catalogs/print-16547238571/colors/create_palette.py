#!/usr/bin/env python3
"""
Generate PNG color chip images for botanical pattern themes using PIL.
This script creates the colors directory and generates all palette images.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Ensure the colors directory exists
colors_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(colors_dir, exist_ok=True)

# Define the color palettes for each theme
themes = {
    'wild-meadow-florals': {
        'name': 'Wild Meadow Florals',
        'colors': ['#F7FAF7', '#7FB069', '#D4A574', '#E07A5F', '#81B29A', '#F2CC8F', '#E8F3E8']
    },
    'tropical-leaf-symphony': {
        'name': 'Tropical Leaf Symphony', 
        'colors': ['#F9FBF9', '#2D5016', '#4A7C59', '#8FBC8F', '#228B22', '#6B8E23', '#B8E6B8']
    },
    'herb-garden-delight': {
        'name': 'Herb Garden Delight',
        'colors': ['#FEFEFE', '#9CAF88', '#C7B377', '#8B7355', '#A0522D', '#556B2F', '#E8E8E8']
    },
    'sakura-blossom-dance': {
        'name': 'Sakura Blossom Dance',
        'colors': ['#FDF8F6', '#FFB7C5', '#FF69B4', '#DA70D6', '#B19CD9', '#87CEEB', '#F8F5F3']
    },
    'eucalyptus-grove': {
        'name': 'Eucalyptus Grove',
        'colors': ['#FAFAFF', '#B8C5B8', '#8FBC8F', '#98FB98', '#90EE90', '#E0E0E0', '#FFFFFF']
    }
}

def create_color_palette_image(theme_key, theme_data):
    """Create a professional color palette image using PIL."""
    colors = theme_data['colors']
    theme_name = theme_data['name']
    
    # Image dimensions
    chip_width = 120
    chip_height = 100
    chip_spacing = 10
    margin = 30
    title_height = 50
    label_height = 30
    
    # Calculate total image size
    total_width = len(colors) * chip_width + (len(colors) - 1) * chip_spacing + 2 * margin
    total_height = title_height + chip_height + label_height + 2 * margin
    
    # Create image with white background
    img = Image.new('RGB', (total_width, total_height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Use default font
    try:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default() 
    except:
        title_font = None
        label_font = None
    
    # Draw title
    title_x = total_width // 2 - len(theme_name) * 6
    title_y = margin + 15
    draw.text((title_x, title_y), theme_name, fill='#333333', font=title_font)
    
    # Draw color chips and labels
    start_y = margin + title_height
    
    for i, color in enumerate(colors):
        # Calculate position
        x = margin + i * (chip_width + chip_spacing)
        y = start_y
        
        # Draw color chip with border
        draw.rectangle([x-1, y-1, x + chip_width + 1, y + chip_height + 1], fill='#CCCCCC')
        draw.rectangle([x, y, x + chip_width, y + chip_height], fill=color)
        
        # Draw hex label
        label_x = x + chip_width // 2 - len(color) * 4
        label_y = y + chip_height + 10
        draw.text((label_x, label_y), color.upper(), fill='#333333', font=label_font)
    
    # Save the image
    filename = f"{theme_key}-palette.png"
    filepath = os.path.join(colors_dir, filename)
    img.save(filepath, 'PNG')
    
    return filepath

# Generate all palette images
print("Generating color palette images...")

for theme_key, theme_data in themes.items():
    try:
        filepath = create_color_palette_image(theme_key, theme_data)
        print(f"Created: {filepath}")
    except Exception as e:
        print(f"Error creating {theme_data['name']}: {e}")

print("Color palette generation complete!")