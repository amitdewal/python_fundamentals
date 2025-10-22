from time import process_time

import numpy as np

unsorted_numbers = np.array([5,2,9,1,7])
print(unsorted_numbers)

sorted_numbers = np.sort(unsorted_numbers)
print(sorted_numbers)

print("-------")
# 2-d array sorting

matrix_scores = np.array([
    [6, 4, 5],
    [3, 1, 2]
])
print(matrix_scores)
print("-------")
sorted_scores = np.sort(matrix_scores)
print(sorted_scores)

# column wise sorted
print("-------")
colum_sorted = np.sort(matrix_scores, axis=0)
print(colum_sorted)

# sorting string
student_names = np.array(["Zara","Arjun","Meena","Amit"])
print(student_names)
sorted_names = np.sort(student_names)
print(sorted_names)