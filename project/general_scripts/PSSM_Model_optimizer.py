import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import all_parsers
'''
PSSM testing SVC models
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
for windowlen in range(3,32,2):
    X, Y = all_parsers.PSSM_input(DB, windowlen)
    model = svm.SVC(kernel = "poly", cache_size = 3000, degree=3, coef0=1)
    score = cross_val_score(model, X, Y, cv = 3)
    print("windowlen",windowlen, "score",np.average(score))