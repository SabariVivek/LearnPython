# ReadingJsonFile.py...
import json
import os

# Declaration...
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "DataFiles\\Employee.json")
json_file = open(path, 'r')
json_data = json_file.read()

# Parsing...
obj = json.loads(json_data)
print(str(obj["Name"]))
print(str(obj["Location"]))
print(str(obj["Role"]))
print(str(obj["Experience"]))
print(str(obj["Skills"]))
print(obj)
