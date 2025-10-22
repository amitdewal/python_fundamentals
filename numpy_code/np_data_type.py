import numpy as np

integer_array = np.array([1, 2, 3])
print(integer_array)
print(integer_array.dtype)  # this tell data type present in the array

float_array = np.array([1.1, 2.0, 3.4])
print(float_array.dtype)

bool_array = np.array([True, False, True])
print(bool_array.dtype)
str_array = np.array(["joe", "doe", "josh"])
print(str_array.dtype)

# one data type to other data type conversion
int_array = np.array([1, 2, 3])
print(int_array.dtype)

convert_to_float_from_integer = np.array([1, 2, 3],dtype=np.float64)
print(convert_to_float_from_integer)
print(convert_to_float_from_integer.dtype)

# size of the array checking
num = np.array([1, 2, 3])
print(num.itemsize)