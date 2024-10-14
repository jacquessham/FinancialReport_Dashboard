from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
"""
Be sure to update the node definition file
"""
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_nvda_balsht.json')
	return json.load(f)

# To determine how the link is linked between nodes and determine link colours
# Be sure to clarify acct='liability' or acct='equity' if it is not asset acct
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
	nodes_colors = ['green']*12+['black','red','blue']+['red']*7+['blue']*2


	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	"""
	Mapping the nodes with links based on metric values, each operating
	consists of:
	1 - Extract the value
	2 - Determine the direction of the link, the color is always green for
		asset, red for liabilities, blue for equity. In case of negative number in
		retained earning or related, switch the link direction
	3 - Declare the link

	The algo consists of Asset, Libilities, Equity, as reflected on 10-K or 10-Q,
	in 3 sections

	Each section will loop over subcategories or current accounts first, 
	then link it to main account (asset, libilities, equity),
	and link the libilities and equity to asset. Long-term accounts 
	may be connected directly to the main account without a long-term node, ie,
	long-term asset/libilities directly connect with Asset/Libilities node.
	"""

	# Asset here
	## Current Assets
	curr_asset = 0
	for i in range(0,5):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 11, curr_value,'asset')
		# Add links from current node to current asset
		links = add_node_to_link(links, link_temp[0],link_temp[1],
			link_temp[2],link_temp[3])
		curr_asset += curr_value
	# Add link from current asset to total asset
	links = add_node_to_link(links, 11, 12, curr_asset, 'lightgreen')

	## Long-term Asset
	for i in range(5,11):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(i, 12, curr_value,'asset')
		## Add links from current node to total asset
		links = add_node_to_link(links, link_temp[0],link_temp[1],
			link_temp[2],link_temp[3])


	# Liabilities here
	lib = 0
	## Current Liabilities
	curr_lib = 0
	for i in range(16,19):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(15, i, curr_value,'liability')
		## Add links from current liability to current node
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		curr_lib += curr_value
	lib += curr_lib # Add curr_lib to total lib
	# Add link from total liability to current liability
	links = add_node_to_link(links, 13, 15, curr_lib, 'lightpink')

	## Long-term Liabilities
	for i in range(19,22):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(13, i, curr_value,'liability')
		# Add link from total liability to current node
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		lib += curr_value # Add curr_value directly to total lib

	# Add link from total asset to total liability
	links = add_node_to_link(links, 12, 13, lib, 'lightpink')


	# Equity here
	equ = 0
	for i in range(22,24):
		curr_value = df[df['Node_num']==i]['Value'].values[0]
		link_temp = get_link_direction(14, i, curr_value,'equity')
		# Add equity from total equity to current node
		links = add_node_to_link(links, link_temp[0],link_temp[1],
		link_temp[2],link_temp[3])
		equ += curr_value

	# Add link from total asset to total equity
	links = add_node_to_link(links, 12, 14, equ, 'lightblue')



	return nodes_label, nodes_colors, links

