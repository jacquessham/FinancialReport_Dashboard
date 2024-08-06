import pandas as pd
import income_googl_poc as example # For poc purpose, delete later
from income_googl import *


"""
# For Google
# For poc purpose, delete later
def income_statement_GOOGL():
	return example.fig
"""

# Function called by dashboard.py
def income_statement_figure(company, data):
	if company == 'googl':
		# print(data)
		# return example.fig
		return income_statement_GOOGL(data)
	return None