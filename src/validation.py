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


def validate_guess(guess):
    while True:
        try:
            # Check if the guess is a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Each guess must be a single alphabetical character.")
            return True
        except ValueError as e:
            print(f"Invalid guess: {e}")
            return False
            

    
    