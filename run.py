from src.instructions import get_instructions
from src.validation import validate_choice, validate_enter
from src.utils import clear_screen, select_level, display_menu
from src.game import start_game


def main():
    """
    This function displays the menu for the game.
    It loops until the user selects a valid input
    to play game, view instructions or quit game.
    """
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
