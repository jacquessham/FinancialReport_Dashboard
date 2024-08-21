# Dashboard
The dashboard is currently under development, the alpha version maybe tested with instruction under the instruction section.
<br><br>
More details are coming soon...

## Developement Update
The dashboard layout is drafted and able to displaying the chart with pre-matured backend. Currently the dashboard is only able to generate the financials of Google with selected period. The backend is drafted and undergo with various testing. The next step is to add more companies to the default setup, and investigate the possibility of adding more features to the existing frontend. Stay tuned in the future releases. Here are the screenshots of the current version of the dashboard.
<br><br>
<img src=../gallery/income_v002.png>
<img src=../gallery/balance_v002.png>
<img src=../gallery/cashflow_v002.png>

## Instruction
### Prepare the Data
Currently, there is only Google's 2022 10-K data is prepared. More dataset will be prepared in the future release. However, the dataset template is available in the dataset folder in each company folder under the [Data](data) folder. Detailed Instruction will be available in the [Data](data) folder. In the current version, the sample data is sufficient to run the dashboard.

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
