from pathlib import Path
import json
import pandas as pd


# Read the Node structure setup json file
"""
Be sure to update the node definition file
"""
def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_XXXX_incsmt.json')
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


	
	# Hardcode the colors
	"""
	Define the node color here, use gray for revenue,
	green for positive income, red for expense or negative income

	Example:
	nodes_colors = ['gray']*10 + ['red'] + ['green'] + ['red']*4 

	"""
	

	# Map each KPI with the preassigned index number in nodes_label
	df_temp = {'Items': [k for k in nodes.keys()], 
		'Node_num':[nodes[k] for k in nodes.keys()]}
	df = pd.merge(df, pd.DataFrame(df_temp), on='Items', how='inner')

	# Add with itemized revenue
	"""
	If the revenue is partitioned, you need to aggregate all itemized
	revenue to the revenue node. You may do it in a for loop. 
	Here are the steps:
	1 - Define revenue metrics
	2 - Go over a for loop
		a - Obtain the value to this node
		b - Create a link, place the link between the itemized revenue
			and the sub-revenue node, with the value and colour
		c - Incrementally add the current value to the revenue metric
	3 - After the loop place the link between the sub-revenue node and 
		the revenue node. 

	Note: If the revenue is not partitioned (Such as Meta), a for loop
		  is not needed. If there is more sub-partitions, feel free to
		  have more inner for loop.

	
	Example:
	item_value = 0
	for i in range(3):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		links = add_node_to_link(links, i, 7, curr_value, 'lightgray')
		ads_value += curr_value
	links = add_node_to_link(links, 7, 8, item_value , 'lightgray')
	"""


	## Other Revenue and to handle losses
	"""
	If there is any entries not belong to the standard revenue reporting
	but counted toward to the total revenue, such as other income, you
	may place it here. Use a for loop needed.

	Here are the steps:
	1 - (Optional) Define aggregated metrics only if reported
		in the financial reports
	2 - Create a link (Either individually or in a for loop)
		a - Obtain the value to this node
		b - Place the link between the itemized revenue
			and the revenue or sub-revenue node, with the value and colour
		c - (Optional) Incrementally add the current value to the 
			revenue metric only if reported in the financial reports
	3 - (Optional) After the loop place the link between the sub-revenue node 
		and the revenue node only if reported in the financial reports
	4 - Change color to red if the income is a loss 

	Example:
	for i in range(5,7):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		if curr_value >= 0:
			links = add_node_to_link(links, i, 9, curr_value, 'lightgray')
		else:
			links = add_node_to_link(links, 9, i, -1*curr_value, 'red')
	"""

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

	Example:
	cost_expense = 0
	for i in range(12, 16):
		df_revenue = df[df['Node_num']==i]
		curr_value = df_revenue['Value'].values[0]
		cost_expense += curr_value
		links = add_node_to_link(links, 10, i, curr_value, 'pink')
	links = add_node_to_link(links, 9, 10, cost_expense, 'pink')
	"""

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



	ebit = 0
	### Income Tax
	curr_value = df[df['Node_num']==18]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 17, 18, curr_value, 'pink')
		nodes_colors.append('red')
	else:
		links = add_node_to_link(links, 18, 17, curr_value, 'lightgreen')
		nodes_colors.append('green')
	ebit += curr_value

	if ebit > 0:
		nodes_colors[17] = 'green'
	else:
		nodes_colors[17] = 'red'

	### Net Income
	curr_value = df[df['Node_num']==19]['Value'].values[0] 
	if curr_value >0:
		links = add_node_to_link(links, 17, 19, curr_value, 'lightgreen')
		nodes_colors.append('green')

	else:
		links = add_node_to_link(links, 19, 17, curr_value, 'pink')
		nodes_colors.append('red')
	ebit += curr_value
	links = add_node_to_link(links, 11, 17, ebit, 'lightgreen')
	"""

	

	# Return result
	return nodes_label, nodes_colors, links
	