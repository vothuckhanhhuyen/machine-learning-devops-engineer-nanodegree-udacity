from flask import Flask, request
import pandas as pd
app = Flask(__name__)

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

@app.route('/')
def index():
    user = request.args.get('user')
    return str(user=='Bradford') + '\n'   

@app.route('/medians')
def summary():
    filename = request.args.get('filename')  
    thedata=readpandas(filename)
    return str(thedata.median(axis=0))

app.run(host='0.0.0.0', port=8000)
