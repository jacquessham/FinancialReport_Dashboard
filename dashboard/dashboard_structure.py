from dash import dcc, html


# Sort periods in Year, then quarter in desc order
## The format must be FYXX or XXQX
def periods_dropdown(periods):
	periods_temp = []
	for period in periods:
		# If this is a Annual report (10-K)
		if 'FY' in period:
			year = int(period[2:])
			quarter = 5 # To rank after all 10-Qs
		# If this is a Quarterly report (10-Q)
		elif 'Q' in period:
			year = int(period[:2])
			quarter = int(period[3])
		# If this is an Intreim report (Semiannual)
		elif 'H' in period:
			year = int(period[:2])
			quarter = int(period[3])
		else:
			continue

		# (labels, year in int, quarter in int)
		periods_temp.append((period, year, quarter))
	periods_temp = sorted(periods_temp, key=lambda x: (-x[1],-x[2]))

	# Only returning the labels
	return [t[0] for t in periods_temp]

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
				
				html.Div([
					html.P('Select a company:'),
					dcc.Dropdown(id='company-choices',
						options=dropdown_choices,
						value=dropdown_choices[0]['value'],
						style={'width':'70%','text-align':'left'}
						)
					], style={'width':'80%', 'display':'inline-block'}),
				html.Div([
					html.P('Select the Reporting Period:'),
					dcc.Dropdown(id='period-choices',
                        options=[],
                        value=None,
                        style={'width':'90%','text-align':'left',
                            'float':'center'
                        })
					], style={'width':'18%', 'display':'inline-block'}),
				html.P()
				]),
			# Tabs for choosing the consoldiated statements
			dcc.Tabs(
				id='dashboard-tabs',value=tab_labels[0],
				children=create_tabs(tab_labels)
			),
			# Div to display Graph
			html.Div(id='content', style={'height':'1000px'})
		])
	return app

tab_labels = ['income_statement','balance_sheet','cashflow_statement']
