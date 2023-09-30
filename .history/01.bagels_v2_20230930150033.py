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

I'm thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:



'''.format(NUM_DIGITS))
