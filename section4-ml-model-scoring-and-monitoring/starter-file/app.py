from flask import Flask, request
import json
import os
import diagnostics
import scoring



######################Set up variables for use in our script
app = Flask(__name__)
# app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'

with open('config.json','r') as f:
    config = json.load(f) 

output_folder_path = config["output_folder_path"]
prod_deployment_path = config['prod_deployment_path']
test_data_path = config['test_data_path']
final_data_name = config["final_data_name"]
trained_model_name = config["trained_model_name"]
test_data_name = config["test_data_name"]

dataset_csv_path = os.path.join(config['output_folder_path'], final_data_name) 
deployed_model_path = os.path.join(config['prod_deployment_path'], trained_model_name)
test_data_file_path = os.path.join(config['test_data_path'], test_data_name)


#######################Prediction Endpoint
@app.route("/prediction", methods=['POST','OPTIONS'])
def predict():        
    #call the prediction function you created in Step 3
    test_data_file_path = request.form.get('path')
    result = diagnostics.model_predictions(test_data_file_path[1:-1])
    return json.dumps([int(item) for item in result]) #add return value for prediction outputs

#######################Scoring Endpoint
@app.route("/scoring", methods=['GET','OPTIONS'])
def score():        
    #check the score of the deployed model
    f1_score = scoring.score_model(deployed_model_path, test_data_file_path)
    return json.dumps(f1_score) #add return value (a single F1 score number)

#######################Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def summary():        
    #check means, medians, and modes for each column
    df_stat = diagnostics.dataframe_summary()
    return df_stat.to_dict() #return a list of all calculated summary statistics

#######################Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnose():        
    #check timing and percent NA values
    timing = diagnostics.execution_time()
    na_percents = diagnostics.dataframe_missing()
    if os.path.isfile('dependencies.json'):
        dependencies = json.load(open('dependencies.json'))
    else:
        dependencies = diagnostics.dependencies_checking().to_dict('records')
    diagnose_dict = {
        'timing': timing,
        'na_percents': na_percents,
        'dependencies': dependencies
    }
    return json.dumps(diagnose_dict) #add return value for all diagnostics

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
