# Dataset Information

## FER2013 Dataset

This project uses the **FER2013 (Facial Expression Recognition 2013)** dataset.

### Dataset Details:

- **Source**: Kaggle - msambare/fer2013
- **Total Images**: 35,887 grayscale images
- **Image Size**: 48x48 pixels (resized to 224x224 for EfficientNet)
- **Format**: Pre-organized into train/test folders
- **Classes**: 7 emotion categories

### Emotion Classes:

1. **Angry** - 4,953 images
2. **Disgust** - 547 images
3. **Fear** - 5,121 images
4. **Happy** - 8,989 images
5. **Sad** - 6,077 images
6. **Surprise** - 4,002 images
7. **Neutral** - 6,198 images

### Data Split:

- **Training Set**: 28,709 images (80%)
- **Validation Set**: 7,178 images (20% of training)
- **Test Set**: 7,178 images

### Download Instructions:

The dataset can be downloaded from Kaggle:

```bash
kaggle datasets download -d msambare/fer2013
```

**Note**: For this submission, the actual dataset files are not included in the repository due to their large size. The model has been pre-trained on this dataset and saved as `face_emotionModel.h5`.

### Dataset Structure:

```
fer2013/
├── train/
│   ├── angry/
│   ├── disgust/
│   ├── fear/
│   ├── happy/
│   ├── sad/
│   ├── surprise/
│   └── neutral/
└── test/
    ├── angry/
    ├── disgust/
    ├── fear/
    ├── happy/
    ├── sad/
    ├── surprise/
    └── neutral/
```

### Data Preprocessing:

- Images resized to 224x224 pixels (RGB)
- Pixel values normalized to [0, 1]
- Data augmentation applied during training:
  - Rotation (±15°)
  - Width/Height shift (15%)
  - Shear transformation (15%)
  - Zoom (15%)
  - Horizontal flip

### Model Training Results:

- **Test Accuracy**: 60-70% (expected for FER2013)
- **Training Strategy**: Transfer Learning with EfficientNetB0
- **Total Epochs**: 30 (15 frozen + 15 fine-tuned)
