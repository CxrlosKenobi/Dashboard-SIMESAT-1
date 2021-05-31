import dash
import dash_html_components
import dash_bootstrap_components as dbc
 from config import config
import os

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
LOGO = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/81/satellite_1f6f0.png"

app = dash.Dash(
	__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "📡 SIMES-1"

server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
