import numpy as np
from sklearn.model_selection import cross_val_score
import all_parsers
from sklearn.tree import RandomForestClasifier
'''
Results for random forest clasifier
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
for windowlen in range(3,32,2):
    X, Y = all_parsers.PSSM_input(DB, windowlen)
    model = RandomForestClasifier()
    score = cross_val_score(model, X, Y, cv = 3)
    print(np.average(score))