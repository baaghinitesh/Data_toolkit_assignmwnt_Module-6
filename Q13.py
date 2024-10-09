# 13. Create two NumPy arrays, x and y, each containing 100 random float values between 0 and 1. Perform the following tasks using Matplotlib and NumPy:
# a) Create a scatter plot using x and y, setting the color of the points to red and the marker style to 'o'.
# b) Add a horizontal line at y = 0.5 using a dashed line style and label it as y = 0.5'.
# c) Add a vertical line at x = 0.5 using a dotted line style and label it as 'x = 0.5'.
# d) Label the x-axis as 'X-axis' and the y-axis as 'Y-axis'.
# e) Set the title of the plot as 'Advanced Scatter Plot of Random Values'.
# f) Display a legend for the scatter plot, the horizontal line, and the vertical line.

import numpy as np
import matplotlib.pyplot as plt

# Create two NumPy arrays with 100 random float values between 0 and 1
x = np.random.rand(100)
y = np.random.rand(100)

# a) Create a scatter plot
plt.scatter(x, y, color='red', marker='o', label='Random Points')

# b) Add a horizontal line at y = 0.5
plt.axhline(y=0.5, color='blue', linestyle='--', label='y = 0.5')

# c) Add a vertical line at x = 0.5
plt.axvline(x=0.5, color='green', linestyle=':', label='x = 0.5')

# d) Label the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# e) Set the title of the plot
plt.title('Advanced Scatter Plot of Random Values')

# f) Display a legend
plt.legend()

# Show the plot
plt.show()
