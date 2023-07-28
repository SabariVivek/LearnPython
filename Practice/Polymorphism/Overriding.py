# Overriding is the concept of declaring the properties of parent class in child class...
class A:
    a = 5

    def method(self):
        print("I am in class A")


class B(A):
    a = 10

    def method(self):
        print("I am in class B")


"""
But, when we are using the child object we can only call the immediate properties (same class)...
If we want to call the parent properties, we have to use the super keyword...
"""
obj = B()
print(obj.a)
obj.method()
