import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)


fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = [
        'Operating Activities', 'Net Income', 
        'Net Cash Provided by Operating Activities', ## 2
        'Investing Activities', 'Financing Activities', 'Net Increase in Cash',
        'Adjustments','Change in assets and Liabilities, net acquisitions' ## 7
      ],
      color = [
        'green', 'green', 'green',
        'red', 'red', 'green',
        'green', 'red'
      ]
    ),
    link = dict(
      source = [
        1, 2, 0, 0, 0, 6, 
        2
      ], 
      target = [
        0, 0, 3, 4, 5, 2, 
        7
      ],
      value = [
        59972, 91495-59972, 20298,
        69757+506, 934, (15287+641+19362-8081+5519+1030),
        (-1)*(-2317+584-5046+707+3915-445+367)
      ],
      color = [
        'lightgreen', 'lightgreen', 'pink',
        'pink', 'lightgreen','lightgreen',
        'pink'
      ]
  ))])

fig.update_layout(title_text="Alphabet FY22 Cashflow Statement (in Millions)")

plotly.offline.plot(fig, filename='cashflow_googl2022.html')