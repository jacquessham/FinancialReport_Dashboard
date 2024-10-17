import pandas as pd
import data.googl.poc_charts.balancesheet_googl_poc as example  # For poc purpose, delete later
from data.googl.balance_sheet_googl import *
from data.aapl.balance_sheet_aapl import *
from data.meta.balance_sheet_meta import *
from data.bac.balance_sheet_bac import *
from data.ge.balance_sheet_ge import *
from data.nvda.balance_sheet_nvda import *


# Function called by dashboard.py
def balancesheet_figure(company, data):
	if company == 'googl':
		return balance_sheet_GOOGL(data)
	elif company == 'aapl':
		return balance_sheet_AAPL(data)
	elif company == 'meta':
		return balance_sheet_META(data)
	elif company == 'bac':
		return balance_sheet_BAC(data)
	elif company == 'ge':
		return balance_sheet_GE(data)
	elif company == 'nvda':
		return balance_sheet_NVDA(data)
	return None