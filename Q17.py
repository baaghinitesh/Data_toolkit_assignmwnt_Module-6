# 17. Create a Seaborn scatter plot of two random arrays, color points based on their position relative to the origin (quadrants), add a legend, label the axes, and set the title as 'Quadrant-wise Scatter Plot'.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)  # For reproducibility
x = np.random.uniform(-10, 10, 100)
y = np.random.uniform(-10, 10, 100)

# Create a DataFrame
data = pd.DataFrame({'X': x, 'Y': y})

# Determine the quadrant
conditions = [
    (data['X'] > 0) & (data['Y'] > 0),  # Quadrant 1
    (data['X'] < 0) & (data['Y'] > 0),  # Quadrant 2
    (data['X'] < 0) & (data['Y'] < 0),  # Quadrant 3
    (data['X'] > 0) & (data['Y'] < 0)   # Quadrant 4
]
quadrants = ['Q1', 'Q2', 'Q3', 'Q4']
data['Quadrant'] = np.select(conditions, quadrants, default='Origin')

# Create a Seaborn scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='X', y='Y', hue='Quadrant', palette='deep', style='Quadrant', s=100)

# Add a legend
plt.legend(title='Quadrants')

# Label the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the title of the plot
plt.title('Quadrant-wise Scatter Plot')

# Show the plot
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')  # X-axis
plt.axvline(0, color='black', lw=0.5, ls='--')  # Y-axis
plt.show()
