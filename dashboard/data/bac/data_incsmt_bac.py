from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_bac_incsmt.json')
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


	# Node 16-19 taken care later since depends on +/- numbers
	# Hardcode the colors
	nodes_colors = ['gray']*15+['red']*12
	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	
	# Revenue
	## Interest Income
	inc_netint = 0
	for i in range(5):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, i, 12, curr_value, 'lightgreen')
		inc_netint += curr_value
	
	## Interest Expense
	for i in range(5,9):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, 12, i, curr_value, 'lightpink')
		inc_netint -= curr_value

	# Connect interest income to renvenue
	links = add_node_to_link(links, 12, 14, inc_netint, 'lightgreen')

	## Noninterest Income
	inc_nonint = 0
	for i in range(9,12):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		### Other income maybe negative
		if curr_value > 0:
			links = add_node_to_link(links, i, 13, curr_value, 'lightgreen')
		else:
			links = add_node_to_link(links, 13, i, -1*curr_value, 'lightpink')
		inc_nonint += curr_value
	links = add_node_to_link(links, 13, 14, inc_nonint, 'lightgreen')

	
	# Add itemized expense
	exp_nonint = 0
	for i in range(18,25):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, 15, i, curr_value, 'lightpink')
		exp_nonint += curr_value
	links = add_node_to_link(links, 14, 15, exp_nonint, 'lightpink')

	### Provision for Credit Loses
	df_revenue = df[df['Node_num']==17]
	curr_value = df_revenue['Value'].values[0]
	links = add_node_to_link(links, 14, 17, curr_value, 'lightpink')


	### EBIT
	ebit = 0
	#### Income Tax
	curr_value = df[df['Node_num']==25]['Value'].values[0] 
	if curr_value > 0:
		links = add_node_to_link(links, 16, 25, curr_value, 'lightpink')
	else:
		links = add_node_to_link(links, 25, 16, curr_value, 'lightgreen')
	ebit += curr_value

	#### Net Income
	curr_value = df[df['Node_num']==26]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 16, 26, curr_value, 'lightgreen')
		nodes_colors[26] = 'green'
	else:
		links = add_node_to_link(links, 26, 16, curr_value, 'lightpink')
	ebit += curr_value
	links = add_node_to_link(links, 14, 16, ebit, 'lightgreen')

	# Change node colour if EBIT > 0
	if ebit > 0:
		nodes_colors[16] = 'green'

	# Return result
	return nodes_label, nodes_colors, links
	