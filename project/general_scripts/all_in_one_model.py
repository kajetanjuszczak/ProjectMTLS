import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn import svm
from sklearn.externals import joblib
import time
'''
My modeler is taking all windows of whole dataset as one list as it does not matter which seq the window belong to for taining purposes
'''
testDB = "../datasets/buried_exposed_beta.3line.txt"
#buried_exposed_beta.3line
###EXTRACTING NAME, SEQUENCE AND TOPOLOGY FROM FILE INTO DIFFERENT LISTS###
start = time.time()
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
map = {'A' : 1, 'R' : 2, 'D' : 3, 'N' : 4, 'C': 5, 'E': 6, 'Q': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}
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
windowlen = 17
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
    print(np.array(listofwindows).shape)
listalls = np.array(listofstates)
### ENCODING INTO SVM INPUT, CROSSVALIDATING USING KMEANS AND PRINTING AVERAGE ACCURACY###
enc = OneHotEncoder(n_values=21)
encodedwindows = enc.fit_transform(listofwindows).toarray()
listalls = np.array(listalls)
#model = svm.SVC(kernel="linear", cache_size=2000, tol=0.003).fit(encodedwindows, listalls)
#joblib.dump(model, 'model.pkl')
### tried Kfol cv it seems like it was also working fine ###
#kf = KFold(n_splits=crosval)
#scorelist = []
#for train, test in kf.split(encodedwindows, listalls):
#    X_train, X_test, y_train, y_test = encodedwindows[train], encodedwindows[test], listalls[train], listalls[test]
#    clf = svm.SVC().fit(X_train, y_train)
#    score2 = clf.score(X_test, y_test)
#    scorelist.append(score2)
#avgscore = (np.average(scorelist))*100
end = time.time()
time = end - start
#print(time)
#print("average accuracy:","%.2f" % avgscore,"% for widow lenght of", windowlen,"and Kfold cross validation for k:", crosval, "time: ", "%.2f" % (time), "s.")
#"%.2f" %
