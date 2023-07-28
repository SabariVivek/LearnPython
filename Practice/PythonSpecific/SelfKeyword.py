"""
1. Self keyword represents something that belongs to the class...
2. It can be used to access the variables and methods that are inside the class...
3. Inside the class we have to use self to access the properties
    and outside the class we have to use object reference to access the class properties....
4. Self parameter can be renamed...
"""


class Car:
    wheels = 4

    @staticmethod
    def start_the_car():
        print("Car has started...")

    def switch_off_the_car(self):
        print(self.wheels)
        self.start_the_car()


obj = Car()
print(obj.wheels)
obj.switch_off_the_car()
