#Find the second largest number in a list
# List of numbers
"""numbers = [12, 45, 67, 89, 34]
# Sort the list in ascending order (smallest → largest)
numbers.sort()   # After sorting: [12, 34, 45, 67, 89]
# Print the second largest element
print("Second Largest:", numbers[-2])"""

##Find the second largest element in a list without using the sort()
"""numbers = [12, 45, 67, 89, 34]
largest = numbers[0]   #12
second = numbers[0]    #12
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second largest:", second)"""

#What is enumerate() in Python?
#Simple definition:
"""enumerate() is a Python built-in function that gives us both the index (position) 
and the value of each item while looping through a sequence."""
#Normally, if you loop through a list:
"""students = ["Rahul", "Anil", "Priya"]

for student in students:
    print(student)"""
    
# ---------------------------------------------------------
# EXAMPLE: enumerate()
# ---------------------------------------------------------
# We create a list called "students".
#
# This list contains 3 student names.
#
# Python automatically gives every item an index (position):
#
# Index 0 → Rahul
# Index 1 → Anil
# Index 2 → Priya
"""students = ["Rahul", "Anil", "Priya"]
for index, student in enumerate(students):
    # print() is used to display information on the screen.
    #
    # Here:
    #
    # index   → prints the student's position
    # student → prints the student's name
    #
    # First iteration:
    # index = 0
    # student = "Rahul"
    #
    # print(0, "Rahul")
    #
    # Output:
    # 0 Rahul
    #
    #
    # Second iteration:
    # index = 1
    # student = "Anil"
    #
    # Output:
    # 1 Anil
    #
    #
    # Third iteration:
    # index = 2
    # student = "Priya"
    #
    # Output:
    # 2 Priya
    #
    print(index, student)"""
    
# ---------------------------------------------------------
# FIND THE INDEX POSITIONS OF NUMBER 50
# ---------------------------------------------------------
"""numbers = [10, 50, 40, 50, 50, 34]
for index, num in enumerate(numbers):
    if num == 50:
            # If num is 50, print its index/position.
            #
            # We print index, NOT num.
            #
            # This tells us WHERE 50 is located in the list.
            #
        print(index)"""

#Check if a list is a palindrome
"""list1 = [1, 2, 3, 2, 1]
if list1 == list1[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome")"""
    
#Find the common elements between two lists
"""list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for x in list1:
    if x in list2:
        common.append(x)
print(common)"""

#Find all even numbers from a list
"""numbers = [10, 15, 20, 25, 30]
evennumbers=[]
for num in numbers:
    if num%2==0:
        evennumbers.append(num)
print("Even numbers:", evennumbers)"""

#print vowels from a list of cities
cities = ["hyderabad", "mumbai", "Banglore", "Kolkata", "chennai"]
vowels = "aeiouAEIOU"   # include uppercase vowels also
for city in cities:               # loop through each city
    print("City:", city)  #hyderabad
    for ch in city:               # check each character in the city name
        if ch in vowels:          # if character is a vowel
            
            print(ch, end=" ")    # print vowel
    print()  # move to next line after each city