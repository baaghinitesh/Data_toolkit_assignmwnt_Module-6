# 20. Using Plotly, create a basic line plot of a randomly generated dataset, label the axes, and set the title as 'Simple Line Plot'.


import plotly.graph_objects as go
import numpy as np

# Generate random data
np.random.seed(0)  # For reproducibility
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.random.rand(100)  # 100 random values

# Create a line plot
fig = go.Figure()

# Add a line trace
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Random Data'))

# Label the axes
fig.update_layout(
    title='Simple Line Plot',
    xaxis_title='X-axis',
    yaxis_title='Y-axis'
)

# Show the plot
fig.show()
