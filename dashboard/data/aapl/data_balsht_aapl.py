from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_aapl_balsht.json')
	return json.load(f)

# To determine how the link is linked between nodes and determine link colours
def get_link_direction(left_node, right_node, curr_value, acct='asset'):
	# For Liability
	if acct=='liability':
		# Normal liability balance
		if curr_value>0:
			return left_node, right_node, curr_value, 'lightpink'
		# Negative liability balance
		else:
			return right_node, left_node, -1*curr_value, 'lightgreen'
	# For Equity
	elif acct=='equity':
		if curr_value>0:
			return left_node, right_node, curr_value, 'lightblue'
		# Negative retain earnings
		else:
			return right_node, left_node, -1*curr_value, 'lightpink'

	# For Assets accounts
	if curr_value>0:
		return left_node, right_node, curr_value, 'lightgreen'
	# Negative asset balance
	else:
		return right_node, left_node, -1*curr_value, 'lightpink'


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

	# Nodes colour, green=asset, red=liability, blue=equity, black=Total Asset
	nodes_colors = ['green']*11 + ['black'] + ['red'] + ['blue'] 
	nodes_colors += (['red']*9 + ['blue']*2)

	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Asset here
	## Current asset
	curr_asset = 0
	for i in range(0,6):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 9, curr_value, 'asset')
		# Add links from current node to current asset
		links = add_node_to_link(links, link_temp[0],link_temp[1],
			link_temp[2],link_temp[3])
		curr_asset += curr_value
	# Add link from current asset to total asset
	links = add_node_to_link(links, 9, 11, curr_asset, 'lightgreen')

	## Long-term Asset
	noncurr_asset = 0
	for i in range(6,9):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 10, curr_value,'asset')
		## Add links from current node to total asset
		links = add_node_to_link(links, link_temp[0],link_temp[1],
			link_temp[2],link_temp[3])
		noncurr_asset += curr_value
	# Add link from non-current asset to total asset
	links = add_node_to_link(links, 10, 11, noncurr_asset, 'lightgreen')

	# Liabilities here
	lib = 0
	## Current Liabilities
	curr_lib = 0
	for i in range(16,21):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(14, i, curr_value,'liability')
		## Add links from current liability to current node
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		curr_lib += curr_value
	lib += curr_lib # Add curr_lib to total lib
	# Add link from total liability to current liability
	links = add_node_to_link(links, 12, 14, curr_lib, 'lightpink')


	## Long-term Liabilities
	noncurr_lib = 0
	for i in range(21,23):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(15, i, curr_value,'liability')
		# Add link from total liability to current node
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		noncurr_lib += curr_value # Add curr_value directly to total lib
	# Add link from total liability to current liability
	links = add_node_to_link(links, 12, 15, noncurr_lib, 'lightpink')
	# Add link from total asset to totla liability
	lib += noncurr_lib
	links = add_node_to_link(links, 11, 12, lib, 'lightpink')

	# Equity here
	equ = 0
	for i in range(23,25):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(13, i, curr_value,'equity')
		# Add equity from total equity to current node
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		equ += curr_value
	# Add link from total asset to total equity
	links = add_node_to_link(links, 11, 13, equ, 'lightblue')


	return nodes_label, nodes_colors, links