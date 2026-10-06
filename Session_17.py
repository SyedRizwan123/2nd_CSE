#Program to check if two strings are anagrams
"""An anagram is a word  formed by rearranging the letters of another word , using all the original letters exactly once. 
For example, listen" and "silent" are anagrams because both use the same letters in a different order."""
"""str1 = "listen"
str2 = "silent"

# Sort both strings and compare
print(sorted(str1))  #['e', 'i', 'l', 'n', 's', 't']
print(sorted(str2))  #['e', 'i', 'l', 'n', 's', 't']

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")"""
    
# Program to remove all duplicate characters from a string
# Input string with duplicate characters
"""input_string = "programming"
# Initialize an empty string to store the result without duplicates
# This will be used to build the final string
result_string = ""
# Loop through each character of the input string
# For each character, we check if it's already in our result string
for char in input_string:
    # Check if the current character 'char' is NOT in 'result_string'
    # The 'in' operator efficiently checks for membership in a string.
    # It returns True if the character is found, and False otherwise.
    # We use 'not in' to only proceed if the character is new.
    if char not in result_string:
        # If the character is not already in 'result_string', we append it.
        # This ensures that only the first occurrence of each character is kept.
        result_string += char
print(result_string)"""


#find longest word
"""text='python programming is easy'
longest=''   #longest='python', longest='programming'
for word in text.split():    #['python', 'programming','is','easy']
    if len(word)>len(longest):   #6>0, 11>6, 2>11, 4>11
        longest=word
print(longest)"""   #programming

#Reverse words in a string
"""text='python programming is easy'
words=text.split()   #['python', 'programming','is','easy']
#the split() method in Python is used to split a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines). In this case, the string 'Hello World Python' is split into a list of words: ['Hello', 'World', 'Python'].
result=' '.join(reversed(words))  #['Python', 'Worls', 'Hello']
#.join() method in Python is used to concatenate a list or iterable of strings into a single string, with a specified separator between each element. In this case, we are using a space (' ') as the separator to join the reversed list of words back into a single string.
#reversed() function in Python is used to reverse the order of elements in an iterable (like a list, tuple, or string). In this case, it reverses the order of the words in the list created by text.split().
#so finally the result will be "Python World Hello"
print(result)"""  #Python Worls Hello

#List: List are mutable sequance, typically used to store collections of homogenious items
# Lists are represented by comma-separated items within square brackets []

listpeople = ["tom","harry","jane","liz"]
"""print(type(listpeople))
print(listpeople)"""
listflowers = ["rose","lily","tulip","jasmine"]
listpets = ["cat","turtle","goat","dog"]
listnumfriends = [21,33,10,51]
#List of heterogenious items are not incorrect, just atypical
"""listAtypical = [1,'cat',0x43,567.55]       #0x45 UTF-8 ENCODING FOR 69
print(listAtypical)"""

#concatenate lists
"""listCon= listpeople + listflowers
print("listcon->", listCon)
#Length of lists
print("length position->",len(listpeople))
print("length position->",len(listCon))"""

#refer to item in list with index
"""print("listpeople[2]->", listpeople[2])
print("listpeople[-3]->", listpeople[-3])"""


for item in listpeople:
    print(item)

