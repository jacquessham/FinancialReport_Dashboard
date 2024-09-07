from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_ge_cshfsmt.json')
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
	cont_op = 0
	## Net Income here
	curr_value = df[df['Node_num']==0]['Value'].values[0]
	link_temp = get_link_direction(0, 14, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 0, curr_value)
	cont_op += curr_value
	
	## Net Increase in Cash
	curr_value = df[df['Node_num']==33]['Value'].values[0]
	link_temp = get_link_direction(15, 33, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 33, curr_value)

	## Adjustmetns to cash from operating activities here
	adjust_op = 0
	for i in range(1,12):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 13, curr_value)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		adjust_op += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	link_temp = get_link_direction(13, 14, adjust_op)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 13, adjust_op)
	cont_op += adjust_op

	## Link Continue Activities to Operating Activities
	link_temp = get_link_direction(14, 15, cont_op)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 14, cont_op)

	## Link Discontinue Activities to Operating Activities
	curr_value = df[df['Node_num']==12]['Value'].values[0]
	link_temp = get_link_direction(12, 15, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	# Discontinue Operating Activities Node
	nodes_colors = change_node_color(nodes_colors, 12, curr_value)
	# Operating Activities Node
	nodes_colors = change_node_color(nodes_colors, 15, curr_value+cont_op) 

	# Investing Activities here
	invest = 0
	for i in range(21,26):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(18, i, curr_value, False, True)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		invest += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities to Continue Operating Activities
	link_temp = get_link_direction(16, 18, invest, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 18, invest)

	## Link Investing Activities to Disontinue Investing Activities
	curr_value = df[df['Node_num']==20]['Value'].values[0]
	link_temp = get_link_direction(20, 16, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 20, curr_value)
	invest += curr_value

	## Link Operating Activities to Investing Activities
	link_temp = get_link_direction(15, 16, invest, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 16, invest)

	# Financing Activities here
	fin = 0
	for i in range(26,31):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(19, i, curr_value, False, True)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		fin += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities to Financing Activities
	link_temp = get_link_direction(17, 19, fin, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 19, fin)

	## Link Financing Activities to Continue Financing Activities
	curr_value = df[df['Node_num']==31]['Value'].values[0]
	link_temp = get_link_direction(31, 17, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 31, curr_value)
	fin += curr_value

	## Link Operating Activities to Finacing Activities
	link_temp = get_link_direction(15, 17, fin, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 17, fin)

	# Net Effect on Exchange Rate
	curr_value = df[df['Node_num']==32]['Value'].values[0]
	link_temp = get_link_direction(15, 32, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 32, curr_value)
	
	return nodes_label, nodes_colors, links
