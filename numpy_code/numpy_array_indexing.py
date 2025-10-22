import numpy as np

from numpy_code.np_example import cube_data_array

score_array = np.array([10, 20, 30, 40, 50])
print(score_array)

print(score_array[0])
print(score_array[2])
print(score_array[-1])
print(score_array[-2])

# 2-d
marks_matrix = np.array([[90, 85, 80],
                         [70, 75, 80]])
print(marks_matrix)
#
print(marks_matrix[0, 0])
print(marks_matrix[0, 1])
print(marks_matrix[0, 2])

print(marks_matrix[1, 0])
print(marks_matrix[1, 1])
print(marks_matrix[1, 2])

print(marks_matrix[0])
print(marks_matrix[1])

# 3-d array


cube_data_array = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(cube_data_array)
#
# print(cube_data_array[0, 0, 0])
# print(cube_data_array[0, 1, 2])
print(cube_data_array.shape)
print("-----------------------")
print(cube_data_array[0])
# print(cube_data_array[1])
print(cube_data_array[0, 0])
print(cube_data_array[0, 0,0])
print(cube_data_array[0, 0,1])
print(cube_data_array[0, 0,2])


