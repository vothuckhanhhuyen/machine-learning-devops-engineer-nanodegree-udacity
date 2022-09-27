from flask import Flask, request
import pandas as pd

app = Flask(__name__)

def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata

@app.route('/')
def index():
    user = request.args.get('user')
    return "Hello " + user

@app.route('/size')
def size():
    filename = request.args.get('filename')
    thedata=readpandas(filename)
    return str(len(thedata.index))

@app.route('/summary')
def summary():
    filename = request.args.get('filename')
    thedata=readpandas(filename)
    return str(thedata.mean(axis=1))

app.run(host='0.0.0.0', port=8000)

# curl "192.168.3.34:8000?user=Huyen" 
# curl "192.168.3.34:8000/size?filename=testdata.csv" 
# curl "192.168.3.34:8000/summary?filename=testdata.csv" 


