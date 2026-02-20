import pandas as pd
from django.db import connection
from django.shortcuts import render

from .suicide_rate import plot_suicide_gender, plot_suicide_age
from .survey import plot_country, plot_age, plot_occupation, plot_gender, plot_water, plot_diet, plot_meals, \
    plot_first_meal, plot_last_meal, plot_same_meal, plot_stress, plot_mental_diseases
from .tools import plot_bar_chart, plot_count, plot_hexbin, plot_hist, plot_stacked_bar, plot_line, box_plot, \
    plot_nested_bar, plot_nested_bar1, plot_heatmap, plot_nested_bar2, plot_nested_bar3, plot_nested_bar4
from ..models import Survey, Diabetes, Depression, SuicideRate
import numpy as np
import pandas_bokeh


def index(request):
    return render(request, '../templates/visualization/index.html', {})


def survey_result(request):
    query = str(Survey.objects.all().query)
    survey = pd.read_sql_query(query, connection)
    script_country, div_country = plot_country()
    script_age, div_age = plot_age()
    script_job, div_job = plot_occupation()
    script_gender, div_gender = plot_gender()
    script_water, div_water = plot_water()
    script_diet, div_diet = plot_diet()
    script_meals, div_meals = plot_meals()
    script_first_meal, div_first_meal = plot_first_meal()
    script_last_meal, div_last_meal = plot_last_meal()
    script_same_meal, div_same_meal = plot_same_meal()

    important_cols = survey['mental_important'].value_counts().keys().tolist()
    important_counts = survey['mental_important'].value_counts().tolist()
    mental_important = {'important': important_cols, 'counts': important_counts}
    mental_important_df = pd.DataFrame(mental_important)
    fill_color = ["#F06543", "#EBD2B4", "#F5EE9E", "#4CB944", "#246EB9"]
    script_mental_important, div_mental_important = plot_bar_chart(mental_important_df['important'],
                                                                   mental_important_df['counts'],
                                                                   title="Mental Health Importance",
                                                                   fill_color=fill_color)

    effect_cols = survey['mental_effect'].value_counts().keys().tolist()
    effect_counts = survey['mental_effect'].value_counts().tolist()
    mental_effect = {'effect': effect_cols, 'counts': effect_counts}
    mental_effect_df = pd.DataFrame(mental_effect)
    script_mental_effect, div_mental_effect = plot_bar_chart(mental_effect_df['effect'],
                                                             mental_effect_df['counts'],
                                                             title="Mental Health Effect",
                                                             fill_color=fill_color)

    script_stress, div_stress = plot_stress()
    script_md, div_md = plot_mental_diseases()

    i = ['Jobs/School', 'Family', 'Friends', 'Relationship with partner', 'Social Media', 'Money']
    level = ['1', '2', '3', '4', '5', '6', '7']

    data = {'i': i,
            '1': [80, 56, 56, 74, 72, 63],
            '2': [38, 42, 52, 43, 60, 50],
            '3': [42, 63, 65, 43, 48, 48],
            '4': [33, 31, 39, 34, 30, 45],
            '5': [31, 34, 36, 24, 21, 24],
            '6': [27, 28, 12, 43, 32, 25],
            '7': [13, 10, 4, 3, 1, 9]}

    script_nest, div_nest = plot_nested_bar(i, level, data, "Which of the following makes you feel anxious?")

    i1 = ['Depression', 'Anxiety Disorder', 'Bipolar Disorder']
    level1 = ['Not at all', 'Heard of it', 'Not so much', 'Relatively know', 'Very detailed']

    data1 = {'i1': i,
             "Not at all": [13, 18, 75],
             "Heard of it": [34, 47, 53],
             "Not so much": [30, 58, 52],
             "Relatively know": [127, 99, 62],
             "Very detailed": [60, 42, 23]
             }

    script_nest1, div_nest1 = plot_nested_bar1(i1, level1, data1, "Do you know about these diseases?")

    data_dict = {'survey': survey, 'script_country': script_country, 'div_country': div_country,
                 'script_age': script_age, 'div_age': div_age,
                 'script_job': script_job, 'div_job': div_job,
                 'script_gender': script_gender, 'div_gender': div_gender,
                 'script_water': script_water, 'div_water': div_water,
                 'script_diet': script_diet, 'div_diet': div_diet,
                 'script_meals': script_meals, 'div_meals': div_meals,
                 'script_first_meal': script_first_meal, 'div_first_meal': div_first_meal,
                 'script_last_meal': script_last_meal, 'div_last_meal': div_last_meal,
                 'script_same_meal': script_same_meal, 'div_same_meal': div_same_meal,
                 'script_mental_important': script_mental_important, 'div_mental_important': div_mental_important,
                 'script_mental_effect': script_mental_effect, 'div_mental_effect': div_mental_effect,
                 'script_stress': script_stress, 'div_stress': div_stress,
                 'script_md': script_md, 'div_md': div_md,
                 'script_nest': script_nest, 'div_nest': div_nest,
                 'script_nest1': script_nest1, 'div_nest1': div_nest1}
    return render(request, '../templates/visualization/survey.html', data_dict)


def diabetes_result(request):
    query = str(Diabetes.objects.all().query)
    diabetes = pd.read_sql_query(query, connection)

    # tested
    tested_cols = diabetes['tested'].value_counts().keys().tolist()
    tested_counts = diabetes['tested'].value_counts().tolist()
    tested = {'tested': tested_cols, 'counts': tested_counts}
    tested_df = pd.DataFrame(tested)
    fill_color = ["#097E8F", "#ECC14D"]
    script_tested, div_tested = plot_count(tested_df['tested'], tested_df['counts'], "Tested Counts", fill_color)

    # age
    age = diabetes['age'].value_counts().tolist()
    script_age, div_age = plot_count(tested_cols, age, "age", fill_color)

    # insu
    x = np.array(diabetes['insu'])
    y = np.array(diabetes['age'])
    title = "Hexbin for insulin and age"
    script_insu, div_insu = plot_hexbin(x, y, title)

    # age distribution
    df_dist = pd.DataFrame({
        'tested_positive': diabetes["age"][diabetes['tested'] == 'tested_positive'],
        'tested_negative': diabetes["age"][diabetes['tested'] == 'tested_negative']
    }, columns=['tested_positive', 'tested_negative'])

    script_dist, div_dist = plot_hist(df_dist, np.arange(0, 100, 10), "Age distribution", "Age")

    labels = ['Unhealthy', 'Healthy', 'Overweight', 'Obese']
    tested = ['tested_positive', 'tested_negative']
    data = {'labels': labels,
            'tested_positive': [2, 7, 44, 215],
            'tested_negative': [9, 105, 136, 250]}
    script_stacked, div_stacked = plot_stacked_bar(labels, tested, data, "")

    script_line, div_line = plot_line(diabetes[diabetes['tested'] == 'tested_positive']['age'],
                                      diabetes[diabetes['tested'] == 'tested_positive']['insu'])

    data_dict = {'script_tested': script_tested, 'div_tested': div_tested,
                 'script_age': script_age, 'div_age': div_age,
                 'script_insu': script_insu, 'div_insu': div_insu,
                 'script_dist': script_dist, 'div_dist': div_dist,
                 'script_stacked': script_stacked, 'div_stacked': div_stacked,
                 'script_line': script_line, 'div_line': div_line}
    return render(request, '../templates/visualization/diabetes.html', data_dict)


def depression_result(request):
    query = str(Depression.objects.all().query)
    depression = pd.read_sql_query(query, connection)
    yy = depression['total_ds']
    g = depression['education']
    script_box, div_box = box_plot(yy, g)

    labels = ['Unemployed', 'Agriculturist', 'Employee', 'Vendor']
    counts = [10, 9, 8.4, 10.4]
    df = {'labels': labels, 'counts': counts}
    df = pd.DataFrame(df)
    fill_color = ["#313557", "#2B73AC", "#379386", "#50C7B6"]
    script_bar, div_bar = plot_count(df['labels'], df['counts'], "", fill_color)

    df_dist = pd.DataFrame({
        'Good relationship': depression["total_ds"][depression['relationship_with_family'] == 2],
        'Bad relationship': depression["total_ds"][depression['relationship_with_family'] == 1]
    }, columns=['Good relationship', 'Bad relationship'])

    script_dist, div_dist = plot_hist(df_dist, np.arange(0, 30, 1), "Bad relationships cause higher depression rate",
                                      "Bad relationships cause higher depression rate")

    dep_symptoms = depression.loc[:, 'ds1':'ds10']
    dep_symptoms = dep_symptoms.replace([0, 1, 2, 3], ['Most of the time', 'Sometimes', 'Not very often', 'Not at all'])
    df1 = dep_symptoms.melt(var_name='columns', value_name='index')
    result = pd.crosstab(index=df1['index'], columns=df1['columns'])

    script_hm, div_hm = plot_heatmap(result)

    data_dict = {'script_box': script_box, 'div_box': div_box,
                 'script_bar': script_bar, 'div_bar': div_bar,
                 'script_dist': script_dist, 'div_dist': div_dist,
                 'script_hm': script_hm, 'div_hm': div_hm
                 }
    return render(request, '../templates/visualization/depression.html', data_dict)


def suicide_result(request):
    query = str(SuicideRate.objects.all().query)
    suicide = pd.read_sql_query(query, connection)
    script_gender, div_gender = plot_suicide_gender()
    i = ['15-24', '25-34', '35-54', '5-14', '55-74', '75+']
    level = ['female', 'male']

    data = {'i': i,
            'female': [0.1875, 0.2083, 0.50, 0.01, 0.45, 0.22],
            'male': [0.625, 0.9375, 1.8, 0.03, 1.23, 0.45]}

    script_age, div_age = plot_nested_bar2(i, level, data, "Worldwide Suicide on total suicide by Age (1985-2015)")

    i1 = ['Russian Federation', 'United States', 'Japan', 'France', 'Ukraine', 'Germany', 'Republic of Korea', 'Brazil',
          'Poland', 'United Kingdom']

    data1 = {'i': i1,
             'female': [0.21, 0.21, 0.25, 0.09, 0.05, 0.08, 0.08, 0.03, 0.01, 0.02],
             'male': [1.0, 0.82, 0.58, 0.22, 0.23, 0.21, 0.18, 0.18, 0.1, 0.09]}

    script_country, div_country = plot_nested_bar3(i1, level, data1,
                                                   "Top 10 countries total suicide Hue Sex (1985-2015)")

    script_age_range, div_age_range = plot_suicide_age()

    i2 = ['15-24', '25-34', '35-54', '5-14', '55-74', '75+']

    data2 = {'i': i2,
             'female': [4, 5, 7, 0.5, 9.5, 13],
             'male': [15, 21, 28, 0.7, 30.5, 46]}

    script_100k, div_100k = plot_nested_bar2(i2, level, data2, "Suicide rate 100k Population by age range (1985-2015)")

    i3 = ['male', 'female']
    level2 = ['Generation X', 'Silent', 'G.I. Generation', 'Boomers', 'Millenials', 'Generation Z']

    data3 = {'i': i3,
             'Generation X': [380, 90],
             'Silent': [400, 150],
             'G.I. Generation': [250, 120],
             'Boomers': [730, 190],
             'Millenials': [180, 40],
             'Generation Z': [10, 8]}

    script_g, div_g = plot_nested_bar4(i3, level2, data3, "Number of suicides by generations (1985-2015)")

    cols = suicide['generation'].value_counts().keys().tolist()
    counts = suicide['generation'].value_counts().tolist()
    generation = {'cols': cols,
                  'counts': counts}
    generation_df = pd.DataFrame(generation)
    fill_color = ["#16697a", "#489fb5", "#82c0cc", "#ede7e3", "#ffa62b", "#f1dca7"]
    script_generation, div_generation = plot_count(generation_df['cols'],
                                                   generation_df['counts'],
                                                   title="Worldwide Suicide on total suicide by generation (1985-2015)",
                                                   fill_color=fill_color)

    data_dict = {'script_gender': script_gender, 'div_gender': div_gender,
                 'script_age': script_age, 'div_age': div_age,
                 'script_country': script_country, 'div_country': div_country,
                 'script_age_range': script_age_range, 'div_age_range': div_age_range,
                 'script_100k': script_100k, 'div_100k': div_100k,
                 'script_generation': script_generation, 'div_generation': div_generation,
                 'script_g': script_g, 'div_g': div_g}
    return render(request, '../templates/visualization/suicide_rate.html', data_dict)
