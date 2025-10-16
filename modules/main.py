"""
different ways to import the modules
"""

# import mymath
# print(mymath.add(10,20))
# print(mymath.subtract(10,20))
# print(mymath.square(10,))



# from mymath  import  add,subtract
# print(add(10,20))
# print(subtract(10,20))

import  mymath as mm
print(mm.square(10))
print(mm.subtract(10,20))


import mymath

# this dir function tell all the funtion available in the module
print(dir(mymath))