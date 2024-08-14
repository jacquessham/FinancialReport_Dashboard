import pandas as pd
import balancesheet_googl_poc as example
from data.googl.balance_sheet_googl import *


# Function called by dashboard.py
def balancesheet_figure(company, period):
	if company == 'Google':
		# return balance_sheet_GOOGL(data)
		return example.fig
	return example.fig