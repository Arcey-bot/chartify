from click import DateTime
import pandas as pd
import chartify

# Generate example data
data = chartify.examples.example_data()

# Sum price grouped by date
price_by_date = data.groupby("date")["total_price"].sum().reset_index()  # Move 'date' from index to column
print(price_by_date.head())

# Plot the data
ch = chartify.Chart(blank_labels=True, x_axis_type="datetime")
ch.set_title("Line charts")
ch.set_subtitle("Plot two numeric values connected by an ordered line.")

# price_by_date["date"] = price_by_date["date"].apply(lambda x : str(x.date()))
ch.plot.line(   
    # Data must be sorted by x column
    data_frame=price_by_date.sort_values("date"),
    x_column="date",
    y_column="total_price",
    hoverable=True,
    hover_info=[("date", "@date{%F}"), ("total_price", "@total_price")],
    hover_formatters={"@date": "datetime"},
    hover_mode="vline",
)
ch.show()