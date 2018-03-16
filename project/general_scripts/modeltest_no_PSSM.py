import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import all_parsers
'''
My modeler is taking all windows of whole dataset as one list as it does not matter which seq the window belong to for taining purposes
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
for windowlen in range(3,22,2):
    X, Y = all_parsers.no_PSSM_input(DB, windowlen)
    model = svm.LinearSVC(max_iter=10000, tol=0.0003)
    score = cross_val_score(model, X, Y, cv = 3)
    print(np.average(score))