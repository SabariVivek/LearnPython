"""
List is used to store multiple values into a variable...
But, List is mutable...
Mutable means the value can be changed once declared...
"""

# Declaring the list...
fruits = ["Orange", "Mango", "Strawberry", "Banana", "Apple"]

# Getting the type of the list using type() method...
print(type(fruits))

# Printing the whole list...
print(fruits)

# Finding the length of the list...
print("The length of the list is", len(fruits))

# Printing the whole list using the index mechanism...
for i in range(len(fruits)):
    print(fruits[i])

# Printing the fruits with for-each loop...
for fruit in fruits:
    print(fruit)

# Adding the element into the list...
fruits.append("Watermelon")
print(fruits)

# Inserting the element into the list...
fruits.insert(1, "Kiwi")
print(fruits)

# Removing the element from the list...
fruits.remove("Kiwi")
print(fruits)

# Removing the last element from the list using pop()
fruits.pop()
print(fruits)

# Popping the element from the list using index...
fruits.pop(1)
print(fruits)

# Clearing all the values form the list...
""" 
fruits.clear()
print(fruits)
"""

# Reversing the list...
fruits.reverse()
print(fruits)

# Sorting (Alphabetically) the elements in the list...
fruits.sort()
print(fruits)

# Finding the index of the given element in the list...
print(fruits.index("Banana"))

# Nested list
numbers = [2, [1, 2, 3, 5], 0, 8, 19, 99]
print(numbers)
print(numbers[1][2])

# Storing different values into the same list...
versatile = [21, "Sabari", 21.08, True, 'A']
print(versatile)

# Forward and Backward Index...
print(versatile[2])
print(versatile[-2])  # -2 + (list_size) 5 = 3

# Slicing lists...
print(versatile[1:4])

# Finding the number of times an element repeated in the list...
new_list = [2, 4, 3, 52, 2, 5, 4, 8, 3, 2, 5, 3, 2]
print(new_list.count(2))

# Finding the maximum and minimum value in the list...
print("Minimum value in the list : ", min(new_list))
print("Maximum value in the list : ", max(new_list))

# Finding the sum of elements in the list...
print(sum(new_list))

# Deleting the declared list...
# del new_list
# print(new_list)

# Checking whether the particular element is available in the list or not...
# By using in and not...
mlist = [2, 3, 4, 53, 2, 64, 36, 74]
print(2 in mlist)
print(24 in mlist)
print(25 not in mlist)

# Concatenation of the two list...
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_3 = list_1 + list_2
print(list_3)

# Instead of concatenation of the two list, we can extend the list_1 using extend() function...
list_1.extend(list_2)
print(list_1)
