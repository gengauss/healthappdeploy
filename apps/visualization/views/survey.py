from math import pi

import pandas as pd
from bokeh.embed import components
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum


def data_info(df):
    # Data Info
    data_size = df.shape
    return data_size


def plot_country():
    x = {
        'Japan': 171,
        'Vietnam': 56,
        'Uzbekistan': 33,
        'Australia': 2,
        'Canada': 1,
        'Germany': 1,
        'China': 1,
        'Thailand': 1,
        'Malaysia': 1,
    }

    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Country", toolbar_location=None,
               tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_age():
    x = {
        '20代 20s': 142,
        '20歳未満 Under 20': 62,
        '50代 50s': 36,
        '40代 40s': 21,
        '30代 30s': 19,
        '60代 60s': 4,
        '60歳以上 Above 60': 2
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'age'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Age", toolbar_location=None,
               tools="hover", tooltips="@age: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='age', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_occupation():
    x = {
        '大学生 University Student': 148,
        '正社員・常勤職 I have a permanent job': 82,
        '高校生 High School Student': 47,
        '無職 I do not work': 5,
        'フリーランス Freelancer': 2,
        '大学院生 Doctoral student': 1,
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'occupation'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Occupation", toolbar_location=None,
               tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='occupation', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_gender():
    x = {
        '男性 Male': 150,
        '女性 Female': 129,
        '答えたくない Prefer not to say': 7
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'gender'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Gender", toolbar_location=None,
               tools="hover", tooltips="@gender: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='gender', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_water():
    x = {
        '2L未満 Less than 2 liter': 146,
        '2L 2 liter': 87,
        '2L以上 More than 2 liter': 53
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'water'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Water per day", toolbar_location=None,
               tools="hover", tooltips="@water: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='water', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_diet():
    x = {
        '同じくらい Balanced': 155,
        '肉中心 Meat focused': 98,
        '野菜中心 Vegetable focused': 33
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'diet'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Diet", toolbar_location=None,
               tools="hover", tooltips="@diet: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='diet', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_meals():
    x = {
        '3食 3 meals': 175,
        '3食未満 Less than 3 meals': 88,
        '3食以上 More than 3 meals': 23
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'meals'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Number of meals", toolbar_location=None,
               tools="hover", tooltips="@diet: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='meals', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_first_meal():
    x = {
        '9時以降 After 9:00': 110,
        '7:00 - 8:00': 79,
        '8:00 - 9:00': 47,
        '6:00 - 7:00': 43,
        '6時前 Before 6:00': 7
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'first_meal'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="First meal time", toolbar_location=None,
               tools="hover", tooltips="@first_meal: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='first_meal', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_last_meal():
    x = {
        '19:00 - 20:00': 101,
        '20:00 - 21:00': 81,
        '21時以降 After 21:00': 50,
        '18:00 - 19:00': 44,
        '18時前 Before 18:00': 10
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'last_meal'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Last meal time", toolbar_location=None,
               tools="hover", tooltips="@last_meal: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='last_meal', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_same_meal():
    x = {
        'あまりそうしていない Not really': 118,
        'そうしている Yes': 90,
        '全くそうしていない Not at all': 38,
        'どちらとも言えない  I don’t know': 32,
        '必ずそうしている Definitely': 8
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'same_meal'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Having meals at the same time every day", toolbar_location=None,
               tools="hover", tooltips="@same_meal: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='same_meal', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_stress():
    x = {
        '時々 Sometimes': 133,
        'あんまり Not really': 50,
        'どちらとも言えない  I don’t know': 32,
        'ほとんどの時間 Most of the time': 31,
        'どういたしまして Not at all': 18
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'stress'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Do you feel stressed every day?", toolbar_location=None,
               tools="hover", tooltips="@stress: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='stress', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div


def plot_mental_diseases():
    x = {
        'いいえ No': 182,
        '多分 Maybe': 43,
        'はい Yes': 39
    }
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'mental_diseases'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, plot_width=550, title="Have you experienced any disorder?", toolbar_location=None,
               tools="hover", tooltips="@mental_diseases: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='mental_diseases', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    script, div = components(p)
    return script, div
