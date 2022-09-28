import pandas as pd
import timeit
import os
import json
import pickle
import subprocess

##################Load config.json and get environment variables
with open('config.json','r') as f:
    config = json.load(f) 

prod_deployment_path = config["prod_deployment_path"]
output_folder_path = config['output_folder_path']
test_data_path = config["test_data_path"]
trained_model_name = config["trained_model_name"]
final_data_name = config["final_data_name"]
test_data_name = config["test_data_name"]

deployed_model_path = os.path.join(prod_deployment_path, trained_model_name)
dataset_csv_path = os.path.join(output_folder_path, final_data_name)
test_data_file_path = os.path.join(test_data_path, test_data_name)

##################Function to get model predictions
def model_predictions(test_data_file_path):
    #read the deployed model and a test dataset, calculate predictions
    model = pickle.load(open(deployed_model_path, 'rb'))
    df = pd.read_csv(test_data_file_path)
    X_test = df[['lastmonth_activity', 'lastyear_activity', 'number_of_employees']]
    pred = model.predict(X_test)
    return pred #return value should be a list containing all predictions

##################Function to get summary statistics
def dataframe_summary():
    #calculate summary statistics here
    df = pd.read_csv(dataset_csv_path)
    df_stats = df.describe().iloc[1:3]
    median_list = []
    for col in df_stats.columns:
        median_list.append(df[col].median(axis=0))
    df_median = pd.DataFrame([median_list], columns=df_stats.columns, index=['median'])
    df_stats = pd.concat([df_stats, df_median])
    return df_stats #return value should be a list containing all summary statistics

##################Function to check for missing data
def dataframe_missing():
    #calculate the percentage of na values
    df = pd.read_csv(dataset_csv_path)
    na_list = list(df.isna().sum(axis=0))
    na_percents = [na_list[i]/len(df.index) for i in range(len(na_list))]
    return na_percents #return the percentage of na values

##################Function to get timings
def execution_time():
    #calculate timing of training.py and ingestion.py
    start_time = timeit.default_timer()
    os.system('python ingestion.py')
    ingestion_time = timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    os.system('python training.py')
    training_time = timeit.default_timer() - start_time
    return [ingestion_time, training_time] #return a list of 2 timing values in seconds

##################Function to check dependencies
def dependencies_checking():
    #get a table of current and latest versions of modules used in this script
    if not os.path.isfile('requirements.txt'):
        subprocess.check_output(['pip', 'freeze'])

    with open('requirements.txt', 'r') as f:
        modules = f.read().splitlines()
    
    modules_dict = {'module_name': [], 'current_version': [], 'latest_version': []}
    for module in modules:
        module_name, current_version = module.split('==')
        latest_version = subprocess.check_output(['pip', 'index', 'versions', module_name])
        latest_version = latest_version.split(b'versions: ')[1].split(b', ')[0]
        latest_version = latest_version.decode('ascii')
        modules_dict['module_name'].append(module_name)
        modules_dict['current_version'].append(current_version)
        modules_dict['latest_version'].append(latest_version)
    df_modules = pd.DataFrame(modules_dict)
    with open('dependencies.json', 'w') as f:
        json.dump(df_modules.to_dict('records'), f)
    return df_modules #return a table of current and latest versions of modules used in this script


if __name__ == '__main__':
    print("Model Prediction:\n", model_predictions(test_data_file_path))
    print("-----------------------------------------")

    print("Dataframe Summary:\n", dataframe_summary())
    print("-----------------------------------------")

    print("Dataframe Missing:\n", dataframe_missing())
    print("-----------------------------------------")

    print("Execution Time:\n", execution_time())
    print("-----------------------------------------")

    print("Dependencies Checking:\n", dependencies_checking())




    
