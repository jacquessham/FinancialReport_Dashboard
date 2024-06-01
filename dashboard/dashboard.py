import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dashboard_structure import *
from income_statement import income_statement_figure
from balancesheet import balancesheet_figure
from cashflow_statement import cashflow_statement_figure


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
        return [html.Div(dcc.Graph(figure=income_statement_figure(company)))]
    # Balance Sheet
    if tab == tab_labels[1]:
        return [html.Div(dcc.Graph(figure=balancesheet_figure(company)))]
    # Cashflow Statement
    return [html.Div(dcc.Graph(figure=cashflow_statement_figure(company)))]
    

# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)
