# The Plan
The plan is to develop a dashboard displays the financials of selected publicly traded companies. 

## The Idea
The goal is to allow user to use the publicly disclosed data and upload to the dashboard to display the financials (Income Statement and Balance Sheet, maybe Cashflow Statement). In the early version, the plan is to have user to obtain data from either 10-Q or 10-K and save into CSVs or Excel spreadsheets upload to the dashboard and display the analysis. The dashboard will be rendered by Plotly and Dash using Python and be hosted in Docker. Since the project is inspired by the sankey chart displaying Google FY 2022 Income statement, we will be primarily visualizing income statement and balance sheet using sankey charts. Therefore, the visualizations are planned to be manually set up for each company. 
<br><br>
As mentioned, the data is expected to be obtained from 10-Qs and 10-Ks, there is no plan to integrated with Bloomberg terminal or other paying platforms.


## Beta
Beta version would allow user to upload data via CSVs. Only display the following selected publicly:
<ul>
	<li>Google (GOOGL)</li>
	<li>Apple (AAPL)</li>
	<li>Meta (FB)</li>
	<li>General Electric (GE)</li>
	<li>Bank of America (BAC)</li>
</ul>

<br>
The dashboard is planned hosted in Docker in Beta version.

## Version 1
Version 1 will allow user to upload either CSV or Excel spreadsheet, and allow developer to set up new company visualizations in the dashboard application.


## Version 2 (If Process)
The idea of next steps are
<ul>
	<li>Add cashflow statement visualization to the dashboard</li>
	<li>Allow dashboard to obtain data directly from SEC Edgar site</li>
</ul>

<br>
The plan for version 2 is subjected to change or cancel.
