from src.ascii_art import hangman_stages
from src.utils import clear_screen
from src.validation import validate_guess
from src.api import get_words_from_api
from colorama import Fore, Style

def start_game(level):
    clear_screen()
    print(Fore.YELLOW + "Try to guess the word by guessing one letter at a time." + Style.RESET_ALL)

    secret_word = get_words_from_api(level)
    #print(secret_word)
    
    # display secret word as underscores with spaces
    display_word = " ".join(["_" for char in secret_word])
   
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = len(hangman_stages) - 1  

    print(hangman_stages[incorrect_guesses])
    
    while True:
        print("Word to guess:", display_word)
        print(Fore.YELLOW + "\nGuessed letters:", ", ".join(guessed_letters) + Style.RESET_ALL)

        while True:
            guess = input("Enter a letter and press enter: ").lower()

            if validate_guess(guess, guessed_letters):
                break        

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in secret_word:
            clear_screen()
            print(Fore.GREEN + "Correct guess!" + Style.RESET_ALL)
            print("Attempts remaining:", max_attempts - incorrect_guesses)
            # Update the display word to reveal the guessed letters
            display_word = " ".join([char if char in guessed_letters else "_" for char in secret_word])

            print(hangman_stages[incorrect_guesses])

        # Check if the player has guessed all the letters
            if display_word.replace(" ","") == secret_word:
                print(Fore.YELLOW + "Congratulations! You've guessed the word:", secret_word + Style.RESET_ALL)
                break

        else:
            clear_screen()
            print(Fore.RED + "Incorrect guess!" + Style.RESET_ALL)
            incorrect_guesses += 1
            print("Attempts remaining:", max_attempts - incorrect_guesses)

            print(hangman_stages[incorrect_guesses])

            # Check if the player has used all their attempts and displays secret word
            if incorrect_guesses == max_attempts:
                print(Fore.RED + "Game over, you've run out of attempts!" + Style.RESET_ALL)
                print("The word was:", secret_word)
                break
