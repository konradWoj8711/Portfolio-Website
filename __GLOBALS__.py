import dash
import os
import datetime

THREADS = {}
PATH = os.path.dirname(__file__)
RETURN_DICT = {}

APP = dash.Dash(__name__)