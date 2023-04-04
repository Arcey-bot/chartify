import chartify._core.chart as chartify
import chartify._core.plot
import chartify.examples as examples

def main():
    c = chartify.Chart(y_axis_type='density')
    data = examples.example_data()
    c.set_title('A title')
    c.set_subtitle('A subtitle')
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
    # c.plot.bar(data_frame=grouped_bar_data,
    #         categorical_columns=['fruit', 'country'],
    #         numeric_column='quantity',
    #         color_column='fruit')
    # c.show()
    ndata = data.groupby(['fruit', 'country'])[['quantity']].sum().reset_index()

    # print(data.head(50))
    c.plot.cumulative_histogram(data_frame=data.head(50),
            values_column='unit_price',
            color_column='fruit',
            )
#     c.plot.cumulative_histogram(data_frame=data, values_column="unit_price",bins=50)
    
    c.show()
    with open('data.txt', 'w') as f:
        f.write(str(data))

if __name__ == '__main__':
    main()