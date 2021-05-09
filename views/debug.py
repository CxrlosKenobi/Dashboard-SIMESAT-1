import dash_bootstrap_components as dbc
import dash_html_components as html
from server import app

layout = html.Div(
    [
        # Header
        html.Div(
            [
                html.Div(
                    [html.H4(
                        'Demostration / Debug menu',
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
