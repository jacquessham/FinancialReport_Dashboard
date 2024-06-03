import pandas as pd
import income_googl as example


# For Google
def income_statement_GOOGL():
	return example.fig

# Function called by dashboard.py
def income_statement_figure(company):
	if company == 'Google':
		return income_statement_GOOGL()
	return example.fig