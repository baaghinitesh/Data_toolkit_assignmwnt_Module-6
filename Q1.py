# 1. Demonstrate three different methods for creating identical 2D arrays in NumPy. Provide the code for each method and the final output after each method.

#	Method 1: Using numpy.array()
import numpy as np

# Creating a 2D array using numpy.array()
array1 = np.array([[1, 2, 3], [4, 5, 6]])
print("Method 1:\n", array1)

#	Method 2: Using numpy.zeros()
# Creating a 2D array filled with zeros and then assigning values
array2 = np.zeros((2, 3), dtype=int)
array2[0] = [1, 2, 3]
array2[1] = [4, 5, 6]
print("Method 2:\n", array2)

#	Method 3: Using numpy.ones()
# Creating a 2D array filled with ones and then multiplying
array3 = np.ones((2, 3), dtype=int) * [1, 2, 3]
array3[1] = [4, 5, 6]
print("Method 3:\n", array3)
