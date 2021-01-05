#Arianna Brieva
from diceroll import Die
import json

rollvals = []
times_rolled = 10,000
        
#Refer to the classification of Die, where the die sides values were set to 6 so I don't have to do it here.
die_1 = Die()
die_2 = Die()
die_3 = Die()
        
for rollval_num in range(1,10001):
    roll = die_1.roll()+die_2.roll()+die_3.roll()
    rollvals.append(roll)
    
    #Calculate and print the roll number averages. I also made the sums and averages it's seperate
 #varibales so that It could be just an easy print statement.
sum_rolls = sum(rollvals)
avg_rolls = sum_rolls / 10,000
print(f"The average for all of the numbers is {avg_rolls}.")

        
        
#This is where you write the code to put the values into the json file.
with open('numbers.json', 'w') as f:
    json.dump(rollvals, f)


            
