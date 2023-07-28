# RangeDataType.py

# Declaration, printing type...
val = range(10)
print(val)  # Output --> range(0, 10)...
print(type(val))

# Using for loop for printing the range values...
for a in val:
    print(a)

# Different types of range declaration...
for a in range(3):
    print(a)

for a in range(1, 5):
    print(a)

for a in range(1, 10, 2):
    print(a)

for a in range(10, 1, -2):
    print(a)

# Indexing in range...
print(val[0])
print(val[1])
print(val[2])

# Slicing in range...
new_value = range(10)
print(val[4:9])
print(val[:4])
print(val[6:])
print(val[:])
