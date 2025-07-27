from PIL import Image, ImageDraw, ImageFont
import os

# Wild Meadow Florals palette
colors = ['#F7FAF7', '#7FB069', '#D4A574', '#E07A5F', '#81B29A', '#F2CC8F', '#E8F3E8']
theme_name = 'Wild Meadow Florals'

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
img.save('wild-meadow-florals-palette.png', 'PNG')
print("Created wild-meadow-florals-palette.png")