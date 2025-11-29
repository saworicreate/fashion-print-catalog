#!/usr/bin/env python3
"""
Color Chip Generator for NEO POP MODERNISM Collection
Generates color palette visualization chips for each pattern
"""

import json
from PIL import Image, ImageDraw, ImageFont
import os

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_color_chip(color_hex, width=300, height=300):
    """Create a single color chip"""
    img = Image.new('RGB', (width, height), hex_to_rgb(color_hex))
    return img

def create_palette_visualization(pattern_data, output_path):
    """Create a complete palette visualization for a pattern"""
    colors = pattern_data['colors']

    # Collect all colors
    all_colors = []
    color_labels = []

    # Primary color
    all_colors.append(colors['primary'])
    color_labels.append('Primary')

    # Secondary colors
    for i, color in enumerate(colors['secondary'], 1):
        all_colors.append(color)
        color_labels.append(f'Secondary {i}')

    # Background
    all_colors.append(colors['background'])
    color_labels.append('Background')

    # Accent
    all_colors.append(colors['accent'])
    color_labels.append('Accent')

    # Calculate dimensions
    chip_size = 200
    padding = 20
    label_height = 60
    cols = 4
    rows = (len(all_colors) + cols - 1) // cols

    img_width = cols * (chip_size + padding) + padding
    img_height = rows * (chip_size + label_height + padding) + padding + 100  # Extra for title

    # Create main image
    img = Image.new('RGB', (img_width, img_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Try to use a font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        hex_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        hex_font = ImageFont.load_default()

    # Draw title
    title = f"{pattern_data['name']} - Color Palette"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((img_width - title_width) // 2, 30), title, fill=(0, 0, 0), font=title_font)

    # Draw color chips
    y_offset = 100
    for idx, (color, label) in enumerate(zip(all_colors, color_labels)):
        row = idx // cols
        col = idx % cols

        x = padding + col * (chip_size + padding)
        y = y_offset + row * (chip_size + label_height + padding)

        # Draw color chip
        chip_img = create_color_chip(color, chip_size, chip_size)
        img.paste(chip_img, (x, y))

        # Draw border
        draw.rectangle([x, y, x + chip_size, y + chip_size], outline=(200, 200, 200), width=2)

        # Draw label
        label_y = y + chip_size + 10
        label_bbox = draw.textbbox((0, 0), label, font=label_font)
        label_width = label_bbox[2] - label_bbox[0]
        draw.text((x + (chip_size - label_width) // 2, label_y), label, fill=(0, 0, 0), font=label_font)

        # Draw hex code
        hex_y = label_y + 25
        hex_bbox = draw.textbbox((0, 0), color.upper(), font=hex_font)
        hex_width = hex_bbox[2] - hex_bbox[0]
        draw.text((x + (chip_size - hex_width) // 2, hex_y), color.upper(), fill=(100, 100, 100), font=hex_font)

    # Save image
    img.save(output_path, 'PNG', quality=95)
    print(f"Created palette visualization: {output_path}")

def create_individual_chips(pattern_data, output_dir):
    """Create individual color chip files"""
    colors = pattern_data['colors']
    pattern_id = pattern_data['id']

    # Create individual chips
    chips_created = []

    # Primary
    chip_path = os.path.join(output_dir, f"pattern{pattern_id}_primary.png")
    chip = create_color_chip(colors['primary'], 400, 400)
    chip.save(chip_path, 'PNG')
    chips_created.append(chip_path)

    # Secondary colors
    for i, color in enumerate(colors['secondary'], 1):
        chip_path = os.path.join(output_dir, f"pattern{pattern_id}_secondary{i}.png")
        chip = create_color_chip(color, 400, 400)
        chip.save(chip_path, 'PNG')
        chips_created.append(chip_path)

    # Background
    chip_path = os.path.join(output_dir, f"pattern{pattern_id}_background.png")
    chip = create_color_chip(colors['background'], 400, 400)
    chip.save(chip_path, 'PNG')
    chips_created.append(chip_path)

    # Accent
    chip_path = os.path.join(output_dir, f"pattern{pattern_id}_accent.png")
    chip = create_color_chip(colors['accent'], 400, 400)
    chip.save(chip_path, 'PNG')
    chips_created.append(chip_path)

    return chips_created

def main():
    # Load pattern specs
    with open('print-19779957339/pattern-specs.json', 'r') as f:
        specs = json.load(f)

    # Create output directory
    os.makedirs('print-19779957339/colors', exist_ok=True)

    # Generate color chips for each pattern
    for pattern in specs['patterns']:
        print(f"\nProcessing Pattern {pattern['id']}: {pattern['name']}")

        # Create full palette visualization
        palette_path = f"print-19779957339/colors/pattern{pattern['id']}_palette.png"
        create_palette_visualization(pattern, palette_path)

        # Create individual color chips
        chips = create_individual_chips(pattern, 'print-19779957339/colors')
        print(f"Created {len(chips)} individual color chips")

    print("\n✓ All color chips generated successfully!")

if __name__ == '__main__':
    main()
