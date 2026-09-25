#print even nubers and odd numbers
"""for i in range(1, 11):  #1,2,3,4,5,6,,7,8,9,10
    if i % 2 == 0:     #1%2==1,  2%2==0
        print(i, "= even")    #2 =even
    else:
        print(i, "= odd")"""   #1 =odd"""
        
#print only even number
"""for i in range(0, 11, 2):    #0+2=2, 2+2=4,
    if i % 2 == 0:
        print(i, "= even")
    else:
        print(i, "= odd")"""
        
#print 2nd table
"""n = int(input("Enter a number: "))     #2 * 1= 2*1=2,  2*2=4 2*3=6 2*4=8
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")"""
    

#Sum of natural numbers
"""n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):  
    sum = sum + i       #0+1=1,   1+2=3, 3+3=6 6+4=10 10+5=15
print(sum)"""

#Sum of natural numbers using while loop
"""n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1
print(sum)"""

#print ASCII values
"""for i in range(65, 91):
    print(f"{chr(i)}={i}")"""

"""for i in range(97, 123):
    print(f"{chr(i)}={i}")"""

#Find the given is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     
"""n=int (input("Enter a number: "))
count=0    #we have to write this count after writting if statement

for i in range(1, n + 1):    #range(1, n+1): Generates a sequence of numbers from 1 to n (inclusive)
    if n % i == 0:        #3%1==0,  3%3=0
        count += 1      #coun=count+1, 0+1=1

if count == 2:
    print("Given number is a prime number")
else:
    print("Given number is not a prime number")"""
    
#Find the given is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     

"""prime = int(input("Enter the number: "))
count = 0

# Check if the input number is prime
for i in range(1, prime + 1):
    if prime % i == 0:
        count += 1

if count == 2:
    print(prime, "is a prime number")
else:
    # If the number is not prime, find the next prime number
    prime += 1  # Start checking from the next number
    while True:
        count = 0  # Reset count for the new number
        for i in range(1, prime + 1):
            if prime % i == 0:
                count += 1
        if count == 2:  # Check if the current number is prime
            print("The next prime number is:", prime)
            break
        prime += 1  # Move to the next number"""


#print even nubers and odd numbers
"""even_count=0
odd_count=0
for i in range(1, 11):  #1,2,3,4,5,6,,7,8,9,10
    if i % 2 == 0:     #1%2==1,  2%2==0
        even_count+=1
    else:
        odd_count+=1
print(f"Even number count is = {even_count} and odd number count is = {odd_count}")"""
    