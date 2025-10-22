import numpy as np

numbers_array = np.array([10, 20, 30, 40, 50, 60])
print(numbers_array)

# split into 3 parts
split_result = np.array_split(numbers_array, 3)
for part in split_result:
    print(part)


# 2 d array
table_data_array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

print(table_data_array)

row_chunks = np.array_split(table_data_array, 2)
for row_part in row_chunks:
    print(row_part)


column_chunks = np.array_split(table_data_array, 2,1)
for column_chunks_part in column_chunks:
    print(column_chunks_part)


print("----------------------------")
# using hsplit and vsplit
hsplit = np.hsplit(table_data_array, 3)
for hsplit_part in hsplit:
    print(hsplit_part)

print("----------------------------")
vsplit = np.vsplit(table_data_array, 2)
for vsplit_part in vsplit:
    print(vsplit_part)