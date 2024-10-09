# 21. Using Plotly, create an interactive pie chart of randomly generated data, add labels and percentages, set the title as 'Interactive Pie Chart'.

import plotly.graph_objects as go
import numpy as np

# Generate random data
np.random.seed(0)  # For reproducibility
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = np.random.randint(10, 100, size=len(labels))

# Create a pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, 
                               textinfo='label+percent', 
                               insidetextorientation='radial')])

# Set the title
fig.update_layout(title_text='Interactive Pie Chart')

# Show the plot
fig.show()
