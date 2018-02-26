import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import time

testDB = "D:/projekt/project/datasets/buried_exposed_beta.3line.txt"
#buried_exposed_beta.3line

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

map = {'A' : 1, 'R' : 2, 'D' : 3, 'N' : 4, 'C': 5, 'E': 6, 'Q': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}
seqinnumbers = []
for seq in listofsequences:
    newseq = []
    for aa in seq:
        number = map[aa]
        newseq.append(number)
    seqinnumbers.append(newseq)

map = {"B":0, "E":1}
statesinnumbers = []
for state in listofstates:
    newstate = []
    for position in state:
        number = map[position]
        newstate.append(number)
    statesinnumbers.append(newstate)
    
windowlen = 0
while windowlen % 2 == 0:
    windowlen = int(input("select window len(has to be odd number):"))

crosval = int(input("select fold of cross validation:"))

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
        
enc = OneHotEncoder()
encodedwindows = enc.fit_transform(listofwindows).toarray()
encodedwindows = np.array(encodedwindows)
listalls = np.array(listalls)
 
kf = KFold(n_splits=crosval)
for train, test in kf.split(encodedwindows, listalls):
    X_train, X_test, y_train, y_test = encodedwindows[train], encodedwindows[test], listalls[train], listalls[test]
clf = svm.SVC().fit(X_train, y_train)
score2 = clf.score(X_test, y_test)
avgscore = np.average(score2)
end = time.time()
time = end - start
print("average accuracy:", "%.4f" % avgscore,"for widow lenght of", windowlen,"and Kfold cross validation for k:", crosval, "time: ", "%.2f" % (time), "s.")
