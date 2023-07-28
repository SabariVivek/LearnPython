"""
Operator Precedence is something that indicates which operator should perform the action first...
() --> Circular bracket is having the highest priority...
** --> Exponential operator (Next)...
* / % // --> Followed by
+ - --> Least Precedence (But, having same precedence)
"""

# Example 1...
print(2 + (5 * 2))

# Example 2...
print(2 + 4 ** 2 + (5 * 2))

# Example 3...
print(2 * 4 / 8 % 6 // 9 ** 2 + (5 * 2))

# Example 4...
print(4 - 2 + 8)