import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import all_parsers
'''
PSSM testing SVC models (didnt know cros val function for it exists)
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 17
X, Y = all_parsers.PSSM_input(DB, windowlen)
for toler in range(1,31,3):
    toler  = toler/10000
    model = svm.SVC(kernel = "linear", cache_size = 3000, tol = toler)
    score = cross_val_score(model, X, Y, cv = 3)
    print(np.average(score))