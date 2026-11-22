# Health Study Report
## Python Programming Course Assignment
The aim of this assignment is to produce a comprehensive report on a given dataset. The dataset contains information about each participant, and the task involves presenting a relevant analysis in a Jupyter Notebook.

All program-related documents, except for the notebook, will be written in English; the notebook report itself will be delivered in Swedish.

## Run the notebook for Part 1

On Windows, start PowerShell in the repository root, install Python 3.14, and start JupyterLab.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

The notebook reads the included CSV and records the package versions and simulation seeds.

## Notebook layout

The report notebook checks the CSV schema and participant IDs before analysis and uses the available observations for each calculation. For part 1, all code except what's IO-related is located in the notebook file itself.

## Statistical methods

The normal approximation and percentile bootstrap are two ways to assess uncertainty in the mean systolic blood pressure. The one-sided Welch test matches the question of whether smokers have higher mean blood pressure.

The power simulation then repeats the Welch test at zero and positive differences to estimate false-positive rates and detection power. Separate fixed NumPy seeds make them reproducible.
