import requests
import random
from src.words import WORDS as backup_words
from colorama import Fore, Style

def get_words_from_api(level):
    """
    Retrieves words from the random-word-api.
    If failed, uses backup words from words.py
    """
    try:
        if level == 1:  # Easy level
            response = requests.get("htps://random-word-api.herokuapp.com/word?lang=en&number=10&length=4")
        elif level == 2:  # Medium level
            response = requests.get("https://random-word-api.herokuapp.com/word?lang=en&number=10&length=6")
        elif level == 3:  # Hard level
            response = requests.get("https://random-word-api.herokuapp.com/word?lang=en&number=10&length=8")

        if response.status_code == 200:
            words = response.json()
            return random.choice(words)
        
    except Exception:
        print(Fore.RED + "Failed to retrive words from api so using backup words."+ Style.RESET_ALL)
    return random.choice(backup_words)