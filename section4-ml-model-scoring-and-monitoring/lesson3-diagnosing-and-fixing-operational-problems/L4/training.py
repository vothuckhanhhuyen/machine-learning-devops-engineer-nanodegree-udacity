
import pandas as pd

from sklearn.linear_model import LogisticRegression

trainingdata=pd.read_csv('samplefileingested.csv')

    
X=trainingdata.loc[:,['col1','col2']].values.reshape(-1, 2)
y=trainingdata['col3'].values.reshape(-1, 1).ravel()


LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                    intercept_scaling=1, l1_ratio=None, max_iter=100,
                    multi_class='warn', n_jobs=None, penalty='l2',
                    random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                    warm_start=False)
model = LogisticRegression(solver='liblinear', random_state=0).fit(X, y)







