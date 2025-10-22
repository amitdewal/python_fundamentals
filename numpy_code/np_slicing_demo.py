import numpy as np

from set.set_remove import remove_item

scores_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(scores_array)

print(scores_array[1:4])
print(scores_array[:5])
print(scores_array[5:])
print(scores_array[:])
print(scores_array[::2])  # start:end:steps
print(scores_array[::3])
