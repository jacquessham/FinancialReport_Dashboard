from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_googl_incsmt.json')
	return json.load(f)

# Add sankey links with data, color, direction
def add_node_to_link(links, source, target, value, color):
	links['source'].append(source)
	links['target'].append(target)
	links['value'].append(value)
	links['color'].append(color)
	return links

# Translate CSV data into sankey setup
def get_data(df):
	# Initiate result dict
	links = {
		'source': [],
		'target': [],
		'value': [],
		'color': []
	}
	# Obtain prepared sankey nodes setup
	nodes = get_nodes()
	nodes_label = [k for k in nodes.keys()]
	# nodes_num = [nodes[k] for k in nodes.keys()]


	# Node 16-19 taken care later since depends on +/- numbers
	# Hardcode the colors
	nodes_colors = ['gray']*10 + ['red'] + ['green'] + ['red']*4 
	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Add with itemized revenue
	## Google Advertising
	ads_value = 0
	for i in range(3):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, i, 7, curr_value, 'lightgray')
		ads_value += curr_value
	links = add_node_to_link(links, 7, 8, ads_value , 'lightgray')
	
	## Google Service
	curr_value = df[df['Node_num']==3]['Value'].values[0]
	srv_value = ads_value + curr_value
	links = add_node_to_link(links, 3, 8, curr_value, 'lightgray')

	## Revenue less Other Revenue
	### Service Revenue
	links = add_node_to_link(links, 8, 9, srv_value, 'lightgray')
	### Google Clouds
	links = add_node_to_link(links, 4, 9,
		df[df['Node_num']==4]['Value'].values[0],'lightgray')

	## Other Revenue - Hedging Gain and Other Bets
	for i in range(5,7):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		if curr_value >= 0:
			links = add_node_to_link(links, i, 9, curr_value, 'lightgray')
		else:
			links = add_node_to_link(links, 9, i, -1*curr_value, 'red')

	# Add itemized expense
	## Income from Operation
	inc_op = 0
	### Other income, net
	curr_value = df[df['Node_num']==16]['Value'].values[0] 
	if curr_value < 0:
		links = add_node_to_link(links, 11, 16, -1*curr_value, 'pink')
		nodes_colors.append('red')
	else:
		links = add_node_to_link(links, 16, 11, curr_value, 'lightgray')
		nodes_colors.append('gray')
	inc_op += -1*curr_value

	### EBIT
	ebit = 0
	nodes_colors.append(None) # Placeholder for EBIT node
	#### Income Tax
	curr_value = df[df['Node_num']==18]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 17, 18, curr_value, 'pink')
		nodes_colors.append('red')
	else:
		links = add_node_to_link(links, 18, 17, curr_value, 'lightgreen')
		nodes_colors.append('green')
	ebit += curr_value

	if ebit > 0:
		nodes_colors[17] = 'green'
	else:
		nodes_colors[17] = 'red'


	#### Net Income
	curr_value = df[df['Node_num']==19]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 17, 19, curr_value, 'lightgreen')
		nodes_colors.append('green')

	else:
		links = add_node_to_link(links, 19, 17, curr_value, 'pink')
		nodes_colors.append('red')
	ebit += curr_value
	links = add_node_to_link(links, 11, 17, ebit, 'lightgreen')

	## Income from Operation
	inc_op += ebit
	links = add_node_to_link(links, 9, 11, inc_op, 'lightgreen')

	## Cost and Expense
	cost_expense = 0
	for i in range(12, 16):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		cost_expense += curr_value
		links = add_node_to_link(links, 10, i, curr_value, 'pink')
	links = add_node_to_link(links, 9, 10, cost_expense, 'pink')

	# Return result
	return nodes_label, nodes_colors, links
	