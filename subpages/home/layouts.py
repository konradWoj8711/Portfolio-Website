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

                html.Div(
                    className= 'row',
                    style = {'padding-top':'3%'},
                    children = [
                        html.A(                    
                            html.Img(
                                src = app.get_asset_url("github.png"),
                                style = {'width':'50px','margin-right':'1%'},
                            ),
                            href = 'https://github.com/konradWoj8711',
                            className= "text-percent"
                        ),

                        html.A(                    
                            html.Img(
                                src = app.get_asset_url("LI-In-Bug.png"),
                                style = {'width':'50px'},

                            ),
                            href = 'https://www.linkedin.com/in/konrad-wojcik-3a2520205/',
                            className= "text-percent"
                        ),
                    ]
                )   
            ]
        ),

        html.Div(
            className = 'row title-block',
            style = {'margin-top':'40vh'},
            children = [
                 html.H1("Personal Highlights"),
                 html.P("These are some of the more interesting things I've made which I wanted to share. Bare in mind while I am self taught I have been developing things commercially for over two years, this is just a tiny scope!"),


                html.Div(
                    className = 'row',
                    children = [
                        html.H2("Path Finding Snake"),
                        html.A(
                            html.Img(
                                src = app.get_asset_url("snake.gif"),
                                className = 'full-percent column',
                                style = {'margin-bottom':'1%'},

                            ),
                            href = 'https://github.com/konradWoj8711/Snake-Project',
                            className= "full-percent column"
                        ),

                        html.P("This project was based around creating a 'Snake' game with player vs AI. Only Python and PyGame were used to make this for the added challenge. The video showcases the path finding algorithm playing on its own. The snake is able to successfully locate the food and reach it while avoiding itself, other players and boundaries. Click on the video to go the repository for this project."),

                        html.H2("Purchase Order Booking"),
                        html.Video(
                            src = app.get_asset_url("po_program.mp4"),
                            className = 'full-percent column',
                            autoPlay='autoPlay',
                            controls ='controls',
                            style = {'margin-bottom':'1%'}
                        ),

                        html.P("I've developed this project as a means to extend the capabilities of our database systems at Gadget Express. This software communicates live through APIs to speed up the booking in process. Users can have this software installed on multiple computers and book in at the same time. The program will internally track each user's progress and allow them to switch between different suppliers/purchase orders. As this is a commercial solution the code is not available to be viewed."),
                        html.P("The success of this program amounted to saving around 7 hours daily of employee time and shipping out orders dramatically sooner. The project was done in Python in combination with QT for the interfacing.")

                    ]
                )
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