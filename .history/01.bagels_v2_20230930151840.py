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

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretCODE)
            print(clues)
            numGuesses += 1

            if guess == secretCODE:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretCODE))
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretCODE():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    digits = list(
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # Create a list of digits 0 to 9.
    random.shuffle(digits)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret code:
    secretCODE = ''
    for i in range(NUM_DIGITS):
        secretCODE += str(digits[i])
    return secretCODE


def getClues(guess, secretCODE):
    """Returns a string with the Almost, Yes, Nope clues to the user."""
    if guess == secretCODE:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretCODE[i]:
            clues.append('Yes')
        elif guess[i] in secretCODE:
            clues.append('Almost')
    if len(clues) == 0:
        return 'Nope'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
