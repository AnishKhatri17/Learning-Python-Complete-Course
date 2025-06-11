# module = a file containing code we want to include in our program
#          use 'import' to include a module (built-in or our own)
#          useful to break up a large program reusable seperate files

# print(help("modules"))
# print(help("math"))

import math
import math as m   # m is the nickname of the module 
from math import pi  # directly importing the value
# Note: "from math import pi" don't use like this because there could be name conflicts

print(math.pi)
print(m.pi)
print(pi)
print("\n\n")


import Example_39 # using my module

pi_value = Example_39.pi
square = Example_39.square(3)
cube = Example_39.cube(4)
circumference = Example_39.circumference(3)
area = Example_39.area(10)

print(pi_value)
print(square)
print(cube)
print(circumference)
print(area)

# When we run this module file Python creates a folder named "__pycache__ automatically to cache the compiled version to speed up things leave it as it is..."