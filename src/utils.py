import os
from src.validation import validate_choice

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def select_level():
    print("Select Game Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    return validate_choice()

