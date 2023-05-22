"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
This code is available at https://nostarch.com/big-book-small-python-programming
4. A version of this game is featured in the book, "Invent Your Own
5. Computer Games with Python" https://nostarch.com/inventwithpython
6. Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # constant for the number of digits in the number to guess (!) Can be set from 1 to 10
MAX_GUESSES = 10  # constant for the maximum number of guesses the player has (!) Can be set from 1 to 100

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart but re-created by Caroline Sanicola

I'm thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Almost       One digit is correct but in the wrong position.
  Yes         One digit is correct and in the right position.
  Nope         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Yes Almost.'''.format(NUM_DIGITS))
    
    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the Almost, Yes, Nope clues to the user."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Yes')
        elif guess[i] in secretNum:
            clues.append('Almost')
    if len(clues) == 0:
        return 'Nope'

