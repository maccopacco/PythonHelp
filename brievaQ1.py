# Arianna Brieva
import json
from typing import List

from diceroll import Die

# When I first ran this file, I got
# The average for all of the numbers is (10497.6, 0).
# When I removed the commas from all of the "10,000"s, I got
# The average for all of the numbers is 10.4779
# a = 10,000 makes a tuple, kinda like a list, defiantly not what you want
# b = 10000 makes an integer, what you want


# this is type hinting, I prefer to do it in languages that don't have strong typing*, if you allowed to use a better
# developer software, it helps make sure you don't rewrite variables on accident later
# *: python allows you to use a variable for multiple different types, not all languages do
# variable naming is a mix between being super specific and saving space, but in this case
# i think its worth just expanding it out
roll_values: List[int] = []
times_to_roll: int = 10000

# Refer to the classification of Die, where the die sides values were set to 6 so I don't have to do it here.
die_1 = Die()  # wont bother with type hinting here, type is obvious
die_2 = Die()
die_3 = Die()

for _ in range(0, times_to_roll):
    # use the number you defined instead of retyping it so it can be changed in one
    # place later
    # if you're not using the variable name in the loop, (which is fine), show that it isn't used

    roll: int = die_1.roll() + die_2.roll() + die_3.roll()
    roll_values.append(roll)

# Calculate and print the roll number averages. I also made the sums and averages it's separate
# variables so that it could be just an easy print statement.
sum_rolls: float = sum(roll_values)
avg_rolls: float = sum_rolls / times_to_roll
print(f"The average for all of the numbers is {avg_rolls}")
# I think the period at the end of the sentence is more confusing given you're already dealing with decimal places

# This is where you write the code to put the values into the json file.
with open('numbers.json', 'w') as f:
    json.dump(roll_values, f)
