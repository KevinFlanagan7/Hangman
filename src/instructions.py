from colorama import Fore, Style

def get_instructions():
    print(Fore.YELLOW + "Instructions:\n"+ Style.RESET_ALL)
    print("1. Select Start Game.")
    print("2. Select a level between Easy (4 letter word),\n   Medium (6 letter word) or Hard level (8 letter word).")
    print("3. Enter a single letter guess and press enter.")
    print("4. Continue to guess until attempts run out or you guess the word.\n")


