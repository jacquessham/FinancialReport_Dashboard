from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_meta_incsmt.json')
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


	# Node 9 taken care later since depends on +/- numbers
	# Hardcode the colors
	nodes_colors = ['gray'] + ['red'] + ['green'] + ['red']*6 + ['green']
	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Revenue not need to setup since revenue is not itemized
	# Cost of expense
	cogs = 0
	for i in range(3,7):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, 1, i, curr_value, 'lightpink')
		cogs += curr_value
	links = add_node_to_link(links, 0, 1, cogs, 'lightpink')

	# EBIT
	ebit = 0

	## Interest and other income(expense)
	df_revenue = df[df['Node_num']==7]
	curr_value = df_revenue['Value'].values[0]
	if curr_value < 0:
		links = add_node_to_link(links, 2, 7, curr_value, 'lightpink')
	else:
		links = add_node_to_link(links, 7, 2, curr_value, 'lightgreen')
		nodes_colors[7] = 'green'
	ebit += -1*curr_value # Adjustment by multiply by -1

	## Income tax
	df_revenue = df[df['Node_num']==8]
	curr_value = df_revenue['Value'].values[0]
	links = add_node_to_link(links, 2, 8, curr_value, 'lightpink')
	ebit += curr_value

	## Net Income
	df_revenue = df[df['Node_num']==9]
	curr_value = df_revenue['Value'].values[0]
	### When profit
	if curr_value > 0:
		links = add_node_to_link(links, 2, 9, curr_value, 'lightgreen')
	### When lost
	else:
		links = add_node_to_link(links, 9, 2, curr_value, 'lightpink')
		nodes_colors[9] = 'red'
	ebit += curr_value


	links = add_node_to_link(links, 0, 2, ebit, 'lightgreen')

	# Return result
	return nodes_label, nodes_colors, links

