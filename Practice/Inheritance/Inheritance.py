# Inheritance is the concept of aquiring the properties of parent class to child class...
class A:
    a = 5

    def method(self):
        print("I am in method of Class A...")


class B(A):
    # Instead of keeping the whole class null, we can put pass keyword...
    pass


obj = B()
print(obj.a)
obj.method()
