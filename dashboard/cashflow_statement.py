import pandas as pd
import cashflow_googl as example


# For Google
def cashflow_statemetn_GOOGL():
	return example.fig

# Function called by dashboard.py
def cashflow_statement_figure(company, period):
	if company == 'Google':
		return cashflow_statemetn_GOOGL()
	return example.fig
