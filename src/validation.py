from colorama import Fore, Style

def validate_choice():
    while True:
        try:
            choice = int(input(Fore.BLUE + "Enter your choice of 1, 2 or 3 and press enter: "+ Style.RESET_ALL))
            if 1 <= choice <= 3:
                return choice
            else:
                print(Fore.RED + "Invalid input: Please enter a number between 1 and 3." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input: Please enter a number between 1 and 3." + Style.RESET_ALL)

def validate_enter():
    """
    Validates that the user presses Enter to go back to the main menu.
    """
    while True:
        try:
            user_input = input(Fore.BLUE + "Press Enter to go back to the main menu..." + Style.RESET_ALL)
            if user_input == "":
                break  
            else:
                raise ValueError(Fore.RED + "Invalid input. Please press Enter to go back to the main menu..." + Style.RESET_ALL)
        except ValueError as e:
            print(e)
            

def validate_guess(guess, guessed_letters):
    try:
        
        if len(guess) != 1:
            raise ValueError(Fore.RED + "Invalid input: Please enter a single character." + Style.RESET_ALL)
        
        if not guess.isalpha():
            raise ValueError(Fore.RED + "Invalid input: Please enter an alphabetical character." + Style.RESET_ALL)
               
        if guess in guessed_letters:
            raise ValueError(Fore.RED + "Invalid input: You've already guessed this letter. Try another one." + Style.RESET_ALL)
        return True
    except ValueError as e:
        print(e)
        return False

    
    