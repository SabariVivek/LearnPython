# __init__ method is like a constructor in java...
class A:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(self.a, self.b, self.c, self.d, sep=" : ")


obj = A(10, 20, 30, 40)
