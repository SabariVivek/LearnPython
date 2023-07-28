# Super keyword is used to call the parent properties of the child class...
class A:
    def __init__(self):
        print("I am in class \"A\" constructor")

    a = 5

    def method(self):
        print("The value of a is", A.a)


class B(A):
    def __init__(self):
        super().__init__()
        print("I am in class \"B\" constructor")

    a = 10

    def method(self):
        print(obj.a)
        print(super().a)
        super().method()
        print("The value of a is", self.a)


obj = B()
obj.method()
