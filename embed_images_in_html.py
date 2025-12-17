#!/usr/bin/env python3
"""
Script to embed all images in apresentacao.html as base64 data URIs.
This fixes the issue where images don't render when the HTML is downloaded.
"""
import base64
import re
import os
from pathlib import Path


def image_to_base64(image_path):
    """Convert an image file to base64 data URI."""
    try:
        with open(image_path, 'rb') as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            
        # Determine MIME type based on extension
        ext = image_path.suffix.lower()
        mime_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
        }
        mime_type = mime_types.get(ext, 'image/png')
        
        return f"data:{mime_type};base64,{encoded}"
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None


def embed_images_in_html(html_path, output_path=None):
    """
    Replace all relative image paths in HTML with base64 data URIs.
    
    Args:
        html_path: Path to the input HTML file
        output_path: Path to the output HTML file (if None, overwrites input)
    """
    html_path = Path(html_path)
    if output_path is None:
        output_path = html_path
    else:
        output_path = Path(output_path)
    
    # Read the HTML file
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Find all image references
    # Pattern matches: src="./path/to/image.png" or src='./path/to/image.png'
    img_pattern = r'src=["\'](\./[^"\']+\.(?:png|jpg|jpeg|gif|svg))["\']'
    
    matches = re.finditer(img_pattern, html_content, re.IGNORECASE)
    
    replacements = {}
    base_dir = html_path.parent
    
    for match in matches:
        relative_path = match.group(1)
        # Convert relative path to absolute path
        image_path = base_dir / relative_path.lstrip('./')
        
        if image_path.exists():
            print(f"Encoding: {relative_path}")
            base64_data = image_to_base64(image_path)
            if base64_data:
                replacements[relative_path] = base64_data
        else:
            print(f"Warning: Image not found: {image_path}")
    
    # Apply replacements
    for original_path, base64_data in replacements.items():
        # Replace both single and double quote versions
        html_content = html_content.replace(f'src="{original_path}"', f'src="{base64_data}"')
        html_content = html_content.replace(f"src='{original_path}'", f"src='{base64_data}'")
    
    # Write the updated HTML
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\nSuccessfully embedded {len(replacements)} images into {output_path}")
    return len(replacements)


if __name__ == '__main__':
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    html_file = script_dir / 'apresentacao.html'
    
    if html_file.exists():
        print(f"Processing {html_file}...")
        count = embed_images_in_html(html_file)
        print(f"\nDone! {count} images have been embedded as base64 data URIs.")
        print("The HTML file can now be downloaded and viewed offline with all images intact.")
    else:
        print(f"Error: {html_file} not found!")
