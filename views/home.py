import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


from db.api import get_current_time, get_bmp_pr_data, get_hdc_te_data, get_hdc_hu_data, get_mpu9250_ac_data, get_mpu9250_gy_data, get_mpu9250_ma_data
from server import app
import os

MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiY3hybG9za2Vub2JpIiwiYSI6ImNrangwOG1mMjJ5ejcyeXFseWM1NHF1MDAifQ.Icq82Gz4RRFvfScW3ltvMA'
MAPBOX_STYLE = 'mapbox://styles/plotlymapbox/cjyivwt3i014a1dpejm5r7dwr'
GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)
app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

#  Home / Stats menu
layout = html.Div(
    [
        # Header
        html.Div(
            [
                html.Div(
                    [html.H4(
                        'SIMES-1 CANSAT',
                        className='app__header__title'
                    ),
                    html.P(
                    '''Charts display with random data for debug
                    and set demo phase at each graph while the final
                    code release is not concluded.''',
                    className='app__header__title--grey',
                    ),
                    ],
                    className='app__header__desc'
                ),
                html.Div(
                    [html.Img(
                        src=app.get_asset_url('SIMES_white.png'),
                        className='app__menu__img',
                    ),
                    ],
                    className='app__header__logo',
                ),
            ],
            className='app__header',
        ),
    ],
    className='app__container'
)
