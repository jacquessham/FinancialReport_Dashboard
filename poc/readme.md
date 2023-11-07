# Proof of Concept
The goal is to replicate the sankey chart of Alphabet Inc (ticker: GOOGL) FY 2022 Income Statement with Plotly to produce a prototype visualization.

## Methology
### Income Statement
We would go to <a href="https://www.sec.gov/edgar/searchedgar/companysearch">SEC Edgar</a> to search for the Alphabet's 2022 10-K to obtain the income statement and the supplemental data. We will produce a sankey chart like this <a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">post</a> using Plotly and Python, while the data will be hardcoded in the script.

### Balance Sheet
In the same 10-K report, you may find the balance sheet. We will produce a sankey chart on balance sheet inspired from the last visualization using Plotly and Python, while the data will be hardcoded in the script.

### Cashflow Statement
Coming soon...

## Files
Here are the files used for the proof of concept:
<ul>
	<li>income_googl2022.py</li>
	<li>balancesheet_googl2002.py</li>
	<li>Coming soon...</li>
</ul>

## Result
### Income Statement
<img src=googl_income2022.png>

### Balance Sheet
<img src=googl_balance2022.png>

### Cashflow Statement
Coming soon...
