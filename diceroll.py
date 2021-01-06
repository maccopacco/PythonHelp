# Arianna Brieva
# 12/28/2020
# DV2
from random import randint


# if you import randint you will be able to randomize the numbers so it's truly random
# ^ randomness is actually really hard to do with computers, so avoid the word truly

class Die:
    """Classification for the single die roll."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """The return of a random number between 1 and number of sides."""
        # It's better to return the randint in a method so that it's easier to find.
        # ^ It's best to keep your lines under 120 characters or so, keeps it cleaner
        return randint(1, self.num_sides)
