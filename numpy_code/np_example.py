import numpy as np

nums = np.array([10, 20, 30, 40, 50])

print(nums)
print(type(nums))

# tuple
number_tupe_array = np.array((10, 20, 30, 40, 50))
print(number_tupe_array)

# 0-d
simple_value_array = np.array(99)
print(simple_value_array, simple_value_array.shape)

# 1-d
student_scores_array = np.array([80, 85, 90, 95, 100])
print(student_scores_array, student_scores_array.shape)

# 2-d

matrix_table_array = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_table_array)

print(matrix_table_array.shape)

# 3-d

cube_data_array = np.array([[[1, 2, 3], [4, 5, 6]],
                            [[7, 8, 9], [10, 11, 12]], ])

print(cube_data_array)
