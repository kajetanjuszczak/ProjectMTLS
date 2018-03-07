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
    matrix = np.genfromtxt("../datasets/PSSMasci/"+filename+".fasta.pssm", skip_header = 3, skip_footer = 6, dtype=None,usecols = range(22,42))
    listofseq.append(matrix)
   
### create windows + match the states
windowlen = 17
n = windowlen // 2
listofwindows = []
listofstates = []
zeros = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
for prot in listofseq:
    for aa in range(len(prot)):
        window = []
        if aa in range(0, n):
            for nr in range(aa ,n):
                window.append(zeros)
            window.extend(prot[0:aa + n + 1])
            #window = np.append(listof0 + prot[0:aa + n + 1])
            print(window)
            
            #window.extend(listof0 + prot[0:aa + n + 1])
        #elif aa in range(len(prot) - n,len(prot)):
        #    listof0 = zeros * (n + 1 + aa -len(prot))
        #    window.extend(prot[aa - n:len(prot)] + listof0)
        else:
            continue
        listofwindows.append(window)
        print(np.array(listofwindows).shape)
    break

        
