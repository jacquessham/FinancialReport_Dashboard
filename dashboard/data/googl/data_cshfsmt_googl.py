from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_googl_cshfsmt.json')
	return json.load(f)

# Link Direction
def get_link_direction(left_node, right_node, value, pos=True):
	# If value is negative while pos=True
	if pos and value < 0:
		return right_node, left_node, -1*value, 'lightpink'
	# If value is positive while pos=False
	elif pos is False and value < 0:
		return left_node, right_node, -1*value, 'lightgreen'
	# If value is positive while pos=False
	elif pos is False and value > 0:
		return right_node, left_node, -1*value, 'lightpink'
	# If value is positive while pos
	return left_node, right_node, value, 'lightgreen'

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

	# Nodes colour, fix it later
	nodes_colors = ['gray']*len(nodes)

	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')
	# print(df) # Delete later

	# Operating Activities here
	## Net Income here
	curr_value = df[df['Node_num']==0]['Value'].values[0]
	link_temp = get_link_direction(0, 9, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
	
	## Net Increase in Cash
	curr_value = df[df['Node_num']==10]['Value'].values[0]
	link_temp = get_link_direction(0, 10, curr_value)
	links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])

	print(links) # Delete later

	## Non-Cash Charges here

	# Investing Activities here

	# Financing Activities here


	return nodes_label, nodes_colors, links
