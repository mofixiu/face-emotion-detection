"""
TEST VERSION of app.py - For local testing without TensorFlow
This version simulates the emotion detection for testing the UI/UX
DO NOT DEPLOY THIS VERSION - Use app.py for deployment
"""

from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Emotion labels and responses
EMOTIONS = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

EMOTION_RESPONSES = {
    'angry': "You look angry! Take a deep breath and relax. 😤",
    'disgust': "You seem disgusted. What's bothering you? 😖",
    'fear': "You appear fearful. Don't worry, everything will be okay! 😨",
    'happy': "You're happy! Keep smiling, it looks great on you! 😊",
    'sad': "You look sad. Cheer up! Better days are ahead. 😢",
    'surprise': "You seem surprised! What caught your attention? 😲",
    'neutral': "You have a neutral expression. Calm and composed! 😐"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route for the web application"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            email = request.form.get('email')
            age = request.form.get('age')
            
            # Validate inputs
            if not name or not email or not age:
                return render_template('index.html', error="All fields are required!")
            
            # Check if image was uploaded
            if 'image' not in request.files:
                return render_template('index.html', error="No image uploaded!")
            
            file = request.files['image']
            
            if file.filename == '':
                return render_template('index.html', error="No image selected!")
            
            # Check file type
            allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
            if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
                return render_template('index.html', error="Invalid file type! Please upload an image file.")
            
            # Save the uploaded file
            filename = f"{name.replace(' ', '_')}_{file.filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # SIMULATE emotion detection (for testing only)
            print("\n" + "="*60)
            print("🧪 TEST MODE - Simulating emotion detection")
            print("="*60)
            
            # Randomly select an emotion for testing
            emotion = random.choice(EMOTIONS)
            confidence = round(random.uniform(0.65, 0.95), 2)
            
            print(f"📸 Image saved: {filename}")
            print(f"😊 Detected emotion: {emotion.upper()}")
            print(f"📊 Confidence: {confidence * 100:.1f}%")
            print("="*60 + "\n")
            
            # Get personalized message
            message = EMOTION_RESPONSES.get(emotion, "Emotion detected!")
            
            # Prepare result
            result = {
                'name': name,
                'emotion': emotion.capitalize(),
                'confidence': f"{confidence * 100:.1f}%",
                'message': message
            }
            
            return render_template('index.html', result=result)
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return render_template('index.html', error=f"An error occurred: {str(e)}")
    
    # GET request - display the form
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint for deployment platforms"""
    return {'status': 'ok', 'mode': 'test'}, 200

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🧪 RUNNING IN TEST MODE")
    print("="*60)
    print("⚠️  This is a TEST version without TensorFlow")
    print("⚠️  Emotions are randomly generated for UI testing")
    print("⚠️  Use app.py for production deployment")
    print("="*60)
    print("\n🌐 Starting Flask server...")
    print("📱 Open: http://localhost:5000")
    print("⏹️  Press CTRL+C to stop\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
