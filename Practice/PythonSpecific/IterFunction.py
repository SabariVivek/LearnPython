# Iter function is used to iterate next value in list, set, tuple, dictionary values...

values = [21, 8, 99, 23, 5, 676]
iterator = iter(values)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  # Since there are only 6 values, this will throw a StopIteration error...
