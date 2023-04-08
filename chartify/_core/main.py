import numpy as np
import pandas as pd
import chartify._core.chart as chartify
import chartify._core.plot
import chartify.examples as examples

def main():
    # test_cumulative_histogram()
    test_area_chart()

def test_cumulative_histogram():
    c = chartify.Chart(y_axis_type='density')
    c.set_title('Cumulative histogram')
    c.set_subtitle('A subtitle')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    data = examples.example_data()
    # c.plot.cumulative_histogram(data_frame=data, values_column="unit_price",bins=50)
    c.plot.cumulative_histogram(data_frame=data.head(50), values_column='unit_price', color_column='fruit',)
    c.show()

# Filling area chart with 0 on NaN values (https://github.com/spotify/chartify/issues/56)
def test_area_chart():
    d = {
        'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'B': [1, 2, 3, 4, 0, 0, 0, 8, 9, 10],
        'C': [10, 9, 8, 7, 6, 5, np.nan, np.nan, np.nan, np.nan],
    }
    df = pd.DataFrame(data=d)
    data = examples.example_data()
    total_quantity_by_month_and_fruit = (
        data.groupby([data["date"] + pd.offsets.MonthBegin(-1), "fruit"])["quantity"]
        .sum()
        .reset_index()
        .rename(columns={"date": "month"})
        .sort_values("month")
    )
    
    total_quantity_by_month_and_fruit = total_quantity_by_month_and_fruit[total_quantity_by_month_and_fruit.fruit != 'Apple']
    total_quantity_by_month_and_fruit = total_quantity_by_month_and_fruit[total_quantity_by_month_and_fruit.fruit != 'Grape']

    total_quantity_by_month_and_fruit['quantity'].iloc[8:10] = np.nan
    total_quantity_by_month_and_fruit['quantity'].iloc[-7:] = np.nan
    total_quantity_by_month_and_fruit['quantity'].iloc[-1] = -10

    c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
    c.set_title('Unstacked Area chart')
    c.set_subtitle('Show overlapping values. Automatically adjusts opacity.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.area(
        data_frame=df,
        x_column='A',
        y_column='B',
        stacked=False,
    )
    # c.plot.area(
    #     data_frame=total_quantity_by_month_and_fruit,
    #     x_column='month',
    #     y_column='quantity',
    #     color_column='fruit',
    #     stacked=False,
    # )
    c.show()

if __name__ == '__main__':
    main()