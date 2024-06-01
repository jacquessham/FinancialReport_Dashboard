from dash import dcc, html


def create_tabs(tab_labels):
	tabs = []
	for tab_label in tab_labels:
		tabs.append(
				dcc.Tab(
					label=f'{tab_label.title().replace('_',' ')}', 
					value=f'{tab_label}'
				)
			)
	return tabs


def dash_layout(app, tab_labels, dropdown_choices):
	app.layout = html.Div([
			# Dashboard Top
			html.Div([
				html.H1(children='Financial Dashboard',
					style={'text-align':'center'}),
				html.P('Select a company:'),
				dcc.Dropdown(id='company-choices',
					options=dropdown_choices,
					value=dropdown_choices[0],
					style={'width':'70%','text-align':'left'}
					),
				html.P()
				]),
			# Tabs for choosing the consoldiated statements
			dcc.Tabs(
				id='dashboard-tabs',value=tab_labels[0],
				children=create_tabs(tab_labels)
			),
			# Div to display Graph
			html.Div(id='content')
		])
	return app

tab_labels = ['income_statement','balance_sheet','cashflow_statement']
