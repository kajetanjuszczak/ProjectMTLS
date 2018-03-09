import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import time
import os
'''
take PSSM file and predict the state.
'''
testDB = "../datasets/testdata/testDB.txt"
start = time.time()
listofnames =  []
listofsequences = []
listofstates = []
for i, line in enumerate(open(testDB, "r")):
    if i % 3 == 0:
        listofnames.append(line.strip(">\n"))
    if i % 3 == 1:
        listofsequences.append(line.strip("\n"))
    if i % 3 == 2:
        listofstates.append(line.strip("\n"))
### find a file based on name of it
map = {'A': [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'R': [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'N': [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'D': [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'C': [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'Q': [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'E': [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
       'G': [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
       'H': [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
       'I': [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
       'L': [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
       'K': [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
       'M': [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
       'F': [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0], 
       'P': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
       'S': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
       'T': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0], 
       'W': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
       'Y': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
       'V': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]}
listofseq = []
seqinnumbers = []
for seq in listofsequences:
    newseq = []
    for aa in seq:
        number = map[aa]
        newseq.append(number)
    seqinnumbers.append(newseq)

windowlen = 17
n = windowlen // 2
zeros = np.asarray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
listofsinglewindows = []
for prot in seqinnumbers:
    listofwindows = []
    for aa in range(len(prot)):
        window = []
        if aa in range(0, n):
            for nr in range(aa ,n):
                window.append(zeros)
            window.extend(prot[0:aa + n + 1])
        elif aa in range(len(prot) - n,len(prot)):
            window.extend(prot[aa - n:len(prot)])
            for nr in range(0,aa - len(prot) + n + 1):
                window.append(zeros)
        else:
            window.extend(prot[aa - n :aa + n + 1])
        window = np.array(window)
        b =  window.flatten()
        listofwindows.append(b)
    listofsinglewindows.append(listofwindows)
print(len(listofsinglewindows))
model = joblib.load("modelPSSM.pkl")
listofpredictions = []
for i in range(len(listofsinglewindows)):
    prediction = model.predict(listofsinglewindows[i])
    listofpredictions.append(prediction)
listofstates = []    
for seqofstate in listofpredictions:
    newstate = []
    for position in seqofstate:
        if position == 0:
            newstate.append("B")
        else:
            newstate.append("E")
    listofstates.append(newstate)
stringsofstates = []
for i in range(len(listofstates)):
    stringsofstates.append("".join(listofstates[i]))
resultdir = '../results/'
os.chdir(resultdir)
with open("predictedPSSM.txt", "w") as f:
    for i in range(len(listofnames)):
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])
        f.write(("\n"))
        f.write(stringsofstates[i])
        f.write(("\n"))