import os
from src.instructions import get_instructions
from src.validation import validate_choice
from src.clear import clear_screen
from src.game import start_game


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Welcome to Hangman!")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit")
    

def main():
    while True:
        clear_screen()
        display_menu()
        choice = validate_choice()

        if choice == 1:
            start_game()
            input("Press Enter to return to the main menu...")
        elif choice == 2:
            clear_screen()
            get_instructions()
            input("Press Enter to return to the main menu...")
        elif choice == 3:
            clear_screen()
            print("Quitting game...")
            break

main()