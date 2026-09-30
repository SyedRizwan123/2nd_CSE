#program prints a right-angled  pattern of letters.
"""for i in range(1, 6):       # This is the outer loop. It will iterate 5 times, with 'i' taking values from 1 to 5.
                            # This loop controls the number of rows to be printed.

    ch = 'A'                # Inside the outer loop, we initialize a variable 'ch' to the character 'A'
                                # at the beginning of each new row. This ensures that every row starts with 'A'.
    for j in range(1, i + 1):  # This is the inner loop. It depends on the current value of 'i'.
                                # For each row 'i', it will run 'i' times, with 'j' from 1 up to 'i'.
                                # This loop is responsible for printing the characters in each row.
        print(ch, end=' ')  # This prints the current character 'ch' followed by a space.
                                    # The 'end=' argument prevents a new line, keeping the characters on the same line.
        ch = chr(ord(ch) + 1)  # This is the key line for character manipulation.
                                # 1. 'ord(ch)' gets the ASCII (or Unicode) value of the current character 'ch'.
                                # 2. We add 1 to this value to get the next character's ASCII value.
                                # 3. 'chr()' converts this new ASCII value back into a character.
                                # This effectively moves to the next letter of the alphabet (A -> B, B -> C, etc.).
    print()"""   
    
# Alphabet Triangle Pattern Program
"""ch = ord('A')  # Initialize 'ch' with the ASCII value of 'A'
for i in range(1, 6):         # Outer loop for rows (1 to 5)
    for j in range(1, i+1):   # Inner loop for columns in each row
        print(chr(ch), end=' ')  # Print the character
        ch += 1                  # Move to next character (ASCII value)
    print()"""


"""print("'Hello Vignan'")
print("\"Syed\"")
print("sayyad"*2)"""

#string formating:In Python, string formatting is the process of creating a formatted string by embedding variables or values within a text string. This allows you to create dynamic strings that incorporate variable values, making your code more readable and flexible.
#using '%' operator: This  % operator use to insert values into a string.

"""name = "Syed"
age = 25
print("My name is %s and I am %d years old." % (name, age))"""

#Using format().: This method format() method is use to format strings. It allows for more flexibility in terms of the order of variables and additional formatting options.
"""name = "Rizwana"
age = 25
print("My name is {} and I am {} years old.".format(name, age))"""

#Using f-strings (Formatted String Literals):  f-strings are a concise and readable way to format strings. They allow you to embed expressions directly within string literals by using curly braces {}
"""name="Ram"
age=25
print(f"my name is {name} and I am {age} years old")"""

"""print("we'll first learn how to print.", end="")# end=' ' is used to specify what should be printed at the end of the output. By default, it is a newline character (\n), which means that each print statement will be printed on a new line. However, by setting end=' ', we are telling Python to print a space instead of a newline at the end of the output, allowing us to print multiple statements on the same line.
print("Then we'll learn how to comment code.")"""

print("Then we'll learn how to comment code.\n we'll first learn how to print.")
