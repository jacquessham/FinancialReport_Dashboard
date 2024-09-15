# Data for Bank of America
This folder contains all the supporting scripts, sample dataset, and dataset template required to display Bank of America's (BAC) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

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
	<li>bac_income_template.csv</li>
	<li>bac_balancesheet_template.csv</li>
	<li>bac_cashflow_template.csv</li>
</ul>

## Data Prepartion
For the current version, data is expected to be added to the sample data CSV files (Files with name end with <b>\_example.csv</b>). Data preparers are expected to copy the format from the template files (Files with name end with <b>\_template.csv</b>), and copy the numbers from 10-K or 10-Q without changing the signs. All entries across all periods (No matter annual data or quarterly data) are saved under one file of its corresponding statement. Please do not separate the files into different period, the backend expects the period differentiate by the value under the <i>Period</i> column. For example, you may copy the format <i>bac_income_template</i>, less the header, from the file. Then, replace period value with the period you are providing. And lastly, enter the value from the source. Each row represents an entry of one of the statements from 10-K or 10-Q, however, there are some entries are combined. Please refer to the individual statement dataset section for detail. If you want to add the entries from another period, please copy the format, less the header, and append to the same dataset file.


### Income Statement Dataset
You may find all the non-interest income, all expense, EBIT, and net income values from the consolidated statement of income section of the report. The segmented interest-income value maybe obtained from the supplemental section (Note 2 - Net Interest Income and Noninterest Income) after the consolidated statement sections. No field is combined in this visualization setup. Simply copy the number from the income statement without changing the sign of the number.

### Balance Sheet Dataset
You may find all balance sheet entries, except the <i>Retained earning</i> from the consolidated balance sheets section. All assets and liabilities values may be retreived from the balance and directly copy the value to the dataset. 
<br><br>
Note:
<ul>
	<li>Debt Securities (Node 6) - Copy the number from <i>Total Debt Securities</i> under Assets</li>
	<li>Loans and Leases, net (Node 7) - Copy the number from <i>Loans and Leases, net of allowance</i></li>
	<li>Retained Earning (Node 32) - Sum of Retained Earning and Accumulated other comprehensive income(loss) under the Shareholders' equity section</li>
</ul>

<img src=Images/bac_balsht_cal1_explain.png>

### Cash Flow Statement Dataset
You may find all values required by the cash flow statement in the consolidated statements of cash flow section. Please copy the data without changing the signs for all values.
<br><br>
There are 8 entries required summing their dependent columns or name change:
<ul>
	<li>Loans Held-for-sales (Node 7) - Sum of <i>Originations and Purchases</i> and <i>Proceeds from sales and paydowns of loans originally classified as held for sale and instruments</i> under the <i>Loans Held-for-sales</i>item under Operating Activities</li>
	<li>All Investing Activities, includes the following, except the <i>Other Investing Activities, net</i>. For all the following items, sum all its sub-tems, and input on the CSV file:<ul>
		<li>Net Change in Deposits, Short-term Borrowing, and Federal Funds under Agreement to Resell (Node 17)</li>
		<li>Debt Securities Carried at Fair Value (Node 18)</li>
		<li>Held-for-maturity Debt Securities (Node 19)</li>
		<li>Loans and Leases (Node 20)</li>
	</ul></li>
	<li>The following Financing Activities. For all the following items, sum all its sub-tems, and input on the CSV file: <ul>
		<li>Net Change in Deposits, Short-term Borrowing, and Federal Funds under Agreement to Repurchase (Node 22)</li>
		<li>Long-term Debt Activities (Node 23)</li>
		<li>Preferred Stock Activities (Node 24)</li>
	</ul></li>
</ul>


<img src=Images/bac_cshfsmt_cal1_explain.png>
<img src=Images/bac_cshfsmt_cal2_explain.png>
<img src=Images/bac_cshfsmt_cal3_explain.png>


## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_bac_incsmt.json</i>, <i>nodes_bac_balsht.json</i>, and <i>nodes_bac_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
The definitions of nodes used for Bank of America's income statement sankey charts can be found in <i>nodes_bac_incsmt.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/bac_incsmt_sankey.png>

### Balance Sheet
The definitions of nodes used for Bank of America's balance sheet sankey charts can be found in <i>nodes_bac_balsht.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/bac_bal_sankey.png>


### Cash Flow Statement
The definitions of nodes used for Bank of America's cashflow statement sankey charts can be found in <i>nodes_bac_cshfsmt.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/bac_cshfsmt_sankey.png>

## Scripts
Here are the scripts utilized by <i>dashboard.py</i>:
<ul>
	<li><i>income_bac.py</i>: Organizate income statement data at <i>data_incsmt_bac.py</i> and generate sankey chart figure object.</li>
	<li><i>balance_sheet_bac.py</i>: Organizate balance sheet data at <i>data_balsht_bac.py</i> and generate sankey chart figure object.</li>
	<li><i>cashflow_bac.py</i>: Organizate cashflow statement data at <i>data_cshfsmt_bac.py</i> and generate sankey chart figure object.</li>
	<li><i>data_incsmt_bac.py</i>: Assign links metadata for the income statement sankey charts.</li>
	<li><i>data_balsht_bac.py</i>: Assign links metadata for the balance sheet sankey charts.</li>
	<li><i>data_cshfsmt_bac.py</i>: Assign links metadata for the cashflow statement sankey charts.</li>
</ul>

<br>
<i>data_incsmt_bac.py</i>, <i>data_balsht_bac.py</i>, <i>data_cshfsmt_bac.py</i> are the scripts that are responable on converting financial data to a format that is accepted by Plotly sankey chart package, ie, defining nodes and node links. The nodes name, position (index number) are predefined in <i>nodes_bac_incsmt.json</i>, <i>nodes_bac_balsht.json</i>, and <i>nodes_bac_cshfsmt.json</i>. The scripts will first map the data to those nodes and create links that will generate on the sankey chart. The idea is to provide detailed level data to the CSV file, the script will obtain the data and aggregate it for the high level metrics on the sankey chart. Below is the overview of the algorithm of the scripts.

### data_incsmt_bac.py
This script prepares the sankey chart of bace's income statement. The data preparer will provide data on Node 0-11, 16-26. The script first calculate the net change in interest income (aggregated interest income minus aggregated interest expense), then aggregate non-interest income, itemized expenses, and finally EBIT and net income.

### data_balsht_bac.py
This script prepares the sankey chart of bace's balance sheet. The data preparer will provide data on Node 0-12, 20-32. The script will treat assets, liabilities, and equity into three blocks and aggregate the data in each block and link these blocks together at the end.

### data_cshfsmt_bac.py
This script prepares the sankey chart of bace's cashflow statement. The data preparer will provide data on Node 0-11, 20-32. The script will treat operating activities, financing activities, investment activities into three blocks and aggregate the data in each block and link these blocks together at the end.


## Reference
BAC's filing on SEC Edgar page - <a href="https://www.sec.gov/edgar/browse/?CIK=70858&owner=exclude">link</a>
<br><br>
2023 10-K - <a href="https://www.sec.gov/Archives/edgar/data/70858/000007085824000122/bac-20231231.htm">link</a>