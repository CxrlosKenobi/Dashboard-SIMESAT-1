import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

from db.api import get_bmp_data, get_current_time, get_hdc_data
from server import app
import os

GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)
app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

#  Home / Stats menu
layout = html.Div([
    #  Header
    html.Div([
        html.Div([
            html.H4(
                'SIMES-1 CANSAT',
                className='app__header__title'
            ),
            html.P(
                'This app continually queries a SQL database and displays the live data from the nano satellite.',
                className='app__header__title--grey',
            ),
        ], className='app__header__desc'),
        html.Div([
            html.A(href='https://aeroespacial.centrosimes.com/'),
            html.Img(
                src=app.get_asset_url('SIMES_white.png'),
                className='app__menu__img',
            )
        ], className='app__header__logo'),
    ], className='app__header'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H6(
                        'Live Conditions Plot',
                        className='graph__title'
                    )
                ]),
                dcc.Graph(
                    id='BMP-live',
                    figure=dict(
                        layout=dict(
                            plot_bgcolor=app_color['graph_bg'],
                            paper_bgcolor=app_color['graph_bg'],
                        ),
                    ),
                ),
                dcc.Interval(
                    id='BMP-update',
                    interval=int(GRAPH_INTERVAL),
                    n_intervals=0
                ),
            ], className='two-thirds column wind__speed__container')
        ])
    ]),
    html.Div([
        html.Div([
            html.Div([
                html.H6(
                    'HDC1080 Feed',
                    className='graph__title'
                )]
            ),
            dcc.Graph(
                id='HDC-live',
                figure=dict(
                    layout=dict(
                        plot_bgcolor=app_color['graph_bg'],
                        paper_bgcolor=app_color['graph_bg'],
                    )
                )
            ),
            dcc.Interval(
                id='HDC-update',
                interval=int(GRAPH_INTERVAL),
                n_intervals=0
            ),
        ], className='graph__container first'),
        html.Div([
            html.Div([
                html.H6(
                    'Live GPS Feed',
                    className='graph__title'
                )
            ]),
            dcc.Graph(
                figure=dict(
                    layout=dict(
                        plot_bgcolor=app_color['graph_bg'],
                        paper_bgcolor=app_color['graph_bg'],
                    )
                )
            ),
            dcc.Interval(
                interval=int(GRAPH_INTERVAL),
                n_intervals=0
            ),
        ], className='graph__container second')
    ], className='one-third column histogram__direction')
], className='app__container')

@app.callback(
    Output('BMP-live', 'figure'), [Input('BMP-update', 'n_intervals')]
)
def update_bmp(n):
    total_time = get_current_time()
    df = get_bmp_data(total_time - 200, total_time)

    trace = dict(
        type="scatter",
        y=df["bmp280_te"],
        line={"color": "#42C4F7"},
        mode="lines",
    )
    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=570,
        autosize=True,
        showlegend=False,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Time Elapsed (sec)",
        },
        yaxis={
            "range": [
                min(df["bmp280_te"]),
                max(df["bmp280_te"]),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [trace], 'layout': layout}

@app.callback(
    Output('HDC-live', 'figure'), [Input('HDC-update', 'n_intervals')]
)
def update_hdc(n):
    total_time = get_current_time()
    df = get_hdc_data(total_time - 200, total_time)

    trace = dict(
        type="scatter",
        y=df["hdc1080_te"],
        line={"color": "#42C4F7"},
        mode="lines",
    )
    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=570,
        autosize=True,
        showlegend=False,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Time Elapsed (sec)",
        },
        yaxis={
            "range": [
                min(df["hdc1080_te"]),
                max(df["hdc1080_te"]),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [trace], 'layout': layout}

