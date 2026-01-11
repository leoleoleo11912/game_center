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
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        snake_path = os.path.join(script_dir, 'snake_game.py')
        logger.info(f"Attempting to launch Snake game from: {snake_path}")
        
        # Check if file exists
        if not os.path.exists(snake_path):
            logger.error(f"Snake game not found at: {snake_path}")
            flash('Error: Snake game file not found!', 'error')
            return redirect(url_for('home'))
            
        # Try running the game
        process = subprocess.Popen(
            [sys.executable, snake_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        logger.info(f"Snake game launched with PID: {process.pid}")
        flash('Snake game launched in a new window!', 'success')
        
    except Exception as e:
        logger.error(f"Error launching Snake game: {str(e)}", exc_info=True)
        flash(f'Error launching Snake game: {str(e)}', 'error')
    
    return redirect(url_for('home'))

@app.route('/hangman')
def hangman():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        hangman_path = os.path.join(script_dir, 'hangman.py')
        logger.info(f"Attempting to launch Hangman game from: {hangman_path}")
        
        # Check if file exists
        if not os.path.exists(hangman_path):
            logger.error(f"Hangman game not found at: {hangman_path}")
            flash('Error: Hangman game file not found!', 'error')
            return redirect(url_for('home'))
            
        # Create a batch file to run the game
        bat_path = os.path.join(script_dir, 'run_hangman.bat')
        with open(bat_path, 'w') as f:
            f.write(f'@echo off\n')
            f.write(f'title Hangman Game\n')
            f.write(f'cd /d "{script_dir}"\n')
            f.write(f'"{sys.executable}" "{hangman_path}"\n')
            f.write('pause\n')
        
        # Run the batch file in a new console window
        if os.name == 'nt':  # Windows
            import ctypes
            ctypes.windll.shell32.ShellExecuteW(None, "open", bat_path, None, script_dir, 1)
            logger.info("Hangman game launched in a new window!")
            flash('Hangman game launched in a new window!', 'success')
        else:
            # For non-Windows systems, fall back to the previous method
            process = subprocess.Popen(
                [sys.execpatible, hangman_path],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            logger.info(f"Hangman game launched with PID: {process.pid}")
            flash('Hangman game launched in a new window!', 'success')
        
    except Exception as e:
        logger.error(f"Error launching Hangman game: {str(e)}", exc_info=True)
        flash(f'Error launching Hangman game: {str(e)}', 'error')
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    try:
        print("Starting Flask server on http://127.0.0.1:5001")
        print("Press Ctrl+C to stop the server")
        app.run(debug=True, port=5001, host='0.0.0.0')
    except Exception as e:
        print(f"Error starting server: {e}")
        print("Please check if port 5001 is available and try again.")
