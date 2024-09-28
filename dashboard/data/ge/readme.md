# Data for GE
This folder contains all the supporting scripts, sample dataset, and dataset template required to display GE's (GE) financial data on the dashboard. You may find the instructions on how to prepare more data and the technical overviews of the supporting scripts found in this folder.

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
	<li>ge_income_template.csv</li>
	<li>ge_balancesheet_template.csv</li>
	<li>ge_cashflow_template.csv</li>
</ul>

## Data Prepartion
For the current version, data is expected to be added to the sample data CSV files (Files with name end with <b>\_example.csv</b>). Data preparers are expected to copy the format from the template files (Files with name end with <b>\_template.csv</b>), and copy the numbers from 10-K or 10-Q without changing the signs. All entries across all periods (No matter annual data or quarterly data) are saved under one file of its corresponding statement. Please do not separate the files into different period, the backend expects the period differentiate by the value under the <i>Period</i> column. For example, you may copy the format <i>ge_income_template</i>, less the header, from the file. Then, replace period value with the period you are providing. And lastly, enter the value from the source. Each row represents an entry of one of the statements from 10-K or 10-Q, however, there are some entries are combined. Please refer to the individual statement dataset section for detail. If you want to add the entries from another period, please copy the format, less the header, and append to the same dataset file.

### Income Statement Dataset
You may find all the cost expenses, EBIT, and net income values from the consolidated statement of income section of the report. Please copy and paste the number without changing the sign from the report, the script will take care of the signs. If the number is not available on the consolidated statement, put 0 to that item, and <b>DO NOT OMIT THE ITEM</b>.

### Balance Sheet Dataset
You may find all the entries in the consoldiated balance sheet. Please copy and paste the number without chaning the sign from the report. The only entries required summation is <i>Retained Earning</i>, please sum <i>Retained Earning</i>,<i>Less common stock held in treasury</i>, and <i>Accumulated other comprehensive income (loss) - net attributable to GE</i>.

<br><br>
<img src=Images/ge_balsht_cal_explain.png>

### Cash Flow Statement Dataset
You may find all the entries in the consoldiated cashflow statement, except the entries. Please aggregate with the following instruction:
<ul>
	<li>Operating Activities:<ul>
		<li>Pension Activities - Summation of <i>Principal pension plans cost</i>, <i>Principal pension plans employer contributions</i>, and <i>Other postretirement benefit plans</i></li>
		<li>Income Taxes Activities - Summation of <i>Provision (benefit) for Income Taxes</i> and <i>Cash recovered (paid) during the year for income taxes</i></li>
		<li>Change in operating working capital - Summation of all subitems under the <i>Changes in operating working capital</i> entry</li>
	</ul></li>
	<li>Investing Activities:<ul>
		<li>Capital Expenditure, net - Summation of <i>Additions to property, plant and equipment and internal-use software</i> and <i>Dispositions of property, plant and equipment</i></li>
		<li>Principal Businesses Purchased, net - Summation of <i>Net cash from (payment for) principal businesses purchased</i> and <i>Dispositions of retained ownership interests</i></li>
	</ul></li>
	<li>Financing Activities:<ul>
		<li>Debt Activities - Summation of <i>Net increase (decrease) in borrowings (maturities of 90 days or less)</i>, <i>Newly issued debt (maturities longer than 90 days)</i>, <i>Repayments and other debt reductions (maturities longer than 90 days)</i>, and <i>Cash received (paid) for debt extinguishment costs</i></li>
	</ul></li>
</ul>

<br><br>
Please copy and paste the number without changing the sign from the report, the script will take care of the signs. If the number is not available on the consolidated statement, put 0 to that item, and <b>DO NOT OMIT THE ITEM</b>.

<img src=Images/ge_cshfsht_cal1_explain.png>
<img src=Images/ge_cshfsht_cal2_explain.png>
<img src=Images/ge_cshfsht_cal3_explain.png>

## Nodes Explained
In the Plotly sankey chart package, nodes represents a categorical entry while the links represents the value between the nodes. The nodes in this setting are generally represents the positions of the charts from left to right. It is designed in way to make scripts creation and modification clear, and especially to emphasize the hierarchy among nodes and have user's input data on either furthest left or furthest right of the chart.

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_ge_incsmt.json</i>, <i>nodes_ge_balsht.json</i>, and <i>nodes_ge_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. Data prepare will not need to interact these files. In the coming subsections will provide the visualization of the nodes definitions of the corresponding sankey chart structures.

### Income Statment
The definitions of nodes used for GEe's income statement sankey charts can be found in <i>nodes_ge_incsmt.json</i>, and here is the visualization of the node relation.
<br><br>
<img src=Images/ge_incsmt_sankey.png>

### Balance Sheet
The definitions of nodes used for GEe's balance sheet sankey charts can be found in <i>nodes_ge_balsht.json</i>, and here is the visualization of the node relation.
<br><br>
<img src=Images/ge_bal_sankey.png>


### Cash Flow Statement
The definitions of nodes used for GEe's cashflow statement sankey charts can be found in <i>nodes_ge_cshfsmt.json</i>, and here is the visualization of the node relation.
<br><br>
<img src=Images/ge_cshfsmt_sankey.png>


## Scripts
Here are the scripts utilized by <i>dashboard.py</i>:
<ul>
	<li><i>income_ge.py</i>: Organizate income statement data at <i>data_incsmt_ge.py</i> and generate sankey chart figure object.</li>
	<li><i>balance_sheet_ge.py</i>: Organizate balance sheet data at <i>data_balsht_ge.py</i> and generate sankey chart figure object.</li>
	<li><i>cashflow_ge.py</i>: Organizate cashflow statement data at <i>data_cshfsmt_ge.py</i> and generate sankey chart figure object.</li>
	<li><i>data_incsmt_ge.py</i>: Assign links metadata for the income statement sankey charts.</li>
	<li><i>data_balsht_ge.py</i>: Assign links metadata for the balance sheet sankey charts.</li>
	<li><i>data_cshfsmt_ge.py</i>: Assign links metadata for the cashflow statement sankey charts.</li>
</ul>

<br>
<i>data_incsmt_ge.py</i>, <i>data_balsht_ge.py</i>, <i>data_cshfsmt_ge.py</i> are the scripts that are responable on converting financial data to a format that is accepted by Plotly sankey chart package, ie, defining nodes and node links. The nodes name, position (index number) are predefined in <i>nodes_ge_incsmt.json</i>, <i>nodes_ge_balsht.json</i>, and <i>nodes_ge_cshfsmt.json</i>. The scripts will first map the data to those nodes and create links that will generate on the sankey chart. The idea is to provide detailed level data to the CSV file, the script will obtain the data and aggregate it for the high level metrics on the sankey chart. Below is the overview of the algorithm of the scripts.

### data_incsmt_ge.py
This script prepares the sankey chart of GE's income statement. The data preparer will provide data on Node 0-12. The scirpt will first aggregate revenue among Node 0-3, then expense among Node 3-11, and aggregate income from operation and EBIT at the end.

### data_balsht_ge.py
This script prepares the sankey chart of GE's balance sheet. The data preparer will provide data on Node 0-14, 20-34. The script will treat assets, liabilities, and equity into three blocks and aggregate the data in each block and link these blocks together at the end.

### data_cshfsmt_ge.py
This script prepares the sankey chart of GE's cashflow statement. The data preparer will provide data on Node 0-12, 21-33. The script will treat operating activities, financing activities, investment activities into three blocks and aggregate the data in each block and link these blocks together at the end.


## Reference
GE's filing on SEC Edgar page - <a href="https://www.sec.gov/edgar/browse/?CIK=40545&owner=exclude">link</a>
<br><br>
2023 10-K - <a href="https://www.sec.gov/Archives/edgar/data/40545/000004054524000027/ge-20231231.htm">link</a>