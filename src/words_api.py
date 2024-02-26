import requests
import random
from src.words import words as backup_words

def get_words_from_api():
    """
    Retrieves words from the random-word-api.
    If failed, uses backup words from words.py
    """
    try:
        response = requests.get("https://random-word-api.herokuapp.com/all")
        if response.status_code == 200:
            words = response.json()
            return random.choice(words)
        else:
            return random.choice(backup_words)
    except Exception:
        print("An error occurred: Failed to retrieve words from API so using backup_words stored locally.")
        return random.choice(backup_words)