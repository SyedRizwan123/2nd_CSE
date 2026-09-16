# Program to swap two numbers using a third variable
# Take input from user
"""a = int(input("Enter value of a: "))  #10
b = int(input("Enter value of b: ")) #20
# Swapping logic using third variable
temp = a   # store value of a in temp   #10
a = b      # assign value of b to a    #20
b = temp   # assign value of temp (old a) to b  #10

# Display values after swapping
print("After swapping a =", a, "b =", b)"""

# Program to swap two numbers without using a third variable
"""a = int(input("Enter value of a: "))  #10
b = int(input("Enter value of b: "))   #20

a=a+b  # Step 1: a now holds the sum of a and b   #30
b=a-b  # Step 2: b now holds the original value of a  #30-20=10 
a=a-b  # Step 3: a now holds the original value of b  #30-10=20

a,b=b,a
# Display values after swapping
print("\nAfter swapping a =", a, "b =", b)"""


# Program to calculate Gross Salary
# Take basic salary input from user
"""basic_salary = int(input("Enter basic salary: "))  #30000

# Calculate allowances based on percentage
hra = basic_salary * 0.8   # 80% of basic salary
ta = basic_salary * 0.4    # 40% of basic salary
da = basic_salary * 0.3    # 30% of basic salary

# Calculate gross salary
gross_salary = basic_salary + hra + ta + da
# Display results
print("\nHRA (80%) =", hra)
print("TA (40%) =", ta)
print("DA (30%) =", da)
print("\nGross Salary =", gross_salary)"""

# Program to calculate sum of N natural numbers
"""Problem Explanation: Sum of N Natural Numbers
What is the Problem?
we need to calculate the sum of first N natural numbers.

Natural numbers → 1, 2, 3, 4, ... , N
Example: If N = 5 → Sum = 1 + 2 + 3 + 4 + 5 = 15

#Mathematical Concept
S=n(n+1)/2
S → Sum of numbers
n → Number of terms

#Simple Understanding
--> Instead of adding numbers one by one
--> We use a direct formula to save time

#Steps to Solve
--> Take n value from user
--> Apply formula → n × (n + 1) / 2
--> Display the result"""

# Take input from user
"""n = int(input("Enter n value: "))  #5

# Calculate sum using formula
sum_n = (n * (n + 1)) // 2   # // for integer result
#n=5 then sum_n = (5 * (5 + 1)) // 2 = (5 * 6) // 2 = 30 // 2 = 15

# Display result
print("Sum of", n, "natural numbers is =", sum_n)"""

# Program to calculate sum of squares of N natural numbers
""" Problem Explanation: Sum of Squares of N Natural Numbers
# What is the Problem?
we need to calculate the sum of squares of first N natural numbers.

Example:
If N = 3
Sum = 1² + 2² + 3² = 1 + 4 + 9 = 14

Mathematical Concept

S=n(n+1)(2n+1)/6

--> S → Sum of squares
--> n → Number of terms

# Simple Understanding
--> Instead of calculating:1² + 2² + 3² + ... + n²
--> We use a direct formula to save time

#Steps to Solve
--> Take n value from user
--> Apply formula → n(n+1)(2n+1)/6
--> Display the result """
# Take input from user
"""n = int(input("Enter n value: "))

# Calculate result using formula
result = (n * (n + 1) * (2 * n + 1)) // 6   # // gives integer result
# If n=3 then result = (3 * (3 + 1) * (2 * 3 + 1)) // 6
# = (3 * 4 * 7) // 6

# Display result
print("Sum of squares of", n, "is =", result)"""

# Program to calculate Volume of a Cylinder
""" Problem Explanation: Volume of a Cylinder
# What is the Problem?
we need to calculate the volume of a cylinder using:

--> Radius (r)
--> Height (h)

Mathematical Concept
Volume (V) of cylinder = πr²h 

V → Volume
r → Radius
h → Height
π (pi) → 3.1415

# Simple Understanding
--> A cylinder is like a pipe or water tank
--> Volume means how much space it can hold
--> Formula → π × r² × h 

# Steps to Solve
--> Take radius and height as input
--> Apply formula → π × r × r × height
--> Display the result """
# Define constant PI
"""PI = 3.1415

# Take input from user
radius = float(input("Enter radius: "))     # 3.0
height = float(input("Enter height: "))     # 5.0

# Calculate volume using formula: PI * r * r * h
volume = PI * radius * radius * height   # volume = 3.1415 * 3.0 * 3.0 * 5.0 = 141.3675

# Display the result
print("Volume of Cylinder:", volume)"""

#membership operators
"""my_list=[1,2,3,4,5]
a=3
b=7
print(a in my_list)
print(b in my_list)

print(a not in my_list)
print(b not in my_list)"""

"""a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))

print(a is b)
print(a is not b)"""


x=10
y=20
if x<=y:
    if y<=x:
        print("True")
    else:
        print("false")
else:
    print("Condition is false")