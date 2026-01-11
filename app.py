from flask import Flask, render_template, redirect, url_for, flash, request
import subprocess
import sys
import os
import logging

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/snake')
def snake():
    return render_template('snake_web.html')

@app.route('/hangman')
def hangman():
    return render_template('hangman_web.html')

if __name__ == '__main__':
    try:
        print("Starting Flask server on http://127.0.0.1:5001")
        print("Press Ctrl+C to stop the server")
        app.run(debug=True, port=5001, host='0.0.0.0')
    except Exception as e:
        print(f"Error starting server: {e}")
        print("Please check if port 5001 is available and try again.")
