#loops
#what is loop?
"""A loop in python is used to execute a block of code repeatedly as long as a certain condition is true 
or for a fixed number of times. loops help to reduce code length and make the program more efficient"""

#for loop: The for loop is used to iterate over a sequence (list,tuple,string,range,etc) or other iterable objects.
# it runs a specific number of times.
#Syntax: for variable in sequence:
                #code to be executed

"""for number in range(0,11+1):
    print(number)"""
    
# range(0, 10, 3) generates numbers:
# Start = 0
# Stop = 10 (10 is not included)
# Step = 3 (increase by 3 each time)
"""
for number in range(0, 10, 3):

    # print() displays the current value of number
    print(number)"""
    
# Program to print numbers in reverse order
"""for i in range(5,0,-1):
    print(i)"""
    
#while loop: The while loop is used to execute a block of code as long as the given condition is True
#it repeats the block code until the condition becomes false 
"""number = 1
while number <= 3:   #1<=3, 2<=3, 3<=3, 4<=3
    print(number)
    number = number + 1"""

"""x=10
while x>0:
   print(x)
   x-=1 """   

#Loop control statement: python provides some special statements to control the flow of loops.
#Break statement: Terminates the loop completely
"""for i in range(5):
    if i==3:
        break
    print(i)"""

#continue: Skips the current iteration and continue with the next value
"""for i in range(5):
    if i==3:
        continue
    print(i)"""
    
#nested loop
for i in range(1, 4):        # Outer loop → rows
    for j in range(1, 4):       # Inner loop → columns
        print(i * j, end="  ")
    print()  # new line after inner loop"""


