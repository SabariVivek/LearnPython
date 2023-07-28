"""
Prioritizing the variables and methods in the class to restrict the access from outside...
if we put "__" before a variable or a method, system will consider that as a private variable/method...
"""


class A:
    __a = 10

    def __old_method(self):
        print("The value of a from old method is", self.__a)

    def method(self):
        self.__old_method()
        print("The value of a is", self.__a)


class B(A):
    pass


obj = B()
obj.method()
