from __GLOBALS__ import RETURN_DICT as RETURN_DICT
from __GLOBALS__ import PATH as PATH
from __GLOBALS__ import APP as app

from dash import dcc
from dash import html

layout = html.Div(
    className = "row navbar",
    children = [

        html.Div(
            className = 'row navbar-content',
            style = {'max-width':'800px'},
            children = [
                html.A(                    
                    html.Img(
                        src = app.get_asset_url("logo.svg")
                    ),
                    href = '/',
                    className= "ten-percent column"
                ),
                html.P("Work", className='text-percent column'),
                html.P("About", className='text-percent column'),
                html.P("Contact", className='text-percent column'),

            ]
        )
    ]
)