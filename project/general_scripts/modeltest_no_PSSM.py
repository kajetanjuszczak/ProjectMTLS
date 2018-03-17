import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import all_parsers
'''
My modeler is taking all windows of whole dataset as one list as it does not matter which seq the window belong to for training purposes,
didnt know about cros val function for this one
'''
### didnt know, cross_val have function for this realised in 17.03 so it was to late for corrections ###
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
for windowlen in range(3,22,2):
    X, Y = all_parsers.no_PSSM_input(DB, windowlen)
    model = svm.LinearSVC(max_iter=20000, tol=0.0003)
    score = cross_val_score(model, X, Y, cv = 3)
    print(np.average(score))