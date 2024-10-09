# 5. Create a NumPy array with random integers between 1 and 10 of shape (5, 6). After creating the array perform the following operations:
# a) Extract all even integers from array.
# b) Extract all odd integers from array.


import numpy as np

# Create a 5x6 array with random integers between 1 and 10
random_array = np.random.randint(1, 11, size=(5, 6))

print("Random Array:\n", random_array)

# a) Extract all even integers from the array
even_integers = random_array[random_array % 2 == 0]
print("\nEven Integers:\n", even_integers)

# b) Extract all odd integers from the array
odd_integers = random_array[random_array % 2 != 0]
print("\nOdd Integers:\n", odd_integers)
