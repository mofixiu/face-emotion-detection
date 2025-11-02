# 🚀 Manual Installation Guide

## Current Installation Status:

✅ Flask - INSTALLED
✅ Gunicorn - INSTALLED  
✅ Pillow - INSTALLED
✅ NumPy - INSTALLED
❌ TensorFlow - NOT INSTALLED (SSL issues)
❌ OpenCV - NOT INSTALLED (SSL issues)

---

## 🔧 How to Fix the SSL Issue

Your system has SSL certificate verification issues. Here are 3 solutions:

### **Solution 1: Use a VPN or Different Network** (Recommended)

1. Connect to a VPN service
2. Or try a completely different WiFi network
3. Then run:

```bash
cd '/Users/mofiyinebo/Documents/Covenant University/Last Year/Alpha Semester/2025:2026 Notes/CSC415/Assignments/Models/FACE_DETECTION'
pip3 install --user tensorflow opencv-python
```

### **Solution 2: Update SSL Certificates**

```bash
# Install certifi to update SSL certificates
/Applications/Python\ 3.13/Install\ Certificates.command
```

Or manually:

```bash
pip3 install --upgrade certifi
```

### **Solution 3: Download From Browser & Install Locally**

1. **Download TensorFlow:**

   - Go to: https://pypi.org/project/tensorflow/#files
   - Download: `tensorflow-2.20.0-cp313-cp313-macosx_12_0_arm64.whl`
   - Save to: FACE_DETECTION folder

2. **Download OpenCV:**

   - Go to: https://pypi.org/project/opencv-python/#files
   - Download: `opencv_python-4.12.0.88-cp37-abi3-macosx_13_0_arm64.whl`
   - Save to: FACE_DETECTION folder

3. **Install them:**

```bash
cd '/Users/mofiyinebo/Documents/Covenant University/Last Year/Alpha Semester/2025:2026 Notes/CSC415/Assignments/Models/FACE_DETECTION'
pip3 install tensorflow-2.20.0-cp313-cp313-macosx_12_0_arm64.whl
pip3 install opencv_python-4.12.0.88-cp37-abi3-macosx_13_0_arm64.whl
```

---

## 📝 Next Steps (After Installation)

Once TensorFlow and OpenCV are installed, you'll:

1. **Step 4: Train the Model**

   ```bash
   python3 model_training.py
   ```

   This will take 1-3 hours depending on your hardware.

2. **Step 5: Test the Web App Locally**

   ```bash
   python3 app.py
   ```

   Then open: http://localhost:5000

3. **Step 6: Deploy to Render**
   - Push code to GitHub
   - Connect to Render
   - Deploy!

---

## 🆘 If You Get Stuck

Let me know once you've successfully installed TensorFlow and OpenCV, and I'll guide you through training the model!

---

**Quick Verification Command:**

```bash
python3 -c "import tensorflow; import cv2; print('✅ All packages installed!')"
```
