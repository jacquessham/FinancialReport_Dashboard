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

<br><br>
More details are coming soon...

## Data Prepartion
Coming soon...


## Nodes Explained
Coming soon...

### Nodes Definitions
The nodes used in the sankey charts are defined in the json files - <i>nodes_googl_incsmt.json</i>, <i>nodes_googl_balsht.json</i>, and <i>nodes_googl_cshfsmt.json</i>, respective to income statement, balance sheet, cashflow statement. The definitions are responsible to map the datasets to the node definitions. More instructions will be coming soon...

### Income Statment
The definitions of nodes used for Google's income statement sankey charts can be found in <i>nodes_googl_incsmt.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/googl_incsmt_sankey.png>
<img src=Images/googl_incsmt_example.png>

### Balance Sheet
The definitions of nodes used for Google's balance sheet sankey charts can be found in <i>nodes_googl_balsht.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/googl_bal_sankey.png>

<br>
<b>Note</b>: We noticed that <i>Intangible Assets, net</i> has been stopped reporting in the FY23 10-K and onward. It is okay to leave the value to be 0, or omit the whole entry. In the sample dataset, such entry is omitted for FY23 and onward.

### Cash Flow Statement
The definitions of nodes used for Google's cashflow statement sankey charts can be found in <i>nodes_googl_cshfsmt.json</i>, and here is the visualization of the node relation.
<br>

<img src=Images/googl_cshfsmt_sankey.png>
<img src=Images/googl_cshfsmt_cal1_explain.png>

## Scripts
More instructions are coming soon...<br>
Here are the scripts used:

<ul>
	<li><i>income_googl.py</i>: Organizate income statement data at <i>data_incsmt_googl.py</i> and generate sankey chart figure object.</li>
	<li><i>balance_sheet_googl.py</i>: Organizate balance sheet data at <i>data_balsht_googl.py</i> and generate sankey chart figure object.</li>
	<li><i>cashflow_googl.py</i>: Organizate cashflow statement data at <i>data_cshfsmt_googl.py</i> and generate sankey chart figure object.</li>
	<li><i>data_incsmt_googl.py</i>: Assign links metadata for the income statement sankey charts.</li>
	<li><i>data_balsht_googl.py</i>: Assign links metadata for the balance sheet sankey charts.</li>
	<li><i>data_cshfsmt_googl.py</i>: Assign links metadata for the cashflow statement sankey charts.</li>
</ul>



## Reference
2022 10-K - <a href="https://www.sec.gov/ix?doc=/Archives/edgar/data/0001652044/000165204423000016/goog-20221231.htm">link</a>