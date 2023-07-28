"""
In Python, we can use Bool() function as if condition...
"""

# 0 --> False...
# Any Number --> True...
print("Value 0 : ", bool(0))
print("Value more than : ", bool(5))
print("Value not 0 : ", bool(-3))

# Empty value --> False...
# Any Value --> True...
print("Empty String :", bool(""))
print("Non empty String:", bool("Sabari Vivek"))

print("Empty List :", bool([]))
print("Non Empty List :", bool(["Sabari", "Vivek"]))
print("Empty Tuple :", bool(()))
print("Non Empty Tuple :", bool(("Sabari", "Vivek")))
print("Empty Set :", bool({}))
print("Non Empty Set :", bool({"Sabari", "Vivek"}))
print("Non Empty Dictionary :", bool({"First Name": "Sabari", "Last Name": "Vivek"}))

print("None :", bool(None))
print("False :", bool(False))
print("True :", bool(True))
