"""
    * Declared using {}
    * Mutable
    * No-index mechanism
    * Duplicates are ignored
    * Elements are not stored in a given order
"""

# Declaring the set...
fruits = {"Orange", "Mango", "Strawberry", "Banana", "Apple"}
print(fruits)

# Finding the type...
print(type(fruits))

# Finding the length...
print(len(fruits))

# Adding values...
fruits.add("Grapes")
fruits.add("Blueberry")
fruits.update(["Jackfruit", "Kiwi", "Guava"])  # To add multiple vales...
print(fruits)

"""
Removing the values (Remove vs Discard)...
    
    * Remove - it is used to remove the value from the set, 
                    but if the value is not available, it will throw the error...
    * Discard - it is also used to remove, but if the value doesn't available, 
                    it will ignore instead of throwing error...
"""
fruits.remove("Grapes")
fruits.discard("Grapes")

# Randomly removing te value since there is no index mechanism...
fruits.pop()
print(fruits)

# Clearing all the values...
# fruits.clear()
print(bool(fruits))  # Returns false if the set is empty...

# Deleting the set...
# del fruits
# print(fruits)

# For loop & For each loop (We cannot use for loop since there is no index mechanism)...
for fruit in fruits:
    print(fruit)

# In and Not In operator...
print("Kiwi" in fruits)
print("Dragon Fruit" not in fruits)

# Nested Set (Set can only nest Tuple since the value cannot be changed)...
# Set cannot nest List and Set
new_set = {1, 2, 3, (4, 5, 6), 7, 8}
print(new_set)

# Converting list to a set...
list_example = [1, 2, 3, 4, 5]
print(type(list_example))
set_example = set(list_example)
print(type(set_example))

"""
    * Union - All the values...
    * Intersection - Common values...
    * Difference - eg., (a-b) --> Removing all the common values and b values from a...
    * Symmetric Difference - Except the common values, everything should come...
"""
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union...
print(a.union(b))
print(a | b)

# Intersection...
print(a.intersection(b))
print(a & b)

# Difference...
print(a.difference(b))
print(a - b)
print(b - a)

# Symmetric Difference...
print(a.symmetric_difference(b))
print(a ^ b)

# Min, Max, Sum...
print(min(a))
print(max(a))
print(sum(a))
