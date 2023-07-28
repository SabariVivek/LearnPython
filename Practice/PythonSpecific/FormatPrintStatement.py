"""
There are a couple of ways to format the print statements...
        * Using ,
        * Using +
        * Using format()
        * Using format() with index
        * Using % operator
"""

name = "Sabari"
role = "Automation Tester"
experience = 4

# Way 1...
print("My name is " + name + " and My role is " + role + " and My experience is " + str(experience))

# Way 2...
print("My name is", name, "and My role is", role, "and My experience is", experience)

# Way 3...
print("My name is {} and My role is {} and My experience is {}".format(name, role, experience))

# Way 4...
print("My name is {2} and My role is {0} and My experience is {1}".format(role, experience, name))

# Way 5...
print("My name is %s and My role is %s and My experience is %d" % (name, role, experience))
