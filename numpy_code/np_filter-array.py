import numpy as np

ages_array = np.array([12, 17, 19, 21, 15, 18, 22])

print(ages_array)

above_18 = ages_array > 18
print(above_18)

filtered_result = ages_array[above_18]
print(filtered_result)

# filter even numbers
even_numbers = ages_array[ages_array % 2 == 0]
print(even_numbers)

# filter odd ages
odd_numbers = ages_array[ages_array % 2 == 1]
print(odd_numbers)