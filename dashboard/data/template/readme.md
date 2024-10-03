# Plug-in Templates and Script Explanations
Currently, the dashboard is only able display a list of selected companies because it is not able to handle the dynamics on the financial report formats among all publically traded companies. In order to add more companies, it is possible add more companies to the list by creating a plug-in. This folder contains the templates and instructions to create the plug-in. 

## How the Dashboard Scripts Work?
All the scripts are saved under the <i>dashboard</i> folder, which is the root folder of the dashboard. The dashboard driver script is <i>dashboard.py</i> where it defines the dashboard setup and interactions. When <i>dashboard.py</i> is executed, it loads all the data through <i>loaddata.py</i> in the <i>data</i> folder and saved in the <i>company_data</i> in a dictionary, and render the dashboard frontend via the definitons according to <i>data_structure.py</i>.
<br><br>
When the user intereacts with dashboard or render based on default setting, it will render the visualizations through one of these scripts, <i>income_statement.py</i>, <i>balancesheet.py</i>, and <i>cashflow_statement.py</i>, corresponding to the tab selection among income statement, balance sheet, or cashflow statement of the selcted company at the selected period. Each respective script will convert the data in <i>company_data</i> to the format accepted by Plotly through <i>data_incsmt_XXXX.py</i>, <i>data_balsht_XXXX.py</i>, or <i>data_cshfsmt_XXXX.py</i>, respective to its reporting.
<br><br>

Here is the visualization of the scripts relationship:
<img src=dashboard_structure.png>

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
On the Github side, create a new branch based on the <i>development</i> branch first. Create a folder under the <i>data</i> folder in the <i>dashboard</i> folder, name it with the ticker of the company in lower cases. Within the folder, create another folder named <i>dataset</i> in lower cases. <b>Due to the dashboard scripts setup, please follow the letter cases stated in this instruction!</b> It is recommended to create a folder named <i>Images</i> for storing images for documentation. 
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

The Node index represents the node position on building the sankey chart utilizing the Plotly package, and will be used in the scripts in the later steps. The Sankey Chart on the financial reports happens to have all input data to be plotted at the furthest left and furthest right of the chart, that is the observation after the conducting the Proof of Concept. Therefore, it is wise to set the index for all input data to be beginning of the indexes and the ending of the indexes, and leave all the aggregated metrics to be the median of the index numbers. For example, if we are going to assign the nodes on a company's balance sheet sankey chart, assign all asset account data from 0 to the available current and long-term asset, while assign the numbers from total number of nodes lessthe available current and long-term liabilities and equity to the total number of nodes. Here is the visual explanation:
<img src=step2_ex.png>

<br>
Given the company has 3 inputs on current assets, 1 input on long-term asset, 2 inputs on current liabilities, 1 input on long-term liability, 2 inputs on Equity. To assign the node index, I assign 0-3 for all inputs on asset, then assign sub-category on asset (current asset and long-term asset), then Asset. After that, assign the sub-category on liabilities and equity (if reported on the balance sheet), and finally all inputs on liabilities and quity. Therefore, all liabilities input are 9-13.
<br><br>
Using this indexing method will allow a more easier and systematically logics when developing the <i>data_</i> scripts in the later steps. 

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

<br><br>
<b>Tips</b>: When writing scripts on preparing data for charting, the rule of thumb is to ingest lower granularity data. Whatever the smaller entries, it should be indexed to be lowest or highest in the node definition. Whatever the aggregated entries should be indexed in the relative closed to the median indexes.


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
First, declare the node color array <i>nodes_colors</i>. You may pre-set the colors and change the color along the scripts. The Node colors are assigned to <b>Asset - green</b>, <b>Liabilities - red</b>, and <b>Equity - blue</b>, while node color should not be changed while displaying the records on a balance sheet. Then, keep the part where the script ingest data in a Pandas format. After that, create the sankey chart links in three main sections - Asset, Liabilities, and Equity sections.
<br><br>
In each section, create the links between the input data from the <i>XXXX_balancesheet_example.csv</i> and the sub-section nodes first, then create links from the sub-section node, such as current asset or current liabilities, and the section node (Asset, Liabilities, Equity). Long-term asset or long-term liabilities are not required have their own nodes, but try to be consistent with the format on the financial reports. Since the the input data nodes ranked in the beginning and the end of the <i>nodes_XXXX_balsht.json</i> file, for loops can be utilized to streamline the creation. Balance sheet rarely report negative number, but sometimes you may find that at Depreciation under assets, or, more likely Retained Earning or Accumulated Earning. Be sure to handle the link direction and node color if the input is negative.
<br><br>
While creating links between nodes, utilize the <i>get_link_direction()</i> function to dynamically determine link direction, value, and color without hard-coding. Be sure to state the left node index, right node index, and <b>indicating ACCOUNT TYPE</b> (asset, liabilities, equity) to generate the right color.

### Step 7: Develop and modify scripts to handle cashflow statement data and chart
Copy <i>data_cshfsmt_XXXX.py</i> to the company file. Keep all the supporting functions. And develop in the <i>get_data()</i> function.

<br><br>
First, declare the node color array <i>nodes_colors</i>. Add the colors for a placeholders, but the node color will be switch to green or red when creating the node links. After that, create the sankey chart links in three main sections - Operating Activities, Investment Activities, and Financing Activities, follow by supplement links, such as effect of exchange of rate, and finished with the link of Net Increase in Cash.

<br><br>
In each section, create the links between the input data from the <i>XXXX_cashflow_example.csv</i> and the sub-section nodes first, then create links from the sub-section node, such as non-cash operation under Operating Activities, and the section node (3 major activities). Try to be consistent with the format on the financial reports. Since the the input data nodes ranked in the beginning and the end of the <i>nodes_XXXX_cshfsmt.json</i> file, for loops can be utilized to streamline the creation. Cashflow statement may report both positive or negative number, use <i>get_link_direction</i> to handle the link direction and node color. If the node color require additional negation, use <i>change_node_color</i> to do so.
<br><br>

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




## Example - Creating a Plug-in for Google
Let's walkthrough the steps with the example of adding Google plug-in to the dashboard:

### Step 1: Create a Folder for Google to Initiate the Plug-in
Create a new branch in Github and create a folder (Use Google's ticker <i>googl</i> as the folder name). The structure now should look like this:

```
--dashboard
 |- data
 	|- googl
		|- dataset
		|- Images
```

### Step 2: Development Definition Files (Node Indexes) for Plug-in
Go to SEC Edgar and obtain the latest <a href="https://www.sec.gov/Archives/edgar/data/1652044/000165204423000016/goog-20221231.htm">10-K</a>.
<br><br>
Go to consolidated balance sheet, and identify all the input entries (All the entries that cannot be calculated/aggregated, see the red boxed entires in the below image). Because the aggregated entries, such as Total cash, cash equivalents, and marketable securities, Total current asset, can be added up from their dependent entries, it can be added up in the later scripts. Assign node index to entries found in the 10-K, assign the beginning index number for all asset entries, then asset subcategories, then asset, liabilities, equity, then subcategories on liabilities and equity, and finally liabilities and equity input entries. If the entries is too small, you may combine the related entries into one entry, but be sure to document it.
<br><br>
After assigning the node index on balance sheet, do the same for income statement, and cashflow statement. At the end, visualize the node relationship on those definition files and visualize it on readme.
<br>

<img src=balsht_nodes.png>


<br><br>
The structure now should look like this:
<br>

```
--dashboard
 |- data
 	|- googl
		|- dataset
		|- Images
		|- nodes_googl_incsmt.json
		|- nodes_googl_balsht.json
		|- nodes_googl_cshfsmt.json
```

### Step 3: Prepare the Sample Data for the Dashboard
Copy <i>XXXX_income_template.csv</i>, <i>XXXX_income_example.csv</i>, <i>XXXX_balancesheet_template.csv</i> and replace XXXX with <i>googl</i>. Copy the node requires input, or input entries into the template files, and put the placeholder for Period and Value on the template file. Once prepared the template for all those files, duplicate the template and rename it to sample date files and input all sample data from the 10-K. So far the folder should have:

```
--dashboard
 |- data
 	|- googl
		|- dataset
			|- googl_income_template.csv
			|- googl_balancesheet_template.csv
			|- googl_cashflow_template.csv
			|- googl_income_example.csv
			|- googl_balancesheet_example.csv
			|- googl_cashflow_example.csv
```

### Step 4: Draft Sample Scripts to Display Sample Dashboards
Write the scripts to display sample dashboard. Therefore, we drafted <i>income_googl_poc.py</i>, <i>balancesheet_googl_poc.py</i>, and <i>cashflow_googl_poc.py</i>.


### Step 5,6,7: Develop and modify scripts to handle all data and chart
Copy <i>data_incsmt_XXXX.py</i>, <i>data_balsht_XXXX.py</i>, <i>data_cshfsmt_XXXX.py</i> to the company file. Keep all the supporting functions. And develop in the get_data() function. See the [Google](../googl) folder for the finalized version.
<br><br>
The structure now should look like this:
<br>


```
--dashboard
 |- data
 	|- googl
		|- dataset
			|- googl_income_template.csv
			|- googl_balancesheet_template.csv
			|- googl_cashflow_template.csv
			|- googl_income_example.csv
			|- googl_balancesheet_example.csv
			|- googl_cashflow_example.csv
		|- nodes_googl_incsmt.json
		|- nodes_googl_balsht.json
		|- nodes_googl_cshfsmt.json
		|- data_incsmt_googl.py
		|- data_balsht_googl.py
		|- data_cshfsmt_googl.py
```


### Step 8, 9: Integrate and Test the Scripts with the Dashboard in the Development environment
Integrate the scripts in the folder and test the dashboard.

### Step 9: Rollout to the production Environment
Happy analyzing!

