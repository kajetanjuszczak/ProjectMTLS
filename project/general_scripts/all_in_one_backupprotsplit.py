import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_score

testDB = "D:/projekt/project/datasets/testDB.txt"
#buried_exposed_beta.3line

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
seqwindows = []
countwin = 0
listofstates = []
for count in range(len(seqinnumbers)):
    listofwindows = []
    for aa in range(len(seqinnumbers[count])):
        if aa in range(0, n):
            listof0 = [0] * (n - aa)
            listofwindows.append(np.array(listof0 + seqinnumbers[count][0:aa + n + 1]))
            listofstates.append(statesinnumbers[count][aa])
            countwin +=1
        elif aa in range(len(seqinnumbers[count]) - n,len(seqinnumbers[count])):
            listof0 = [0] * (n + 1 + aa -len(seqinnumbers[count]))
            listofwindows.append(np.array(seqinnumbers[count][aa - n:len(seqinnumbers[count])] + listof0))
            listofstates.append(statesinnumbers[count][aa])
            countwin +=1
        else:
            listofwindows.append(np.array(seqinnumbers[count][aa - n :aa + n + 1]))
            listofstates.append(statesinnumbers[count][aa])
            countwin +=1
    seqwindows.append(listofwindows)
listalls = np.array(listofstates)
listallw = []
for i in range(len(seqwindows)):
    for j in range(len(seqwindows[i])):
        listallw.append(seqwindows[i][j])

#listofencodedwindows = []
#for seq in seqwindows:
#    enc = OneHotEncoder()
#    encodedwindow = enc.fit_transform(seq).toarray()
#    listofencodedwindows.append(encodedwindow)
#listofencodedwindows = np.array(listofencodedwindows)
#statelist = np.array(statelist)
        
enc = OneHotEncoder()
encodedwindows = enc.fit_transform(listallw).toarray()
encodedwindows = np.array(encodedwindows)
listalls = np.array(listalls)
x = encodedwindows.shape
y = listalls.shape
#clf = svm.SVC(kernel='linear', C=1.0).fit(encodedwindows, listalls) 
#score2 = cross_val_score(clf, encodedwindows, listalls, cv=crosval)
#avgscore = np.average(score2)
#print(avgscore)
