"""
Exception Handling is used to handle the exceptions which occurs during the run time of the program...
"""

try:
    a = 10 / 0
except ArithmeticError:
    print("Exception occurred...")
except FileNotFoundError:
    print("Exception occurred...")
else:
    print("No exception occurred...")
finally:
    print("Successfully executed the program...")
