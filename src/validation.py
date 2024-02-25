def validate_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError as e:
            print(f"Invalid input: {e}")


def validate_guess(guess, guessed_letters):
    try:
        # Check if the guess is a single character
        if len(guess) != 1:
            raise ValueError("Please enter a single character.")
        
        # Check if the guess is an alphabetical character
        if not guess.isalpha():
            raise ValueError("Please enter an alphabetical character.")
        
        # Check if the guess has already been guessed
        if guess in guessed_letters:
            raise ValueError("You've already guessed this letter. Try another one.")
        
        return True
    except ValueError as e:
        print("Invalid guess:", e)
        return False

    
    