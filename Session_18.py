
listpeople = ["tom","harry","jane","liz"]
listflowers = ["rose","lily","tulip","jasmine"]
listpets = ["cat","turtle","goat","dog"]


#unlike strings, Lists are mutable
#assign to an index, we can update a value
"""print(listpets)
listpets[0]='t-rex'
print(listpets)"""

#Assign to a slice
"""listpets[0:2] =['python','elephant']
print(listpets)"""

#delete a slice
"""listpets[2:4]=[]
print(listpets)
"""
#append new items to list
"""listpets.append('fox')
print(listpets)"""

#clear a list by assignment to an empty list
"""listpets[:]=[]
print(listpets)"""

#nested list
"""nestedlist=[listpeople,listflowers]
print(nestedlist)
print(nestedlist[0])
print(nestedlist[1][0])"""


#lists with integers
"""list1=[100,200,300]
list2=[5,15,25]
list3=[10,50,50,20,0,10,50]
list1.append(-400)   #Add an item to the end of the list. equalent to list
print("list1 Append:",list1)

list2.extend(list1)  #Extend the list2 by appending all the time in list1.
print("list2extend:", list2)

list2.remove(-400)  #Remove the first item from list2 whose value is -400.
print("list2 Remove Element:",list2)

del list2[3]       #Remove the item at index[3]
print("delete list2[3]:", list2)

list2.pop()       #Remove and returns the last item in the list
print("list2 pop():", list2)

popped=list2.pop()
print(popped)

list3=[10,50,50,20,0,10,50]
print("Index of an element:", list3.index(20)) #Returns the index in list3 of element position

print(list3.count(50))   # the number of times 50 appears in list

list3.reverse()    #Reverse the items of list3 in place
print("list3 Reverse:", list3)


list3.sort()      #Sort the items of list3 in place
print("list3 sorted:",list3)

list3.clear()      #Remove all items from the list
print("list3 clear:",list3)

del list3        #Delete the list
print("delete list3:")"""
#print(list3)


#Find the largest and smallest number in a list
"""numbers = [12, 45, 67, 2, 89, 34]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))"""


#Find the largest and smallest element in a list without using built-in functions
"""numbers = [12, 45, 67, 2, 89, 34]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)
print(numbers.index(largest))
print(numbers.index(smallest))"""

#Reverse a list without using built-in reverse()
"""numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed:", reversed_list)"""

#Find the sum and average of list elements
"""numbers = [10, 20, 30, 40, 50]
total=sum(numbers)  #150
average=total/len(numbers)
print(total, " ", average )"""

#Remove duplicates from a list
"""numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []

for num in numbers:
    if num not in unique:   # check if element already exists
        unique.append(num)
print("Unique List:", unique)"""

numbers = ["Syed", "Rizzu", "Syed"]
unique = []

for num in numbers:
    if num not in unique:   # check if element already exists
        unique.append(num)
print("Unique List:", unique)