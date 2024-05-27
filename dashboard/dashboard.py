import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dashboard_structure import *
from static_vis import *

"""
Load your data here
"""

# Dash Set up
tab_labels = ['income_statement','balance_sheet','cashflow_statement']
port = 8000
app = dash.Dash()
app = dash_layout(app, tab_labels)


# Display Income Statement
@app.callback([Output('content','children')],
    [Input('dashboard-tabs','value')])
def display_income_statement(tab):
    if tab == tab_labels[0]:
        return [html.Div(dcc.Graph(figure=static_linechart()))]
    if tab == tab_labels[1]:
        return [html.Div(dcc.Graph(figure=static_scatterplot()))]
    return [html.Div(dcc.Graph(figure=static_heatmap()))]
    

# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)