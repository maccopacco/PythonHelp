#Arianna Brieva
import json
import statistics
from diceroll import Die
import math
rollval = []

die_1 = Die()
die_2 = Die()
die_3 = Die()

#Bring in the json file
with open('numbers.json', 'w') as f:
    json.dump(rollval, f)

data = 'numbers.json'
 
max_num = 18  #Sets the maximum result for all three die
min_num = 3 #Sets minimum result for all three die
frqncies = [] #Put all the frequencies in a list

while f==open:
    for value in range(min_num, max_num):  #Gives range and tells you what to do when the json opens.
        freq = rollval.count(str(value))
        frqncies.append(freq) #Makes the list
    
y=0
for value in range(3, 19): #Gives range and tells you how to print with values.
    if value < 10:
        print(f'0{value} - {frqncies[y]}.')
        value+=1
    elif value >= 10:
        print(f'{value} - {frqncies[y]}.')
        value+=1
        

#Standard deviation code
def variance (data):
    """defines the variance for the standard deviation."""
    n = len(data)
    mean = sum(data)/n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance

def stdev(data):
    """puts the functions for the standard deviation."""
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev
    

#It prints the standard deviation
print("Standard Deviation of the sample is % s "% (stdev(data)))
    


    
