# Data for Google
This folder contains all the supporting scripts, sample dataset, and dataset template required to display Google's (GOOGL) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

## Sample Dataset and Template
The sample dataset and dataset template files are available in the [Dataset](dataset) folder. 
<br><br>
Current, the sample dataset consists of:
<ul>
	<li>Income Statement:<ul>
		<li>23Q3</li>
		<li>FY22</li>
		<li>FY21</li>
		</ul>
	</li>
	<li>Balance Sheet:<ul>
		<li>FY23</li>
		<li>23Q2</li>
		<li>FY22</li>
		</ul>
	</li>
	<li>Income Statement:<ul>
		<li>FY23</li>
		<li>23Q3</li>
		<li>FY22</li>
		</ul>
	</li>
</ul>

<br>
Here are the templates:
<ul>
	<li>googl_income_template.csv</li>
	<li>googl_balancesheet_template.csv</li>
	<li>googl_cashflow_template.csv</li>
</ul>

## Data Prepartion
For the current version, data is expected to be added to the sample data CSV files (Files with name end with <b>\_example.csv</b>). Data preparers are expected to copy the format from the template files (Files with name end with <b>\_template.csv</b>), and copy the numbers from 10-K or 10-Q without changing the signs. All entries across all periods (No matter annual data or quarterly data) are saved under one file of its corresponding statement. Please do not separate the files into different period, the backend expects the period differentiate by the value under the <i>Period</i> column. For example, you may copy the format <i>googl_income_template</i>, less the header, from the file. Then, replace period value with the period you are providing. And lastly, enter the value from the source. Each row represents an entry of one of the statements from 10-K or 10-Q, however, there are some entries are combined. Please refer to the individual statement dataset section for detail. If you want to add the entries from another period, please copy the format, less the header, and append to the same dataset file.

### Income Statement Dataset
You may find all the cost expenses, EBIT, and net income values from the consolidated statement of income section of the report. The segmented income value maybe obtained from the supplemental section (Disaggregated Revenues under the Revenue sections) after the consolidated statement sections. No field is combined in this visualization setup.

<img src=Images/googl_disagg_income.png>

### Balance Sheet Dataset
You may find all balance sheet entries, except the <i>Other Long-term Liabilities</i> column, and Retained earning from the consolidated balance sheets section. All assets and liabilities values may be retreived from the balance and directly copy the value to the dataset. 
<br><br>
There are 2 entries required summing their dependent columns:
<ul>
	<li>Other Long-term Liabilities (Node 25): Sum of Income Taxes Payable, non-current, Deferred Income Taxes, non-current, and Other Long-term Liabilities</li>
	<li>Common Stocks (Node 27): Sum of Preferred Stock, all classes shares issued and outstanding, and Accumulated other comprehensive income</li>
</ul>

<br>
Here are visual explaination:

<img src=Images/googl_balsht_cal1_explain.png>
<br>
<b>Note</b>: We noticed that <i>Intangible Assets, net</i> has been stopped reporting in the FY23 10-K and onward. It is okay to leave the value to be 0, or omit the whole entry. In the sample dataset, such entry is omitted for FY23 and onward.

### Cash Flow Statement Dataset
You may find all values required by the cash flow statement in the consolidated statements of cash flow section. Please copy the data without changing the signs for all values.
<br><br>
There are 5 entries required summing their dependent columns or name change:
<ul>
	<li>Change in Assets and Liailities, net of effects of Acquisitions (Node 7): They are sum of:
		<ul>
			<li>Accounts Receivable, net</li>
			<li>Income Taxes, net</li>
			<li>Other assets</li>
			<li>Account Payable, net</li>
			<li>Accrued expense and other liabilities</li>
			<li>Deferred Revenue</li>
		</ul>
	</li>
	<li>Capital Expenditure (Node 13): Purchase of Property and Equipment</li>
	<li>Securities Investment (Node 14): Sum of Purchases of marketable securities, Maturities of securities, Purchase of non-marketable securities, and Maturities of non-marketable securities</li>
	<li>Repurchase of Stock and Stock-based Award Activities (Node 17): Sum of Net Payment to award activities, and Purchase of stock</li>
	<li>Debt-related Activities (Node 18): Sum of Net Payment to award activities, and Repurchase of stock</li>
</ul>

<br>
Here are visual explaination:

<img src=Images/googl_cshfsmt_cal1_explain.png>
<img src=Images/googl_cshfsmt_cal2_explain.png>



## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_googl_incsmt.json</i>, <i>nodes_googl_balsht.json</i>, and <i>nodes_googl_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
The definitions of nodes used for Google's income statement sankey charts can be found in <i>nodes_googl_incsmt.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/googl_incsmt_sankey.png>

### Balance Sheet
The definitions of nodes used for Google's balance sheet sankey charts can be found in <i>nodes_googl_balsht.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/googl_bal_sankey.png>


### Cash Flow Statement
The definitions of nodes used for Google's cashflow statement sankey charts can be found in <i>nodes_googl_cshfsmt.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/googl_cshfsmt_sankey.png>


## Scripts
Here are the scripts utilized by <i>dashboard.py</i>:
<ul>
	<li><i>income_googl.py</i>: Organizate income statement data at <i>data_incsmt_googl.py</i> and generate sankey chart figure object.</li>
	<li><i>balance_sheet_googl.py</i>: Organizate balance sheet data at <i>data_balsht_googl.py</i> and generate sankey chart figure object.</li>
	<li><i>cashflow_googl.py</i>: Organizate cashflow statement data at <i>data_cshfsmt_googl.py</i> and generate sankey chart figure object.</li>
	<li><i>data_incsmt_googl.py</i>: Assign links metadata for the income statement sankey charts.</li>
	<li><i>data_balsht_googl.py</i>: Assign links metadata for the balance sheet sankey charts.</li>
	<li><i>data_cshfsmt_googl.py</i>: Assign links metadata for the cashflow statement sankey charts.</li>
</ul>

<br><br>
More explantations on nodes aggregations are coming soon...<br>


## Reference
2022 10-K - <a href="https://www.sec.gov/ix?doc=/Archives/edgar/data/0001652044/000165204423000016/goog-20221231.htm">link</a>