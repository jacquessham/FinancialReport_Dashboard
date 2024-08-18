import os
import json
import pandas as pd


data_loc = 'data'

# Get a list of available companies
def get_companies():
	f = open(f'{data_loc}/companies.json')
	company2ticker = json.load(f)
	companies = [company for company in company2ticker.keys()]
	tickers = [company2ticker[company] for company in companies]

	return companies, tickers, company2ticker

# Get available data and get available periods
def read_csv(path):
	data = pd.read_csv(path)
	periods = data['Period'].unique().tolist()
	return {'data':data, 'periods':periods}

def load_alldata():
	# Get a list of available companies
	companies, tickers, company2ticker = get_companies()
	companies_data = {}

	# Loop over all available companies (folder)
	for ticker in tickers:
		if os.path.exists(f'{data_loc}/{ticker}'):
			# Initiate container to store all data
			companies_data[ticker] = {}

			# Dataset folder location
			dataset_loc = f'{data_loc}/{ticker}/dataset/'

			# Load Income Statement data
			inc_smt_loc = dataset_loc+f'{ticker}_income_example.csv'
			companies_data[ticker]['income_statement'] = read_csv(inc_smt_loc)

			# Load Balance Sheet data
			bal_sht_loc = dataset_loc+f'{ticker}_balancesheet_example.csv'
			companies_data[ticker]['balance_sheet'] = read_csv(bal_sht_loc)

			# Load Cashflow Statement data
			cshf_loc = dataset_loc+f'{ticker}_cashflow_example.csv'
			companies_data[ticker]['cashflow_statement'] = read_csv(cshf_loc)


	return companies, tickers, company2ticker, companies_data
