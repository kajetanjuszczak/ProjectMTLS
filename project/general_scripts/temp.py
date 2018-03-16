import all_parsers
import pickle
import conf_matrix
'''
Results for random forest clasifier
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 17
X, Y = all_parsers.PSSM_input(DB, windowlen)
with open('../models/PSSM_model', 'rb') as f:
    sv = pickle.load(f)
CM = conf_matrix.plot(sv, X, Y)
print(CM)