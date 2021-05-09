from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.io as pio
import plotly
import dash

from server import app, server
from db.api import get_bmp_data, get_current_time
from views import sidebar

import os
import csv
import sqlite3
import datetime as dt
import pandas as pd

## Graph setup
app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)

app.layout = html.Div([
    html.Div([
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
    ], className='main'),
    ])


@app.callback(
    Output('BMP-live', 'figure'), [Input('BMP-update', 'n_intervals')]
)
def update(n):
    total_time = get_current_time()
    df = get_bmp_data(total_time - 200, total_time)

    trace = dict(
        type="scatter",
        y=df["bmp280"],
        line={"color": "#42C4F7"},
        hoverinfo="skip",
        mode="lines",
    )
    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=700,
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
                min(df["bmp280"]),
                max(df["bmp280"]),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [trace], 'layout': layout}


if __name__ == '__main__':
    app.run_server(host='127.0.0.2', debug=True)
