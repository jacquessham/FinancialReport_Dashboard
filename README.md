# Financial Report Dashboard
Inspired from the sankey chart found in this <a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">post</a> on Reddit, the goal is to develop a dashboard to display similar visualization for other companies on income statement, balance sheet, and cash flow statement. This project is aimed to visualize financial reports with sankey charts along with other useful visualizations that helps users to conduct fundamental analysis on publicly traded company.
<br><br>
Currently, the dashboard is still under development <b>v0.1.2</b> (Beta).


## Dashboard
The Dashboard is in a matured state and allow users to select Google (GOOGL), Meta (META), Apple (AAPL), Bank of America (BAC), General Electrics (GE), and Nvidia (NVDA) on selected period of data. You may check out the progress in the [Dashboard](dashboard) folder. You may run the dashboard by execute the following code in the command line:

```
python dashboard/dashboard.py
```

<br>
Then, go to <b>127.0.0.1</b> (localhost) to access the dashboard.
<br><br>
<b>Note: the <i>dashboard.py</i> locates at the <i>dashboard</i> folder, not the current directory</b>


<br>
<img src=gallery/income_v004.png>
<img src=gallery/balance_v004.png>
<img src=gallery/cashflow_v004.png>

Screenshots of latest development.

## Project Plan
### Future Plans
Here are the features will be added before Official Launch:
<ul>
	<li>Feature to ingest data from administrator and ensure data quality</li>
	<li>Add Nvidia (NVDA) to the dashboard</li>
	<li>Docker Configuration</li>
</ul>

<br>
Here is the list of features in consideration after launched, but not committed:
<ul>
	<li>Allow dashboard to obtain data directly from SEC Edgar site</li>
</ul>

### Proof of Concept (Historical Record)
Before the development phase, the first step is to replicate the sankey chart found in this <a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">post</a> to look at the visualization rendered by Plotly and Python before building the framework of the Dashboard. You may find more details on the previous works in the [Proof of Concept](/poc) folder and at this <a href="https://medium.com/gitconnected/using-sankey-chart-for-financial-reports-40e5443f394c">Medium post</a> on how to generate sankey chart with Plotly.
<br><br>
You may find the details on the development plans in the [The Plan](plan) folder after confirmed in the Proof of Concept phase.

## Reference
<a href="https://www.reddit.com/r/dataisbeautiful/comments/10ur1ya/oc_how_google_makes_money_its_2022_income/">Google Financial Report in Sankey Chart</a>
<br><br>
<a href="https://www.sec.gov/edgar/searchedgar/companysearch">SEC Edgar (To access 10-Qs and 10-Ks)</a>
<br><br>
<a href="https://www.sec.gov/Archives/edgar/data/1652044/000165204423000016/goog-20221231.htm">Alphabet Inc FY 2022 10-K</a>