import os
from src.validation import validate_choice
from colorama import Fore, Style
from src.ascii_art import welcome


def display_menu():
    """
    Display the main menu of the game.
    """
    welcome()
    print("1. Start Game")
    print("2. Instructions")
    print("3. Quit\n")


def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def select_level():
    """
    Prompt the user to select the game level.
    Returns the selected game level.
    """
    print(Fore.YELLOW + "Select Game Level:\n" + Style.RESET_ALL)
    print("1. Easy (4 letter word)")
    print("2. Medium (6 letter word)")
    print("3. Hard (8 letter word)\n")
    return validate_choice()
