from random import randint

from art import logo

def get_difficulty():
    """Get the difficulty level from the user."""
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        print("Invalid choice. Please enter 'easy' or 'hard'.")
        return get_difficulty()

def get_guess():
    """Prompt the user for a guess and validate it as an integer."""
    try:
        return int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return get_guess()

def check_guess(guess, answer):
    """Check if the guess is correct, too high, or too low."""
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return True
    elif guess < answer:
        print("Too Low.")
    else:
        print("Too High.")
    return False

def start_game():
    """Start the number guessing game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    remaining_guesses = get_difficulty()

    while remaining_guesses > 0:
        print(f"You have {remaining_guesses} attempts remaining to guess the number.")
        guess = get_guess()

        if check_guess(guess, answer):
            return
        remaining_guesses -= 1

        if remaining_guesses == 0:
            print("You've run out of guesses. Refresh the page to play again.")
            print(f"The answer was {answer}.")
        else:
            print("Guess again.")

start_game()

