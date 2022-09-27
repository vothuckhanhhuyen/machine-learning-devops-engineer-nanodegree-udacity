import ast
import numpy as np

newr2=0.3625

with open('previousscores.txt', 'r') as f:
    r2list = ast.literal_eval(f.read())

firsttest = newr2<np.min(r2list)
print(firsttest)

secondtest = newr2<np.mean(r2list)-2*np.std(r2list)
print(secondtest)

iqr = np.quantile(r2list,0.75)-np.quantile(r2list,0.25)

thirdtest = newr2<np.quantile(r2list,0.25)-iqr*1.5
print(thirdtest)


