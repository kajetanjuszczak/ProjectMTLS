import numpy as np
import time
from sklearn.preprocessing import OneHotEncoder
from sklearn.externals import joblib
import os
testDBP = "../datasets/testDBP.txt"
#buried_exposed_beta.3line
###EXTRACTING NAME, SEQUENCE AND TOPOLOGY FROM FILE INTO DIFFERENT LISTS###
start = time.time()
listofnames =  []
listofsequences = []
for i, line in enumerate(open(testDBP, "r")):
    if i % 2 == 0:
        listofnames.append(line.strip("\n"))
    if i % 2 == 1:
        listofsequences.append(line.strip("\n"))
map = {'A' : 1, 'R' : 2, 'D' : 3, 'N' : 4, 'C': 5, 'E': 6, 'Q': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}

seqinnumbers = []
for seq in listofsequences:
    newseq = []
    for aa in seq:
        number = map[aa]
        newseq.append(number)          
    seqinnumbers.append(newseq)
windowlen = 17
n = windowlen // 2
listofwindows_single = []
for count in range(len(seqinnumbers)):   
    listofwindows = []
    for aa in range(len(seqinnumbers[count])):
        if aa in range(0, n):
            listof0 = [0] * (n - aa)
            listofwindows.append(np.array(listof0 + seqinnumbers[count][0:aa + n + 1]))
        elif aa in range(len(seqinnumbers[count]) - n,len(seqinnumbers[count])):
            listof0 = [0] * (n + 1 + aa -len(seqinnumbers[count]))
            listofwindows.append(np.array(seqinnumbers[count][aa - n:len(seqinnumbers[count])] + listof0))
        else:
            listofwindows.append(np.array(seqinnumbers[count][aa - n :aa + n + 1]))
    listofwindows_single.append(listofwindows)
enc = OneHotEncoder(n_values=21)
apendencoded = []
for i in range(len(listofwindows_single)):
    encodedwindows = enc.fit_transform(listofwindows_single[i]).toarray()
    encodedwindows = np.array(encodedwindows)
    apendencoded.append(encodedwindows)
model = joblib.load("model.pkl")
listofpredictions = []
for i in range(len(apendencoded)):
    prediction = model.predict(apendencoded[i])
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
with open("predictor.txt", "w") as f:
    for i in range(len(listofnames)):
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])
        f.write(("\n"))
        f.write(stringsofstates[i])
        f.write(("\n"))
### TODO: encode using one hot encoder, one by one and predict one by one ###
### TODO: if one aminoacid not present ruin the whole thing ###