import pandas as pd
import chartify._core.chart as chartify
import chartify._core.plot
import chartify.examples as examples

def main():
    chart = chartify.Chart(x_axis_type="density")

    data = {
    'United States': 157,
    'United Kingdom': 93,
    'Japan': 89,
    'China': 63,
    'Germany': 44,
    'India': 42,
    'Italy': 40,
    'Australia': 35,
    'Brazil': 32,
    'France': 31,
    'Taiwan': 31,
    'Spain': 29
}
    data = pd.Series(data).reset_index(name='value').rename(columns={'index': 'country'})


    with chart as c:
        # data = examples.example_data()
        c.set_title('Cumulative Frequency Histogram')
        c.set_subtitle('Example Code Running')
        c.set_source_label('Source: A source')
        c.axes.set_xaxis_label('Unit price for a fruit batch')
        c.axes.set_yaxis_label('Number of fruits')
        c.style.set_color_palette('categorical', 'Dark2')
        c.set_title("Parallel coordinate charts")
        c.set_subtitle("")
        c.plot.pie(
            data_frame=data,
            categorical_column=["country"],
            numeric_column="value",
            color_column="country"
        )    
        c.show()

    with open('data.txt', 'w') as f:
        f.write(str(data))

if __name__ == '__main__':
    main()