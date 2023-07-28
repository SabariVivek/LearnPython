# For loop with one parameter...
for i in range(10):
    print(i, end=" - ")  # 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9

# For loop with some range...
for i in range(0, 11):
    print(i, end=" : ")  # 0 : 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10

# For loop with increment...
for i in range(2, 10, 2):
    print(i, end=" # ")  # 2 # 4 # 6 # 8

# For loop with decrement...
for i in range(10, 1, -1):
    print(i, end=" | ")  # 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2

# For loop with else block...
for i in range(3):
    print("Hi, I am", i)
else:
    print("I am out of the for loop")
