#!/bin/bash

# Installation Script for Facial Emotion Detection Project
# Run this script when you have a stable internet connection

echo "=========================================="
echo "Installing Dependencies"
echo "=========================================="
echo ""

# Try installing all packages at once
echo "[1/2] Attempting to install all packages..."
pip3 install --user tensorflow flask opencv-python pillow numpy gunicorn

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All packages installed successfully!"
    echo ""
    echo "You can now proceed to train the model by running:"
    echo "python3 model_training.py"
else
    echo ""
    echo "❌ Installation failed. Trying individual installations..."
    echo ""
    
    # Try installing packages one by one
    echo "[1/6] Installing Flask..."
    pip3 install --user flask
    
    echo "[2/6] Installing Gunicorn..."
    pip3 install --user gunicorn
    
    echo "[3/6] Installing Pillow..."
    pip3 install --user pillow
    
    echo "[4/6] Installing NumPy..."
    pip3 install --user numpy
    
    echo "[5/6] Installing OpenCV..."
    pip3 install --user opencv-python
    
    echo "[6/6] Installing TensorFlow..."
    pip3 install --user tensorflow
    
    echo ""
    echo "Installation complete! Check above for any errors."
fi

echo ""
echo "=========================================="
echo "Verifying Installation"
echo "=========================================="
python3 << 'EOF'
import sys

packages = {
    'tensorflow': 'TensorFlow',
    'flask': 'Flask', 
    'cv2': 'OpenCV',
    'PIL': 'Pillow',
    'numpy': 'NumPy'
}

print("\nChecking installed packages:\n")
for module, name in packages.items():
    try:
        __import__(module)
        print(f"✅ {name} - Installed")
    except ImportError:
        print(f"❌ {name} - Not installed")

print("\nDone!")
EOF
