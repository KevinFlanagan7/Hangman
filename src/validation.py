def validate_choice():
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")