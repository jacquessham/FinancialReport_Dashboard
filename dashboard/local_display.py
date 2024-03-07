import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.offline import *
from income_googl import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

fig.update_layout(title_text="Alphabet FY22 Income Statement (in Millions)")

plotly.offline.plot(fig, filename='income_goog2022.html')