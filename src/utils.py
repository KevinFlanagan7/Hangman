import os
from src.validation import validate_choice
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def select_level():
    print(Fore.CYAN + "Select Game Level:\n"+ Style.RESET_ALL)
    print("1. Easy")
    print("2. Medium")
    print("3. Hard\n")
    return validate_choice()

