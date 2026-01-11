import sys

# Add your project directory to the Python path
path = '/home/your_username/GameCenter'
if path not in sys.path:
    sys.path.append(path)

# Import your Flask application
from app import app as application  # noqa

# Set the secret key if needed
application.secret_key = 'your-secret-key-here'
