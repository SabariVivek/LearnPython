# Getter & Setter is used to access the private variables from outside the class...
class A:
    __age = 0

    def set_age(self, age):
        A.__age = age

    def get_age(self):
        return self.__age


obj = A()
obj.set_age(24)
print(obj.get_age())
