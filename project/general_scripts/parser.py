import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
testDB = "D:/projekt/project/datasets/testDB.txt"

def filetodictionary(filename):
    dictionary = {}
    with open(filename, "r") as file1:
        file2 = file1.readlines()
    for i, line in enumerate(open(filename, "r")):
        if line.startswith(">") == True:
            dictionary[line.strip(">\n")] = [file2[i + 1].strip("\n"), file2[i + 2].strip("\n")]
    return dictionary
    
def aatonumbers(dictionary):
    '''
    Create a list of numbers 1-20 with respect to aa names
    '''
    aadict = {'A' : 1, 'R' : 2, 'D' : 3, 'N' : 4, 'C': 5, 'E': 6, 'Q': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}
    for key in dictionary:
        seq = (dictionary[key])[0]
        seqinnumbers = []
        for aa in seq:
            seqinnumbers.append(aadict[aa])
        dictionary[key][0] = seqinnumbers
    return dictionary
def featurestonumbers(dictionary):
    '''
    Creates a list of numbers 0(burried) or 1(exposed) depending on the state of aa. (dict[list2])
    '''
    statedict = {"B":0, "E":1}
    for key in dictionary:
        state1 = (dictionary[key])[1]
        statenumbers = []
        for state in state1:
            statenumbers.append(statedict[state])
        dictionary[key][1] = statenumbers
    return dictionary

def worksofar(filename):
    return featurestonumbers(aatonumbers(filetodictionary(filename)))

def selectwidowlen():
    windowlen = input("select window len:")
    return windowlen

def createwindow(windowlen):
    '''
    creates the window desired by user
    problem3 - where to store window ?
    and as a result produce an 2d array where a window of n residues is taken and the central one is described by feature in this place
    '''
    window = 0
    return window
def SVMconventer(window, state):
    '''
    converts window into SVM accepted format(onehotencoder)
    '''
    
    
if __name__ == "__main__":
    #print(filetodictionary(testDB))
    #featurestonumbers(filetodictionary(testDB))
    print(worksofar(testDB))