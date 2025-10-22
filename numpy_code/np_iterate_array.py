import numpy as np

numbers_array = np.array([10, 20, 30, 40])

for row in numbers_array:
    print(row)

numbers_two_d_array = np.array([
    [10, 20, 30],
    [50, 60, 80]
])

for row in numbers_two_d_array:
    # print(row)
    for item in row:
        print(item)

numbers_array_3_d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

for block in numbers_array_3_d:
    for row in block:
        for item in row:
            print(item)

# nditer() best approach

student_marks_table_row = np.array([
    [85, 90, 95],
    [88, 92, 96]
])

for score in np.nditer(student_marks_table_row):
    print(score)

