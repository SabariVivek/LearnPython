# Sabari should match exactly with case, Regex are case sensitive...

import re

pattern = "Sabari"

print("Enter your input : ")
text = input()

if re.search(pattern, text):
    print("Pattern matched...")
else:
    print("Pattern not matched...")
