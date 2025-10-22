import numpy as np

numbers_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
result_forty = np.where(numbers_array == 40)
print(result_forty)  # index 3

greater_than_thirtyfive = np.where(numbers_array > 35)
print(greater_than_thirtyfive)

exam_scores = np.array([1, 2, 3, 45, 4, 4, 4])
print(exam_scores)

positions_of_fours = np.where(exam_scores == 4)
print(positions_of_fours)

all_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])
even_indexes = np.where(all_numbers % 2 == 0)
print(even_indexes)

sorted_data = np.array([6, 7, 8, 9])
print(sorted_data)

insertion_point = np.searchsorted(sorted_data, 7)
print(insertion_point)
