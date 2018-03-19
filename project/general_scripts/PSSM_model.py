from sklearn import svm
import pickle
import all_parsers
'''
PSSM modeling programme
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 17
X, Y = all_parsers.PSSM_input(DB, windowlen)
model = svm.SVC(kernel = "linear", cache_size = 3000)
model.fit(X, Y)
with open('../models/PSSM_model', 'wb') as f:
    pickle.dump(model, f)