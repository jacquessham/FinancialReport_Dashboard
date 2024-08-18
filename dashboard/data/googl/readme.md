# Data for Google
Coming soon...

## Sample Dataset and Template
The sample dataset and dataset template files are available in the [Dataset](dataset) folder. More details are coming soon...

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