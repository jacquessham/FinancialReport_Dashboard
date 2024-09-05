import pandas as pd
import data.googl.poc_charts.cashflow_googl_poc as example  # For poc purpose, delete later
from data.googl.cashflow_googl import *
from data.ge.cashflow_ge import *


# Function called by dashboard.py
def cashflow_statement_figure(company, data):
	if company == 'googl':
		return cashflow_statement_GOOGL(data)
	elif company == 'ge':
		return cashflow_statement_GE(data)
	return None
