# Data for Apple
This folder contains all the supporting scripts, sample dataset, and dataset template required to display Apple's (AAPL) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

## Sample Dataset and Template
The sample dataset and dataset template files are available in the [Dataset](dataset) folder. 
<br><br>
Current, the sample dataset consists of:
<ul>
	<li>Income Statement:<ul>
		<li>FY23</li>
		</ul>
	</li>
	<li>Balance Sheet:<ul>
		<li>FY23</li>
		</ul>
	</li>
	<li>Income Statement:<ul>
		<li>FY23</li>
		</ul>
	</li>
</ul>

<br>
Here are the templates:
<ul>
	<li>aapl_income_template.csv</li>
	<li>aapl_balancesheet_template.csv</li>
	<li>aapl_cashflow_template.csv</li>
</ul>

## Data Prepartion
For the current version, data is expected to be added to the sample data CSV files (Files with name end with <b>\_example.csv</b>). Data preparers are expected to copy the format from the template files (Files with name end with <b>\_template.csv</b>), and copy the numbers from 10-K or 10-Q without changing the signs. All entries across all periods (No matter annual data or quarterly data) are saved under one file of its corresponding statement. Please do not separate the files into different period, the backend expects the period differentiate by the value under the <i>Period</i> column. For example, you may copy the format <i>aapl_income_template</i>, less the header, from the file. Then, replace period value with the period you are providing. And lastly, enter the value from the source. Each row represents an entry of one of the statements from 10-K or 10-Q, however, there are some entries are combined. Please refer to the individual statement dataset section for detail. If you want to add the entries from another period, please copy the format, less the header, and append to the same dataset file.

### Income Statement Dataset
Coming soon...

### Balance Sheet Dataset
Coming soon...

### Cash Flow Statement Dataset
Coming soon...

## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_aapl_incsmt.json</i>, <i>nodes_aapl_balsht.json</i>, and <i>nodes_aapl_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
Coming soon...

<br><br>
<img src=Images/aapl_inc_sankey.png>

### Balance Sheet
Coming soon...

<br><br>
<img src=Images/aapl_balsht_sankey.png>

### Cash Flow Statement
Coming soon...

## Scripts
Here are the scripts utilized by <i>dashboard.py</i>:
<ul>
	<li><i>income_aapl.py</i>: Organizate income statement data at <i>data_incsmt_aapl.py</i> and generate sankey chart figure object.</li>
	<li><i>balance_sheet_aapl.py</i>: Organizate balance sheet data at <i>data_balsht_aapl.py</i> and generate sankey chart figure object.</li>
	<li><i>cashflow_aapl.py</i>: Organizate cashflow statement data at <i>data_cshfsmt_aapl.py</i> and generate sankey chart figure object.</li>
	<li><i>data_incsmt_aapl.py</i>: Assign links metadata for the income statement sankey charts.</li>
	<li><i>data_balsht_aapl.py</i>: Assign links metadata for the balance sheet sankey charts.</li>
	<li><i>data_cshfsmt_aapl.py</i>: Assign links metadata for the cashflow statement sankey charts.</li>
</ul>

<br>
<i>data_incsmt_aapl.py</i>, <i>data_balsht_aapl.py</i>, <i>data_cshfsmt_aapl.py</i> are the scripts that are responable on converting financial data to a format that is accepted by Plotly sankey chart package, ie, defining nodes and node links. The nodes name, position (index number) are predefined in <i>nodes_aapl_incsmt.json</i>, <i>nodes_aapl_balsht.json</i>, and <i>nodes_aapl_cshfsmt.json</i>. The scripts will first map the data to those nodes and create links that will generate on the sankey chart. The idea is to provide detailed level data to the CSV file, the script will obtain the data and aggregate it for the high level metrics on the sankey chart. Below is the overview of the algorithm of the scripts.

### data_incsmt_aapl.py
This script prepares the sankey chart of aaple's income statement. The data preparer will provide data on Node 0-3, 5, 11-17 . The scirpt will first aggregate revenue among Node 0-3, 5, then expense among Node 13-14, 16-17, and aggregate income from operation, expenses, and EBIT at the end.

### data_balsht_aapl.py
This script prepares the sankey chart of aaple's balance sheet. The data preparer will provide data on Node 0-8, 16-24. The script will treat assets, liabilities, and equity into three blocks and aggregate the data in each block and link these blocks together at the end.

### data_cshfsmt_aapl.py
This script prepares the sankey chart of aaple's cashflow statement. The data preparer will provide data on Node 0-5, 9-17. The script will treat operating activities, financing activities, investment activities into three blocks and aggregate the data in each block and link these blocks together at the end.


## Reference
AAPL's filing on SEC Edgar page - <a href="https://www.sec.gov/edgar/browse/?CIK=320193&owner=exclude">link</a>
<br><br>
2023 10-K - <a href="https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm">link</a>
