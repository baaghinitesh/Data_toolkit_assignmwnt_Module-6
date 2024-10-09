# 6. Create a 3D NumPy array of shape (3, 3, 3) containing random integers between 1 and 10. Perform the following operations:
# a) Find the indices of the maximum values along each depth level (third axis).
# b) Perform element-wise multiplication of between both array.

import numpy as np

# Create a 3D array of shape (3, 3, 3) with random integers between 1 and 10
array_3d = np.random.randint(1, 11, size=(3, 3, 3))

print("3D Array:\n", array_3d)

# a) Find the indices of the maximum values along each depth level (third axis)
max_indices = np.argmax(array_3d, axis=2)
print("\nIndices of Maximum Values along each Depth Level:\n", max_indices)

# b) Perform element-wise multiplication of the array with itself
multiplied_array = array_3d * array_3d
print("\nElement-wise Multiplication of the Array:\n", multiplied_array)
