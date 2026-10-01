"""decimal_number = 10
binary_value =bin(decimal_number) [2:]
print(binary_value)"""

#String Operations:
"""f_name="Syed"
l_name="Rizwan"
number=99
print(f_name +number)"""
#print(f_name + " " + l_name) #Concatenation

# string can be counted from the left using +ve indices, starting with 0
word = "python"
"""print(word[0])
print(word[1])
print(word[2])
print(word[3])        
print(word[4])
print(word[5])"""

#string can be counted fromm the right using -ve indices,starting with -1
"""print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])"""

"""word="python"
for char in word:
    print(char)"""
    
"""word="python"
for i in range(len(word)-1,-1,-1):
    print(word[i])"""
#print(len(word))

#slicing
# - string can be sliced with [startIndex:endIndex]
# - startIndex is included and endIndex is excluded
# - startIndex must be < endIndex, else empty string is returned
# - if a slice index is out of range, python will go as far as it can
"""word="python"
print(word[0:3])
print(word[0:10])
print(word[-3:-1])
print(word[-3:-6])
print(word[:2])
print(word[4:])"""

"""word="pyhton"
#word[0] = 'e'
print('J'+ word)"""

"""word="pyhton"
newword1=word[0] + word[5]
print(newword1)"""


print(len('python'))
print('python'.find('t')) #find index of substring in string
print('python'.startswith('p'))  # check string starts with substring
print('python'.endswith('n'))    # check string ends with substring
print('PYTHON'.lower())
print('python'.upper())
print('a'.isalpha())  #True
print('abc123'.isalnum())  #True
print('12345'.isdigit())  #True #check if all characters in the string are digits
print('syed'.capitalize())  #Syed
print('  python  '.strip())  #python
print("syed rizwan".title())   #Syed Rizwan If you want each word’s first letter capitalized, use .title():
print("Syed".count('S'))
print('python is very easy'.split())  #the split() method in Python is used to split a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines). In this case, the string 'python is very easy' is split into a list of words: ['python', 'is', 'very', 'easy'].

#.join() method in Python is used to concatenate a list or iterable of strings into a single string, with a specified separator between each element.
words = ["Python", "is", "fun"]
print(words)

sentence = " @  ".join(words)   # join with a space
print(sentence)

#print vowels in a given string

