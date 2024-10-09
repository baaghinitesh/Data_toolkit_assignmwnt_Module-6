#2. Using the Numpy function, generate an array of 100 evenly spaced numbers between 1 and 10 and Reshape that ID array into a 2D array.

import numpy as np

# Generate an array of 100 evenly spaced numbers between 1 and 10
array = np.linspace(1, 10, 100)

# Reshape the array into a 2D array (for example, 10 rows and 10 columns)
reshaped_array = array.reshape(10, 10)

print("2D Reshaped Array:\n", reshaped_array)
