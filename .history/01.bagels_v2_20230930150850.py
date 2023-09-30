"""Bagels, by Al Sweigart al@inventwithpython.com
2nd Version: Include numbers and letters in the guesses.
"""

import random

# constant for the number of digits in the number to guess (!) Can be set from 1 to 10
NUM_DIGITS = 4
# constant for the maximum number of guesses the player has (!) Can be set from 1 to 100
MAX_GUESSES = 20


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart but re-created by Caroline Sanicola and modified by me.

I'm thinking of a {}-digit code with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Almost       One digit is correct but in the wrong position.
  Yes         One digit is correct and in the right position.
  Nope         No digit is correct.

For example, if the secret number was L48 and your guess was 84M, the
clues would be Yes Almost.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretCODE = getSecretCODE()
        print('I have thought up a code.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
