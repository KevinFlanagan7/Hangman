from src.ascii_art import STAGES
from src.utils import clear_screen
from src.validation import validate_guess
from src.api import get_words_from_api
from colorama import Fore, Style


def start_game(level):
    """
    Starts the hangman game with the specified level selected.
    """
    clear_screen()
    Info = "Try to guess the word by guessing one letter at a time."
    print(Fore.YELLOW + Info + Style.RESET_ALL)

    secret_word = get_words_from_api(level)

    # display secret word as underscores with spaces
    display_word = " ".join(["_" for char in secret_word])

    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = len(STAGES) - 1
    print(STAGES[incorrect_guesses])

    while True:
        print("Word to guess:", display_word)
        Guessed = ', '.join(guessed_letters)
        print(f"{Fore.YELLOW}\nGuessed letters: {Guessed}{Style.RESET_ALL}")

        while True:
            guess = input("Enter a letter and press enter: ").lower()

            if validate_guess(guess, guessed_letters):
                break

        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            clear_screen()
            print(Fore.GREEN + "Correct guess!" + Style.RESET_ALL)
            print("Attempts remaining:", max_attempts - incorrect_guesses)
            # Update the displayed word to reveal the guessed letters
            display_chars = (
                    char if char in guessed_letters else "_"
                    for char in secret_word
                    )
            display_word = " ".join(display_chars)

            print(STAGES[incorrect_guesses])

        # Check if the player has guessed all the letters correctly
            if display_word.replace(" ", "") == secret_word:
                Congrats = "Congratulations! You've guessed the word:"
                print(Fore.YELLOW + Congrats, secret_word + Style.RESET_ALL)
                break

        else:
            clear_screen()
            print(Fore.RED + "Incorrect guess!" + Style.RESET_ALL)
            incorrect_guesses += 1
            print("Attempts remaining:", max_attempts - incorrect_guesses)

            if incorrect_guesses < max_attempts:
                print(STAGES[incorrect_guesses])
            else:
                print(Fore.RED + STAGES[incorrect_guesses] + Style.RESET_ALL)

            # Checks if attempts have run out
            if incorrect_guesses == max_attempts:
                Game_Over = "Game over, you've run out of attempts!"
                print(Fore.RED + Game_Over + Style.RESET_ALL)
                print("The word was:", secret_word)
                break
