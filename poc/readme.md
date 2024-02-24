# Proof of Concept
The Financial Report Dashboard is inspired by this <a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">post</a> displaying the 2022 Income Statement of Alphabet Inc (ticker: GOOGL), aka Google, on Reddit. It would be great if one could view all the consolidated statements in one dashboard for selected companies. Before implement the dashboard, we shall prove that it is possible. The goal of the proof of concept phase is to replicate the sankey chart of Alphabet Inc (ticker: GOOGL) FY 2022 Income Statement, Balance Sheet, and Cashflow Statment with Plotly to produce a prototype visualization.
<br><br>
This <a href=>Medium post</a> also explains this proof of concept.


## Why Sankey Chart?
Sankey chart is a great visualization to show the flow and movement. In the nature of financial report, the logic of different metrics are interconnected with a flow. For example, the income statement shows how revenue is realized and subtract different expense to yield the final net income. In this process, we can see how revenue is proportionally taken away in each step, which is very similar to a flow, until the end. Therefore, it is very useful and clean to display the report in visual.

## Methology
We would generate 3 different sankey diagrams on income statement, balance sheet, and cashflow statement of GOOGL. First, We would go to <a href="https://www.sec.gov/edgar/searchedgar/companysearch">SEC Edgar</a> to search for the Alphabet's 2022 10-K to obtain the income statement and the supplemental data. Then, we will generate the Sankey charts with Plotly and Python.

### Income Statement
Using the 10-K, we will produce a sankey chart like this <a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">post</a> using Plotly and Python, while the data will be hardcoded in the script. The script that generates the income statement is <i>income_googl2022.py</i>.

### Balance Sheet
In the same 10-K report, you may find the balance sheet. We will produce a sankey chart on balance sheet inspired from the last visualization using Plotly and Python, while the data will be hardcoded in the script. The script that generates the income statement is <i>balancesheet_googl2022.py</i>.

### Cashflow Statement
In the same 10-K report, you may find the balance sheet. We will produce a sankey chart on balance sheet inspired from a sankey chart like this <a href="https://www.appeconomyinsights.com/p/how-to-analyze-a-cash-flow-statement">post</a> using Plotly and Python, while the data will be hardcoded in the script.  The script that generates the income statement are <i>cashflow_googl2022_v1.py</i> and <i>cashflow_googl2022_v2.py</i>.

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
