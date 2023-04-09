# import chartify


# data = chartify.examples.example_data()

# quantity_by_fruit_and_country = data.groupby(["fruit", "country"])["quantity"].sum().reset_index()
# print(quantity_by_fruit_and_country.head())

# c = chartify.Chart(blank_labels=True, y_axis_type="categorical")
# c.set_title('Stacked Horizontal Bar chart')
# c.set_subtitle('Stacked columns by a categorical factor.')
# c.set_source_label('Source: Example Data')
# c.axes.set_xaxis_label('Unit price for a fruit batch')
# c.axes.set_yaxis_label('Number of fruits')
# c.style.set_color_palette('categorical', 'Dark2')
# c.plot.bar_stacked(
#     data_frame=quantity_by_fruit_and_country,
#     categorical_columns=["fruit"],
#     numeric_column="quantity",
#     stack_column="country",
#     normalize=False,
# )

# c.plot.text(
#     data_frame=quantity_by_fruit_and_country,
#     categorical_columns=["fruit"],
#     numeric_column="quantity",
#     text_column="quantity",
#     color_column="country",
# )

# c.show()

import chartify


data = chartify.examples.example_data()

quantity_by_fruit_and_country = data.groupby(["fruit", "country"])["quantity"].sum().reset_index()
print(quantity_by_fruit_and_country.head())

c = chartify.Chart(blank_labels=True, y_axis_type="categorical")
c.set_title('Stacked Horizontal Bar chart')
c.set_subtitle('Stacked columns by a categorical factor.')
c.set_source_label('Source: Example Data')
c.axes.set_xaxis_label('Unit price for a fruit batch')
c.axes.set_yaxis_label('Number of fruits')
c.style.set_color_palette('categorical', 'Dark2')
c.plot.bar_stacked(
    data_frame=quantity_by_fruit_and_country,
    categorical_columns=["fruit"],
    numeric_column="quantity",
    stack_column="country",
    normalize=False,
)

# data = data.groupby("fruit")["quantity"].sum().reset_index()
# c.plot.bar(
#     data_frame=data,
#     categorical_columns="fruit",
#     numeric_column="quantity",
#     color_column="fruit",
# )
c.style.color_palette.reset_palette_order()
c.plot.text_stacked_total(
    data_frame=quantity_by_fruit_and_country,
    categorical_columns=["fruit"],
    numeric_column="quantity",
    stack_column="country",
    text_column="quantity",
    color_column="fruit",
)
# c.plot.text(
#     data_frame=data,
#     categorical_columns=["fruit"],
#     numeric_column="quantity",
#     text_column="quantity",
#     color_column="fruit",
# )

c.show()
