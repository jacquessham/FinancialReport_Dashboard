# Data for GE
This folder contains all the supporting scripts, sample dataset, and dataset template required to display GE's (GE) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

## Sample Dataset and Template
Coming soon...

## Data Prepartion
For the current version, data is expected to be added to the sample data CSV files (Files with name end with <b>\_example.csv</b>). Data preparers are expected to copy the format from the template files (Files with name end with <b>\_template.csv</b>), and copy the numbers from 10-K or 10-Q without changing the signs. All entries across all periods (No matter annual data or quarterly data) are saved under one file of its corresponding statement. Please do not separate the files into different period, the backend expects the period differentiate by the value under the <i>Period</i> column. For example, you may copy the format <i>ge_income_template</i>, less the header, from the file. Then, replace period value with the period you are providing. And lastly, enter the value from the source. Each row represents an entry of one of the statements from 10-K or 10-Q, however, there are some entries are combined. Please refer to the individual statement dataset section for detail. If you want to add the entries from another period, please copy the format, less the header, and append to the same dataset file.

### Income Statement Dataset
Coming soon...

### Balance Sheet Dataset
Coming soon...

### Cash Flow Statement Dataset
Coming soon...

## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_ge_incsmt.json</i>, <i>nodes_ge_balsht.json</i>, and <i>nodes_ge_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
The definitions of nodes used for GEe's income statement sankey charts can be found in <i>nodes_ge_incsmt.json</i>, and here is the visualization of the node relation.
<br>
Coming soon...

### Balance Sheet
The definitions of nodes used for GEe's balance sheet sankey charts can be found in <i>nodes_ge_balsht.json</i>, and here is the visualization of the node relation.
<br>
Coming soon...


### Cash Flow Statement
The definitions of nodes used for GEe's cashflow statement sankey charts can be found in <i>nodes_ge_cshfsmt.json</i>, and here is the visualization of the node relation.
<br>
Coming soon...


## Scripts
Coming soon...


## Reference
GE's filing on SEC Edgar page - <a href="https://www.sec.gov/edgar/browse/?CIK=40545&owner=exclude">link</a>
<br><br>
2023 10-K - <a href="https://www.sec.gov/Archives/edgar/data/40545/000004054524000027/ge-20231231.htm">link</a>