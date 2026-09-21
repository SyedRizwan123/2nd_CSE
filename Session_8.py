#Find the factorial number of given value
# To find factorial value
"""n = int(input("Enter any value: "))  #5
fact = 1
i = 1
while i <= n:        # 1<=5  2<=5 3<=5  4<=5 5<=5  6<=5
    fact = fact * i          #1*1=1 fact=1 fact=1*2=2 fact=2*3=6  fact=6*4=24   fact=24*5=120
    i = i + 1
print(f"Factorial value is {fact}")"""

#To find given number is Strong number or not
#Strong number:A Strong number is a number where the sum of the factorials of its digits equals the number itself.
# //ex:145: find factorial with each digit 1!+4!+5!=145 we have to get same digit
"""num = int(input("Enter a number: "))   #145
sum = 0    # sum is used to store the sum of the factorials of the digits.
temp = num #temp stores the original number for comparison later.
while num:
    i = 1
    fact = 1
    r = num % 10 # Extract the last digit         #r=145%10=5 r=4 fact=24 
    while i <= r:    # Calculate factorial of the digit       #1<=5
        fact = fact * i        #fact=1*1=1 fact=1*2=2, fact=2*3=6 fact=6*4=24, fact=24*5=120
        i += 1
    sum = sum + fact  # Add factorial to sum     #sum=0+120=120 //120+24=144  sum=144  sum=144+1=145
    num = num // 10   # Remove the last digit    #num=145/10=14 //14/10=1 num=1       num=144+1=145
if sum == temp:
    print(sum,"is a strong number")
else:
    print(sum,"is not a strong number")"""
    
# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# 6=1+2+3 =6 6 devisors is 1+2+3
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):  # num=6   1<6
    if num % i == 0:  # 6%1==0   6%1==0   6%2==0  6%3==0  6%4=
        sum += i  # sum=0+1=1     sum=1+2=3   sum=3+3=6                      3+4=7

if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")