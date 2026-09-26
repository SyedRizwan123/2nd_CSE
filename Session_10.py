#print armstrong numbers
# 1. Iterate through numbers starting from 1 up to 1999 (stops before 2000).
#    If used: 'i' takes each number in that range one by one.
"""for i in range(1, 2000):
     # 2. Store the current number 'i' in variable 'num'.
        #    If used: Gives us a working copy of 'i' to dismantle digit-by-digit later.
        num = i
    
        # 3. Create another copy of the number in 'temp'.
        #    If used: Preserves the original value for final comparison, since 'num' becomes 0.
        temp = num
    
        # 4. Initialize the accumulator for the Armstrong sum to 0.
        #    If used: Holds the running total of (digit ** count) for each digit.
        arm = 0
    
        # 5. Create a third copy of the number in 'n'.
        #    If used: Gives a disposable variable dedicated solely to counting digits.
        n = num
    
        # 6. Initialize the digit counter to 0.
        #    If used: Will hold the total number of digits (the power 'n' in the definition).
        count = 0
    
        # 7. Loop until 'n' becomes 0 by peeling off one digit per cycle.
        #    If used: Determines how many digits the number has.
        while n != 0:
    
            # 8. Integer division by 10 discards the last digit (e.g., 153 // 10 -> 15).
            #    If used: Reduces 'n' toward 0 without floating-point errors.
            n = n // 10
    
            # 9. Increment the digit count by 1 for each discarded digit.
            #    If used: After this loop terminates, 'count' contains the exact number of digits.
            count += 1
    
        # 10. Loop until 'num' becomes 0 to extract and process each digit.
        #     If used: Calculates the sum of each digit raised to 'count'.
        while num != 0:
    
            # 11. Modulo 10 extracts the last digit of 'num' (e.g., 153 % 10 -> 3).
            #     If used: Isolates the current least-significant digit into 'rem'.
            rem = num % 10
    
            # 12. Raise the digit to the power of 'count' and add to 'arm' (e.g., 3 ** 3 = 27).
            #     If used: Builds the cumulative Armstrong sum.
            arm = arm + rem**count
    
            # 13. Drop the last digit of 'num' using integer division (e.g., 153 // 10 -> 15).
            #     If used: Moves to the next digit to the left until all digits are processed.
            num = num // 10
    
        # 14. Check if the computed sum ('arm') matches the original number ('temp').
        #     If used: Evaluates the mathematical definition of an Armstrong number.
        if temp == arm:
    
            # 15. Print the number followed by "is Armstrong".
            #     If used: Outputs the result to the console when a match is found.
            print(temp, "is Armstrong")"""
        
# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# print the next perfect number
# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# print the next perfect number
# 1.the user for an integer input and convert the string into an integer.
"""num = int(input("Enter a number: "))
# 2. Initialize an accumulator variable 'sum' to store the sum of proper divisors.
sum = 0
# 3. Check every candidate factor from 1 up to (num - 1).
#    Proper divisors cannot include the number itself.
for i in range(1, num):
    # 4. Use modulo (%) to test divisibility: if remainder is 0, 'i' is a proper factor.
    if num % i == 0:
        # 5. Add the factor 'i' to the running total.
        sum += i
# 6. Compare the sum of proper divisors with the original number.
if sum == num:
    # 7. If equal, confirm the input is a perfect number.
    print(f"{num} is a perfect number")
else:
    # 8. If not equal, notify the user.
    print(f"{num} is not a perfect number")
    
    # 9. Start the search for the next candidate starting at (num + 1).
    next_num = num + 1
    
    # 10. Start an indefinite loop to test successive integers until a perfect number is found.
    while True:
        # 11. Reset 'sum' to 0 for each new candidate 'next_num'.
        sum = 0
        
        # 12. Loop through all possible proper divisors for 'next_num' (from 1 to next_num - 1).
        for i in range(1, next_num):
            # 13. Test if 'i' divides 'next_num' evenly.
            if next_num % i == 0:
                # 14. Add the divisor to the sum.
                sum += i

        # 15. Check if the current candidate 'next_num' is equal to its divisor sum.
        if sum == next_num:
            # 16. If matched, print the result.
            print(f"The next perfect number is {next_num}")
            # 17. Exit the 'while True' loop immediately so it stops searching.
            break
            
        # 18. If not perfect, increment by 1 to test the next integer on the next cycle.
        next_num += 1"""
        

# Prompt the user to input the number of terms they want in the Fibonacci series
#Fibonacci series: it is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

"""n = int(input("Enter the number of terms: "))  #10

# Initialize the first two numbers of the Fibonacci series
first = 0
second = 1
# Print the first two numbers of the Fibonacci series
print("Fibonacci Series:", first, ",", second, end=", ")

# Loop to generate and print the remaining terms of the Fibonacci series
for i in range(2, n):    #10
    # Calculate the next term in the Fibonacci series
    next_term = first + second    #0+1=1, 1+1=2 1+2=3,2+3=5, 3+5=8, 5+8=13
    # Print the next term of the Fibonacci series
    print(next_term, end=", ")
    # Update the values of 'first' and 'second' for the next iteration
    first = second    #1``  1,2, 3,5,8,13,21
    second = next_term  #1, 2,3,5,8,13,21,34

# Print a newline character to end the output
print()"""

#Pattern programs
"""for r in range(4):       #rows
    for c in range (6):  #columns
        print("*", end="")
    print()"""
    
for i in range(6):
    print("*",end="")
print()
