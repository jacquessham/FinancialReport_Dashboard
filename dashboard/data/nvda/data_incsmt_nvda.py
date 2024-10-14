from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
"""
Be sure to update the node definition file
"""
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_nvda_incsmt.json')
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


	
	# Define Node colors
	nodes_colors = ['gray','red','gray','red','green']
	nodes_colors += ['red']*3
	nodes_colors += ['green','red','green']

	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Revenue
	"""
	NVDA reports revenue - cost of revenue = gross profit, the structure
	is different with other companies. And there is no subcategorical
	revenue reporting.
	""" 
	revenue = df[df['Node_num']==0]['Value'].values[0]
	cogs = df[df['Node_num']==1]['Value'].values[0]
	gross_profit = revenue - cogs
	links = add_node_to_link(links, 0, 1, cogs, 'lightpink')
	if gross_profit >= 0:
		links = add_node_to_link(links, 0, 2, gross_profit, 'lightgray')
	else:
		links = add_node_to_link(links, 2, 0, -1*gross_profit, 'red')
	

	## Cost and Expense
	"""
	Use a for loop to aggregate all itemized expense to the sub-expense
	or total expense nodes.

	Here are the steps:
	1 - Define total expense or sub-expense metrics
	2 - Go over a for loop
		a - Obtain the value to this node
		b - Create a link, place the link between the itemized revenue
			and the sub-revenue node, with the value and colour
		c - Incrementally add the current value to the total expense 
			or sub-expense metrics
	3 - After the loop place the link between the sub-expense node and 
		the total expense node. 
	"""
	cost_expense = 0
	for i in range(5, 8):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		cost_expense += curr_value
		links = add_node_to_link(links, 3, i, curr_value, 'pink')
	links = add_node_to_link(links, 2, 3, cost_expense, 'pink')


	## EBIT
	"""
	After Handling the revenue and expense sections, the next section
	shall be EBIT, income tax, and net income.

	Here are the steps:
	1 - Define the ebit metric to aggregate all its sub-section links
		to obtain the value placed in its link to connect between EBIT
		and revenue node
	2 - Create link between EBIT income tax, net income, interest expense,
		other income/loss reported in the EBIT section. Be caution:
			a - Handle the direction if the value is negative, ie, switch
				the origin node and destination node. Handle the node link
				color based on negative or positive number
			b - Convert negative number to positive after last step
			c - Handle the node color based on the metric was original a
				negative or positive number
	3 - Incrementally add the current value to the ebit metric
	4 - Create a link between revenue and EBIT
	"""


	
	### Interest Income
	op_income = df[df['Node_num']==8]['Value'].values[0] 
	if op_income <0:
		links = add_node_to_link(links, 2, 8, op_income, 'pink')
		nodes_colors[8]='red'
	else:
		links = add_node_to_link(links, 8, 2, op_income, 'lightgreen')
		nodes_colors[8]='green'

	ebit = 0
	### Income Tax
	curr_value = df[df['Node_num']==9]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 4, 9, curr_value, 'pink')
		nodes_colors[9]='red'
	else:
		links = add_node_to_link(links, 9, 4, curr_value, 'lightgreen')
		nodes_colors[9]='green'
	ebit += curr_value

	### Net Income
	curr_value = df[df['Node_num']==10]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 4, 10, curr_value, 'lightgreen')
		nodes_colors[10]='green'
	else:
		links = add_node_to_link(links, 10, 4, -1*curr_value, 'pink')
		nodes_colors[10]='red'
	ebit += curr_value
	
	## EBIT
	if ebit > 0:
		nodes_colors[4] = 'green'
		links = add_node_to_link(links, 2, 4, ebit, 'lightgreen')
	else:
		nodes_colors[4] = 'red'
		links = add_node_to_link(links, 4, 2, -1*ebit, 'lightpink')
	

	# Return result
	return nodes_label, nodes_colors, links
	