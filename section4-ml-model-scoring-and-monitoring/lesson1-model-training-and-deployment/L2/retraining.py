import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
import os

###################Reading Records#############
with open('deployedmodelname.txt', 'r') as f:
    deployedname = f.read()
print(deployedname)

with open('datalocation.txt', 'r') as f:
    datalocation = f.read()
print(datalocation)

trainingdata=pd.read_csv(os.getcwd()+datalocation)


##################Re-training a Model#############
X=trainingdata.loc[:,['col1','col2']].values.reshape(-1, 2)
y=trainingdata['col3'].values.reshape(-1, 1).ravel()

logit=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                    intercept_scaling=1, l1_ratio=None, max_iter=100,
                    multi_class='auto', n_jobs=None, penalty='l2',
                    random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                    warm_start=False)

model = logit.fit(X, y)


############Pushing to Production###################
pickle.dump(model, open('./production/'+deployedname, 'wb'))







