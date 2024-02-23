import random
from src.ascii_art import hangman_stages
from src.words import words
from src.clear import clear_screen
from src.validation import validate_guess

def start_game():
    clear_screen()
    print("Welcome to Hangman!")
    print("Try to guess the word by guessing one letter at a time.")

    secret_word = random.choice(words)

    # display secret word as underscores with spaces
    display_word = " ".join(["_" for char in secret_word])

    
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = len(hangman_stages) - 1  

    print(hangman_stages[incorrect_guesses])

    while True:
        print("Word to guess:", display_word)
        print("\nGuessed letters:", ", ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        if not validate_guess(guess):
            continue

        # Check if the guess is in the secret word
        if guess in secret_word:
            clear_screen()
            print("Correct guess!")
            print("Attempts remaining:", max_attempts - incorrect_guesses)
            # Update the display word to reveal the guessed letters
            display_word = " ".join([char if char in guessed_letters else "_" for char in secret_word])

            print(hangman_stages[incorrect_guesses])

        # Check if the player has guessed all the letters
            if display_word.replace(" ","") == secret_word:
                print("Congratulations! You've guessed the word:", secret_word)
                break

        else:
            clear_screen()
            print("Incorrect guess!")
            incorrect_guesses += 1
            print("Attempts remaining:", max_attempts - incorrect_guesses)

            # Prints the current hangman stage
            print(hangman_stages[incorrect_guesses])

            # Check if the player has used all their attempts and displays secret word
            if incorrect_guesses == max_attempts:
                print("Sorry, you've run out of attempts!")
                print("The word was:", secret_word)
                break


  