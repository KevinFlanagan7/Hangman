from colorama import Fore, Style


def validate_choice():
    """
    Validate user input for menu choice.
    Returns the validated menu choice.
    """
    while True:
        Enter_Choice = "Enter your choice of 1, 2 or 3 and press enter:\n"
        Invalid_Choice = "Invalid input, enter a number between 1 and 3."
        try:
            choice = int(input(Fore.YELLOW + Enter_Choice + Style.RESET_ALL))
            if 1 <= choice <= 3:
                return choice
            else:
                print(Fore.RED + Invalid_Choice + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + Invalid_Choice + Style.RESET_ALL)


def validate_enter():
    """
    Validates that the user presses Enter to go back to the main menu.
    """
    while True:
        Press_Enter = "Press Enter to go back to the main menu...\n"
        Invalid = "Invalid input, press Enter to go back to the main menu...\n"
        try:
            user_input = input(Fore.YELLOW + Press_Enter + Style.RESET_ALL)
            if user_input == "":
                break
            else:
                raise ValueError(Fore.RED + Invalid + Style.RESET_ALL)
        except ValueError as e:
            print(e)


def validate_guess(guess, guessed_letters):
    """
    Validate user input for guessing a letter.
    Returns True if the guess is valid, False otherwise.
    """
    try:
        Single_Char = "Invalid input: Please enter a single character."
        Alph_Char = "Invalid input: Please enter an alphabetical character."
        Guessed = "You've already guessed this letter. Try another one."
        if len(guess) != 1:
            raise ValueError(Fore.RED + Single_Char + Style.RESET_ALL)
        if not guess.isalpha():
            raise ValueError(Fore.RED + Alph_Char + Style.RESET_ALL)
        if guess in guessed_letters:
            raise ValueError(Fore.RED + Guessed + Style.RESET_ALL)
        return True
    except ValueError as e:
        print(e)
        return False
