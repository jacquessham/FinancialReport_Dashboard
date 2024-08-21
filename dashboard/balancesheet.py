import pandas as pd
import data.googl.poc_charts.balancesheet_googl_poc as example  # For poc purpose, delete later
from data.googl.balance_sheet_googl import *


# Function called by dashboard.py
def balancesheet_figure(company, data):
	if company == 'googl':
		return balance_sheet_GOOGL(data)
	return None