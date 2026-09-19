"""ch = input("Enter a character: ")
if ch.isdigit():  # Check if the input consists of digits only
    print(f"{ch} is a number")
elif len(ch) == 1:  # Check if the input is a single character
    if ch == '#':
        print(f"{ch} is the '#' symbol")
    elif 'a' <= ch <= 'z':
        print(f"{ch} is a small letter")
    elif 'A' <= ch <= 'Z':
        print(f"{ch} is a capital letter")
    else:
        print(f"{ch} is a special character")
else:
    print(f"{ch} is a special character")"""
    
#Write a python program to check Gender Eligible to vote or not    
"""gend = input("Enter gender (M/F): ").upper() # Convert to uppercase for case-insensitive comparison
age = int(input("Enter age: "))
if gend == 'F':                 #F==F
    if age >= 18:             #19>=18
        print("Female and eligible to vote")
    else:
        print("Female and not eligible to vote")
elif gend == 'M':
    if age >= 18:
        print("Male and eligible to vote")
    else:
        print("Male and not eligible to vote")
else:
    if age >= 18:
        print("None and eligible to vote")
    else:
        print("None and not eligible to vote")"""

#Palidrome : A palindrome is a word, number, or sequence of characters that reads the same forward and backward ex:121
"""num = 121        #num=12       #num=1  num=0
temp = num
rev = 0
while num != 0:
    rem = num % 10         #rem=121%10=1 rem=1     rem=12%10=2       rem=1%10=1
    rev = rev * 10 + rem   #rev=0*10+1=1           rev=1*10+2=12     rev=12*10+1=121
    num = num // 10         #num=121/10=12         num=12//10=1       num//10=0
    
print(f"rev value = {rev}")    #121
    
if temp == rev:      #121==121
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")"""

#Armstrong number:An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. Specifically, 
#for a three-digit number like 153:
#153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725
num = int(input("Enter any value: "))
temp = num
Arm = 0
count = 0

# Count number of digits
n = num
while n != 0:
    count += 1  # Increment count for each digit found in the number 
    n //= 10

# Compute sum of digits raised to count (power)
n = num   # Reset n to original number
while n != 0:
    rem = n % 10
    Arm= Arm + rem ** count   # use count as exponent
    n //= 10

print(f"The sum of digits^{count} = {Arm}")

if temp == Arm:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")