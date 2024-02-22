import os
from src.instructions import get_instructions
from src.validation import validate_choice

def clear_screen():
    os.system('cls')


def display_menu():
    clear_screen()
    print("Welcome to Hangman!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")

def main():
    while True:
        display_menu()
        choice = validate_choice()

        if choice == 1:
            print("Starting game...")
            input("Press Enter to return to the main menu...")
        elif choice == 2:
            print("Instructions:")
            print(get_instructions())
            input("Press Enter to return to the main menu...")
        elif choice == 3:
            print("Quitting game...")
            break

main()