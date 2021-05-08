from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.io as pio
import plotly
import dash

from colorama import init, Fore, Back, Style

import os
import csv
init(autoreset=True)

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
LOGO = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/81/satellite_1f6f0.png"

app = dash.Dash(
	__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, LOGO],
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)
server = app.server
app.title = "SIMES-1"

## Graph setup
app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}
X = deque(maxlen=40)
X.append(0)

Y = deque(maxlen=40)
Y.append(0)

GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)


app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='HDC-live',
            figure=dict(
                layout=dict(
                    plot_bgcolor=app_color['graph_bg'],
                    paper_bgcolor=app_color['graph_bg'],
                ),
            ),
        ),
        dcc.Interval(
            id='HDC-update',
            interval=int(GRAPH_INTERVAL),
            n_intervals=0
        ),
    ], className='main'),
    html.Div([
        html.Img(src=app.get_asset_url('SIMES_white.png'), className='logo')
    ])
])
@app.callback(
    Output('HDC-live', 'figure'), [Input('HDC-update', 'n_interrvalas')]
)
def update(n):
    X.append(X[-1] + 1)
    Y.append( GET_DATA )

    minV = [min(Y)]
    maxV = [max(Y)]

    trace = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Name',
        mode='lines',
        line={'color':'#FF8300', 'width': 2.5}
    )

    layout = go.Layout(
        plot_bgcolor=app_color['graph_bg'],
        paper_bgcolor=app_color['graph_bg'],
        font={'color': '#FFF'},
        height=570,
        autosize=True,
        showlegend=False,
        xaxis=dict(
            range=[min(X) - 1.5, max(X) + 1.5],
            showline=True,
            zeroline=False,
            fixedrange=True,
            title='Title of X axis'
        ),
        yaxis=dict(
            range=[min(Y) - 1.5, max(Y) + 1.5],
            showgrid=True,
            showline=True,
            fixedrange=True,
            zeroline=False,
            gridcolor=app_color['graph_line']
        ),
    )

    return {'data': [trace], 'layout': layout}


if __name__ == '__main__':
    app.run_server(debug=True)
