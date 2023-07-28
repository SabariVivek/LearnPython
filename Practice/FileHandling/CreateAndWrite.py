"""
'w' keyword is used to write into the file, if it doesn't exist it will create it...
"""

# Creating the file if not exist...
file = open("C:\\Users\\M1070211\\PycharmProjects\\pythonProject\\Resources\\File.txt", "w")

# Writing the values into the file...
file.write("I am Sabari Vivek\n")
file.write("I am working as an Automation Tester\n")
file.write("I am living in Chennai\n")

file.close()
