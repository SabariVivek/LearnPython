"""
*args is used to pass multiple arguments...
Here "args" are user defined name, and it can be anything, * is mandatory...
"""


# Usage 1...
def func_1(*args):
    for temp in args:
        print(temp, end=" | ")


func_1(2, 1, 0, 8, 9, 9)


# Usage 2...
def func_2(a, b, c, d):
    print()
    print(a, b, c, d, sep=" | ")


arr = [2, 1, 0, 8]
func_2(*arr)
