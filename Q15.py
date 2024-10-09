# 15. Create a NumPy array data containing 1000 samples from a normal distribution. Perform the following tasks using Matplotlib:
# a) Plot a histogram of the data with 30 bins.
# b) Overlay a line plot representing the normal distribution's probability density function (PDF).
# c) Label the x-axis as 'Value' and the y-axis as 'Frequency/Probability'.
# d) Set the title of the plot as 'Histogram with PDF Overlay.


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate 1000 samples from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)  # Mean = 0, Std Dev = 1

# a) Plot a histogram of the data with 30 bins
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')

# b) Overlay the normal distribution's probability density function (PDF)
xmin, xmax = plt.xlim()  # Get the range of the x-axis
x = np.linspace(xmin, xmax, 100)  # Generate 100 points from xmin to xmax
p = stats.norm.pdf(x, loc=0, scale=1)  # Calculate the PDF

plt.plot(x, p, 'k', linewidth=2, label='PDF')
plt.legend()

# c) Label the axes
plt.xlabel('Value')
plt.ylabel('Frequency/Probability')

# d) Set the title of the plot
plt.title('Histogram with PDF Overlay')

# Show the plot
plt.show()
