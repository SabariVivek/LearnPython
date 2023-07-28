class A:
    def method(self, a=None, b=None):
        if (a and b is None):
            print("Default Method")
        elif (a is not None):
            print("Method with argument A :", a)
        elif (b is not None):
            print("Method with argument B :", b)
        elif (a and b is not None):
            print("Method with argument A and B :", a, b)


obj = A()
obj.method()
obj.method(10)
obj.method(None, 20)
obj.method(10, 20)
