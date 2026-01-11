# 🎮 Game Center

A web-based game center featuring two classic games: Snake and Hangman. This project is built with Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend.

## 🎮 Features

### 🐍 Snake Game
- Classic Snake gameplay with keyboard controls
- Score tracking
- Game over detection (hitting walls or self)
- Responsive design that works on different screen sizes

### 💀 Hangman
- Word guessing game with a visual hangman
- Keyboard and mouse input support
- Visual feedback for correct/incorrect guesses
- Game state management (win/lose conditions)

## 🚀 Technologies Used

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Version Control**: Git, GitHub

## 🛠️ Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/leoleoleo11912/game_center.git
   cd game_center
   ```

2. **Install dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open in your browser**:
   ```
   http://127.0.0.1:5001
   ```

## 🎮 How to Play

### Snake Game
- Use arrow keys (←, →, ↑, ↓) to control the snake
- Eat the red food to grow longer and increase your score
- Avoid hitting the walls or yourself
- Try to get the highest score possible!

### Hangman
- Guess letters by clicking the on-screen keyboard or typing on your physical keyboard
- You have 6 incorrect guesses before the game ends
- Guess all letters in the word to win
- Press Enter to start a new game when the current game ends

## 📂 Project Structure

```
game_center/
├── app.py                # Main Flask application
├── templates/
│   ├── index.html        # Home page
│   ├── snake_web.html    # Snake game interface
│   └── hangman_web.html  # Hangman game interface
├── snake_game.py         # Original terminal Snake game
├── hangman.py           # Original terminal Hangman game
└── highscores.json      # Score tracking (future implementation)
```

## 🛠 Challenges & Solutions

### 1. Terminal to Web Conversion
**Problem**: Initially, both games were terminal-based, which limited accessibility and user experience.
**Solution**: Rewrote both games using HTML5, CSS3, and vanilla JavaScript to create interactive web interfaces while maintaining the core game logic.

### 2. Hangman ASCII Art Display
**Problem**: The hangman's ASCII art wasn't displaying correctly in the browser due to formatting issues with multi-line strings in JavaScript.
**Solution**: Restructured the hangman stages as an array of strings with proper line breaks and used template literals for better readability and maintenance.

### 3. Keyboard Input Handling
**Problem**: The games needed to support both mouse clicks and keyboard input for better accessibility.
**Solution**: Implemented comprehensive event listeners for both keyboard and mouse events, with visual feedback for keyboard interactions.

### 4. Game State Management
**Problem**: Managing game state between browser refreshes was challenging.
**Solution**: Implemented client-side game state management using JavaScript variables and ensured all game state is reset properly when starting a new game.

### 5. Cross-browser Compatibility
**Problem**: Some JavaScript features worked differently across browsers.
**Solution**: Used standard JavaScript practices and tested on multiple browsers to ensure consistent behavior.

## 🔧 Future Improvements

- Add user authentication
- Implement high score system
- Add more games
- Mobile responsiveness improvements
- Sound effects and animations
- Multiplayer support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Created by Leo - 2024
