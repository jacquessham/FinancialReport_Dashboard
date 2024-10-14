import pandas as pd
import data.googl.poc_charts.income_googl_poc as example # For poc purpose, delete later
# from income_googl import *
from data.googl.income_googl import *
from data.aapl.income_aapl import *
from data.meta.income_meta import *
from data.bac.income_bac import *
from data.ge.income_ge import *
from data.nvda.income_nvda import *


# Function called by dashboard.py
def income_statement_figure(company, data):
	# For Google
	if company == 'googl':
		return income_statement_GOOGL(data)
	elif company == 'aapl':
		return income_statement_AAPL(data)
	elif company == 'meta':
		return income_statement_META(data)
	elif company == 'bac':
		return income_statement_BAC(data)
	elif company == 'ge':
		return income_statement_GE(data)
	elif company == 'nvda':
		return income_statement_NVDA(data)
	return None