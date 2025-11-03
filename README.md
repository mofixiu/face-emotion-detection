# 😊 Facial Emotion Detection Web Application

A machine learning web application that detects emotions from facial images using a Convolutional Neural Network (CNN) trained on the FER2013 dataset.

## 📋 Features

- **Emotion Detection**: Classifies faces into 7 emotions (Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral)
- **Web Interface**: Simple HTML form for user input and image upload
- **Database Storage**: Saves user information and images to SQLite database
- **Personalized Responses**: Returns emotion-specific messages
- **Face Detection**: Uses OpenCV's Haar Cascade for face detection

## 📁 Project Structure

```
FACE_DETECTION/
│
├── app.py                   # Flask web application
├── model_training.py        # Model training script
├── requirements.txt         # Python dependencies
├── database.db             # SQLite database (created on first run)
├── face_emotionModel.h5    # Trained model (created after training)
├── link_web_app.txt        # Deployment URL
├── .gitignore              # Git ignore file
├── README.md               # This file
│
└── templates/
     └── index.html         # Frontend interface
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- FER2013 dataset downloaded

### Installation

1. Navigate to the project directory:

```bash
cd FACE_DETECTION
```

2. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Training the Model

1. Ensure the FER2013 dataset is in the correct location
2. Run the training script:

```bash
python model_training.py
```

3. Wait for training to complete (may take 1-3 hours depending on hardware)
4. The trained model will be saved as `face_emotionModel.h5`

### Running the Application

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and go to:

```
http://localhost:5000
```

3. Fill in the form and upload an image to test the emotion detection!

## 🧪 Testing

Test the application with various facial images showing different emotions. The model works best with:

- Clear, front-facing photos
- Good lighting
- Single person in the image
- Visible facial features

## 📊 Model Details

- **Architecture**: CNN with 4 convolutional blocks
- **Input**: 48x48 grayscale images
- **Output**: 7 emotion classes
- **Dataset**: FER2013 (35,887 images)
- **Framework**: TensorFlow/Keras

## 🌐 Deployment

This application can be deployed to Render or similar platforms. Full deployment instructions will be provided in the guide.

## 📝 Notes

- The model's accuracy depends on image quality and facial visibility
- First-time training may take significant time
- Database and uploads folders are created automatically


## 📄 License

This project is for educational purposes.
