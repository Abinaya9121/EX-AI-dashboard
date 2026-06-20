# import dash
# from dash import dcc, html, Input, Output, State
# import dash_bootstrap_components as dbc

# # Initialize the app
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.title = "EXAI Dashboard"
# server = app.server


# # Layout for the front page
# front_page_layout = dbc.Container([
#     html.H1(" "),
#     html.H2(
#         "Explainable AI Dashboard",
#         className="text-center mb-3",
#         style={
#             "backgroundColor": "white",       # white background
#             "border": "1px solid #C9C7C7",    # light black border
#             "padding": "15px",                # spacing inside
#             "borderRadius": "5px",             # rounded corners
#             "boxShadow": "2px 2px 8px rgba(0,0,0,0.2)"  # shaded border effect
#         }
#     ),
#     dbc.Row([ ]),
#     dbc.Row([
#         dbc.Col([
#             html.H5("Upload Model File"),
#             dcc.Upload(
#                 id='upload-model',
#                 children=html.Div(['Drag and Drop or ', html.A('Select a Model File')]),
#                 style={
#                     'width': '100%', 'height': '60px', 'lineHeight': '60px',
#                     'borderWidth': '1px', 'borderStyle': 'dashed',
#                     'borderRadius': '5px', 'textAlign': 'center'
#                 },
#                 multiple=False
#             ),
#         ], width=6),
        
#         dbc.Col([
#             html.H5("Upload Sample Dataset"),
#             dcc.Upload(
#                 id='upload-dataset',
#                 children=html.Div(['Drag and Drop or ', html.A('Select a Dataset File')]),
#                 style={
#                     'width': '100%', 'height': '60px', 'lineHeight': '60px',
#                     'borderWidth': '1px', 'borderStyle': 'dashed',
#                     'borderRadius': '5px', 'textAlign': 'center'
#                 },
#                 multiple=False
#             ),
#         ], width=6),
#     ], className="mb-4"),
    
#     dbc.Row([
#         dbc.Col(dbc.Button("Global Explanation", id="btn-page1", color="primary", className="me-2")),
#         dbc.Col(dbc.Button("Local Explanation", id="btn-page2", color="secondary")),
#     ], className="text-center"),
    
#     dcc.Location(id='url', refresh=False)
# ])


# # Layouts for other pages
# page1_layout = dbc.Container([
#     html.H2("Page 1"),
#     html.P("This is the first page.")
# ])

# page2_layout = dbc.Container([
#     html.H2("Page 2"),
#     html.P("This is the second page.")
# ])

# # App layout with dynamic content
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])

# @app.callback(
#     dash.Output('tabs-content-horizontal', 'children'),
#     dash.Input('tabs-horizontal', 'value')
# )
# def update_horizontal(tab):
#     if tab == 'tab-1':
#         return html.Div([html.H3("Overview Content")])
#     elif tab == 'tab-2':
#         return html.Div([html.H3("Performance Content")])
#     elif tab == 'tab-3':
#         return html.Div([html.H3("Risk Analysis Content")])
        
# # Callbacks for navigation
# @app.callback(
#     Output('url', 'pathname'),
#     [Input('btn-page1', 'n_clicks'),
#      Input('btn-page2', 'n_clicks')],
#     prevent_initial_call=True
# )
# def navigate(btn1, btn2):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return '/'
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     if button_id == 'btn-page1':
#         return '/page1'
#     elif button_id == 'btn-page2':
#         return '/page2'
#     return '/'

# @app.callback(
#     Output('page-content', 'children'),
#     Input('url', 'pathname')
# )
# def display_page(pathname):
#     if pathname == '/page1':
#         return page1_layout
#     elif pathname == '/page2':
#         return page2_layout
#     else:
#         return front_page_layout

# if __name__ == '__main__':
#     app.run(debug=True)

import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
 
# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "EXAI Dashboard"
server = app.server
 
# Layout for the front page
front_page_layout = dbc.Container([
    html.H1(" "),
    html.H2(
        "Explainable AI Dashboard",
        className="text-center mb-3",
        style={
            "backgroundColor": "white",       # white background
            "border": "1px solid #C9C7C7",    # light black border
            "padding": "15px",                # spacing inside
            "borderRadius": "5px",             # rounded corners
            "boxShadow": "2px 2px 8px rgba(0,0,0,0.2)"  # shaded border effect
        }
    ),
    dbc.Row([]),
    dbc.Row([
        dbc.Col([
            html.H5("Upload Model File"),
            dcc.Upload(
                id='upload-model',
                children=html.Div(['Drag and Drop or ', html.A('Select a Model File')]),
                style={
                    'width': '100%', 'height': '60px', 'lineHeight': '60px',
                    'borderWidth': '1px', 'borderStyle': 'dashed',
                    'borderRadius': '5px', 'textAlign': 'center'
                },
                multiple=False
            ),
        ], width=6),
 
        dbc.Col([
            html.H5("Upload Sample Dataset"),
            dcc.Upload(
                id='upload-dataset',
                children=html.Div(['Drag and Drop or ', html.A('Select a Dataset File')]),
                style={
                    'width': '100%', 'height': '60px', 'lineHeight': '60px',
                    'borderWidth': '1px', 'borderStyle': 'dashed',
                    'borderRadius': '5px', 'textAlign': 'center'
                },
                multiple=False
            ),
        ], width=6),
    ], className="mb-4"),
 
    dbc.Row([
        dbc.Col(dbc.Button("Global Explanation", id="btn-page1", color="primary", className="me-2")),
        dbc.Col(dbc.Button("Local Explanation", id="btn-page2", color="secondary")),
    ], className="text-center"),
    # NOTE: removed the duplicate dcc.Location(id='url', ...) that was here.
    # There must only be ONE component with id='url' in the whole app,
    # and it already lives in app.layout below.
])
 
# Layouts for other pages
page1_layout = dbc.Container([
    html.H2("Page 1"),
    html.P("This is the first page.")
])
 
page2_layout = dbc.Container([
    html.H2("Page 2"),
    html.P("This is the second page.")
])
 
# App layout with dynamic content
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
 
# NOTE: removed the callback for 'tabs-content-horizontal' / 'tabs-horizontal'
# because those component IDs did not exist anywhere in the layout.
# If you want tabs, add a dcc.Tabs(id='tabs-horizontal', ...) and a matching
# html.Div(id='tabs-content-horizontal') somewhere in a layout, then this
# callback can be restored:
#
# @app.callback(
#     Output('tabs-content-horizontal', 'children'),
#     Input('tabs-horizontal', 'value')
# )
# def update_horizontal(tab):
#     if tab == 'tab-1':
#         return html.Div([html.H3("Overview Content")])
#     elif tab == 'tab-2':
#         return html.Div([html.H3("Performance Content")])
#     elif tab == 'tab-3':
#         return html.Div([html.H3("Risk Analysis Content")])
 
# Callbacks for navigation
@app.callback(
    Output('url', 'pathname'),
    [Input('btn-page1', 'n_clicks'),
     Input('btn-page2', 'n_clicks')],
    prevent_initial_call=True
)
def navigate(btn1, btn2):
    ctx = dash.callback_context
    if not ctx.triggered:
        return '/'
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'btn-page1':
        return '/page1'
    elif button_id == 'btn-page2':
        return '/page2'
    return '/'
 
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/page1':
        return page1_layout
    elif pathname == '/page2':
        return page2_layout
    else:
        return front_page_layout
 
if __name__ == '__main__':
    app.run(debug=True)