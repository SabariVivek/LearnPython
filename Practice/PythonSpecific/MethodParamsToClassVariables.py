"""
In other languages, we cannot assign the parameter of the functions to class variables...
In python, with the help of self keyword we can declare the function parameters to class variables...
"""


class A:
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience
        print(name, role, experience, sep=" | ")

    def func(self):
        print(self.name, self.role, self.experience, sep=" : ")


obj = A("Sabari", "Automation Tester", 12)
obj.func()
