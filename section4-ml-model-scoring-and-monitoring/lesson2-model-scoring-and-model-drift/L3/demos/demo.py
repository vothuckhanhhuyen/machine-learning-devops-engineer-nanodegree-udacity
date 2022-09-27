import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import f1_score

with open('samplemodel.pkl', 'rb') as file:
    model = pickle.load(file)

testdata=pd.read_csv('testdata.csv')
X = testdata[['bed','bath']].values.reshape(-1,2)
y = testdata['highprice'].values.reshape(-1,1)

predicted=model.predict(X)

f1score=metrics.f1_score(predicted,y)
print(f1score)