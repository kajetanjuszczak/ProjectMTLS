import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_score

testDB = "D:/projekt/project/datasets/testDB.txt"
#buried_exposed_beta.3line
def filetolist(filename):
    listofnames =  []
    listofsequences = []
    listofstates = []
    for i, line in enumerate(open(filename, "r")):
        if i % 3 == 0:
            listofnames.append(line)
        if i % 3 == 1:
            listofsequences.append(line.strip("\n"))
        if i % 3 == 2:
            listofstates.append(line.strip("\n"))
    return listofnames, listofsequences, listofstates
    
def letterstonumbers(filename):
    '''
    Create a list of numbers 1-20 with respect to aa names
    '''
    map = {'A' : 1, 'R' : 2, 'D' : 3, 'N' : 4, 'C': 5, 'E': 6, 'Q': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}
    listofsequences = filetolist(filename)[1]
    seqinnumbers = []
    for seq in listofsequences:
        newseq = []
        for aa in seq:
            number = map[aa]
            newseq.append(number)
        seqinnumbers.append(newseq)
    return seqinnumbers
    
def statestonumbers(filename):
    filetolist(filename)
    map = {"B":0, "E":1}
    listofstates = filetolist(filename)[2]
    statesinnumbers = []
    for state in listofstates:
        newstate = []
        for position in state:
            number = map[position]
            newstate.append(number)
        statesinnumbers.append(newstate)
    return statesinnumbers

def selectwidowlen():
    '''
    allow user to enter the windowlen
    *problem how not to allow string input
    '''
    windowlen = 0
    while windowlen % 2 == 0:
        windowlen = int(input("select window len(has to be odd number):"))
    return windowlen

def createwindow(windowlen, filename):
    '''
    creates the window of the lenght desired by user
    and as a result produce an 2d array where a window of n residues is taken and the central one is described by feature in this place
    '''
    seqinnumbers = letterstonumbers(filename)
    statesinnumbers = statestonumbers(filename)
    n = windowlen // 2
    seqwindows = []
    statelist = []
    for count in range(len(seqinnumbers)):
        listofwindows = []
        listofstates = []
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
        seqwindows.append(listofwindows)
        statelist.append(np.array(listofstates))
    return seqwindows, statelist

def SVMconventer(filename):
    '''
    converts window into SVM accepted format(onehotencoder)
    '''
    #np.set_printoptions(threshold=np.nan)
    windowlen = selectwidowlen()
    seqwindows = createwindow(windowlen, filename)[0]
    statelist = createwindow(windowlen, filename)[1]
    listofencodedwindows = []
    for seq in seqwindows:
        enc = OneHotEncoder()
        encodedwindow = enc.fit_transform(seq).toarray()
        listofencodedwindows.append(encodedwindow)
    listofencodedwindows = np.array(listofencodedwindows)
    statelist = np.array(statelist)
    return listofencodedwindows, statelist

def crossvalidation(filename):
    data = SVMconventer(filename)
    x = data[0][1]
    y = data[1][1]
    
    clf = svm.SVC()
    clf.fit(x, y) 
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    scoreofcv = clf.score(X_test, y_test)  
    return scoreofcv
    
if __name__ == "__main__":
    #print(SVMconventer(testDB))
    #print(selectwidowlen())
    print(crossvalidation(testDB))