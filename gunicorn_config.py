# Gunicorn configuration for Render deployment
# Optimized for emotion detection with face processing

import multiprocessing

# Worker configuration
workers = 1  # Use only 1 worker to save memory on free tier
worker_class = 'sync'
worker_connections = 10

# Timeout configuration (increase for slow face detection)
timeout = 120  # 2 minutes (default is 30 seconds)
graceful_timeout = 120
keepalive = 5

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Performance
preload_app = True  # Load model once, share across workers
max_requests = 100  # Restart worker after 100 requests (prevent memory leaks)
max_requests_jitter = 10

# Binding
bind = '0.0.0.0:10000'
