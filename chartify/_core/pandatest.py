import random
import pandas as pd
import numpy as np

import chartify

def example_data():
    """Data set used in Chartify examples."""
    np.random.seed(1)
    N_SAMPLES = 1000

    example_data = pd.DataFrame()
    date_range = pd.date_range("2017-01-01", "2017-12-31")

    COUNTRIES, COUNTRY_P = ["US", "GB", "CA", "JP", "BR"], [0.35, 0.17, 0.23, 0.15, 0.1]

    FRUIT = ["Orange", "Apple", "Banana", "Grape"]
    PRICE = [0.5, 1.0, 0.25, 2.0]
    fruit_price_map = dict(list(zip(FRUIT, PRICE)))
    day_probabilities = np.random.dirichlet(list(range(1, 366)))
    example_data["date"] = np.random.choice(date_range, p=day_probabilities, size=N_SAMPLES)

    COUNTRY_FRUIT_P = {c: np.random.dirichlet([len(FRUIT)] * len(FRUIT)) for c in COUNTRIES}
    example_data["country"] = np.random.choice(COUNTRIES, p=COUNTRY_P, size=N_SAMPLES)

    example_data["fruit"] = example_data["country"].apply(lambda x: np.random.choice(FRUIT, p=COUNTRY_FRUIT_P[x]))

    example_data["unit_price"] = example_data["fruit"].map(fruit_price_map) * (
        1.0 + np.random.normal(0, 0.1, size=N_SAMPLES)
    )
    example_data["quantity"] = example_data["unit_price"].apply(
        lambda x: max(0, np.random.poisson(max(3.0 - x * 1.25, 0)) + 1)
    )
    example_data["total_price"] = example_data["unit_price"] * example_data["quantity"]
    return example_data

f = lambda x: 'Apple' if x < 0.3 else 'Banana' if x < 0.7 else 'Orange'

d = {
    'date': [ pd.Timestamp('2018-01-01') + pd.Timedelta(days=i) for i in range(100)],
    'upper': [np.random.random() / 2 for i in range(100)],
    'lower': [-np.random.random() / 2 for i in range(100)],
    'quantity': [random.randrange(1, 20) for i in range(100)],
    'fruit': [f(np.random.random()) for i in range(100)],
    }
df = pd.DataFrame(data=d)

# df['upper'].iloc[25] = np.nan
# df['lower'].iloc[25] = np.nan

# df['upper'].iloc[75] = np.nan
# df['lower'].iloc[75] = np.nan

# df['upper'].iloc[90:] = np.nan
# df['lower'].iloc[90:] = np.nan

# print(df)

c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
c.set_title('Unstacked Area chart')
c.set_subtitle('Show overlapping values. Automatically adjusts opacity.')
c.set_source_label('Source: Example Data')
c.axes.set_xaxis_label('Unit price for a fruit batch')
c.axes.set_yaxis_label('Number of fruits')
c.style.set_color_palette('categorical', 'Dark2')

data = example_data()
data = data.groupby([data["date"] + pd.offsets.MonthBegin(-1), "country",],).sum().reset_index().sort_values("date")
data = data[data.country != 'GB']
data = data[data.country != 'BR']

# Delete at ends for US and CA
data['unit_price'].iloc[-1] = np.nan
data['total_price'].iloc[-1] = np.nan
data['unit_price'].iloc[-2] = np.nan
data['total_price'].iloc[-2] = np.nan
data['unit_price'].iloc[-4] = np.nan
data['total_price'].iloc[-4] = np.nan

# Delete 2 US in middle of area
data['unit_price'].iloc[-18] = np.nan
data['total_price'].iloc[-18] = np.nan
data['unit_price'].iloc[-19] = np.nan
data['total_price'].iloc[-19] = np.nan
print(data)
c.plot.area(
    data_frame=data,
    x_column='date',
    y_column='total_price',
    second_y_column='unit_price',
    color_column='country',
    stacked=False,
)
# data = example_data()
# data = data.groupby([data["date"] + pd.offsets.MonthBegin(-1), "fruit",],)["quantity"].sum().reset_index().sort_values("date")
# c.plot.area(
#     data_frame=data,
#     x_column='date',
#     y_column='quantity',
#     # second_y_column='unit_price',
#     color_column='fruit',
#     stacked=False,
# )
# c.plot.area(
#     data_frame=total_quantity_by_month_and_fruit,
#     x_column='month',
#     y_column='quantity',
#     color_column='fruit',
#     stacked=False,
# )
c.show()

