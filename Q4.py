# 4. Generate a 3x3 array with random floating-point numbers between 5 and 20. Then, round each number in the array to 2 decimal places.

import numpy as np

# Generate a 3x3 array with random floating-point numbers between 5 and 20
random_array = np.random.uniform(5, 20, (3, 3))

# Round each number in the array to 2 decimal places
rounded_array = np.round(random_array, 2)

print("Random Array:\n", random_array)
print("\nRounded Array:\n", rounded_array)
