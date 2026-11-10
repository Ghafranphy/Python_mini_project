"""
====================================================
Random Number Generator – Python Practice Project
===================================================
This project demonstrates different approaches to generating and comparing random numbers in Python. It covers the use of the random module,
functions, recursive function calls, while loops, for loops, conditional statements, and loop termination using break statements. 
The main purpose of this beginner-level project is to strengthen Python programming skills through practical exercises.
"""

# random number generator function
import random
def random_number_generator(y):
    random_number=random.randint(1,y)
    if random_number == y:
        print(f'the number is equal to  {random_number}')
    else:
        print("Guess is wrong")
        return random_number_generator(y)
    
random_number_generator(6)    


##########################################################
#  random number generator function using while loop
import random
def random_number_generator(y):
    random_number=random.randint(1,y)
    while random_number==y:
        print("Guess are equall")
        break
    else:
        print('Number are not equall')
        return random_number
        

random_number_generator(6)
#############################################################
#  random number generator function using while loop
import random
def random_number_generator(y): 
    random_number=0     
    while random_number != y:
      random_number = random.randint(1, y)
      print(random_number)
    else:
        return random_number

random_number_generator(6)
###################################################################################
#  random number generator function using for loop
import random
from itertools import count   # python built in function
for i in count():
    y=random.randint(0,10)     # random number generated
    if i==y:
        print(f'Both numbers {i} and {y} are same')
        break
    else:
        print(f'Both number {i} and {y} are not same')
print("Loop completed")                               
