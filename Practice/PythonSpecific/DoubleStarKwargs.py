"""
**kwargs is used to get the multiple value as key and value pair...
As like args here kwargs is also a user defined name...
"""


# Usage 1...
def func_1(**kwargs):
    for key, value in kwargs.items():
        print(key, value, sep=" - ")


func_1(name="sabari", password="Sabari@123")


# Usage 2...
def func_2(name, password, city):
    print(name, password, city, sep=", ")


details = {"name": "Sabari", "password": "Sabari@123", "city": "Chennai"}
func_2(**details)
