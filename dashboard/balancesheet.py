import pandas as pd
import balancesheet_googl_poc as example
from data.googl.balance_sheet_googl import *


# Function called by dashboard.py
def balancesheet_figure(company, data):
	if company == 'googl':
		# balance_sheet_GOOGL(data) # For testing, delete later
		return balance_sheet_GOOGL(data)
	return example.fig