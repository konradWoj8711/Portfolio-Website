from __GLOBALS__ import APP as app

from dash import dcc
from dash import html
from dash.dependencies import Input, Output

layout = html.Div(
    children = [
        html.Div(
            style = {'z-index':'-1'},
            className = "hero banner-background",
            children = [
                html.Img(
                    src = app.get_asset_url("hero.svg"),
                    className= "banner-bg"
                ),
            ]
        ),

        html.Div(
            id = 'particles-js',
            className= "particles-js banner-bg"
        ),
        
        html.Div(
            className = 'row title-block',
            style = {'padding-top':'1%'},
            children = [
                 html.H1("At a glance...", className = 'text-white'),
                 html.P("Currently I am working as a Supplier Insight Analyst for TDX Group. During my work I make use of my self taught Python abilities, SQL and sometimes (really rarely) my creative education. My strongest card is definitely Python, as such I choose to develop this website on my own using Dash and Plotly. Explore around! Hope you enjoy.", className = 'text-white'),
            ]
        ),

        dcc.Interval(id = 'page-load', n_intervals=0, max_intervals=0)
    ]
)

app.clientside_callback(
    """
    function(trigger) {
        particlesJS.load('particles-js','assets/particlesjs-config.json');
    }

    """,
    Output('particles-js', 'children'),
    Input('page-load', 'n_intervals')
)