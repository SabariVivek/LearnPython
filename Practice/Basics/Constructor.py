""" Constructors are generally used for instantiating an object.
A constructor is a special method that is called when an object is created.
In Python, the __init__() method is called the constructor and is always called when an object is created."""


class A:

    def __init__(self, a=None, b=None):
        if (a is None) and (b is None):
            print("Default constructor is called...")
        elif (a is not None) and (b is not None):
            print("The value of A and B :", a, b)


obj_one = A(10, 20)
obj_two = A()
