# Health Study Report
## Python Programming Course Assignment
The aim of this assignment is to produce a comprehensive report on a given dataset. The dataset contains information about each participant, and the task involves presenting a relevant analysis in a Jupyter Notebook.

All program-related documents, except for the notebook, will be written in English; the notebook report itself will be delivered in Swedish.

## Run the Part 1 notebook

From the repository root in PowerShell, set up Python 3.14 and start JupyterLab.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

Open [HealthStudyReport.ipynb](notebooks/HealthStudyReport.ipynb), select the Python 3 (ipykernel) kernel, and choose **Restart Kernel and Run All Cells**. The notebook reads the included CSV and records the package versions and simulation seeds.
