"""
'a' keyword is used to append into the file...
"""

# Creating the file if not exist...
file = open("C:\\Users\\M1070211\\PycharmProjects\\pythonProject\\Resources\\File.txt", "a")

# Appending the values into the file...
file.write("I am appending this text to the file")

file.close()
