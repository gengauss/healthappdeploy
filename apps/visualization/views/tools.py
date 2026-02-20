import math

import numpy as np
from bokeh.embed import components
from bokeh.models import HoverTool, FactorRange, ColumnDataSource, LinearColorMapper, ColorBar, BasicTicker, \
    PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


def plot_bar_chart(cols, counts, title, fill_color):
    p = figure(plot_height=350, plot_width=550, title=title, toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9, line_color='white', fill_color=fill_color)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    script, div = components(p)
    return script, div


def plot_count(cols, counts, title, fill_color):
    p = figure(x_range=cols, plot_height=350, plot_width=550, title=title,
               toolbar_location=None, tools="")

    p.vbar(x=cols, top=counts, width=0.9, fill_color=fill_color)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    script, div = components(p)
    return script, div


def plot_hexbin(x, y, title):
    p = figure(title=title, match_aspect=True, plot_height=400, plot_width=550,
               tools="wheel_zoom,reset", background_fill_color='white')
    p.grid.visible = False

    r, bins = p.hexbin(x, y, size=0.5, hover_color="pink", hover_alpha=0.8)

    p.circle(x, y, color="red", size=5)

    p.add_tools(HoverTool(
        tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
        mode="mouse", point_policy="follow_mouse", renderers=[r]
    ))
    p.xaxis.axis_label = 'age'
    p.yaxis.axis_label = 'insu'
    script, div = components(p)
    return script, div


def plot_hist(df, bins, title, xlabel):
    p = df.plot_bokeh(
        kind="hist",
        bins=bins,
        vertical_xlabel=False,
        xlabel=xlabel,
        normed=1000,
        hovertool=False,
        title=title,
        show_figure=False)
    script, div = components(p)
    return script, div


def plot_stacked_bar(cols, classes, data, title):
    colors = ["maroon", "salmon"]

    p = figure(x_range=cols, plot_height=380, plot_width=550, title=title,
               toolbar_location=None, tools="")

    p.vbar_stack(classes, x='labels', width=0.9, color=colors, source=data,
                 legend_label=classes)

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"
    script, div = components(p)
    return script, div


def plot_line(x, y):
    p = figure(plot_width=600, plot_height=350)
    p.line(x, y, line_width=2, line_alpha=0.8)
    script, div = components(p)
    return script, div


def box_plot(yy, g):
    lists = ['Did not go to school', 'Primary school', 'Secondary school', 'Vocational training diloma']
    import pandas as pd
    df = pd.DataFrame(dict(score=yy, group=g))

    # find the quartiles and IQR for each category
    groups = df.groupby('group')
    q1 = groups.quantile(q=0.25)
    q2 = groups.quantile(q=0.5)
    q3 = groups.quantile(q=0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    lower = q1 - 1.5 * iqr

    # find the outliers for each category
    def outliers(group):
        cat = group.name
        return group[(group.score > upper.loc[cat]['score']) | (group.score < lower.loc[cat]['score'])]['score']

    out = groups.apply(outliers).dropna()

    # prepare outlier data for plotting, we need coordinates for every outlier.
    if not out.empty:
        outx = []
        outy = []
        for keys in out.index:
            outx.append(keys[0])
            outy.append(out.loc[keys[0]].loc[keys[1]])

    p = figure(tools="", background_fill_color="white", x_range=lists, toolbar_location=None,
               plot_height=540, plot_width=550)

    # if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
    qmin = groups.quantile(q=0.00)
    qmax = groups.quantile(q=1.00)
    upper.score = [min([x, y]) for (x, y) in zip(list(qmax.loc[:, 'score']), upper.score)]
    lower.score = [max([x, y]) for (x, y) in zip(list(qmin.loc[:, 'score']), lower.score)]

    # stems
    p.segment(lists, upper.score, lists, q3.score, line_color="black")
    p.segment(lists, lower.score, lists, q1.score, line_color="black")

    # boxes
    p.vbar(lists, 0.7, q2.score, q3.score, fill_color="#E08E79", line_color="black")
    p.vbar(lists, 0.7, q1.score, q2.score, fill_color="#3B8686", line_color="black")

    # whiskers (almost-0 height rects simpler than segments)
    p.rect(lists, lower.score, 0.2, 0.01, line_color="black")
    p.rect(lists, upper.score, 0.2, 0.01, line_color="black")

    # outliers
    # if not out.empty:
    #     p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6)

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.grid.grid_line_width = 2
    p.xaxis.major_label_text_font_size = "16px"
    p.xaxis.major_label_orientation = math.pi/2

    # or alternatively:
    p.xaxis.major_label_orientation = "vertical"
    script, div = components(p)
    return script, div


def plot_nested_bar(cols, classes, data, title):
    x = [(col, classs) for col in cols for classs in classes]
    counts = sum(zip(data['1'], data['2'], data['3'], data['4'], data['5'], data['6'], data['7']), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=400, plot_width=1100, title=title,
               toolbar_location=None, tools="")
    palette = ["#FFA69E", "#FAF3DD", "#B8F2E6", "#AED9E0", "#5E6472", "#BB7E8C"]
    p.vbar(x='x', top='counts', width=0.9, source=source, fill_color=factor_cmap('x', palette=palette, factors=classes,
                                                                                 start=1, end=2))

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    script, div = components(p)
    return script, div


def plot_nested_bar1(cols, classes, data, title):
    x = [(col, classs) for col in cols for classs in classes]
    counts = sum(zip(data['Not at all'], data['Heard of it'], data['Not so much'], data['Relatively know'], data['Very detailed']), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=400, plot_width=1100, title=title,
               toolbar_location=None, tools="")
    palette = ["#FFA69E", "#FAF3DD", "#B8F2E6", "#AED9E0"]
    p.vbar(x='x', top='counts', width=0.9, source=source, fill_color=factor_cmap('x', palette=palette, factors=classes,
                                                                                 start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    script, div = components(p)
    return script, div


def plot_nested_bar2(cols, classes, data, title):
    x = [(col, classs) for col in cols for classs in classes]
    counts = sum(zip(data['female'], data['male']), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=400, plot_width=550, title=title,
               toolbar_location=None, tools="")
    palette = ["#2ec4b6", "#f29e4c"]
    p.vbar(x='x', top='counts', width=0.9, source=source, fill_color=factor_cmap('x', palette=palette, factors=classes,
                                                                                 start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    script, div = components(p)
    return script, div


def plot_nested_bar3(cols, classes, data, title):
    x = [(col, classs) for col in cols for classs in classes]
    counts = sum(zip(data['female'], data['male']), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=400, plot_width=1100, title=title,
               toolbar_location=None, tools="")
    palette = ["#2ec4b6", "#f29e4c"]
    p.vbar(x='x', top='counts', width=0.9, source=source, fill_color=factor_cmap('x', palette=palette, factors=classes,
                                                                                 start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    script, div = components(p)
    return script, div


def plot_nested_bar4(cols, classes, data, title):
    x = [(col, classs) for col in cols for classs in classes]
    counts = sum(zip(data['Generation X'], data['Silent'], data['G.I. Generation'],
                     data['Boomers'], data['Millenials'], data['Generation Z']), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    p = figure(x_range=FactorRange(*x), plot_height=430, plot_width=550, title=title,
               toolbar_location=None, tools="")
    palette = ["#233d4d", "#fe7f2d", "#fcca46", "#a1c181", "#619b8a"]
    p.vbar(x='x', top='counts', width=0.9, source=source, fill_color=factor_cmap('x', palette=palette, factors=classes,
                                                                                 start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    script, div = components(p)
    return script, div


def plot_heatmap(data):
    index = list(data.index)
    columns = list(data.columns)

    import pandas as pd
    # reshape to 1D array or rates with a month and year for each row.
    df = pd.DataFrame(data.stack(), columns=['rate']).reset_index()

    # this is the colormap from the original NYTimes plot
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    mapper = LinearColorMapper(palette=colors, low=df.rate.min(), high=df.rate.max())

    TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

    p = figure(title="",
               x_range=list(reversed(columns)), y_range=index,
               x_axis_location="above", plot_width=550, plot_height=390,
               tools=TOOLS, toolbar_location='below',
               tooltips=[('date', '@columns @index'), ('rate', '@rate%')])

    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = math.pi / 3

    p.rect(x="columns", y="index", width=1, height=1,
           source=df,
           fill_color={'field': 'rate', 'transform': mapper},
           line_color=None)

    color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="7px",
                         ticker=BasicTicker(desired_num_ticks=len(colors)),
                         formatter=PrintfTickFormatter(format="%d%%"),
                         label_standoff=6, border_line_color=None, location=(0, 0))
    p.add_layout(color_bar, 'right')
    script, div = components(p)
    return script, div
