# Data for Meta
This folder contains all the supporting scripts, sample dataset, and dataset template required to display Meta's (META) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

## Sample Dataset and Template
The sample dataset and dataset template files are available in the [Dataset](dataset) folder. 
<br><br>
Current, the sample dataset consists of:
<ul>
	<li>Income Statement:<ul>
		<li>FY23</li>
		<li>FY22</li>
		</ul>
	</li>
	<li>Balance Sheet:<ul>
		<li>FY23</li>
		<li>FY22</li>
		</ul>
	</li>
	<li>Income Statement:<ul>
		<li>FY23</li>
		<li>FY22</li>
		</ul>
	</li>
</ul>

<br>
Here are the templates:
<ul>
	<li>meta_income_template.csv</li>
	<li>meta_balancesheet_template.csv</li>
	<li>meta_cashflow_template.csv</li>
</ul>

## Data Prepartion
For the current version, data is expected to be added to the sample data CSV files (Files with name end with <b>\_example.csv</b>). Data preparers are expected to copy the format from the template files (Files with name end with <b>\_template.csv</b>), and copy the numbers from 10-K or 10-Q without changing the signs. All entries across all periods (No matter annual data or quarterly data) are saved under one file of its corresponding statement. Please do not separate the files into different period, the backend expects the period differentiate by the value under the <i>Period</i> column. For example, you may copy the format <i>meta_income_template</i>, less the header, from the file. Then, replace period value with the period you are providing. And lastly, enter the value from the source. Each row represents an entry of one of the statements from 10-K or 10-Q, however, there are some entries are combined. Please refer to the individual statement dataset section for detail. If you want to add the entries from another period, please copy the format, less the header, and append to the same dataset file.

### Income Statement Dataset
You may find all the entries from the consolidated statement of income section of the report. No field is combined in this visualization setup.

### Balance Sheet Dataset
You may find all the entries from the consolidated balance sheet section of the report, except the Common Stock column. All assets and liabilities values may be retreived from the balance and directly copy the value to the dataset.
<br>

<ul>
	<li>Common Stocks (Node 22): Sum of Common stocks and Additonal paid-in capital</li>
</ul>

<img src=Images/meta_balsht_cal1_explain.png>

### Cash Flow Statement Dataset
You may find all values required by the cash flow statement in the consolidated statements of cash flow section. Please copy the data without changing the signs for all values.
<br><br>

There are 3 entries required summing their dependent columns or name change:
<ul>
	<li>Changes in Assets and Liabilities (Node 7): Sum of items under the Operating activities subsection of Changes in assets and liabilities </li>
	<li>Purchases of Property and Equipment and Activities (Node 13): Sum of Purchases of property and equipment, and Proceeds relating to property and equipment</li>
	<li>Marketable Debt Securities Activities (Node 14): Sum of Purchases of marketable debt securities and Sales and maturities of marketable debt securities</li>
</ul>

<img src=Images/meta_cshfsmt_cal1_explain.png>
<img src=Images/meta_cshfsmt_cal2_explain.png>

## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_meta_incsmt.json</i>, <i>nodes_meta_balsht.json</i>, and <i>nodes_meta_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
The definitions of nodes used for Meta's income statement sankey charts can be found in nodes_meta_incsmt.json, and here is the visualization of the node relation.
<br>

<img src=Images/meta_incsmt_sankey.png>

### Balance Sheet
The definitions of nodes used for Meta's balance sheet sankey charts can be found in nodes_meta_balsht.json, and here is the visualization of the node relation.
<br>

<img src=Images/meta_bal_sankey.png>

### Cashflow Statement
The definitions of nodes used for Meta's cashflow statement sankey charts can be found in nodes_meta_cshfsmt.json, and here is the visualization of the node relation.
<br>

<img src=Images/meta_cshfsmt_sankey.png>


## Scripts
Here are the scripts utilized by <i>dashboard.py</i>:
<ul>
	<li><i>income_meta.py</i>: Organizate income statement data at <i>data_incsmt_meta.py</i> and generate sankey chart figure object.</li>
	<li><i>balance_sheet_meta.py</i>: Organizate balance sheet data at <i>data_balsht_meta.py</i> and generate sankey chart figure object.</li>
	<li><i>cashflow_meta.py</i>: Organizate cashflow statement data at <i>data_cshfsmt_meta.py</i> and generate sankey chart figure object.</li>
	<li><i>data_incsmt_meta.py</i>: Assign links metadata for the income statement sankey charts.</li>
	<li><i>data_balsht_meta.py</i>: Assign links metadata for the balance sheet sankey charts.</li>
	<li><i>data_cshfsmt_meta.py</i>: Assign links metadata for the cashflow statement sankey charts.</li>
</ul>

<br>
<i>data_incsmt_meta.py</i>, <i>data_balsht_meta.py</i>, <i>data_cshfsmt_meta.py</i> are the scripts that are responable on converting financial data to a format that is accepted by Plotly sankey chart package, ie, defining nodes and node links. The nodes name, position (index number) are predefined in <i>nodes_meta_incsmt.json</i>, <i>nodes_meta_balsht.json</i>, and <i>nodes_meta_cshfsmt.json</i>. The scripts will first map the data to those nodes and create links that will generate on the sankey chart. The idea is to provide detailed level data to the CSV file, the script will obtain the data and aggregate it for the high level metrics on the sankey chart. Below is the overview of the algorithm of the scripts.

### data_incsmt_meta.py
This script prepares the sankey chart of metae's income statement. The data preparer will provide data on Node 0, 4-9. The scirpt will first aggregate expense among Node 4-6, and aggregate EBIT at the end. Since Meta does not partition into income categories, the script will not aggregate revenue like other companies' script.

### data_balsht_meta.py
This script prepares the sankey chart of metae's balance sheet. The data preparer will provide data on Node 0-9, 15-23. The script will treat assets, liabilities, and equity into three blocks and aggregate the data in each block and link these blocks together at the end.

### data_cshfsmt_meta.py
This script prepares the sankey chart of metae's cashflow statement. The data preparer will provide data on Node 0-8, 18-22. The script will treat operating activities, financing activities, investment activities into three blocks and aggregate the data in each block and link these blocks together at the end.


## Reference
Meta's filing on SEC Edgar page - <a href="https://www.sec.gov/edgar/browse/?CIK=1326801&owner=exclude">link</a>
<br><br>
2023 10-k - <a href="https://www.sec.gov/Archives/edgar/data/1326801/000132680124000012/meta-20231231.htm">link</a>