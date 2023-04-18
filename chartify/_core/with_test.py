import chartify

# Generate example data
data = chartify.examples.example_data()

quantity_by_fruit = data.groupby("fruit")["quantity"].sum().reset_index()

with chartify.Chart(blank_labels=True, x_axis_type="categorical") as ch:
    ch.set_title("Vertical bar plot")
    ch.set_subtitle("Automatically sorts by value counts.")
    ch.plot.bar(
        data_frame=quantity_by_fruit,
        categorical_columns="fruit",
        numeric_column="quantity",
    )
    ch.show()