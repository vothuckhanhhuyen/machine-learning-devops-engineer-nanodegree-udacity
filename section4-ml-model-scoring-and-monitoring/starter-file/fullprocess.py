import scoring
import json
import os
import subprocess

with open('config.json','r') as f:
    config = json.load(f)

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']
prod_deployment_path = config['prod_deployment_path']
trained_model_name = config["trained_model_name"]
ingested_files_name = config['ingested_files_name']
latest_score_name = config["latest_score_name"]

deployed_model_path = os.path.join(prod_deployment_path, trained_model_name)
ingested_files_path = os.path.join(prod_deployment_path, ingested_files_name)
latest_score_path = os.path.join(prod_deployment_path, latest_score_name)

##################Check and read new data
#first, read ingestedfiles.txt
with open(ingested_files_path) as f:
    ingested_files_list = f.read().splitlines()
#second, determine whether the source data folder has files that aren't listed in ingestedfiles.txt
all_files_exist = True
for file_name in os.listdir(input_folder_path):
    file_path = os.path.join(input_folder_path, file_name)
    if file_path not in ingested_files_list:
        all_files_exist = False
        break


##################Deciding whether to proceed, part 1
#if you found new data, you should proceed. otherwise, do end the process here
if not all_files_exist:
    print("New data found. Ingest new datasets from {}".format(input_folder_path))
    subprocess.call(['python', 'ingestion.py'])
else:
    print("No new data found. Exit the process")
    quit()


##################Checking for model drift
#check whether the score from the deployed model is different from the score from the model that uses the newest ingested data
with open(latest_score_path, 'r') as f:
    latest_score = float(f.read())
final_data_name = config['final_data_name']
final_data_path = os.path.join(output_folder_path, final_data_name)
new_score = scoring.score_model(deployed_model_path, final_data_path)
print('lastest score: {}, score on newly ingested data: {}'.format(latest_score, new_score))


##################Deciding whether to proceed, part 2
#if you found model drift, you should proceed. otherwise, do end the process here
if new_score < latest_score:
    print('Detect model drift. Retrain and redeploy model')
else:
    print('No model drift happended')
    quit()


##################Re-deployment
#if you found evidence for model drift, re-run the deployment.py script
subprocess.call(['python', 'training.py'])
subprocess.call(['python', 'scoring.py'])
subprocess.call(['python', 'deployment.py'])


##################Diagnostics and reporting
#run diagnostics.py and reporting.py for the re-deployed model
subprocess.call(['python', 'diagnostics.py'])
subprocess.call(['python', 'reporting.py'])
subprocess.call(['python', 'apicalls.py'])






