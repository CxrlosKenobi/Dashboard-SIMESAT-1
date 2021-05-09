import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly
import dash

from server import app, server
from views import home, sidebar, debug


content = html.Div(id="page-content", className="content")

app.layout = html.Div(
    [dcc.Location(id="url"), sidebar.layout, content]
)

@app.callback(
    Output("page-content", "children"), Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/demo":
        return debug.layout
    elif pathname == "/github":
        return html.P("Redirecting to GitHub repository...")

    #  If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron([
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
    ])

if __name__ == '__main__':
    app.run_server(host='127.0.0.2', debug=True)
