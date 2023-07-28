import random

# Way 1...
print(random.random())  # It will always give a decimal value between 0 and 1...
print(random.random() * 100)  # Multiplying the value with 100 will give you some int...
print(int(random.random() * 100))  # Type casting with int will neglect the decimal...

# Way 2...
print(random.randint(1, 100))
print(random.randint(23, 34))

# Way 3...(randint will print 2 to 5, but randrange won't consider the last value hence --> 2 to 4)
print(random.randrange(2, 5))
print(random.randrange(4, 8))
