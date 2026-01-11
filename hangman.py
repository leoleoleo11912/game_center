import os
import random
from typing import Optional, Set

# Constants
MAX_ATTEMPTS = 6
WORDS = [
    "python", "hangman", "programming", "computer", "keyboard",
    "developer", "software", "algorithm", "variable", "function"
]


class HangmanGame:
    def __init__(self):
        self.word = ""
        self.word_completion = ""
        self.guessed_letters: Set[str] = set()
        self.guessed_words: Set[str] = set()
        self.attempts_left = MAX_ATTEMPTS
        self.game_over = False
        self.won = False
        self._last_displayed_stage = None

    def initialize_game(self) -> None:
        """Initialize a new game with a random word and reset all game state."""
        self.word = random.choice(WORDS)
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = set()
        self.guessed_words = set()
        self.attempts_left = MAX_ATTEMPTS
        self.game_over = False
        self.won = False
        self._last_displayed_stage = None


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_hangman_stage(tries: int) -> str:
    """Return the appropriate hangman stage based on number of incorrect tries.

    Args:
        tries: Number of incorrect guesses so far (0 to 6)
    """
    stages = [
        # Initial empty state (0 incorrect guesses)
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        # Head (1 incorrect guess)
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Head, torso (2 incorrect guesses)
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Head, torso, one arm (3 incorrect guesses)
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        # Head, torso, both arms (4 incorrect guesses)
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        # Head, torso, both arms, one leg (5 incorrect guesses)
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        # Final state: complete hangman (6 incorrect guesses)
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """
    ]
    # Ensure we don't go out of bounds
    return stages[min(tries, len(stages) - 1)]


def display_game_state(game: HangmanGame) -> None:
    """Display the current game state including hangman and word progress."""
    clear_screen()
    print("Let's play Hangman!")
    print(f"Attempts left: {game.attempts_left}")
    print(f"Guessed letters: {', '.join(sorted(game.guessed_letters))}")
    print(get_hangman_stage(MAX_ATTEMPTS - game.attempts_left))
    print(f"Word: {game.word_completion}")


def get_valid_guess() -> Optional[str]:
    """Get and validate user input."""
    while True:
        try:
            guess = input("\nGuess a letter or word (or 'quit' to exit): ").lower()
            if guess == 'quit':
                return None
            if not guess.isalpha():
                print("Please enter only letters.")
                continue
            return guess
        except (EOFError, KeyboardInterrupt):
            print("\nGame ended by user.")
            return None


def process_guess(game: HangmanGame, guess: str) -> bool:
    """Process the user's guess and update game state."""
    if len(guess) == 1:  # Single letter guess
        if guess in game.guessed_letters:
            print(f"You already guessed the letter {guess}")
            return False

        game.guessed_letters.add(guess)

        if guess not in game.word:
            print(f"{guess} is not in the word.")
            game.attempts_left -= 1
            return False

        # Update word completion with correctly guessed letter
        word_list = list(game.word_completion)
        for i, letter in enumerate(game.word):
            if letter == guess:
                word_list[i] = guess
        game.word_completion = "".join(word_list)

        if "_" not in game.word_completion:
            game.won = True
            game.game_over = True
        return True

    else:  # Whole word guess
        if guess in game.guessed_words:
            print(f"You already guessed the word {guess}")
            return False

        game.guessed_words.add(guess)

        if guess == game.word:
            game.word_completion = game.word
            game.won = True
            game.game_over = True
            return True

        print(f"{guess} is not the word.")
        game.attempts_left -= 1
        return False


def show_game_result(game: HangmanGame) -> None:
    """Display the final game result."""
    if game.won:
        print("\nCongratulations, you guessed the word! You win!")
    else:
        print(f"\nSorry, you ran out of tries. The word was {game.word}. Maybe next time!")


def play_hangman() -> None:
    """Main game loop."""
    game = HangmanGame()
    game.initialize_game()
    clear_screen()  # Clear screen at the start of each game

    while not game.game_over and game.attempts_left > 0:
        display_game_state(game)
        guess = get_valid_guess()

        if guess is None:  # User chose to quit
            return

        process_guess(game, guess)

        if game.attempts_left == 0:
            game.game_over = True

    display_game_state(game)
    show_game_result(game)


def main() -> None:
    """Main entry point for the Hangman game."""
    while True:
        play_hangman()
        try:
            play_again = input("\nPlay Again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing!")
                break
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
