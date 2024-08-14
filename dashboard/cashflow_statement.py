import pandas as pd
import cashflow_googl_poc as example
from data.googl.cashflow_googl import *


# Function called by dashboard.py
def cashflow_statement_figure(company, data):
	if company == 'googl':
		return cashflow_statemetn_GOOGL(data) # For testing, delete later
		# return example.fig # return poc image, delete later
		# return cashflow_statemetn_GOOGL()
	return None
