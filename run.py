from src.instructions import get_instructions
from src.validation import validate_choice
from src.clear import clear_screen
from src.game import start_game
from src.ascii_art import welcome

def display_menu():
    welcome()
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit\n")
    
def main():
    while True:
        clear_screen()
        display_menu()
        choice = validate_choice()

        if choice == 1:
            clear_screen()
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