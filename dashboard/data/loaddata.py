import os
import json
import pandas as pd


data_loc = 'data'

def get_companies():
	f = open(f'{data_loc}/companies.json')
	company2ticker = json.load(f)
	companies = [company for company in company2ticker.keys()]
	tickers = [company2ticker[company] for company in companies]

	return companies, tickers, company2ticker

def read_csv(path):
	data = pd.read_csv(path)
	periods = data['Period'].unique().tolist()
	return {'data':data, 'periods':periods}

def load_alldata():
	companies, tickers, company2ticker = get_companies()
	companies_data = {}
	for ticker in tickers:
		if os.path.exists(f'{data_loc}/{ticker}'):
			print(f'I saw {ticker}')
			companies_data[ticker] = {}
			# Load Income Statement data
			inc_smt_loc = f'{data_loc}/{ticker}/{ticker}_income_example.csv'
			companies_data[ticker]['income_statement'] = read_csv(inc_smt_loc)

			# Load Balance Sheet data here
			# Load Cashflow Statement data here

	return companies, tickers, company2ticker, companies_data
