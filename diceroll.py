#Arianna Brieva
#12/28/2020
#DV2
from random import randint
#if you import randit you will be able to randomize the numbers so it's truly random 
class Die: 
    """Classification for the single die roll."""
    def __init__(self,  num_sides = 6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
         
    def roll(self):
        """The return of a random number between 1 and number of sides.""" #It's better to return the randint in a method so that it's easier to find. 
        return randint(1, self.num_sides)
        
        