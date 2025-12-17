#!/usr/bin/env python3
"""
Verification script to ensure all images are properly embedded in apresentacao.html
"""
import re
from pathlib import Path


def verify_embedded_images(html_path):
    """Verify that all images are embedded as base64 data URIs."""
    html_path = Path(html_path)
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Count base64 images
    base64_images = len(re.findall(r'src=["\']data:image/[^"\']+base64,[^"\']+["\']', html_content))
    
    # Check for any remaining relative paths
    relative_paths = re.findall(r'src=["\'](\./[^"\']+\.(?:png|jpg|jpeg|gif|svg))["\']', html_content, re.IGNORECASE)
    
    print("=" * 60)
    print("VERIFICATION REPORT")
    print("=" * 60)
    print(f"✓ Total base64-encoded images found: {base64_images}")
    
    if relative_paths:
        print(f"✗ WARNING: Found {len(relative_paths)} remaining relative paths:")
        for path in relative_paths:
            print(f"  - {path}")
        return False
    else:
        print("✓ No relative image paths found (all images are embedded)")
    
    # Check file size
    file_size_mb = html_path.stat().st_size / (1024 * 1024)
    print(f"✓ File size: {file_size_mb:.2f} MB")
    
    print("=" * 60)
    print("✓ VERIFICATION PASSED!")
    print("=" * 60)
    print("\nThe HTML file can now be downloaded and viewed offline.")
    print("All images will render correctly without needing the assets folder.")
    
    return True


if __name__ == '__main__':
    script_dir = Path(__file__).parent
    html_file = script_dir / 'apresentacao.html'
    
    if html_file.exists():
        verify_embedded_images(html_file)
    else:
        print(f"Error: {html_file} not found!")
