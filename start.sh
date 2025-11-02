#!/bin/bash
# Render startup script with optimized Gunicorn settings

echo "🚀 Starting Facial Emotion Detection..."
echo "📊 Using Gunicorn with custom timeout settings"

# Start gunicorn with config file
gunicorn --config gunicorn_config.py app:app
