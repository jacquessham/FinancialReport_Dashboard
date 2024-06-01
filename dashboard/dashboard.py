import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dashboard_structure import *
from static_vis import *
from income_statement import income_statement_figure


"""
Load your data here
"""

# Dash Set up
companies = ['Google','Apple','Meta','General Electric',
    'Bank of America','Nvidia']
port = 8000
app = dash.Dash()
app = dash_layout(app, tab_labels, companies)


# Display Income Statement
@app.callback([Output('content','children')],
    [Input('dashboard-tabs','value'), Input('company-choices','value')])
def display_income_statement(tab, company):
    # Income Statement
    if tab == tab_labels[0]:
        return [html.Div(dcc.Graph(figure=income_statement_figure('Google')))]
    # Balance Sheet
    if tab == tab_labels[1]:
        return [html.Div(dcc.Graph(figure=static_scatterplot()))]
    # Cashflow Statement
    return [html.Div(dcc.Graph(figure=static_heatmap()))]
    

# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)
