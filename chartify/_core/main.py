import pandas as pd
import chartify._core.chart as chartify
import chartify._core.plot
import chartify.examples as examples

def main():
    c = chartify.Chart(blank_labels=True, x_axis_type="categorical")
    data = examples.example_data()
    c.set_title('Cumulative Frequency Histogram')
    c.set_subtitle('Example Code Running')
    c.set_source_label('Source: A source')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    # c.callout.text('A callout', 25, 25)
    # c.axes.set_xaxis_range(0, 50)
    # c.axes.set_yaxis_range(0, 75)
    grouped_bar_data = (data.groupby(['country', 'fruit'])[['quantity']].sum()
            .reset_index()
           )
    c.style.set_color_palette('categorical', 'Dark2')
    ndata = data.groupby(['fruit', 'country'])[['quantity']].sum().reset_index()

    # print(data.head(50))
    # c.plot.cumulative_histogram(data_frame=data.head(50),
    #         values_column='unit_price',
    #         color_column='fruit',
    #         )
    # c.plot.stacked_histogram(data_frame=data, values_column="unit_price",bins=50)
    
    c.set_title("Parallel coordinate charts")
    c.set_subtitle("")
    total_quantity_by_fruit_and_country = data.groupby(["fruit", "country"])["quantity"].sum().reset_index()
    dd = pd.DataFrame({
        "fruit": ["Apple"],
        "country": ["BR"],
        "quantity": [0]
    })

    total_quantity_by_fruit_and_country.update(dd)

    c = chartify.Chart(blank_labels=True, x_axis_type="categorical")
    c.set_title("Stacked bar chart")
    c.set_subtitle("Stack columns by a categorical factor.")
    c.plot.parallel(
        data_frame=total_quantity_by_fruit_and_country,
        categorical_columns="fruit",
        numeric_column="quantity",
        color_column="country",
        allow_nan=True
    )
    c.show()

    with open('data.txt', 'w') as f:
        f.write(str(data))

if __name__ == '__main__':
    main()