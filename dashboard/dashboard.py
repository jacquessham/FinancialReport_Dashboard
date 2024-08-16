import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dashboard_structure import *
from income_statement import income_statement_figure
from balancesheet import balancesheet_figure
from cashflow_statement import cashflow_statement_figure
from data.loaddata import *


"""
Load your data here
"""
# Load data
companies, tickers, company2ticker, companies_data = load_alldata()
companies_dropdown = [{'label':k, 'value':company2ticker[k]} 
                        for k in company2ticker.keys()]

# Dash Set up
port = 8000
app = dash.Dash()
app = dash_layout(app, tab_labels, companies_dropdown)
graph_height = '600px'


# Display list of Reporting periods after selecting a company
@app.callback([Output('period-choices', 'options'), 
        Output('period-choices', 'value')],
    [Input('dashboard-tabs','value'), Input('company-choices','value')])
def display_period_dropdown(tab, company):
    if tab in companies_data[company]:
        return companies_data[company][tab]['periods'], \
            companies_data[company][tab]['periods'][0]
    # If information is not available
    return [], None

# Display Income Statement
@app.callback([Output('content','children')],
    [Input('dashboard-tabs','value'), Input('company-choices','value'),
     Input('period-choices','value')])
def display_income_statement(tab, company, period):
    # print(f'chart callback during {period}')
    # Income Statement
    if tab == tab_labels[0]:
        curr_data = companies_data[company][tab]['data']
        curr_data = curr_data[curr_data['Period']==period]
        return [html.Div(
                    # P/H1 here if needed
                    # Plotly Chart
                    dcc.Graph(
                        figure=income_statement_figure(
                            company, curr_data
                            ),
                        style={'height':graph_height}
                    ))]
    # Balance Sheet
    if tab == tab_labels[1]:
        curr_data = companies_data[company][tab]['data']
        curr_data = curr_data[curr_data['Period']==period]
        return [html.Div(
                    # P/H1 here if needed
                    # Plotly Chart
                    dcc.Graph(
                        figure=balancesheet_figure(company, curr_data),
                        style={'height':graph_height}

                    ))]
    # Cashflow Statement
    curr_data = companies_data[company][tab]['data']
    curr_data = curr_data[curr_data['Period']==period]
    return [html.Div(
                # P/H1 here if needed
                # Plotly Chart
                dcc.Graph(
                    figure=cashflow_statement_figure(company, curr_data),
                        style={'height':graph_height}

                ))]
    
# Initiate dashboard
if __name__ == '__main__':
    app.run_server(debug=True, port=port)
