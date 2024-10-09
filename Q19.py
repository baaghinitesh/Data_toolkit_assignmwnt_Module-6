# 19. Using Bokeh, generate a bar chart of randomly generated categorical data, color bars based on their values, add hover tooltips to display exact values, label the axes, and set the title as 'Random Categorical Bar Chart'.

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import numpy as np
import pandas as pd

# Specify the output HTML file
output_file("random_categorical_bar_chart.html")

# Generate random categorical data
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = np.random.randint(10, 100, size=len(categories))

# Create a DataFrame
data = pd.DataFrame({'Category': categories, 'Value': values})

# Create a ColumnDataSource
source = ColumnDataSource(data)

# Create a new plot
p = figure(x_range=categories, title='Random Categorical Bar Chart', 
           x_axis_label='Categories', y_axis_label='Values', 
           tools="")

# Add bars with colors based on their values
p.vbar(x='Category', top='Value', source=source, 
        line_color='white', fill_color='blue', 
        width=0.6)

# Add hover tooltips
hover = HoverTool()
hover.tooltips = [("Category", "@Category"), ("Value", "@Value")]
p.add_tools(hover)

# Add grid lines
p.grid.grid_line_color = 'gray'
p.grid.grid_line_alpha = 0.5

# Show the plot
show(p)
