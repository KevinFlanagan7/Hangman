from colorama import Fore, Style


def get_instructions():
    """
    Prints game instructions to the console.
    """
    print(Fore.YELLOW + "Instructions:\n" + Style.RESET_ALL)
    print("1. Select 1 to Start Game.")
    print("2. Select a level.")
    print("3. Enter a single letter guess and press enter.")
    print("4. Quess letters until attempts run out or you guess the word.\n")
