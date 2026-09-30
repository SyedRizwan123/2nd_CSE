#Diamond Pattern
"""n = 5  # Number of rows for the upper half of the diamond
# Upper half of the diamond (including the middle row)
for i in range(1, n+1):  # Loop from 1 to n (1 to 5)
    print(" "*(n-i) + "* " * i) 
# Lower half of the diamond (excluding the middle row)
for i in range(n-1, 0, -1):  # Loop from n-1 down to 1 (4 to 1)
    print(" "*(n-i) + "* " * i)"""
    # " "*(n-i): Prints spaces to center the stars
    # "* " * i: Prints i stars with

#hollow square pattern pattern
# Outer loop: Controls the rows, running from i = 1 to 5 (range stops before 6)
"""for i in range(1, 6):
    
    # Inner loop: Controls the columns within each row, running from j = 1 to 5
    for j in range(1, 6):
        #We want stars only on the boundary of the rectangle."
        # Check if the current position lies on any of the four borders:
        # - i == 1: Top row
        # - i == 5: Bottom row
        # - j == 1: Leftmost column
        # - j == 5: Rightmost column
        if i == 1 or j == 1 or i == 5 or j == 5:
        # Print an asterisk followed by a space, keeping the cursor on the same line
            print("*", end=" ")
        else:
        # For interior cells, print two spaces to keep alignment without a border
            print(" ", end=" ")
    # After finishing all columns for row 'i', print an empty line to move to the next row
    print()"""
    
# This program prints a right-angled triangle pattern of numbers.
"""for i in range(1, 6):     # This is the outer loop. It will run 5 times, with 'i' taking values from 1 to 5.
                        # This loop controls the number of rows to be printed.
    for j in range(1, i + 1):  # This is the inner loop. It depends on the value of 'i' from the outer loop.
                                # For each row 'i', it will run 'i' times, with 'j' taking values from 1 up to 'i'.
                                # This loop is responsible for printing the numbers in each row.
        print(j, end=" ")    # This prints the current value of 'j' followed by a space instead of a new line.
                                # This keeps the numbers for a single row on the same line.
        
    print()"""                 # This prints a new line character after the inner loop completes.
                                    # It moves the cursor to the next line, so the numbers for the next row
                                    # will be printed on a new line.""

#Number Triangle Pattern Program" (also called Floyd’s Triangle in mathematics).
n = 5          # Step 1: Set the number of rows for the pattern (triangle will have 5 rows).
num = 1        # Step 2: Initialize 'num' with 1. 
        # This variable will be printed and incremented each time.
# Step 3: Outer loop → controls the number of rows (from 1 to n).
for i in range(1, n+1):  
    # When n=5 → i takes values 1, 2, 3, 4, 5
    # Step 4: Inner loop → runs 'i' times in each row
    # For row 1 → loop runs 1 time
    # For row 2 → loop runs 2 times
    # For row 3 → loop runs 3 times, etc.
    for j in range(i): 
        # Step 5: Print the current value of 'num'
        # 'end=" "' means: stay on the same line and put a space after printing
        print(num, end=" ")
        # Step 6: Increase 'num' by 1 for the next print
        num += 1
    # Step 7: After finishing one row, move to the next line
    print()
        
