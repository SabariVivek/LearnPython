"""
Dictionary is like a map in java...
We can store as a key, value pair in dictionary...
"""

emp_details = {"Name": "Sabari",
               "City": "Chennai",
               "Role": "Automation Engineer",
               "Experience": "4 Years"}

# Getting the type of the dictionary...
print(type(emp_details))

# Printing the dictionary data...
print(emp_details)

# Getting the value of a key...
print(emp_details["Name"])

# Printing all the keys in a dictionary
print(emp_details.keys())

# Printing all the values in a dictionary
print(emp_details.values())

# Printing all the key, value pairs in a dictionary...
print(emp_details.items())

# Updating the values of the dictionary...
emp_details["Experience"] = "4.2 Years"
print(emp_details)

# Adding the new values into the dictionary...
emp_details["Tools"] = "Selenium"
print(emp_details)

# For loop with dictionary...
for key in emp_details.keys():
    print(key)

for value in emp_details.values():
    print(value)

for item in emp_details.items():
    print(item)

for key, value in emp_details.items():
    print("Key : " + key + " | Value : " + value)

# Removing the last item in the dictionary...
print("Removed Element using popitem() :", emp_details.popitem())
print(emp_details)

# Removing an item having specific key...
print("Removed Element using pop(\"key\") :", emp_details.pop("Name"))
print(emp_details)

# Removing all the values from the dictionary...
emp_details.clear()
print(emp_details)

""" 
Comparing two dictionary data...
*** Order of key & value doesn't matter ***
"""
dict_1 = {"One": 1, "Two": 2, "Three": 3}
dict_2 = {"Two": 2, "One": 1, "Three": 3}

if dict_1 == dict_2:
    print("Two dictionary's are equal")
