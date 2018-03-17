import pickle
import all_parsers
from sklearn.ensemble import RandomForestClassifier
'''
Model creation for random forest clasifier
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 5
X, Y = all_parsers.PSSM_input(DB, windowlen)
model = RandomForestClassifier()
model.fit(X, Y)
with open('../models/RFC_model', 'wb') as f:
    pickle.dump(model, f)
