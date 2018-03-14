import numpy as np
'''
Predictor parser
INPUT: DB, windowlenght
Output: SVC format
'''
def parser(DB, windowlen):
    listofnames =  []
    listofsequences = []
    listofstates = []
    for i, line in enumerate(open(DB, "r")):
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
    seqinnumbers = []
    for seq in listofsequences:
        newseq = []
        for aa in seq:
            number = map[aa]
            newseq.append(number)
        seqinnumbers.append(newseq)
    ### MAPPING TOPOLOGY INTO NUMBERS ###
    map = {"B":0, "E":1}
    statesinnumbers = []
    for state in listofstates:
        newstate = []
        for position in state:
            number = map[position]
            newstate.append(number)
        statesinnumbers.append(newstate)
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
            a = np.array(listofwindows)
        listofsinglewindows.append(a)
    return listofsinglewindows, listofsequences, listofnames, statesinnumbers, 
if __name__ == "__main__":
    print(parser())