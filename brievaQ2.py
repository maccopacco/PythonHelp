# Arianna Brieva
import json
import statistics  # seems to not be needed
from typing import List

from diceroll import Die
import math

# space between imports

# rollval = []
# ^ i'll explain why I commented this out in a second

die_1 = Die()
die_2 = Die()
die_3 = Die()

file_name: str = 'numbers.json'  # use your variables!, and name them a bit better

# with open('numbers.json', 'w') as f:
#     json.dump(rollval, f)

# what this code does, along with the commented out variable above, is takes your empty list and
# writes it to the file numbers.json, effectively erasing it.
# two things:
# 1, don't copy paste too fast
# 2, test as you go, because if you wrote that code then printed out the variable rollval, you'd see its an empty list

# Reads json
with open('numbers.json', 'r') as f:
    # notice passing in open(filename, 'r') as you only need to read the file
    # https://www.w3schools.com/python/ref_func_open.asp
    roll_values: List[int] = json.load(f)

max_num = 6 * 3  # Sets the maximum result for all three die
min_num = 1 * 3  # Sets minimum result for all three die
frequencies: List[int] = []  # Put all the frequencies in a list

# while f == open:
for value in range(min_num, max_num + 1):  # Gives range and tells you what to do when the json opens.
    freq = roll_values.count(value)  # dont want str(value) here, when you count the strings in the list of integers
    # you'll get 0.
    frequencies.append(freq)  # appends to the list, the list is already made

pad = len(str(len(roll_values)))
# count amount of values (~10,000), turn to string, "10000", count length of string, 5, that's the amount
# we want to pad to line stuff up

for value in range(0, max_num - min_num + 1):  # Gives range and tells you how to print with values.
    # Loop from 0 (first index), to last index
    # a few things about this block:
    # if you're gonna be adding one to the value in either case, move it out of the block
    # but you don't need to be adding 1 to value anyway, the loop will do that for you

    # string.rjust(amount of characters to pad, character to pad with)
    # pad value with up to 2 zeros (3 - 18, so we're good)
    # pad frequency at index value with spaces, and the amount we'll pad it with is the calculated amount
    print(f'{str(value + min_num).rjust(2, " ")} - {str(frequencies[value]).rjust(pad, " ")}')

# this is just for funnies
message = "oooh, look how pretty all this spacing is"
carrots = ""
for _ in range(0, len(message)):
    carrots += "^"

print(f'\n{carrots}\n{message}\n')


# Standard deviation code
def variance(data):
    """defines the variance for the standard deviation."""
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


def stdev(data):
    """puts the functions for the standard deviation."""
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


# It prints the standard deviation
# its been forever since i learned about this stuff, not sure if in this case
# the stdev is a function of frequencies or the raw data, but either way its not a function of the file name...
print("Standard Deviation of the sample is % s " % (stdev(frequencies)))
