from pathlib import Path
import json
import pandas as pd


def get_nodes():
	curr_dir = Path(__file__).parent
	f = open(f'{curr_dir}/nodes_googl.json')
	return json.load(f)


def get_data(df):
	nodes = get_nodes()
	nodes_label = [k for k in nodes.keys()]
	print(nodes_label)
	print(df)