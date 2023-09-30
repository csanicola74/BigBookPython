import random

# constant for the number of digits in the number to guess (!) Can be set from 1 to 10
NUM_DIGITS = 3
# constant for the maximum number of guesses the player has (!) Can be set from 1 to 100
MAX_GUESSES = 10
VALID_CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart but re-created by Caroline Sanicola

I'm thinking of a {}-character code made up of numbers and letters with no repeated characters.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Almost       One character is correct but in the wrong position.
  Yes         One character is correct and in the right position.
  Nope         No character is correct.

For example, if the secret code was 24B and your guess was B43, the
clues would be Yes Almost.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a code.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not all(char in VALID_CHARS for char in guess):
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ').upper()

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # They're correct, so break out of this loop.
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
    numbers = list(
        VALID_CHARS)  # Create a list of digits 0 to 9 and letters A to Z.
    random.shuffle(numbers)  # Shuffle them into random order.

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
