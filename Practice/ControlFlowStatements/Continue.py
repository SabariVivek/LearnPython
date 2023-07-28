# Continue Statement...

count = 0
while count <= 5:
    if count == 3:
        count += 1
        continue
    print("I am", count)
    count += 1
else:
    print("I am out of the while loop")
