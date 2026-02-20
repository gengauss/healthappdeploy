from math import pi

import pandas as pd
from bokeh.embed import components
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum


def plot_suicide_gender():
    x = {
        'Male': 76.9,
        'Female': 23.1,
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'gender'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = ["#ff6b6b", "#73bfdc"]

    p = figure(plot_height=350, plot_width=550, title="Worldwide Suicide by Gender (1958 - 2015)", toolbar_location=None,
               tools="hover", tooltips="@gender: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='gender', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_suicide_age():
    x = {
        '35-54': 33.7,
        '55-74': 20.6,
        '15-24': 1,
        '25-34': 19.8,
        '5-14': 19.7,
        '75+': 6.23
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'gender'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = ["#9b5de5", "#f15bb5", "#fee440", "#00bbf9", "#00f5d4", "#f19c79"]

    p = figure(plot_height=350, plot_width=550, title="Popular by age range (1958 - 2015)", toolbar_location=None,
               tools="hover", tooltips="@gender: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='gender', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div
