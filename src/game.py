import random
from src.ascii_art import hangman_stages
from src.words import words
from src.clear import clear_screen

def start_game():
    clear_screen()
    print("Welcome to Hangman!")
    print("Try to guess the word by guessing one letter at a time.")
    print(hangman_stages[0])

    