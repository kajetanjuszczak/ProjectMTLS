import pandas as pd
import numpy as np
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
    print(aadict)
def featurestonumbers(dictionary):
    '''
    Creates a list of numbers 0(burried) or 1(exposed) depending on the state of aa. (dict[list2])
    '''
def selectwidowlen():
    windowlen = input("select window len:")
    return windowlen

def createwindow(windowlen):
    '''
    creates the window desired by user
    problem - what it it is not // 2?
    problem2 - where to start window ?
    problem3 - where to store window ?
    and as a result produce an 2d array where a window of n residues is taken and the central one is described by feature in this place
    '''

if __name__ == "__main__":
    print(filetodictionary(testDB))
    #aatonumbers(filetodictionary(testDB))