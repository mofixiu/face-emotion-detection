# 🚨 RECOVERY GUIDE - Internet Disconnected During Training

## ✅ Good News!

Your model was **automatically saved** during Phase 1 training! The `ModelCheckpoint` callback saved the best model to `/content/best_model.h5`.

---

## 🔧 Recovery Steps

### **Option 1: Load the Saved Model and Continue (Recommended)**

Run this code in a **new cell** in your Colab notebook:

```python
# Load the saved model from Phase 1
from tensorflow.keras.models import load_model

print("📂 Loading saved model...")
model = load_model('/content/best_model.h5')
print("✅ Model loaded successfully!")

# Verify it works
model.summary()

# Check if model is also in Google Drive
import os
if os.path.exists('/content/drive/MyDrive/FER2013_Models/face_emotionModel.h5'):
    print("✅ Model also saved to Google Drive!")
else:
    print("ℹ️ Model not yet saved to Drive (will save at end)")
```

### **Option 2: Skip Phase 1 and Continue to Phase 2**

Since Phase 1 completed (15/15 epochs), you can load the model and go straight to Phase 2 (fine-tuning):

```python
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import Adam

# Load saved model
model = load_model('/content/best_model.h5')
print("✅ Model loaded from Phase 1!")

# Get the base model
base_model = model.layers[0]

# Unfreeze for Phase 2
base_model.trainable = True

# Recompile with lower learning rate
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("✅ Ready for Phase 2 fine-tuning!")

# Now run Phase 2 training
# (Copy the Phase 2 training cell and run it)
```

### **Option 3: Just Download What You Have**

If Phase 1 is good enough (should have ~60-65% accuracy), you can:

```python
from tensorflow.keras.models import load_model
from google.colab import files

# Load the saved model
model = load_model('/content/best_model.h5')

# Save with proper name
model.save('/content/face_emotionModel.h5')
print("✅ Model saved as face_emotionModel.h5")

# Save to Google Drive
model.save('/content/drive/MyDrive/FER2013_Models/face_emotionModel.h5')
print("✅ Model saved to Google Drive!")

# Download to your computer
files.download('/content/face_emotionModel.h5')
print("📥 Downloading to your computer...")
```

---

## 📊 What Phase 1 Accomplished

Phase 1 (15 epochs with frozen base) typically gives:

- **Training Accuracy:** 55-65%
- **Validation Accuracy:** 50-60%
- **Status:** Working model, but Phase 2 will improve it!

Phase 2 (fine-tuning) would add another:

- **+5-10% accuracy improvement**
- **Final accuracy:** 60-70%

---

## 🎯 Recommended Action

**If you want higher accuracy:**

1. Use Option 1 or 2 above
2. Continue to Phase 2 (another 15 epochs)
3. Total time: 15-25 more minutes

**If Phase 1 accuracy is acceptable:**

1. Use Option 3 above
2. Download the model now
3. Use it in your Flask app!

---

## 💡 Pro Tip: Prevent Future Disconnections

Add this cell at the beginning of your notebook to prevent timeouts:

```python
# Keep Colab session alive
import time
from IPython.display import display, Javascript

def keep_alive():
    while True:
        display(Javascript('console.log("Keep alive")'))
        time.sleep(60)  # Every 60 seconds

# Run in background
import threading
thread = threading.Thread(target=keep_alive)
thread.daemon = True
thread.start()

print("✅ Keep-alive started!")
```

---

## ❓ Which Option Should You Choose?

**Choose Option 1 or 2 if:**

- You want 65-70% accuracy
- You have 30 more minutes
- Internet is stable now

**Choose Option 3 if:**

- 60-65% accuracy is acceptable
- You're short on time
- Want to start testing your Flask app now

---

## 🚀 Quick Command Summary

**To resume and continue training:**

```python
model = load_model('/content/best_model.h5')
# Then continue with Phase 2 training cell
```

**To download what you have:**

```python
from google.colab import files
from tensorflow.keras.models import load_model

model = load_model('/content/best_model.h5')
model.save('/content/face_emotionModel.h5')
files.download('/content/face_emotionModel.h5')
```

---

Let me know which option you want to take! 🎉
