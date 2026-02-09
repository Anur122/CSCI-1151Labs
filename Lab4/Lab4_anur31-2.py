"""
Program Name: Lab 4 option 2
Author: Abdullahi Nur
Purpose: Writing a hangman game. The player will guess a number between 1 and 15. 
Starter Code Info: None
Date: 2/10/26
"""

import random

number = random.randint(1,15)

hangman = [
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
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
wrong_guesses = 0

game_over = "no"

guess = input("Guess a number between 1 and 15: ")

while game_over == "no":

    guess = int(guess)

    if guess == number:
        print("Congratulations! You guessed the number!")
        game_over = "yes"

    else:
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")

        print(hangman[wrong_guesses])
        wrong_guesses += 1

        if wrong_guesses == len(hangman):
            print(" OOPS, You ran out of guesses.")
            game_over = "yes"
            break

        guess = input("Guess again: ")