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

#colors = {'background': '#111111', 'text': '#7FDBFF'}
#colors['text']

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
SAT-LOGO = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/81/satellite_1f6f0.png"

app = dash.Dash(
	__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
app.title = "📡 SIMES-1"

app.layout = html.Div([
    html.Div([
        html.Div([
            html.P('Container title')
        ], className='sign'),
        html.Div([
            html.H1('Text')
        ], className='un'),
    ], className='main'),
    html.Div([
        html.Img(src=app.get_asset_url('SIMES_white.png'), className='logo')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
