#Left Triangle Star Pattern
"""for i in range(1, 7):
    for j in range(1, 7):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()"""
"""
n = 5
for i in range(1, n+1):
    print("* " * i)"""
    
#Inverted Left Triangle Pattern
"""n = 5   # Step 1: Assign the value 5 to variable 'n'. 
        # This means the pattern will have 5 rows.

# Step 2: Loop starts from 'n' down to 1, with step -1 (decreasing order).
for i in range(n, 0, -1):  
    # When n=5 → i takes values: 5, 4, 3, 2, 1
    
    # Step 3: For each row, print '* ' repeated 'i' times.
    print("* " * i)"""

#Right Triangle of Stars pattern
"""n = 5   # Step 1: Assign 5 to variable 'n'. 
        # This means the triangle will have 5 rows.

# Step 2: Loop from 1 to n (inclusive).
for i in range(1, n+1):    
    # When n=5 → i takes values: 1, 2, 3, 4, 5
    
    # Step 3: "  " * (n-i) → adds spaces before stars to shift them to the right
    # Step 4: "* " * i → prints stars, count increases with each row
    
    print("  " * (n-i) + "* " * i)""" 
    # Example:
    # i=1 → "  " * (5-1) + "* " * 1 = "        " + "* " = "        * "
    # i=2 → "  " * (5-2) + "* " * 2 = "      " + "* * " = "      * * "
    # i=3 → "  " * (5-3) + "* " * 3 = "    " + "* * * " = "    * * * "
    # i=4 → "  " * (5-4) + "* " * 4 = "  " + "* * * * " = "  * * * * "
    # i=5 → "  " * (5-5) + "* " * 5 = "" + "* * * * * " = "* * * * * "

    
# Simple Triangle Pattern
"""rows = 6  # Sets the total number of rows for the triangle pattern.
for i in range(1, rows):  # Loop from 1 to rows-1 (i = 1 to 5)
    spaces = rows - i - 1         # Calculate number of spaces before the stars for current row
    stars = 2 * i - 1             # Calculate number of stars for current row (odd numbers: 1, 3, 5, ...)
    print(" " * spaces + "*" * stars)"""  # Print spaces followed by stars on the same line
        # " " * spaces: adds leading spaces to center the triangle
        # "*" * stars: prints the required number of stars for the row"""

# Pyramid pattern
"""rows = 6
# The variable `rows` is set to 6, which determines the number of rows in the triangle pattern.
for i in range(1, rows):
    # Outer loop iterates from 1 to `rows - 1` (i.e., 1 to 5).
    # Each iteration corresponds to one row of the triangle.

    for j in range(rows - i - 1):
        # Inner loop 1: Prints spaces before the stars in each row.
        # The number of spaces decreases as `i` increases.
        # For example:
        #   - When `i = 1`, `rows - i - 1 = 4` spaces are printed.
        #   - When `i = 2`, `rows - i - 1 = 3` spaces are printed.
        print(" ", end=" ")
        # Prints a single space (`" "`) without moving to the next line (`end=" "`).

    for j in range(2 * i - 1):
        # Inner loop 2: Prints stars (`*`) in each row.
        # The number of stars increases as `i` increases.
        # For example:
        #   - When `i = 1`, `2 * i - 1 = 1` star is printed.
        #   - When `i = 2`, `2 * i - 1 = 3` stars are printed.
        print("*", end=" ")
        # Prints a single star (`*`) without moving to the next line (`end=" "`).

    print()"""
    # Moves to the next line after printing all spaces and stars for the current row.

#Inverted Pyramid
n = 5   # Assign the number of rows for the triangle. Here, n = 5.
# Loop starts from n down to 1 with step -1.
# So, i will take values: 5, 4, 3, 2, 1
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)
    
