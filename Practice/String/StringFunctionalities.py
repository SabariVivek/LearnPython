"""
In Python, you can store Strings into a variable by surrounding the text with single quotes or double...
This will contain all the string basics of Python...
Strings work like Collection List in Python...
Strings are immutable in Python...
"""

# Declaration of a string (3 ways)...
name = "Sabari Vivek"
place = 'Chennai'
role = str("Automation Engineer")
print(name, place, role, sep=" | ")

# Getting type of a string...
print(type(name))

# String works as a Collection List....
print(name[0])
print(name[1])

# String in for loop...
for c in name:
    print(c)

# To find length of a String...
print("The length of the String is :", len(name))

# String - in and not in...
print("bar" in name)
print("bar" not in name)

# Slicing Strings...
slicing_string = "Automation Testing"
print(slicing_string[2:8])
print(slicing_string[:4])
print(slicing_string[8:])

# String operations...
value = "         this is not for automation     "
print(value.upper())
print(value.lower())
print(value.strip())
print(value.rstrip())
print(value.lstrip())
print(value.replace(' for ', ' ').strip())

# Split in string...
split_text = "I am an automation tester in chennai"
print(split_text.split(" "))
for s in split_text.split(" "):
    print(s)

# Immutable of a string...
str_1 = "Sabari"
str_2 = "Vivek"
print("ID of 1st String :", id(str_1))
print("ID of 2nd String :", id(str_2))

# Capitalize --> Capitalizing the first letter of a String...
cap = "this is an example of capitalize function in a string"
print(cap.capitalize())

# Title --> Capitalizing each letter of a word in a String...
print(cap.title())

# Count --> To count a specified word/letter in a String...
caption = "I am count the count of a count in a count to find c"
print(caption.count("count"))
print(caption.count("c"))

# Find --> Return index if found, otherwise returns -1...
print(caption.find("count"))

# Comparing Strings in Python...
string_1 = "Hello"
string_2 = "Hello"
string_3 = "hello"
print(string_1 == string_2)  # Way 1...
print(string_1.__eq__(string_2))  # Way 2...
print(string_1.casefold() == string_2.casefold())  # Way 3...
