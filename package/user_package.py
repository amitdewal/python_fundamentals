from math_package import basic_operation
from math_package.basic_operation import subtract

from  math_package.advanced_operation import square

print(basic_operation.add(10,20))
print(subtract(110,20))
print(square(10))

import  math_package.basic_operation as basic
basic.add(10,20)
basic.subtract(100,20)

import math_package.advanced_operation
print(dir(math_package.basic_operation))