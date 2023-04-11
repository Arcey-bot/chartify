from math import pi
import pandas as pd
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

from chartify import examples
import chartify

data = examples.example_data()
# data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
data = data.groupby(["fruit"])["quantity"].sum().reset_index()
print(data)

# Divide current value by total value to get angle of the pie wedge
# data['angle'] = data['quantity']/data['quantity'].sum() * 2* pi
# data['color'] = Category20c[len(data)]

# p = figure(height=350, title="Pie Chart", toolbar_location=None,
#            tools="hover", tooltips="@fruit: @quantity", x_range=(-0.5, 1.0))

# p.wedge(x=0, y=1, radius=0.4,
#         start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
#         line_color="white", fill_color='color', legend_field='fruit', source=data)

# p.axis.axis_label = None
# p.axis.visible = False
# p.grid.grid_line_color = None

# show(p)
cc = chartify.Chart(x_axis_type="categorical")
cc.plot.pie(
    data_frame=data,
    categorical_column="fruit",
    numeric_column="quantity",
    color_column="fruit",
)
cc.show()