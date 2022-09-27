import ast
import pandas as pd


thedata=pd.read_csv('samplefile3.csv')

nas=list(thedata.isna().sum())
napercents=[nas[i]/len(thedata.index) for i in range(len(nas))]


thedata['col1'].fillna(pd.to_numeric(thedata['col1'],errors='coerce').mean(skipna=True), inplace = True)
thedata['col2'].fillna(pd.to_numeric(thedata['col2'],errors='coerce').mean(skipna=True), inplace = True)
thedata['col3'].fillna(pd.to_numeric(thedata['col3'],errors='coerce').mean(skipna=True), inplace = True)