"""my_list=[10,20,30,40,50]
print(my_list)
print(my_list[2])"""

"""input_string = "aabbcde"
non_repeating_chars = []  # Initialize an empty list to store non-repeating characters
for char in input_string:
    if input_string.count(char) == 1:
        non_repeating_chars.append(char)  # Add the non-repeating character to the list
if len(non_repeating_chars) >= 2:
    print("The second non-repeating character is:", non_repeating_chars[1])"""  # Print the second non-repeating character
    
#Count vowels and consonants
# Program to count vowels and consonants in a string
input_string = "Hello, World!"
vowel_count = 0
consonant_count = 0
vowel="aeiouAEIOU"  # Define a string containing all vowels
for char in input_string:
    if char.isalpha():  # Check if the character is an alphabet
        if char in vowel:  # Check if the character is a vowel
            vowel_count += 1  # Increment vowel count
        else:
            consonant_count += 1  # Increment consonant count
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)