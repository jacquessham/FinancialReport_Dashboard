# Data for Google
This folder contains all the supporting scripts, sample dataset, and dataset template required to display Google's (GOOGL) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

## Sample Dataset and Template
Coming soon...

## Data Prepartion
Coming soon...

### Income Statement Dataset
Coming soon...

### Balance Sheet Dataset
Coming soon...

### Cash Flow Statement Dataset
Coming soon...

## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_bac_incsmt.json</i>, <i>nodes_bac_balsht.json</i>, and <i>nodes_bac_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
The definitions of nodes used for Bank of America's income statement sankey charts can be found in <i>nodes_bac_incsmt.json</i>, and here is the visualization of the node relation.
<br>

Coming soon...

### Balance Sheet
The definitions of nodes used for Bank of America's balance sheet sankey charts can be found in <i>nodes_bac_balsht.json</i>, and here is the visualization of the node relation.
<br>
Coming soon...


### Cash Flow Statement
The definitions of nodes used for Bank of America's cashflow statement sankey charts can be found in <i>nodes_bac_cshfsmt.json</i>, and here is the visualization of the node relation.
<br>
Coming soon...


## Scripts
Coming soon...

## Reference
BAC's filing on SEC Edgar page - <a href="https://www.sec.gov/edgar/browse/?CIK=70858&owner=exclude">link</a>
<br><br>
2023 10-K - <a href="https://www.sec.gov/Archives/edgar/data/70858/000007085824000122/bac-20231231.htm">link</a>