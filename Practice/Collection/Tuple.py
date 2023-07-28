"""
Tuple is used to store multiple values into a variable...
But, Tuple is immutable...
Immutable means the value cannot be changed once declared...
"""

# Declaring the tuple...
fruits = ("Orange", "Mango", "Strawberry", "Banana", "Apple")

# Getting the type of the tuple using type() method...
print(type(fruits))

# Printing the whole tuple...
print(fruits)

# Finding the length of the tuple...
print("The length of the tuple is", len(fruits))

# Printing the whole tuple using the index mechanism...
for i in range(len(fruits)):
    print(fruits[i])

# Printing the fruits with for-each loop...
for fruit in fruits:
    print(fruit)

"""
Since, the tuple is immutable, we can use the below methods as like list...

1. append()
2. insert()
3. remove()
4. pop()
5. pop(INDEX)
6. reverse()
7. sort()
8. extend(Tuple_Obj)
9. clear() --> is not possible in python, instead you can delete the tuple...
"""

# Finding the index of the given element in the tuple...
print(fruits.index("Banana"))

# Nested tuple
numbers = (2, (1, 2, 3, 5), 0, 8, 19, 99)
print(numbers)
print(numbers[1][2])

# Storing different values into the same tuple...
versatile = (21, "Sabari", 21.08, True, 'A')
print(versatile)

# Forward and Backward Index...
print(versatile[2])
print(versatile[-2])  # -2 + (tuple_size) 5 = 3

# Slicing tuple...
print(versatile[1:4])

# Finding the number of times an element repeated in the tuple...
new_tuple = (2, 4, 3, 52, 2, 5, 4, 8, 3, 2, 5, 3, 2)
print(new_tuple.count(2))

# Finding the maximum and minimum value in the tuple...
print("Minimum value in the tuple : ", min(new_tuple))
print("Maximum value in the tuple : ", max(new_tuple))

# Finding the sum of elements in the tuple...
print(sum(new_tuple))

# Deleting the declared tuple...
""" 
del new_tuple
print(new_tuple) 
"""

# Checking whether the particular element is available in the tuple or not...
# By using in and not...
m_tuple = (2, 3, 4, 53, 2, 64, 36, 74)
print(2 in m_tuple)
print(24 in m_tuple)
print(25 not in m_tuple)

# Concatenation of the two tuple...
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (6, 7, 8, 9, 10)
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
