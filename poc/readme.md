# Proof of Concept
The goal is to replicate the sankey chart of Alphabet Inc (ticker: GOOGL) FY 2022 Income Statement with Plotly to produce a prototype visualization.

## Methology
### Income Statement
We would go to <a href="https://www.sec.gov/edgar/searchedgar/companysearch">SEC Edgar</a> to search for the Alphabet's 2022 10-K to obtain the income statement and the supplemental data. We will produce a sankey chart like this <a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">post</a> using Plotly and Python, while the data will be hardcoded in the script.

### Balance Sheet
In the same 10-K report, you may find the balance sheet. We will produce a sankey chart on balance sheet inspired from the last visualization using Plotly and Python, while the data will be hardcoded in the script.

### Cashflow Statement
In the same 10-K report, you may find the balance sheet. We will produce a sankey chart on balance sheet inspired from a sankey chart like this <a href="https://www.appeconomyinsights.com/p/how-to-analyze-a-cash-flow-statement">post</a> using Plotly and Python, while the data will be hardcoded in the script.

## Files
Here are the files used for the proof of concept:
<ul>
	<li>income_googl2022.py</li>
	<li>balancesheet_googl2022.py</li>
	<li>cashflow_googl2022_v1.py</li>
	<li>cashflow_googl2022_v2.py</li>
</ul>

## Result
### Income Statement
<img src=googl_income2022.png>

### Balance Sheet
<img src=googl_balance2022.png>

### Cashflow Statement
<img src=googl_cashflow2022_v1.png>

<br>
Version 1 rendered by <i>cashflow_googl2022_v1.py</i>
<br><br>

<img src=googl_cashflow2022_v2.png>
Version 2 rendered by <i>cashflow_googl2022_v2.py</i>
