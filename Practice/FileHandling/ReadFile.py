"""
'r' keyword is used to read into the file...
"""

# Creating the file if not exist...
file = open("C:\\Users\\M1070211\\PycharmProjects\\pythonProject\\Resources\\File.txt", "r")

# It will read whole file...
print(file.read())

# It will read the whole file as a list...
print(file.readlines())

# Reading the file using for loop...
for line in file:
    print(line)

file.close()
