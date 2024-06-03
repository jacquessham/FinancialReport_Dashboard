import pandas as pd
import plotly
import plotly.graph_objs as go


fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = [
      	'Asset', 'Liabilities','Equity',
      	'Current Assets', 'Non-marketable Securities', 'Deferred Income Tax',
      	'Properties and Equipments','Operating Lease Assets', 
      	'Intangible Assets', ## 8
      	'Goodwill','Other Non-current Assets','Cash and Cash Equivalents',
      	'Marketable Securities', 'Accounts Receivables', 'Inventory',
      	'Other Current Assets','Current Liabilities', 'Long-term Debt', ## 17
      	'Non-current Deferred Revenue', 'Non-current Income Tax Payable', 
      	'Deferred Income Tax',
      	'Operating Lease Liabilities','Other Long-term Liabilities', ##22
      	'Accounts Payable',
		'Accrued Compensation and Benefits',
		'Accrued Expenses and Other Current Liabilities',
		'Accrued Revenue Share', ## 26
		'Common Stocks', 'Retained Earnings less Accumulated Loss'
      ],
      color = [
      	'black','red', 'blue',
      	'green','green','green',
      	'green','green','green',
      	'green','green','green',
      	'green','green','green',
      	'green', 'red', 'red',
      	'red', 'red', 'red',
      	'red', 'red', 'red', 
      	'red', 'red','red',
      	'blue', 'blue'

      ]
    ),
    link = dict(
      source = [
      	0, 0, 3, 4, 5, 6, 
      	7, 8, 9, 10, 11, 12, 
      	13, 14, 15, 1, 1, 1, 
      	1, 1, 1, 1, 16, 16,
      	16, 16, 2, 2
      ], 
      target = [
      	1, 2, 0, 0, 0, 0, 
      	0, 0, 0, 0, 3, 3, 
      	3, 3, 3, 16, 17, 18, 
      	19, 20, 21, 22, 23, 24,
      	25, 26, 27, 28
      ],
      value = [
      	109120, 256144, 164795, 30492, 5261, 112668, 
      	14381, 2084, 28960, 6623, 21879, 91883,
      	40258, 2670, 8105, 69300, 14701, 599,
      	9258, 514, 12501, 2247, 5128, 14028,
      	37866, 8370, 68184, 195563-7603
      ],
      color = [
      	'pink','lightblue','lightgreen',
      	'lightgreen','lightgreen','lightgreen',
      	'lightgreen','lightgreen','lightgreen',
      	'lightgreen', '#ECFFDC', '#ECFFDC',
      	'#ECFFDC', '#ECFFDC', '#ECFFDC',
      	'pink','pink','pink',
      	'pink','pink','pink',
      	'pink', 'lightpink', 'lightpink',
      	'lightpink', 'lightpink', 'lightblue',
      	'lightblue'
      ]
  ))])
