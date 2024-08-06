import pandas as pd
import plotly
import plotly.graph_objs as go



def income_statement_GOOGL():
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(color = "black", width = 0.5),
          label = [
            'Revenue','Cost and Expense','Income from Operation',
            'Other Income(expense), net','EBIT','Income Tax',
            'Net Income', 'Cost of Revenue', 'Research & Development',
            'Sales & Marketing', 'General and Administrative', 'Google Services',
            'Google Cloud', 'Other Bets', 'Hedging Gains',
            'Google Advertising','Other Platforms','Google Search & Other',
            'YouTube Ads','Google Network'
          ],
          color = [
            'gray','red','green',
            'red','green','red',
            'green','red','red',
            'red','red','gray',
            'gray','gray','gray',
            'gray','gray','gray',
            'gray','gray'
          ]
        ),
        link = dict(
          source = [
            0, 0, 2, 2, 4, 4, 1, 1, 1, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19
          ], 
          target = [2, 1, 4, 3, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 11, 11, 15, 15, 15],
          value = [
            74842, 207994, 71328, 3514, 11356, 59972, 
            126203, 39500, 26567, 15724, 253528, 26280,
            1068, 1960, 224473, 29055, 162450, 29243,
            32780
          ],
          color = [
            'lightgreen', 'pink', 'lightgreen',
            'pink', 'pink', 'lightgreen',
            'pink', 'pink', 'pink',
            'pink', 'lightgray', 'lightgray',
            'lightgray','lightgray','lightgray',
            'lightgray','lightgray','lightgray',
            'lightgray','lightgray'
          ]
      ))])
    return fig

