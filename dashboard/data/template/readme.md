# Plug-in Templates and Script Explanations
Currently, the dashboard is only able display a list of selected companies because it is not able to handle the dynamics on the financial report formats among all publically traded companies. In order to add more companies, it is possible add more companies to the list by creating a plug-in. This folder contains the templates and instructions to create the plug-in. 

## How the Dashboard Scripts Work?
More details are coming soon...

## Instructions on Creating a New Plug-in
The general workflows of creating a plug-in that is integratable to the dashboarding scripts are:
<ol>
	<li>Create a folder under the <i>data</i> folder in the <i>dashboard</i> folder, name it with the ticker of the company in lower cases. Within the folder, create another folder named <i>dataset</i> in lower cases</li>
	<li>Develop definition files for the plug-in</li>
	<li>Prepare the sample data for the dashboard</li>
	<li>Draft sample scripts (hard-coded) to display sample dashboards for planning proof of concept purpose before developing the production scripts</li>
	<li>Develop and modify scripts to handle income statement data and chart</li>
	<li>Develop and modify scripts to handle balance sheet data and chart</li>
	<li>Develop and modify scripts to handle cashflow statement data and chart</li>
	<li>Integrate the scripts with the dashboard in the development environment</li>
	<li>Test the scripts after integrating with the dashboard</li>
	<li>Rollout to the production environment</li>
</ol>

<br><br>

### Step 1: Create a Folder for a Company to Initiate the Plug-in
Create a folder under the <i>data</i> folder in the <i>dashboard</i> folder, name it with the ticker of the company in lower cases. Within the folder, create another folder named <i>dataset</i> in lower cases. <b>Due to the dashboard scripts setup, please follow the letter cases stated in this instruction!</b> It is recommended to create a folder named <i>Images</i> for storing images for documentation. 
<br><br>
Here is the structure:

```
--dashboard
 |- data
 	|- (company)
 		|- data
 			|- dataset
 			|- Images
```

## Step 2: Develop definition files for the plug-in
Create 3 JSON files to define the Node index to map the financial reporting items, with the following formats: <i>nodes\_(company)\_incsmt.json</i>, <i>nodes\_(company)\_balsht.json</i>, and <i>nodes\_(company)\_cshfsmt.json</i>, and saved under the company folder.
<br><br>

The Node index represents the node position on building the sankey chart utilizing the Plotly package, and will be used in the scripts in the later steps. More detailed instructions are coming soon...
<br><br>
The definition files and scripts are expected to saves under company folder due to the dashboard scripts setup. And also <b>due to the dashboard scripts setup, please follow the letter cases stated in this instruction!</b>

<br><br>
Here is the structure:

```
--dashboard
 |- data
 	|- (company)
		|- dataset
		|- Images
		|- nodes_(company)_incsmt.json
		|- nodes_(company)_balsht.json
		|- nodes_(company)_cshfsmt.json
```

### Step 3: Prepare the Sample Data for the Dashboard
Copy <i>XXXX_income_template.csv</i>, <i>XXXX_income_example.csv</i>, <i>XXXX_balancesheet_template.csv</i>, <i>XXXX_balancesheet_example.csv</i>, <i>XXXX_cashflow_template.csv</i> and <i>XXXX_cashflow_example.csv</i> from this folder. Next, prepare the template files. Replace the <i>XXXX</i> with the <b>company ticker</b>.
<br><br>
Prepare the entries for all the template files: First, copy all the non-aggreated node names from the node definition files to the corresponding template CSV files. Aggregared nodes all the financial metrics on the financial reports that can be aggregated from its sub-metrics, such as Revenue, Total Expense, EBIT on the income statement, current asset, asset, liabilities, equity on the balance sheet, or operating activities, investing activities, or financing activities in the cashflow statement. Reference in the example section for a walkthrough example. All node names should be listed on its own line to represent one row of an entry. Also, place template inputs for the other granularities and metrics for each line, namely year and value. Here is the example of a balance sheet entry on a balance sheet template file:

```
"Items","Period","Value"
"Cash and cash equivalent","Year 1",0
```

<br><br>
After prepared the templates, copy all the template entries to the example files. First, go to the <a href="">SEC Edgar</a> and access a report (Either 10-K or 10-Q). Copy the data to the Period and Value entries. Note that for the current setting, follow the Period format on <b>FYXX</b> for annual reports, <b>XXHX</b> for interim/semi-annual reports and <b>XXQX</b> for quarterly reports. Here is the example of a balance sheet entry on a balance sheet example file:

```
"Items","Period","Value"
"Cash and cash equivalent","FY23",1000
```
<br><br>
In the current version, the dashboard will ingest data from the <i>\_example.csv</i> files but <b>the naming convention will be changed in the future versions</b>.

<br><br>
```
--dashboard
 |- data
 	|- (company)
		|- dataset
			|- XXXX_income_template.csv
			|- XXXX_balancesheet_template.csv
			|- XXXX_cashflow_template.csv
			|- XXXX_income_example.csv
			|- XXXX_balancesheet_example.csv
			|- XXXX_cashflow_example.csv
		|- Images
		|- nodes_(company)_incsmt.json
		|- nodes_(company)_balsht.json
		|- nodes_(company)_cshfsmt.json
```

### Step 4: Draft Sample Scripts to Display Sample Dashboards
Write the scripts to display sample dashboards for proof of concept. These scripts are okay to be hard-coded for this purpose. It is recommended to develop to visualize the dashboard for further development and planning. You may use the sample scripts and integrated with the dashboard in the development and/or testing environment.

### Step 5: Develop and modify scripts to handle income statement data and chart
Copy <i>data_incsmt_XXXX.py</i> to the company file. Keep all the supporting functions. And develop in the <i>get_data()</i> function.

<br><br>
First, declare the node color array <i>nodes_colors</i>. You may pre-set the colors and change the color along the scripts, or add placeholders and change the color along the scripts. Then, keep the part where the script ingest data in a Pandas format. After that, create the sankey chart links and change the node colours in three main sections - Revenue, Expense, and EBIT sections.
<br><br>
In each section, create the links between the input data from the <i>XXXX_income_example.csv</i> and the sub-section nodes first, then create links from the sub-section node and the section node (Revenue, Expense, EBIT). Since the the input data nodes ranked in the beginning and the end of the <i>nodes_XXXX_incsmt.json</i> file, for loops can be utilized to streamline the creation. And finally, be sure to handle the link direction and node color if the input is negative.
<br><br>
The Node color should be assigned to <b>Revenue - gray</b>, <b>Expense - red</b>, <b>Positive EBIT - green</b>, and <b>Negative EBIT - red</b>; any income stream should be <b>lightgreen</b>, while losses should be <b>lightpink</b>.

<br><br>
The comment section in the template script provides more instruction to follow, but also reference in the later Example section for a walkthrough.

### Step 6: Develop and modify scripts to handle balance sheet data and chart
Copy <i>data_balsht_XXXX.py</i> to the company file. Keep all the supporting functions. And develop in the <i>get_data()</i> function.

<br><br>
First, declare the node color array <i>nodes_colors</i>. You may pre-set the colors and change the color along the scripts. The Node colors are assigned to <b>Asset - green</b>, <b>Liabilities - red</b>, and <b>Equity - blue</b>, while node color should not be changed while displaying the records on a balance sheet. Then, keep the part where the script ingest data in a Pandas format. After that, create the sankey chart linksin three main sections - Asset, Liabilities, and Equity sections.
<br><br>
In each section, create the links between the input data from the <i>XXXX_balancesheet_example.csv</i> and the sub-section nodes first, then create links from the sub-section node, such as current asset or current liabilities, and the section node (Asset, Liabilities, Equity). Long-term asset or long-term liabilities are not required have their own nodes, but try to be consistent with the format on the financial reports. Since the the input data nodes ranked in the beginning and the end of the <i>nodes_XXXX_balsht.json</i> file, for loops can be utilized to streamline the creation. Balance sheet rarely report negative number, but sometimes you may find that at Depreciation under assets, or, more likely Retained Earning or Accumulated Earning. Be sure to handle the link direction and node color if the input is negative.
<br><br>
While creating links between nodes, utilize the <i>get_link_direction()</i> function to dynamically determine link direction, value, and color without hard-coding. Be sure to state the left node index, right node index, and <b>indicating ACCOUNT TYPE</b> (asset, liabilities, equity) to generate the right color.

### Step 7: Develop and modify scripts to handle cashflow statement data and chart
Copy <i>data_cshfsmt_XXXX.py</i> to the company file. Keep all the supporting functions. And develop in the <i>get_data()</i> function.

<br><br>
More details are coming soon...

<br><br>
```
--dashboard
 |- data
 	|- (company)
		|- dataset
			|- XXXX_income_template.csv
			|- XXXX_balancesheet_template.csv
			|- XXXX_cashflow_template.csv
			|- XXXX_income_example.csv
			|- XXXX_balancesheet_example.csv
			|- XXXX_cashflow_example.csv
		|- Images
		|- nodes_(company)_incsmt.json
		|- nodes_(company)_balsht.json
		|- nodes_(company)_cshfsmt.json
		|- data_incsmt_XXXX.py
		|- data_balsht_XXXX.py
		|- data_cshfsmt_XXXX.py
```


### Step 8: Integrate the scripts with the dashboard in the development environment
Once all the <i>data_</i> scripts are prepared and ready, update the dashboard scripts (<i>income_statement.py</i>, <i>balancesheet.py</i>, and <i>cashflow_statement.py</i>) to connect the dashboard scripts with the <i>data_</i> scripts. In those scripts, simply import the <i>data_</i> scripts in the dashboard scripts, and add the company ticker in the if-statement to allow the dashboard scripts to translate the data to the sankey chart setup.
<br><br>
Note that there is no need to update <i>dashboard.py</i> or <i>loaddata.py</i> as the backend has setup to ingest data for the <i>data_</i> scripts already.

### Step 9: Test the scripts after integrating with the dashboard
Test the scripts in the testing environment and fix any bug before rollout in the testing environment.

### Step 10: Rollout to the production environment
Once the plug-in is ready for the production environment, create a pull request and rollout to the production environment.

### The General Format on Scripts 
When writing scripts on preparing data for charting, the rule of thumb is to ingest lower granularity data (Node numbers are either in the beginning or at the end). More details are coming soon...


## Example - Creating a Plug-in for Google
More details are coming soon...