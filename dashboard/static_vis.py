import pandas as pd
import plotly.graph_objs as go


def static_linechart():
	df = pd.read_csv('cust_num.csv')
	df = df[df['day']=='Monday']
	data = []
	data.append(go.Scatter(x=df['hour'], y=df['customers_count'],
						mode='lines'))
	# Layout
	layout = {'title':{'text':'Number of Customer Trend', 'x':0.5}}

	return {'data': data, 'layout': layout}

def static_scatterplot():
	df = pd.read_csv('tips.csv')
	data = []
	data.append(go.Scatter(x=df['grand_total'], y=df['tips'],
						mode='markers'))
	# Layout
	layout = {'title':{'text':'Everybody\'s Tipping Distribution', 'x':0.5}}

	fig = go.Figure(data=data, layout=layout)
	return {'data': data, 'layout': layout}

def static_heatmap():
	df = pd.read_csv('cust_num.csv')
	data = []
	data.append(go.Heatmap(z=df['customers_count'],
		                   x=df['day'], y=df['hour'],
		                   colorscale='ylorrd'))

	# Layout
	layout = {'title':{'text':'Department Store Traffic',
		               'x':0.5},
		      'xaxis': {'tickmode':'linear'},
		      'yaxis': {'tickmode':'linear'}}

	return {'data': data, 'layout': layout}