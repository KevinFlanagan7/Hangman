def validate_choice():
    while True:
        try:
            choice = int(input("Enter your choice of 1, 2 or 3 and press enter: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid input: Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input: Please enter a number between 1 and 3.")




def validate_enter():
    """
    Validates that the user presses Enter to go back to the main menu.
    """
    while True:
        try:
            user_input = input("Press Enter to go back to the main menu...")
            if user_input == "":
                break  
            else:
                raise ValueError("Invalid input. Please press Enter to go back to the main menu...")
        except ValueError as e:
            print(e)
            

def validate_guess(guess, guessed_letters):
    try:
        
        if len(guess) != 1:
            raise ValueError("Invalid input: Please enter a single character.")
        
        if not guess.isalpha():
            raise ValueError("Invalid input: Please enter an alphabetical character.")
               
        if guess in guessed_letters:
            raise ValueError("Invalid input: You've already guessed this letter. Try another one.")
        
        return True
    except ValueError as e:
        print(e)
        return False

    
    