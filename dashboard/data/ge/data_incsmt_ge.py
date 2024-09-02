from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_ge_incsmt.json')
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

	# Hardcode the colors and take care the color in the loops
	nodes_colors = ['gray']*19


	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Revenue
	## Add Itemized revenue
	for i in range(3):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, i, 13, curr_value, 'lightgray')

	## Other Income (Loss)
	df_revenue = df[df['Node_num']==12]
	curr_value = df_revenue['Value'].values[0]
	if curr_value >= 0:
		links = add_node_to_link(links, 12, 13, curr_value, 'lightgreen')
	else:
		links = add_node_to_link(links, 13, 12, -1*curr_value, 'red')
		nodes_colors[12] = 'red'

	## Cost and Expense
	cost_expense = 0
	for i in range(3, 12):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		cost_expense += curr_value
		if curr_value > 0: 
			nodes_colors[i] = 'red'
			links = add_node_to_link(links, 14, i, curr_value, 'pink')
		# Non-operating benefit cost (income) could be negative
		else:
			nodes_colors[i] = 'green'
			links = add_node_to_link(links, i, 14, -1*curr_value, 'lightgreen')
	links = add_node_to_link(links, 13, 14, cost_expense, 'pink')

	### EBIT
	ebit = 0
	#### Income Tax
	#### Income Tax Provision is negative in GE, each is different from others
	curr_value = df[df['Node_num']==16]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 16, 15, curr_value, 'lightgreen')
		nodes_colors[16] = 'green'
		ebit += curr_value
	else:
		links = add_node_to_link(links, 15, 16, -1*curr_value, 'pink')
		nodes_colors[16] = 'red'
		ebit -= curr_value
	
	#### Net Income
	curr_value = df[df['Node_num']==18]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 15, 18, curr_value, 'lightgreen')
		nodes_colors[18] = 'green'
	else:
		links = add_node_to_link(links, 18, 15, curr_value, 'pink')
		nodes_colors[18] = 'red'
	ebit += curr_value


	#### Earning from discontinued operations, net of taxes
	#### Positive is link toward EBIT
	curr_value = df[df['Node_num']==17]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 17, 15, curr_value, 'lightgreen')
		nodes_colors[17] = 'green'
		ebit -= curr_value
	else:
		links = add_node_to_link(links, 15, 17, -1*curr_value, 'pink')
		nodes_colors[17] = 'red'
		ebit += curr_value

	# Change EBIT node colour
	if ebit > 0:
		links = add_node_to_link(links, 13, 15, ebit, 'lightgreen')
		nodes_colors[15] = 'green'
	else:
		links = add_node_to_link(links, 15, 13, -1*ebit, 'pink')
		nodes_colors[15] = 'red'

	# Return result
	return nodes_label, nodes_colors, links
	