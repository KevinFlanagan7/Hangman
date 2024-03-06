import pyfiglet
from colorama import Fore, Style


def welcome():
    """
    Displays welcome message in ASCII art format.
    """
    message = pyfiglet.figlet_format("Welcome\nTo\nHangman")
    print(Fore.YELLOW + message + Style.RESET_ALL)


STAGES = [
    """
      +---+
          |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]
