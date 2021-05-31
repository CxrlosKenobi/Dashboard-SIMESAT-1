import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly
import dash

from server import app, server
from views import home, sidebar, debug
from db.api import get_current_time, get_bmp_pr_data, get_hdc_te_data, get_hdc_hu_data, get_mpu9250_gy_x_data, get_mpu9250_gy_y_data, get_mpu9250_gy_z_data
from server import app
import os

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}
GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)

layout = html.Div([
    #  Header
    html.Div([
        html.Div([
            html.H4(
                'SIMES-1 CANSAT',
                className='app__header__title'
            ),
            html.P(
                'Esta web-app grafica los datos obtenidos del nano satélite a partir de su base de datos SQL.',
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
                        'GY-91 Sensor status',
                        className='graph__title'
                    )
                ]),
                dcc.Graph(
                    id='GY91-live',
                    figure=dict(
                        layout=dict(
                            plot_bgcolor=app_color['graph_bg'],
                            paper_bgcolor=app_color['graph_bg'],
                        ),
                    ),
                ),
                dcc.Interval(
                    id='GY91-update',
                    interval=int(GRAPH_INTERVAL),
                    n_intervals=0
                ),
            ], className='two-thirds column wind__speed__container'),
        ])
    ]),
    html.Div([
        html.Div([
            html.Div([
                html.H6(
                    'BMP280 Live status',
                    className='graph__title'
                )]
            ),
            dcc.Graph(
                id='BMP280-live',
                figure=dict(
                    layout=dict(
                        plot_bgcolor=app_color['graph_bg'],
                        paper_bgcolor=app_color['graph_bg'],
                        height=250
                    )
                )
            ),
            dcc.Interval(
                id='BMP280-update',
                interval=int(GRAPH_INTERVAL),
                n_intervals=0
            )
        ], className='graph__container first'),
        html.Div([
            html.Div([
                html.H6(
                    'HDC-1080 Sensor status',
                    className='graph__title'
                )
            ]),
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
        ], className='graph__container second')
    ], className='one-third column histogram__direction')
], className='app__container')

@app.callback(
    Output('GY91-live', 'figure'), [Input('GY91-update', 'n_intervals')]
)
def update_bmp(n):
    total_time = get_current_time()
    df0 = get_mpu9250_gy_x_data(total_time - 200, total_time)
    df1 = get_mpu9250_gy_y_data(total_time - 200, total_time)
    df2 = get_mpu9250_gy_z_data(total_time - 200, total_time)

    trace0 = dict(
        name='X-Giroscopio',
        type="scatter",
        y=df0["mpu9250_gy_x"],
        line={"color": "#FF6600"},
        mode="lines",
    )
    trace1 = dict(
        name='Y-Giroscopio',
        type="scatter",
        y=df1["mpu9250_gy_y"],
        line={"color": "#4E00FF"},
        mode="lines",
    )
    trace2 = dict(
        name='Z-Giroscopio',
        type="scatter",
        y=df2["mpu9250_gy_z"],
        line={"color": "#42C4F7"},
        mode="lines",
    )
    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#FFF"},
        height=400,
        autosize=True,
        showlegend=False,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Tiempo transcurrido (seg)",
        },
        # percenMin = min(min(df0["mpu9250_gy_x"]), min(df1['mpu9250_gy_y']), min(df2['mpu9250_gy_z']))
        # percenMax = max(max(df0["mpu9250_gy_x"]), max(df1['mpu9250_gy_y']), max(df2['mpu9250_gy_z']))

        yaxis={
            "range": [
                min(min(df0["mpu9250_gy_x"]), min(df1['mpu9250_gy_y']), min(df2['mpu9250_gy_z'])),
                max(max(df0["mpu9250_gy_x"]), max(df1['mpu9250_gy_y']), max(df2['mpu9250_gy_z'])),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [trace0, trace1, trace2], 'layout': layout}

@app.callback(
    Output('BMP280-live', 'figure'), [Input('BMP280-update', 'n_intervals')]
)
def update_bmp(n):
    total_time = get_current_time()
    df0 = get_hdc_te_data(total_time - 200, total_time)
    df1 = get_bmp_pr_data(total_time - 200, total_time)

    trace0 = dict(
        name='Temperatura (C°)',
        type="scatter",
        y=df0["hdc1080_te"],
        line={"color": "#00BB2D"},
        mode="lines",
    )
    trace1 = dict(
        name='Presión B. (Pa)',
        type="scatter",
        y=df1["bmp280_pr"],
        line={"color": "#FFF"},
        mode="lines",
    )

    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=250,
        autosize=True,
        showlegend=False,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Tiempo transcurrido (seg)",
        },
        yaxis={
            "range": [
                min(min(df0["hdc1080_te"]), min(df1['bmp280_pr'])),
                max(max(df0["hdc1080_te"]), max(df1['bmp280_pr'])),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [trace0, trace1], 'layout': layout}

@app.callback(
    Output('HDC-live', 'figure'), [Input('HDC-update', 'n_intervals')]
)
def update_hdc(n):
    total_time = get_current_time()
    df0 = get_hdc_te_data(total_time - 200, total_time)
    df1 = get_hdc_hu_data(total_time - 200, total_time)

    trace0 = dict(
        name='Temperatura (C°)',
        type="scatter",
        y=df0["hdc1080_te"],
        line={"color": "#00BB2D"},
        mode="lines",
    )
    trace1 = dict(
        name='Humedad (%)',
        type="scatter",
        y=df1["hdc1080_hu"],
        line={"color": "#42C4F7"},
        mode="lines",
    )

    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=250,
        autosize=True,
        showlegend=False,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Tiempo transcurrido (seg)",
        },
        yaxis={
            "range": [
                min(min(df0["hdc1080_te"]), min(df1['hdc1080_hu'])),
                max(max(df0["hdc1080_te"]), max(df1['hdc1080_hu'])),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [trace0, trace1], 'layout': layout}
