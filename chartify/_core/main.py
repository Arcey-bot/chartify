import pandas as pd
import chartify._core.chart as chartify
import chartify._core.plot
import chartify.examples as examples

def main():
    chart = chartify.Chart(blank_labels=True, x_axis_type="categorical")

    with chart as c:
        data = examples.example_data()
        c.set_title('Cumulative Frequency Histogram')
        c.set_subtitle('Example Code Running')
        c.set_source_label('Source: A source')
        c.axes.set_xaxis_label('Unit price for a fruit batch')
        c.axes.set_yaxis_label('Number of fruits')
        c.style.set_color_palette('categorical', 'Dark2')
        c.set_title("Parallel coordinate charts")
        c.set_subtitle("")
        total_quantity_by_fruit_and_country = data.groupby(["fruit", "country"])["quantity"].sum().reset_index()
        c.plot.bar(
            data_frame=total_quantity_by_fruit_and_country,
            categorical_columns=["fruit", "country"],
            numeric_column="quantity",
            color_column="fruit"
        )    
        c.show()

    with open('data.txt', 'w') as f:
        f.write(str(data))

if __name__ == '__main__':
    main()