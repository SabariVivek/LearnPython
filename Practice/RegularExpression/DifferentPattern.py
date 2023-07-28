# DifferentPattern.py
import re

# pattern = "[Pp]ython"
# pattern = "[A-Z]ython"
# pattern = "[a-z]ython"
# pattern = "[A-Za-z]ython"
# pattern = "Pytho[A-Za-z]"
# pattern = "[SFP]it"
# pattern = "[0-9]am"
# pattern = "[A-Za-z0-9]"
# pattern = "[^0-9]ython"  # Opposite of (0-9) means, it will match other than 0-9...
# pattern = "s[^aeiou]t"
# pattern = "\d"  # Replacement of [0-9]
# pattern = "\D"  # Replacement of [^0-9]
# pattern = "\w" # Matches a single word character and is equal to specifying [A-Za-z0-9]
# pattern = "\W"  # Matches a single word character and is equal to specifying [^A-Za-z0-9]
# pattern = "^My"  # Starts with My
# pattern = "on$"  # Ends with on
# pattern = "Sa...i"  # Dot can be anything, each dot represent one value
# pattern = "^I am learning .* as my own$"  # . represent any value, * represent 0 or any no of time
# pattern = "^I am learning .+ as my own$"  # . represent any value, * represent 1 or any no of time
pattern = "Python|python"

print("Enter the text : ")
text = input()

if re.search(pattern, text):
    print("Pattern Matched")
else:
    print("Pattern not Matched")
