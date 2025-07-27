#!/usr/bin/env python3
"""
Convert SVG color palette files to PNG format.
This script converts the SVG files to PNG using available Python libraries.
"""

import os
import subprocess
import base64
from io import BytesIO

def convert_svg_to_png_with_cairosvg():
    """Convert SVG files to PNG using cairosvg if available."""
    try:
        import cairosvg
        svg_files = [
            'wild-meadow-florals-palette.svg',
            'tropical-leaf-symphony-palette.svg', 
            'herb-garden-delight-palette.svg',
            'sakura-blossom-dance-palette.svg',
            'eucalyptus-grove-palette.svg'
        ]
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        for svg_file in svg_files:
            svg_path = os.path.join(current_dir, svg_file)
            png_file = svg_file.replace('.svg', '.png')
            png_path = os.path.join(current_dir, png_file)
            
            if os.path.exists(svg_path):
                cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=300)
                print(f"✓ Converted {svg_file} to {png_file}")
            else:
                print(f"✗ SVG file not found: {svg_file}")
                
        return True
        
    except ImportError:
        print("cairosvg not available")
        return False

def convert_svg_to_png_with_wand():
    """Convert SVG files to PNG using Wand if available."""
    try:
        from wand.image import Image as WandImage
        
        svg_files = [
            'wild-meadow-florals-palette.svg',
            'tropical-leaf-symphony-palette.svg', 
            'herb-garden-delight-palette.svg',
            'sakura-blossom-dance-palette.svg',
            'eucalyptus-grove-palette.svg'
        ]
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        for svg_file in svg_files:
            svg_path = os.path.join(current_dir, svg_file)
            png_file = svg_file.replace('.svg', '.png')
            png_path = os.path.join(current_dir, png_file)
            
            if os.path.exists(svg_path):
                with WandImage(filename=svg_path, resolution=300) as img:
                    img.format = 'png'
                    img.save(filename=png_path)
                print(f"✓ Converted {svg_file} to {png_file}")
            else:
                print(f"✗ SVG file not found: {svg_file}")
                
        return True
        
    except ImportError:
        print("Wand not available")
        return False

def convert_with_system_tools():
    """Try to convert using system tools like rsvg-convert or inkscape."""
    svg_files = [
        'wild-meadow-florals-palette.svg',
        'tropical-leaf-symphony-palette.svg', 
        'herb-garden-delight-palette.svg',
        'sakura-blossom-dance-palette.svg',
        'eucalyptus-grove-palette.svg'
    ]
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Try rsvg-convert first
    try:
        for svg_file in svg_files:
            svg_path = os.path.join(current_dir, svg_file)
            png_file = svg_file.replace('.svg', '.png')
            png_path = os.path.join(current_dir, png_file)
            
            if os.path.exists(svg_path):
                result = subprocess.run([
                    'rsvg-convert', 
                    '--dpi-x', '300', 
                    '--dpi-y', '300',
                    '--format', 'png',
                    '--output', png_path,
                    svg_path
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✓ Converted {svg_file} to {png_file}")
                else:
                    print(f"✗ Error converting {svg_file}: {result.stderr}")
        return True
    except FileNotFoundError:
        print("rsvg-convert not available")
    
    # Try inkscape
    try:
        for svg_file in svg_files:
            svg_path = os.path.join(current_dir, svg_file)
            png_file = svg_file.replace('.svg', '.png')
            png_path = os.path.join(current_dir, png_file)
            
            if os.path.exists(svg_path):
                result = subprocess.run([
                    'inkscape',
                    '--export-type=png',
                    '--export-dpi=300',
                    f'--export-filename={png_path}',
                    svg_path
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"✓ Converted {svg_file} to {png_file}")
                else:
                    print(f"✗ Error converting {svg_file}: {result.stderr}")
        return True
    except FileNotFoundError:
        print("inkscape not available")
    
    return False

def main():
    """Main conversion function."""
    print("Converting SVG color palettes to PNG...")
    print("=" * 50)
    
    # Try different conversion methods
    if convert_svg_to_png_with_cairosvg():
        print("Conversion completed using cairosvg")
    elif convert_svg_to_png_with_wand():
        print("Conversion completed using Wand")
    elif convert_with_system_tools():
        print("Conversion completed using system tools")
    else:
        print("No suitable conversion method found.")
        print("SVG files are available as fallback:")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        for file in os.listdir(current_dir):
            if file.endswith('.svg'):
                print(f"  - {os.path.join(current_dir, file)}")

if __name__ == "__main__":
    main()