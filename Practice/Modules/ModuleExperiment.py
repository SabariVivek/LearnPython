# ModuleExperiment.py
import math

from CalculatorModule import *
from Practice.Modules import CalculatorModule

# To call the functions which are there in Calculator Module...
add(2, 3)
sub(3, 2)
multiply(2, 3)
division(3, 2)

# To know the function which are present in the Calculator Module...
print(dir(CalculatorModule))

# Inbuilt modules...
print(math.sqrt(21))
print(math.ceil(21.08))
print(math.floor(21.08))
print(math.pi)
