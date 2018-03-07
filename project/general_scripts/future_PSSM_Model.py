import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn import svm
from sklearn.externals import joblib
import time
'''
take PSSM file and state
'''
testDB = "../datasets/buried_exposed_beta.3line.txt"

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
    listofseq.append(matrix)
   
### create windows + match the states
windowlen = 17
n = windowlen // 2
listofwindows = []
listofstates = []
zeros = np.asarray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(type(zeros))
for prot in listofseq:
    for aa in range(len(prot)):
        window = np.empty(20, 1)
        if aa in range(0, n):
            #for nr in range(aa ,n):
                #window.concatenate(zeros)
            #print(window)
            break
            window.extend(prot[0:aa + n + 1])
        elif aa in range(len(prot) - n,len(prot)):
            window.extend(prot[aa - n:len(prot)])
            for nr in range(0,aa - len(prot) + n + 1):
                window.append(zeros)
        else:
            window.extend(prot[aa - n :aa + n + 1])
        np.concatenate(window)
        print(window)
        listofwindows.append(window)
    break
    

      
