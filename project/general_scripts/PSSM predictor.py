import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import time
import os
'''
take PSSM file and predict the state.
'''
testDB = "../datasets/buried_exposed_beta.3line.txt"
start = time.time()
listofnames =  []
listofsequences = []
listofstates = []
for i, line in enumerate(open(testDB, "r")):
    if i % 3 == 0:
        listofnames.append(line.strip(">\n"))
    if i % 3 == 2:
        listofstates.append(line.strip("\n"))
### find a file based on name of it
listofseq = []
for filename in listofnames:
    matrix = np.genfromtxt("../datasets/PSSMasci/"+filename+".fasta.pssm", skip_header = 3, skip_footer = 5, dtype=None,usecols = range(22,42))
    listofseq.append(matrix/100)

windowlen = 17
n = windowlen // 2
listofwindows = []
zeros = np.asarray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for prot in listofseq:
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
        a = np.array(listofwindows)
        
model = joblib.load("modelPSSM.pkl")
listofpredictions = []
for i in range(len(a)):
    prediction = model.predict(a[i])
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
with open("predictorPSSM.txt", "w") as f:
    for i in range(len(listofnames)):
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])
        f.write(("\n"))
        f.write(stringsofstates[i])
        f.write(("\n"))