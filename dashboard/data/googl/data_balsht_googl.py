from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_googl_balsht.json')
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
	print(nodes) # Delete later

	# Nodes colour, green=asset, red=liability, blue=equity
	nodes_colors = ['green']*13+['red']+['blue']+['red']*10+['blue']*2

	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')
	print(df) # Delete later

