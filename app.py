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
init(autoreset=True)

print(Style.RESET_ALL + Fore.GREEN + '[ ok ] ' + Style.RESET_ALL +
    'Initializing script ...')

colors = {'background': '#111111', 'text': '#7FDBFF'}
colors['text']

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
LOGO = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/81/satellite_1f6f0.png"

app = dash.Dash(
	__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
app.title = "📡 SIMES-1"

"""
app.layout = html.Div([
    html.H2('Hello world!'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])
@app.callback(dash.dependencies.Output('display-value', 'children'),
[dash.dependencies.Input('dropdown', 'value')])

def display_value(value):
    return f'You have selected {value}'
"""
if __name__ == '__main__':
    app.run_server(debug=True)
