#count of number digits   #1234
"""num=int(input("Enter a number"))
count=0  #4
while num!=0:   #1234!=0, 123!=0, 12!=0, 1!=0, 0!=0
    num=num//10   #num=123 num=12,num=1 num=0
    count+=1
print(count)"""

#Find the ASCII value of a given character
"""ch=input("Enter a charecter")  #a
asci_value=ord(ch)
print(asci_value)"""

#Find the given charecter is Alphabet or not
"""ch = input("Enter a character: ")

if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print(ch, "is an alphabet")
else:
    print(ch, "is not an alphabet")"""
    
#write a python program to find given year is leap year or not
"""Problem Explanation
What is a Leap Year?

A leap year is a year that has 366 days instead of 365 days.

Normally:

1 year = 365 days
February = 28 days

During a leap year:

1 year = 366 days
February = 29 days

Examples:
Year	Leap Year?
2024	Yes
2023	No
2000	Yes
1900	No """

# Take year as input from the user
"""year = int(input("Enter a year: "))  #2024
# Check Leap Year Conditions
# Condition 1: Year must be divisible by 4
# Condition 2: Year must NOT be divisible by 100
# Condition 3: OR year must be divisible by 400

if ( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # If the above condition is True, it is a leap year
    print(f"{year} is a leap year")
else:
    # If the condition is False, it is not a leap year
    print(f"{year} is not a leap year")"""

"""Why Do We Use 4, 100, and 400?
This is the most important part of the program.
The Earth takes approximately 365.2422 days to complete one revolution around the Sun.
But our calendar normally has only 365 days.
So, every few years, we add one extra day to February to adjust the calendar.

Rule 1: Divisible by 4
year % 4 == 0

A year divisible by 4 is usually a leap year.

Examples:

2024 % 4 = 0 → Possible leap year
2020 % 4 = 0 → Possible leap year
2023 % 4 = 3 → Not a leap year

Why 4?

Because approximately every 4 years, the extra fractional days accumulate to almost one full day.

Rule 2: Divisible by 100
year % 100 != 0

Here we exclude century years.
Examples:
1900 is divisible by 4.
But 1900 is also divisible by 100.

According to the calendar rule, not every century year is a leap year.

So, years divisible by 100 are NOT leap years.
But there is one exception.

Rule 3: Divisible by 400
year % 400 == 0

If a century year is divisible by 400, it IS a leap year.

Examples:

Year	Divisible by 4	Divisible by 100	Divisible by 400	Result
2024	Yes	No	No	Leap Year
1900	Yes	Yes	No	Not Leap Year
2000	Yes	Yes	Yes	Leap Year

Why 400?

The calendar system adjusts the extra time accumulated over centuries.

A year divisible by 400 corrects the century exception."""


num1=int(input("Enter your number"))
sign=input("Enter a operator")
num2=int(input("Enter a your number"))

if sign=="+":
    print(num1+num2)
elif sign=="-":
    print(num1-num2)
elif sign=="*":
    print(num1*num2)
elif sign=="%":
    print(num1/num2)
else:
    print("invalid sign")