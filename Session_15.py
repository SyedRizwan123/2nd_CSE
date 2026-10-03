#print vowels in a given string   #
"""input_string = "Hello World!"   #aeiouAEIOU
vowels = "aeiouAEIOU"
vowel_count = 0
vowel_list = []
for char in input_string:
    if char in vowels:
        vowel_list.append(char)
        vowel_count += 1

print("Vowels in the given string:", vowel_list)  #[e,o,o]
print(f"Number of vowels in the given string: {vowel_count}")"""

# Program to reverse a string
"""input_string = "Python"   #nohtyP
reversed_string=input_string[::-1]
print("Reversed string:", reversed_string)"""  #nohtyP

"""input_string = "Python"
reversed_string=""
for char in input_string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)"""  #nohtyP

# Program to check given  string is a palindrome
"""input_string="malayalam"
reversed_string=""
for char in input_string:
    reversed_string=char+reversed_string
if input_string==reversed_string:
    print("given string is palindrome")
else:
    print("given string is not palindrome")"""
    
"""input_string="malayalam"
if input_string==input_string[::-1]:
    print("given string is palindrome")
else:
    print("given string is not palindrome")"""
    
# Program to find the first non-repeating character in a string 
input_string = "aabbcde"
for char in input_string:
    if input_string.count(char) == 1:
        print("First non-repeating character:", char)
        break

    
    




