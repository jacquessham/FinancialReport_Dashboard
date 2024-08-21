import pandas as pd
import data.googl.poc_charts.income_googl_poc as example # For poc purpose, delete later
# from income_googl import *
from data.googl.income_googl import *


# Function called by dashboard.py
def income_statement_figure(company, data):
	# For Google
	if company == 'googl':
		return income_statement_GOOGL(data)
	return None