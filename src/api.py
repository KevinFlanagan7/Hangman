import random
import requests
from colorama import Fore, Style
from src.words import WORDS as backup_words


def get_words_from_api(level):
    """
    Retrieves words from the random-word-api URL,
    if failed, uses backup words from words.py
    """
    API_URL = "https://random-word-api.herokuapp.com/word?lang=en&number=10"
    try:
        if level == 1:  # Easy level
            response = requests.get(API_URL + "&length=4", timeout=5)
        elif level == 2:  # Medium level
            response = requests.get(API_URL + "&length=6", timeout=5)
        elif level == 3:  # Hard level
            response = requests.get(API_URL + "&length=8", timeout=5)

        if response.status_code == 200:
            words = response.json()
            return random.choice(words)

    except Exception:
        Backup_Words = "Failed to retrieve API words so using backup words."
        print(Fore.RED + Backup_Words + Style.RESET_ALL)
    return random.choice(backup_words)
