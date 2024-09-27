from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
"""
Be sure to update the node definition file
"""
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_XXXX_cshfsmt.json')
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
	Investing Activities, as reflected on 10-K or 10-Q, in 3 parts

	Each part will loop over subcategories first, then link it to category,
	and link the category to total. At last, connect Financing Activities and
	Investing Activities with Operating Activities.
	"""


	# Operating Activities here
	"""
	Operating Activities will first handle between Net Income and
	Operating Activities.


	Example:
	## Net Income here
	curr_value = df[df['Node_num']==0]['Value'].values[0]
	link_temp = get_link_direction(0, 9, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 0, curr_value)
	
	
	After handling Net income, create the links between input records
	and Operating Activities subsection. Ignore this step if there is
	no subsections. Finally, create the links between other input records
	and Operating Activies. Use a for loop needed.

	Exmaple:
	## Links between subsections and input records
	op_non_cash = 0
	for i in range(1,8):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 8, curr_value)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		op_non_cash += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)

	## Link Subsection to Operating Activities
	links = add_node_to_link(links, 8, 9, op_non_cash, 'lightgreen')
	nodes_colors = change_node_color(nodes_colors, 8, op_non_cash)
	nodes_colors[9] = 'green' # Operating Activities Node itself
	"""

	# Investing Activities here
	"""
	Create the links between input records and Investing Activities subsection.
	Ignore this step if there is no subsections. Finally, create the links 
	between other input records and Investing Activies. Use a for loop needed.

	
	Example:
	invest = 0
	for i in range(13,17):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(11, i, curr_value, False, True)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		invest += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities to Investing Activities
	link_temp = get_link_direction(9, 11, invest, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 11, invest)
	"""

	# Financing Activities here
	"""
	Create the links between input records and Investing Activities subsection.
	Ignore this step if there is no subsections. Finally, create the links 
	between other input records and Investing Activies. Use a for loop needed.

	Example:
	fin = 0
	for i in range(17,20):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(12, i, curr_value, False, True)
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		fin += curr_value
		nodes_colors = change_node_color(nodes_colors, i, curr_value)
	## Link Operating Activities to Financing Activities
	link_temp = get_link_direction(9, 12, fin, False, True)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 12, fin)
	"""


	## Net Increase in Cash and Exchange Rate Effect 
	"""
	After Complete Operating Activities, Investing Activities, and Financing
	Activities, creates the links:
	- Exchange Rate Effect (If reported)
	- Net Increase in Cash
	For both links, use those nodes as "left node" and Operating Activities
	as "right node"

	# Net Effect on Exchange Rate
	curr_value = df[df['Node_num']==28]['Value'].values[0]
	link_temp = get_link_direction(14, 28, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 28, curr_value)

	# Net Increase in Cash
	curr_value = df[df['Node_num']==10]['Value'].values[0]
	link_temp = get_link_direction(14, 28, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	nodes_colors = change_node_color(nodes_colors, 10, curr_value)
	"""
	
	# Return result
	return nodes_label, nodes_colors, links
