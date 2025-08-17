#!/usr/bin/env python3
"""
Test script to verify resource path resolution works correctly
"""

import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        print(f"Running in PyInstaller environment: {base_path}")
    except Exception:
        base_path = os.path.abspath(".")
        print(f"Running in development environment: {base_path}")
    
    full_path = os.path.join(base_path, relative_path)
    print(f"Resource path: {relative_path} -> {full_path}")
    print(f"File exists: {os.path.exists(full_path)}")
    return full_path

def test_resources():
    """Test various resource paths"""
    print("Testing resource path resolution...")
    print("=" * 50)
    
    # Test database
    db_path = resource_path("rms.db")
    if os.path.exists(db_path):
        print(f"✓ Database found: {db_path}")
        print(f"  Size: {os.path.getsize(db_path)} bytes")
    else:
        print(f"✗ Database not found: {db_path}")
    
    print()
    
    # Test images folder
    images_path = resource_path("images")
    if os.path.exists(images_path):
        print(f"✓ Images folder found: {images_path}")
        image_files = [f for f in os.listdir(images_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
        print(f"  Image files: {len(image_files)}")
        for img in image_files[:5]:  # Show first 5
            print(f"    - {img}")
    else:
        print(f"✗ Images folder not found: {images_path}")
    
    print()
    
    # Test specific image
    logo_path = resource_path("images/logo_p.png")
    if os.path.exists(logo_path):
        print(f"✓ Logo image found: {logo_path}")
        print(f"  Size: {os.path.getsize(logo_path)} bytes")
    else:
        print(f"✗ Logo image not found: {logo_path}")
    
    print()
    
    # Test Python modules
    modules = ["course.py", "student.py", "result.py", "report.py"]
    for module in modules:
        module_path = resource_path(module)
        if os.path.exists(module_path):
            print(f"✓ Module found: {module}")
        else:
            print(f"✗ Module not found: {module}")

if __name__ == "__main__":
    test_resources()
