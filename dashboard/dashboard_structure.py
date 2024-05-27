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


def dash_layout(app, tab_labels):
	app.layout = html.Div([
			dcc.Tabs(
				id='dashboard-tabs',value=tab_labels[0],
				children=create_tabs(tab_labels)
			),
			html.Div(id='content')
		])
	return app