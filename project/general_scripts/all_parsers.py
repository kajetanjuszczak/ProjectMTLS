import numpy as np
'''
take PSSM file and state
'''
### split file into lists ###
def parser(DB):
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
    return listofnames, listofsequences, listofstates
### extract frequency matrix from PSSM files and normalize ###
def PSSM_to_matrix(DB):
    listofnames = parser(DB)[0]
    listofseq = []
    for filename in listofnames:
        matrix = np.genfromtxt("../datasets/full DB/PSSMasci/"+filename+".fasta.pssm", skip_header = 3, skip_footer = 5, dtype=None,usecols = range(22,42))
        listofseq.append(matrix/100)
    return listofseq
def PSSM_to_matrix_pred(DB):
    listofnames = parser(DB)[0]
    listofseq = []
    for filename in listofnames:
        matrix = np.genfromtxt("../datasets/oldtestDB/PSSMasci/"+filename+".fasta.pssm", skip_header = 3, skip_footer = 5, dtype=None,usecols = range(22,42))
        listofseq.append(matrix/100)
    return listofseq
### encode sequence into binary form ###
def seq_to_array(DB):
    listofsequences = parser(DB)[1]
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
    return seqinnumbers
### map states into binary ###
def map_states(DB):
    listofstates = parser(DB)[2]
    map = {"B":0, "E":1}
    statesinnumbers = []
    for state in listofstates:
        newstate = []
        for position in state:
            number = map[position]
            newstate.append(number)
        statesinnumbers.append(newstate)
    return statesinnumbers
### create windows + match the states for PSSM ###
def create_windows_PSSM(DB, windowlen):
    listofseq = PSSM_to_matrix(DB)
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
    return a
### create windows + match the states for sequence(predictor input) ###
def create_windows_no_PSSM_single(DB, windowlen):
    listofseq = seq_to_array(DB)
    n = windowlen // 2
    listofsinglewindows = []
    zeros = np.asarray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    for prot in listofseq:
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
        listofsinglewindows.append(np.array(listofwindows))
    return listofsinglewindows
### create windows + match the states for single sequence info###
def create_windows_no_PSSM_all(DB, windowlen):
    listofseq = seq_to_array(DB)
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
    return a
def create_windows_PSSM_pred(DB, windowlen):
    listofseq = PSSM_to_matrix_pred(DB)
    n = windowlen // 2
    listofsinglewindows = []
    zeros = np.asarray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    for prot in listofseq:
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
        listofsinglewindows.append(np.array(listofwindows))
    return listofsinglewindows
### same states as windows so a state is related to window - only for model ###
def states_of_windows(DB):
    statesinnumbers = map_states(DB)
    states = []
    for state in statesinnumbers:
        for aa in range(len(state)):
            states.append(state[aa])
    states = np.array(states)
    return states
### model PSSM input ###
def PSSM_input(DB, windowlen):
    X = create_windows_PSSM(DB, windowlen)
    Y = states_of_windows(DB)
    return X, Y
### model no PSSM input ###
def no_PSSM_input(DB, windowlen):
    X = create_windows_no_PSSM_all(DB, windowlen)
    Y = states_of_windows(DB)
    return X, Y
### predictor input ###
def no_PSSM_input_single(DB, windowlen):
    listofsinglewindows = create_windows_no_PSSM_single(DB, windowlen)
    listofsequences = parser(DB)[1]
    listofnames = parser(DB)[0]
    return listofsinglewindows, listofsequences, listofnames
def PSSM_input_single(DB, windowlen):
    listofsinglewindows = create_windows_PSSM_pred(DB, windowlen)
    listofsequences = parser(DB)[1]
    listofnames = parser(DB)[0]
    return listofsinglewindows, listofsequences, listofnames
### additional function to check if my DB is balanced ###
def balance(DB):
    state = states_of_windows(DB)
    E = 0
    B = 0
    for i in state:
        if i == 0:
            B +=1
        else:
            E +=1
    print(E,B, E+B)
    
if __name__ == "__main__":
    PSSM_input_single("../datasets/oldtestDB/1prottest.txt", 17)
