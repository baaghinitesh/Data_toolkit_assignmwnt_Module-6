# 18. With Bokeh, plot a line chart of a sine wave function, add grid lines, label the axes, and set the title as 'Sine Wave Function'.

from bokeh.plotting import figure, show, output_file
import numpy as np

# Specify the output HTML file
output_file("sine_wave.html")

# Generate x values
x = np.linspace(0, 2 * np.pi, 100)  # 100 points from 0 to 2π
y = np.sin(x)  # Calculate the sine of each x value

# Create a new plot
p = figure(title='Sine Wave Function', x_axis_label='X-axis', y_axis_label='Y-axis')

# Add a line renderer
p.line(x, y, legend_label='Sine Wave', line_width=2, line_color='blue')

# Add grid lines
p.grid.grid_line_color = 'gray'
p.grid.grid_line_alpha = 0.5

# Show the plot
show(p)
