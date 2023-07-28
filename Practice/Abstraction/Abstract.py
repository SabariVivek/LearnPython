from abc import ABC, abstractmethod

"""
* For partial implementation of Class, we can use Abstract classes...
* When what to implement is clear, but how to implement is not clear,
    then we have to go for Abstract classes and Abstract methods...
"""


class A(ABC):
    @abstractmethod
    def func_one(self):
        pass

    @abstractmethod
    def func_two(self):
        pass

    def func_three(self):
        print("Inside Method 3...")

    def func_four(self):
        print("Inside Method 4...")


class B(A):
    def func_one(self):
        print("Inside Method 1...")

    def func_two(self):
        print("Inside Method 2...")


obj = B()
obj.func_one()
obj.func_two()
obj.func_three()
obj.func_four()
