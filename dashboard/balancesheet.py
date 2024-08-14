import pandas as pd
import balancesheet_googl_poc as example


# For Google
def balancesheet_GOOGL():
	return example.fig

# Function called by dashboard.py
def balancesheet_figure(company, period):
	if company == 'Google':
		# return balancesheet_GOOGL()
		return example.fig
	return example.fig