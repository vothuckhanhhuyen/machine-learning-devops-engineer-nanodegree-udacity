import ast
import pandas as pd


with open('historicmeans.txt', 'r') as f:
    meanslist = ast.literal_eval(f.read())

thedata=pd.read_csv('samplefile2.csv')

themeans=list(thedata.mean())

meancomparison=[(themeans[i]-meanslist[i])/meanslist[i] for i in range(len(meanslist))]

print(themeans)
print(meancomparison)

nas=list(thedata.isna().sum())
napercents=[nas[i]/len(thedata.index) for i in range(len(nas))]

print(nas)
print(napercents)