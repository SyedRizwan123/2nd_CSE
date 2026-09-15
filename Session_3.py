#Bodmas
"""BODMAS Rule

The BODMAS rule is a sequence that tells us the correct order of operations when solving mathematical expressions.

BODMAS stands for:

B → Brackets (solve inside brackets first)

O → Orders (powers, roots, exponents, square roots, etc.)

D → Division (÷)

M → Multiplication (×)

A → Addition (+)

S → Subtraction (−)"""

"""result = 10+(3*-8)/4   #-24/4=-6+10=4
print(result)"""

"""result1=4**2+5/2*3  #16 2.5*3=7.5+16=23.5
print(result1)"""

"""result2 = (8+4)*3/2   #12* 1.5
print(result2)"""

"""result3=16/4+2**3-6    #8 4=12-6
print(result3)"""

# Program to calculate the Area of a Circle
"""What is the Problem?
The task is to calculate the area of a circle when the radius is given by the user."""

"""Understanding the Problem in Simple Words
==> A circle is a round shape (like a coin or plate).
==> The radius is the distance from the center to the boundary.
==> Using the radius, we calculate how much space is inside the circle (area).

Steps to Solve the Problem
==> Take input from the user (radius).
==> Use the formula → Area = π × r × r
==> Calculate the result.
==> Display the output."""

# Define a constant value for PI
"""PI = 3.1415

# Take input from the user (radius of the circle)
# input() takes value as string, so we convert it to float
radius = float(input("Enter radius of circle: "))   #5

# Calculate the area using formula: PI * r * r
area = PI * radius * radius

# Display the result
print("Area of circle:", area)"""



# Program to calculate the Area of a Rectangle
"""Problem Explanation: Area of a Rectangle
What is the Problem?
we need to calculate the area of a rectangle using:

Length
Breadth (Width)

Mathematical Concept

A=l×b

A → Area of rectangle
l → Length
b → Breadth

Simple Understanding
A rectangle is a four-sided shape (like a book or table).
To find its area:
Multiply length × breadth

Steps to Solve
Take length and breadth as input from user
Apply formula → length × breadth
Display the result  """


"""Length=int(input("enter a value"))
Breadth=int(input("Enter a value"))
area=Length*Breadth
print(area )"""


# Program to calculate Total and Average of 3 subjects
"""eng=78
tel=89
maths=90
total=eng+tel+maths
print(total)  #257
Avg=total/3
print(Avg)"""

"""Problem Explanation: Simple Interest
What is the Problem?

You need to calculate Simple Interest (SI) based on:

Principal Amount (P)
Time (T) in years
Rate of Interest (R) in percentage

# Mathematical Concept
SI= P×T×R / 100
	
P → Principal (amount)
T → Time (years)
R → Rate (%)

# Simple Understanding
You invest some money (principal)
Bank gives interest based on:
time
rate
Formula calculates how much extra money you earn

# Steps to Solve
Take amount, time, rate as input
Apply formula → (P × T × R) / 100
Display the result"""

# Program to calculate Simple Interest

# Take input from user
# Convert values into integers
amount = int(input("Enter principal amount: "))  #100000
time = int(input("Enter time (in years): "))    #1
rate = int(input("Enter rate of interest (%): "))   #12

# Calculate simple interest using formula
simple_interest = (amount * time * rate) / 100

# Display result
print("\nRate of Interest =", rate, "%")
print("Simple Interest =", simple_interest)
