# ReadingTextFile.py
import os

# Declaration...
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "DataFiles\\Employee")
text_file = open(path, 'r')

# Reading...
obj = text_file.read()
print(obj)
