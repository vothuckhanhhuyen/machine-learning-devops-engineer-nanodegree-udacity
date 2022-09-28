# A DYNAMIC RISK ASSESSMENT SYSTEM FOR CLIENTS ATTRITION
This is the final project of Machine Learning DevOps Engineer Nanodegree Program.

## Overview
You'll complete the project by proceeding through 5 steps:
- Data ingestion. Automatically check a database for new data that can be used for model training. Compile all training data to a training dataset and save it to persistent storage. Write metrics related to the completed data ingestion tasks to persistent storage.
- Training, scoring, and deploying. Write scripts that train an ML model that predicts attrition risk, and score the model. Write the model and the scoring metrics to persistent storage.
- Diagnostics. Determine and save summary statistics related to a dataset. Time the performance of model training and scoring scripts. Check for dependency changes and package updates.
- Reporting. Automatically generate plots and documents that report on model metrics. Provide an API endpoint that can return model predictions and metrics.
- Process Automation. Create a script and cron job that automatically run all previous steps at regular intervals.

## Running Files
```
pip install -r requirements.txt

python ingestion.py
python training.py
python scoring.py
python deployment.py
python diagnostics.py
python reporting.py

python app.py
python apicalls.py
```

To run the whole process, copy the cron job in cronjob.txt to the system crontab:
```
*/10  * * * * python fullprocess.py
```