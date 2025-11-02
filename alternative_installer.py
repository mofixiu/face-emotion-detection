#!/usr/bin/env python3
"""
Alternative installer using Python to bypass SSL issues
This script will try to install TensorFlow and OpenCV using different methods
"""

import subprocess
import sys
import ssl
import urllib.request

def install_with_pip_no_verify():
    """Try installing with SSL verification disabled"""
    print("=" * 60)
    print("ATTEMPTING INSTALLATION WITH SSL VERIFICATION DISABLED")
    print("=" * 60)
    print("\n⚠️  Warning: This temporarily disables SSL verification\n")
    
    packages = ['tensorflow', 'opencv-python']
    
    for package in packages:
        print(f"\n[Installing {package}...]")
        try:
            # Method 1: Use pip with trusted host
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install',
                '--trusted-host', 'pypi.org',
                '--trusted-host', 'pypi.python.org', 
                '--trusted-host', 'files.pythonhosted.org',
                '--user',
                package
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ {package} installed successfully!")
            else:
                print(f"❌ Failed to install {package}")
                print(f"Error: {result.stderr[:200]}")
                
        except Exception as e:
            print(f"❌ Error installing {package}: {e}")
    
    print("\n" + "=" * 60)
    print("VERIFYING INSTALLATION")
    print("=" * 60)
    verify_installation()

def verify_installation():
    """Check which packages are installed"""
    packages = {
        'tensorflow': 'TensorFlow',
        'cv2': 'OpenCV',
        'flask': 'Flask',
        'PIL': 'Pillow',
        'numpy': 'NumPy'
    }
    
    print("\nChecking installed packages:\n")
    all_installed = True
    
    for module, name in packages.items():
        try:
            __import__(module)
            print(f"✅ {name} - Installed")
        except ImportError:
            print(f"❌ {name} - Not installed")
            all_installed = False
    
    if all_installed:
        print("\n🎉 All packages are installed! You can proceed to training.")
        print("\nNext step: Run 'python3 model_training.py'")
    else:
        print("\n⚠️  Some packages are missing. See suggestions below.")
    
    return all_installed

def main():
    print("\n🔧 ALTERNATIVE PACKAGE INSTALLER")
    print("=" * 60)
    print("This script will try to install TensorFlow and OpenCV")
    print("using methods that bypass SSL verification issues.")
    print("=" * 60)
    
    # First, try to verify if packages are already installed
    print("\n[Step 1: Checking current installation status...]")
    if verify_installation():
        print("\n✅ All required packages are already installed!")
        return
    
    # Try installation
    print("\n[Step 2: Attempting installation...]")
    input("\nPress ENTER to continue with installation...")
    install_with_pip_no_verify()
    
    print("\n" + "=" * 60)
    print("INSTALLATION COMPLETE")
    print("=" * 60)
    print("\nIf packages are still missing, try:")
    print("1. Restart your computer")
    print("2. Try a different network")
    print("3. Or use: brew install python-tk (if you have Homebrew)")

if __name__ == "__main__":
    main()
