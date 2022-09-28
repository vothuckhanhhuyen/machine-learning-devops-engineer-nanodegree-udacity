import os
import json
import shutil



##################Load config.json and correct path variable
with open('config.json','r') as f:
    config = json.load(f) 

output_folder_path = config['output_folder_path']
output_model_path = config['output_model_path']
prod_deployment_path = config["prod_deployment_path"] 
trained_model_name = config["trained_model_name"]
latest_score_name = config["latest_score_name"]
ingested_files_name = config["ingested_files_name"]


####################function for deployment
def store_model_into_pickle():
    #copy the latest pickle file, the latestscore.txt value, and the ingestfiles.txt file into the deployment directory
    if not os.path.isdir(prod_deployment_path):
        os.mkdir(prod_deployment_path)
    shutil.copy(os.path.join(output_model_path, trained_model_name), prod_deployment_path)
    shutil.copy(os.path.join(output_model_path, latest_score_name), prod_deployment_path)
    shutil.copy(os.path.join(output_folder_path, ingested_files_name), prod_deployment_path)

if __name__ == '__main__':
    store_model_into_pickle()
        

