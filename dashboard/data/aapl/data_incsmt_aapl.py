from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_aapl_incsmt.json')
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
	
	# Node 8-12 taken care later since depends on +/- numbers
	# Hardcode the colors
	nodes_colors = ['gray']*7 + ['red']*11
	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Revenue
	## Product sales
	prod_sales = 0
	for i in range(4):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, i, 4, curr_value, 'lightgray')
		prod_sales += curr_value
	links = add_node_to_link(links, 4, 6, prod_sales , 'lightgray')

	## Service sales
	curr_value = df[df['Node_num']==5]['Value'].values[0]
	links = add_node_to_link(links, 5, 6, curr_value , 'lightgray')


	# Operating Income
	## EBIT
	ebit = 0
	### Income Tax
	inc_tax = df[df['Node_num']==11]['Value'].values[0]
	if inc_tax > 0:
		links = add_node_to_link(links, 10, 11, inc_tax, 'lightpink')
	else:
		links = add_node_to_link(links, 11, 10, inc_tax, 'lightgreen')
		# Change node to green if tax refuen
		nodes_colors[11] = 'green'
	ebit += inc_tax

	### Net Income
	net_inc = df[df['Node_num']==12]['Value'].values[0]
	if net_inc > 0:
		links = add_node_to_link(links, 10, 12, net_inc, 'lightgreen')
		# Change net income node and EBIT node to green
		nodes_colors[10] = 'green'
		nodes_colors[12] = 'green'
	else:
		links = add_node_to_link(links, 12, 10, -1*net_inc, 'lightpink')
	ebit += net_inc

	### EBIT
	if ebit > 0:
		links = add_node_to_link(links, 8, 10, ebit, 'lightgreen')
		nodes_colors[8] = 'green'
	else:
		links = add_node_to_link(links, 10, 8, -1*ebit, 'lightpink')

	### Other Income
	inc_other = df[df['Node_num']==15]['Value'].values[0]
	if inc_other > 0:
		links = add_node_to_link(links, 15, 8, inc_other, 'lightgreen')
		nodes_colors[8] = 'green'
	else:
		links = add_node_to_link(links, 8, 15, -1*inc_other, 'lightpink')

	# Cost of Sales
	cogs = 0
	for i in range(16,18):
		df_expense = df[df['Node_num']==i]
		curr_value = df_expense['Value'].values[0]
		links = add_node_to_link(links, 9, i, curr_value, 'lightpink')
		cogs += curr_value
	links = add_node_to_link(links, 6, 9, cogs , 'lightpink')

	### Operating Income to Net Sales
	op_inc = ebit + inc_other
	if op_inc > 0:
		links = add_node_to_link(links, 6, 8, op_inc, 'lightgreen')
	else:
		links = add_node_to_link(links, 8, 6, -1*op_inc, 'lightpink')

	# Operating Expenses
	op_exp = 0
	for i in range(13,15):
		df_expense = df[df['Node_num']==i]
		curr_value = df_expense['Value'].values[0]
		links = add_node_to_link(links, 7, i, curr_value, 'lightpink')
		op_exp += curr_value
	links = add_node_to_link(links, 6, 7, op_exp , 'lightpink')
		

	return nodes_label, nodes_colors, links