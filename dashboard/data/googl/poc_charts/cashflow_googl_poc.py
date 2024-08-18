import pandas as pd
import plotly
import plotly.graph_objs as go


fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = [
        'Operating Activities', 'Net Income', 'Investing Activities', 
        'Financing Activities', 'Net Increase in Cash', 'Non-Cash Charges', ##5
        'Depreciation', 'Stock-based Compensation Expense', 
        'Defferred Income Tax', ##8
        'Gain on Debt and Equity','Other Adjustment',
        'Change in Assets and Liabilities', ## 11
        'Capital Expenditure', 'Securities Investment','Acquisitions', ## 14
        'Other Investment Activities', 
        'Repurchase of Stock and Stock-based award Activities',
        'Debt-related Activities', ##17
        'Effect of Exchange Rate on Cash'
        
      ],
      color = [
        'green', 'green', 'red', 
        'red', 'green', 'green',
        'green', 'green', 'red',
        'green','green', 'red',
        'red', 'green', 'red',
        'green', 'red', 'red',
        'red'
      ]
    ),
    link = dict(
      source = [
        1, 0, 0, 
        0, 5, 6,
        7, 5, 9,
        10, 5, 2,
        13, 2, 15,
        3, 3, 3
      ], 
      target = [
        0, 2, 3, 
        4, 0, 5,
        5, 8, 5,
        5, 11, 12,
        2, 14, 2,
        16, 17, 18

      ],
      value = [
        59972, 20298, 69757+506, 
        934, 91495-59972, 15287+641,
        19362, 8081, 5519,
        1030, 2235, 31485,
        16567, 6969, 1589,
        59296+9300, abs(52872-54068+35), 506
      ],
      color = [
        'lightgreen', 'pink', 'pink',
        'lightgreen','lightgreen','lightgreen',
        'lightgreen', 'pink', 'lightgreen',
        'lightgreen', 'pink', 'pink',
        'lightgreen', 'pink', 'lightgreen',
        'pink', 'pink', 'pink'
      ]
  ))])
