"""
Unpacking the "Collection" and "Range" into individual variables...
"""

# List
list_values = ["Apple", "Orange", "Banana"]
a, b, c = list_values
print(a)
print(b)
print(c)

# Tuple
tuple_values = {"Pomegranate", "JackFruit", "Watermelon"}
a, b, c = tuple_values
print(a)
print(b)
print(c)

# Set
set_values = {"Kiwi", "Mango", "Grapes"}
a, b, c = set_values
print(a)
print(b)
print(c)

# Dictionary
dict_values = {"Fruit 1": "Mango", "Fruit 2": "Grapes", "Fruit 3": "Grapes"}
a, b, c = dict_values.items()
print(a)
print(b)
print(c)
