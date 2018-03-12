import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn import tree
'''
My modeler is taking all windows of whole dataset as one list as it does not matter which seq the window belong to for taining purposes
'''
testDB = "../datasets/full DB/buried_exposed_beta.3line.txt"
#buried_exposed_beta.3line
###EXTRACTING NAME, SEQUENCE AND TOPOLOGY FROM FILE INTO DIFFERENT LISTS###
listofnames =  []
listofsequences = []
listofstates = []
for i, line in enumerate(open(testDB, "r")):
    if i % 3 == 0:
        listofnames.append(line)
    if i % 3 == 1:
        listofsequences.append(line.strip("\n"))
    if i % 3 == 2:
        listofstates.append(line.strip("\n"))
### MAPPING SEQUENCE INTO NUMBERS ###
map = {'A' : 1,
       'R' : 2,
       'D' : 3,
       'N' : 4,
       'C': 5,
       'E': 6,
       'Q': 7,
       'G': 8,
       'H': 9,
       'I': 10,
       'L': 11,
       'K': 12,
       'M': 13,
       'F': 14, 
       'P': 15,
       'S': 16,
       'T': 17, 
       'W': 18,
       'Y': 19,
       'V': 20}
seqinnumbers = []
for seq in listofsequences:
    newseq = []
    for aa in seq:
        number = map[aa]
        newseq.append(number)
    seqinnumbers.append(newseq)
### MAPPING TOPOLOGY INTO NUMBERS ###
map = {"B":0, "E":1}
statesinnumbers = []
for state in listofstates:
    newstate = []
    for position in state:
        number = map[position]
        newstate.append(number)
    statesinnumbers.append(newstate)
for windowlen in range(3,32,2):
    n = windowlen // 2
    listofwindows = []
    listofstates = []
    for count in range(len(seqinnumbers)):   
        for aa in range(len(seqinnumbers[count])):
            if aa in range(0, n):
                listof0 = [0] * (n - aa)
                listofwindows.append(np.array(listof0 + seqinnumbers[count][0:aa + n + 1]))
                listofstates.append(statesinnumbers[count][aa])
            elif aa in range(len(seqinnumbers[count]) - n,len(seqinnumbers[count])):
                listof0 = [0] * (n + 1 + aa -len(seqinnumbers[count]))
                listofwindows.append(np.array(seqinnumbers[count][aa - n:len(seqinnumbers[count])] + listof0))
                listofstates.append(statesinnumbers[count][aa])
            else:
                listofwindows.append(np.array(seqinnumbers[count][aa - n :aa + n + 1]))
                listofstates.append(statesinnumbers[count][aa])
    listalls = np.array(listofstates)
    ### ENCODING INTO SVM INPUT, CROSSVALIDATING USING KMEANS AND PRINTING AVERAGE ACCURACY###
    enc = OneHotEncoder(n_values=21)
    encodedwindows = enc.fit_transform(listofwindows).toarray()
    listalls = np.array(listalls)
    model = svm.LinearSVC(tol=0.003, max_iter=5000)
    score = cross_val_score(model, encodedwindows, listalls, cv=3)
    print("windowlen:", windowlen,"score:", np.average(score))
'''
things to try with my model:
kernel=’rbf’, degree=3, gamma=’auto’, coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape=’ovr’, random_state=None
things cheched without much effect:
C=1.0, degree=3, gamma=’auto’, coef0=0.0
'''