import numpy as np

array_one = np.array([10, 20, 30])
array_two = np.array([40, 50, 60])

print(array_one)
print(array_two)

joined_array = np.concatenate((array_one, array_two))
print(joined_array)

# 2- d array joinning
matrix_one = np.array([
    [1,2],
    [3,4]
])


matrix_two = np.array([
    [5,6],
    [7,8]
])

print(matrix_one)
print(matrix_two)

joined_matrix_vertical = np.concatenate((matrix_one, matrix_two))
print(joined_matrix_vertical)


