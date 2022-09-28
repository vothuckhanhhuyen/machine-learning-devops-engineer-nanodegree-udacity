import pickle
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os



###############Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

prod_deployment_path = config["prod_deployment_path"]
test_data_path = config["test_data_path"]
output_model_path = config["output_model_path"]
trained_model_name = config["trained_model_name"]
test_data_name = config["test_data_name"]
confusion_matrix_name = config["confusion_matrix_name"]

deployed_model_path = os.path.join(prod_deployment_path, trained_model_name)
test_data_file_path = os.path.join(test_data_path, test_data_name)


##############Function for reporting
def score_model():
    #calculate a confusion matrix using the test data and the deployed model
    #write the confusion matrix to the workspace
    model = pickle.load(open(deployed_model_path, 'rb'))
    df = pd.read_csv(test_data_file_path)
    X_test = df[['lastmonth_activity', 'lastyear_activity', 'number_of_employees']]
    y_test = df['exited']
    preds = model.predict(X_test)
    cf_matrix = metrics.confusion_matrix(y_test, preds)
    sns.heatmap(cf_matrix, annot=True)
    plt.savefig(os.path.join(output_model_path, confusion_matrix_name))   



if __name__ == '__main__':
    score_model()
