from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models import Slider
import numpy as np

# Create a new plot
p = figure(title="Interactive Plot with Slider", x_axis_label='x', y_axis_label='y')

# Initial data
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

line = p.line(x, y, line_width=2)

# Callback function to update the plot
def update(attr, old_value, new_value):
    frequency = slider.value
    y = np.sin(frequency * x)
    line.data_source.data['y'] = y

# Create a slider widget
slider = Slider(start=0.1, end=10, value=1, step=0.1, title="Frequency")
slider.on_change('value', update)

# Layout the plot and slider
layout = column(p, slider)

# Add the layout to the current document
curdoc().add_root(layout)

