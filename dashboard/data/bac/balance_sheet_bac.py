import pandas as pd
import plotly
import plotly.graph_objs as go
from data.bac.data_balsht_bac import *


def balance_sheet_BAC(data):
    nodes_label, nodes_colors, links = get_data(data)

    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(color = "black", width = 0.5),
          label = nodes_label,
          color = nodes_colors
        ),
        link = dict(
          source = links['source'], 
          target = links['target'],
          value = links['value'],
          color = links['color']
      ))])
    return fig