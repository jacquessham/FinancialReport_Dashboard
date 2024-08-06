import pandas as pd
# import income_googl_poc as example # For poc purpose, delete later
from income_googl import *


"""
# For Google
# For poc purpose, delete later
def income_statement_GOOGL():
	return example.fig
"""

# Function called by dashboard.py
def income_statement_figure(company, period):
	if company == 'googl':
		print(period)
		return income_statement_GOOGL()
	return None