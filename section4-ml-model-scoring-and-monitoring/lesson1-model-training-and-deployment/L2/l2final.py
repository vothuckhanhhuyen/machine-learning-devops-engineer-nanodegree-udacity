import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
import os


sales=pd.read_csv('sales.csv')

X=sales['timeperiod'].values.reshape(-1, 1)
y=sales['sales'].values.reshape(-1, 1)

lm=LinearRegression()

model = lm.fit(X, y)



filehandler = open('./production/l2emodel.pkl', 'wb') 
pickle.dump(model, filehandler)