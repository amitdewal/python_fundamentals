import numpy as np

original_array = np.array([1, 2, 3, 5, 6,3])
print(original_array)
print(original_array.shape)

# reshaping
reshaped_array = original_array.reshape(2, 3)
print(reshaped_array)
print(reshaped_array.shape)

# 3-d
print("---------------")
reshaped_3_array = original_array.reshape(2,1,3)
print(reshaped_3_array)
print(reshaped_3_array.shape)

# auto reshaping
print("---------------")
auto_reshape = original_array.reshape(2, -1) # there -1 means column but this is decided by the numphy
print(auto_reshape)
print(auto_reshape.shape)

