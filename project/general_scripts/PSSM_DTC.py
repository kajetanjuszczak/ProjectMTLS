import pickle
import all_parsers
from sklearn.tree import DecisionTreeClassifier
'''
model creator for decision tree clasifier
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 11
X, Y = all_parsers.PSSM_input(DB, windowlen)
model = DecisionTreeClassifier(random_state=0).fit(X, Y)
with open('../models/DTC_model', 'wb') as f:
    pickle.dump(model, f)