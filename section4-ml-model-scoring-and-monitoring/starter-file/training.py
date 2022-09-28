import pandas as pd
import pickle
import os
from sklearn.linear_model import LogisticRegression
import json

###################Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

output_folder_path = config['output_folder_path']
output_model_path = config['output_model_path']
final_data_name = config['final_data_name']
trained_model_name = config["trained_model_name"]

dataset_csv_path = os.path.join(output_folder_path, final_data_name) 
model_path = os.path.join(output_model_path, trained_model_name) 


#################Function for training the model
def train_model():
    
    #use this logistic regression for training
    # lr = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
    #                 intercept_scaling=1, l1_ratio=None, max_iter=100,
    #                 multi_class='warn', n_jobs=None, penalty='l2',
    #                 random_state=0, solver='liblinear', tol=0.0001, verbose=0,
    #                 warm_start=False)
    lr = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                intercept_scaling=1, l1_ratio=None, max_iter=100,
                n_jobs=None, penalty='l2',
                random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                warm_start=False)
    
    #fit the logistic regression to your data
    df = pd.read_csv(dataset_csv_path)
    X = df[['lastmonth_activity', 'lastyear_activity', 'number_of_employees']]
    y = df['exited']

    lr.fit(X, y)
    
    #write the trained model to your workspace in a file called trainedmodel.pkl
    if not os.path.isdir(output_model_path):
        os.mkdir(output_model_path)
    pickle.dump(lr, open(model_path, 'wb'))



if __name__ == '__main__':
    train_model()
