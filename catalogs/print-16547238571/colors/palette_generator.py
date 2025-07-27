#!/usr/bin/env python3

# Direct execution of palette generation
import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

exec("""
from PIL import Image, ImageDraw
import os

# Define all themes and their colors
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

def create_palette_image(theme_key, theme_data):
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
    
    # Draw title
    title_x = total_width // 2 - len(theme_name) * 6
    title_y = margin + 15
    draw.text((title_x, title_y), theme_name, fill='#333333')
    
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
        draw.text((label_x, label_y), color.upper(), fill='#333333')
    
    # Save the image
    filename = f"{theme_key}-palette.png"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)
    img.save(filepath, 'PNG')
    
    return filepath

# Generate all images
created_files = []
for theme_key, theme_data in themes.items():
    try:
        filepath = create_palette_image(theme_key, theme_data)
        created_files.append(filepath)
        print(f"✓ Created: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"✗ Error creating {theme_data['name']}: {e}")

print(f"\\nGenerated {len(created_files)} palette images successfully!")
""")