from flask import Flask, request
import pandas as pd
import pickle

app = Flask(__name__)

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

@app.route('/prediction')
def prediction():
    thedata=pd.read_csv('predictiondata.csv')
    with open('deployedmodel.pkl', 'rb') as file:
        themodel = pickle.load(file)
    prediction=themodel.predict(thedata)
    return str(prediction)

app.run(host='0.0.0.0', port=8000)