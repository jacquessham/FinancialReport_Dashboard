# Dashboard
The dashboard is currently under development, the alpha version maybe tested with instruction under the instruction section.
<br><br>
More details are coming soon...

## Developement Update
The dashboard layout is drafted and able to displaying the chart with pre-matured backend. Currently the dashboard has the following avilable companies: Google (GOOGL), Meta (META), Apple (AAPL), Bank of America (BAC), and General Electrics on selected period of data. The backend is drafted and undergo with various testing. The next step is to add more for testing, backend on ingesting and verifying user's input data, and investigate the possibility of adding more features to the existing frontend. Stay tuned in the future releases. Here are the screenshots of the current version of the dashboard.
<br><br>
<img src=../gallery/income_v004.png>
<img src=../gallery/balance_v004.png>
<img src=../gallery/cashflow_v004.png>

## Instruction
### Prepare the Data
Currently, every company contains at least one annual report data. Only Google (GOOGL) contains some quarterly report data. However, the dataset template is available in the dataset folder in each company folder under the [Data](data) folder. Detailed Instruction will be available in the [Data](data) folder. In the current version, the sample data is sufficient to run the dashboard on each company.

### Running the Dashboard
To run the dashboard, run execute this on the command line:

```
python dashboard.py
```

<br>
Then, go to <b>127.0.0.1</b> (localhost) to access the dashboard.


## Personas
Targeted dashboard personas. More details will be coming soon...
<ul>
	<li>Administrator: Dashboard owner. But this persona does not require any technical skills, such as Product Manager.</li>
	<li>Technical Operator: Technical owner. This persona will maintain the dashboard, backend, and as well as data required.</li>
	<li>Viewer: Dashboard consumers. This persona simply use the dashbboard and will only interact the dashboard, but not the backend or preparing the data.</li>
</ul>
