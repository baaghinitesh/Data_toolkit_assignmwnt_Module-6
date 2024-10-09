# 14. Create a time-series dataset in a Pandas DataFrame with columns: 'Date', 'Temperature', 'Humidity' and Perform the following tasks using Matplotlib:
# a) Plot the 'Temperature' and 'Humidity' on the same plot with different y-axes (left y-axis for 'Temperature' and right y-axis for 'Humidity').
# b) Label the x-axis as 'Date'.
# c) Set the title of the plot as 'Temperature and Humidity Over Time'.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a date range
dates = pd.date_range(start='2023-01-01', periods=100)

# Generate random temperature and humidity data
temperature = np.random.uniform(low=15, high=35, size=100)  # Temperature between 15 and 35 degrees
humidity = np.random.uniform(low=30, high=90, size=100)     # Humidity between 30% and 90%

# Create a DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature,
    'Humidity': humidity
})

# Set the date as the index
data.set_index('Date', inplace=True)

# Plot the 'Temperature' and 'Humidity' with different y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot Temperature on the left y-axis
ax1.plot(data.index, data['Temperature'], color='red', label='Temperature', marker='o', linestyle='-', markersize=4)
ax1.set_ylabel('Temperature (°C)', color='red')
ax1.tick_params(axis='y', labelcolor='red')
ax1.grid(False)  # Disable grid for the first y-axis

# Create a second y-axis for Humidity
ax2 = ax1.twinx()
ax2.plot(data.index, data['Humidity'], color='blue', label='Humidity', marker='s', linestyle='-', markersize=4)
ax2.set_ylabel('Humidity (%)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Add grid to the second y-axis
ax2.grid(True, linestyle='--', alpha=0.5)

# Label the x-axis
ax1.set_xlabel('Date')

# Set the title of the plot
plt.title('Temperature and Humidity Over Time')

# Improve layout and display
plt.tight_layout()
plt.show()
