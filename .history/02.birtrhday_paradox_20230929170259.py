"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime
import random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
