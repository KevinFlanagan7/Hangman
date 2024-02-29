from src.instructions import get_instructions
from src.validation import validate_choice, validate_enter
from src.utils import clear_screen
from src.game import start_game
from src.ascii_art import welcome
from src.utils import select_level


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
            level = select_level()
            start_game(level)
            validate_enter()
        elif choice == 2:
            clear_screen()
            get_instructions()
            validate_enter()
        elif choice == 3:
            clear_screen()
            print("Quitting game...")
            print("Press Run Program above to re-start game")
            break

main()