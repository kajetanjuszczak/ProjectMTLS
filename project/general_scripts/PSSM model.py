import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import time
'''
take PSSM file and state
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

map = {"B":0, "E":1}
statesinnumbers = []
for state in listofstates:
    newstate = []
    for position in state:
        number = map[position]
        newstate.append(number)
    statesinnumbers.append(newstate)
### create windows + match the states
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
print(a)
### list of windwo states
states = []
for state in statesinnumbers:
    for aa in range(len(state)):
        states.append(state[aa])
states = np.array(states)
print(a.shape, states.shape)
model = svm.LinearSVC(tol=0.003, max_iter=5000)     
model.fit(a, states)
joblib.dump(model, 'modelPSSM.pkl')
end = time.time()
print(end - start)
    

      
