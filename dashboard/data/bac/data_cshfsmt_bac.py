from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_bac_cshfsmt.json')
	return json.load(f)

# Link Direction
## pos=False means 10-K or 10-Q list negative number as favor to the company
def get_link_direction(left_node, right_node, value, pos=True, color_flip=False):
	# If value is negative while pos=True
	if pos and value < 0:
		color = 'lightpink'
		result = [right_node, left_node, -1*value]
	# If value is positive while pos=False
	elif pos is False and value < 0:
		color = 'lightgreen'
		result = [left_node, right_node, -1*value]
	# If value is positive while pos=False
	elif pos is False and value > 0:
		color = 'lightpink'
		result = [right_node, left_node, value]
	# If value is positive while pos
	else:
		color = 'lightgreen'
		result = [left_node, right_node, value]

	# If color_flip is true
	if color_flip:
		if color=='lightpink':
			color = 'lightgreen'
		else:
			color = 'lightpink'
	return result[0], result[1], result[2], color

# Add sankey links with data, color, direction
def add_node_to_link(links, source, target, value, color):
	links['source'].append(source)
	links['target'].append(target)
	links['value'].append(value)
	links['color'].append(color)
	return links

# If the number is disfavor, change node colour from green to red, or by versa
def change_node_color(nodes_colors, i_node, value):
	if value>0:
		nodes_colors[i_node] = 'green'
	else:
		nodes_colors[i_node] = 'red'
	return nodes_colors

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

	# Initiate node colour and change colour based on metric values
	nodes_colors = ['gray']*len(nodes)

	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')


	"""
	Mapping the nodes with links based on metric values, each operating
	consists of:
	1 - Extract the value
	2 - Determine the direction of the link and its colour
	3 - Declare the link
	4 - Change node color to reflect whether metric value is favor 
		to company or not

	The algo consists of Operating Activities, Financing Activities,
	Investment Activities, as reflected on 10-K or 10-Q, in 3 parts

	Each part will loop over subcategories first, then link it to category,
	and link the category to total
	"""

	
	# Operating Activities here
	## Net Income here
	curr_value = df[df['Node_num']==0]['Value'].values[0]
	link_temp = get_link_direction(0, 14, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 0, curr_value)
	
	## Adjustments to Reconcile Net Income to Net Cash (Operating Activities)
	op_adjust = 0
	for i in range(1,7):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 12, curr_value)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		op_adjust += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities
	links = add_node_to_link(links, 12, 14, op_adjust, 'lightgreen')
	nodes_colors = change_node_color(nodes_colors, 12, op_adjust)


	## Net Change in Assets/Liabilities Accounts (Operating Activities)
	net_assetlib = 0
	for i in range(8,11):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 13, curr_value)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		net_assetlib += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities
	links = add_node_to_link(links, 13, 14, net_assetlib, 'lightgreen')
	nodes_colors = change_node_color(nodes_colors, 13, net_assetlib)

	## Other Major Operating Activities
	for i in [7, 11]:
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 14, curr_value)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	nodes_colors[14] = 'green' # Operating Activities Node itself

	# Investing Activities here
	invest = 0
	for i in range(17,22):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(15, i, curr_value, False, True)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		invest += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities to Investing Activities
	link_temp = get_link_direction(14, 15, invest, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 15, invest)

	# Financing Activities here
	fin = 0
	for i in range(22,28):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(16, i, curr_value, False, True)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		fin += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities to Financing Activities
	link_temp = get_link_direction(14, 16, fin, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 16, fin)

	# Net Effect on Exchange Rate
	curr_value = df[df['Node_num']==28]['Value'].values[0]
	link_temp = get_link_direction(14, 28, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 28, curr_value)

	# Net Increase in Cash
	curr_value = df[df['Node_num']==29]['Value'].values[0]
	link_temp = get_link_direction(14, 29, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 29, curr_value)

	
	return nodes_label, nodes_colors, links
