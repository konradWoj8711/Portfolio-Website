from __GLOBALS__ import RETURN_DICT as RETURN_DICT
from __GLOBALS__ import PATH as PATH
from __GLOBALS__ import APP as app

import importlib.util
import os

from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import sys
sys.path.append(PATH + "//components")

import navbar

def load_dash_pages():
    page_sub_directories = os.listdir(PATH + "//subpages")

    for sub_folder in page_sub_directories:
        files = [file for file in os.listdir(PATH + "//subpages/" + sub_folder) if any(phrase in file for phrase in ["callbacks", "layouts"])]
        for py_file in files:
            library_name = py_file[:py_file.find('.')]
            alter_name = sub_folder + '_' + library_name
            spec = importlib.util.spec_from_file_location(library_name, PATH + "//subpages/" + sub_folder + '/' + py_file)

            globals()[alter_name] = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(globals()[alter_name])

            print("Imported -", alter_name)
    
#Load all sub-pages
load_dash_pages()

app.layout = html.Div(
    children = [
        navbar.layout,
        html.Div(
            id = "page-content",
            className= "row page-content",
        ),

        dcc.Location(id = "url", refresh = False)
    ]
)

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/contact":
        return contact_layouts.layout
    else:
        return home_layouts.layout