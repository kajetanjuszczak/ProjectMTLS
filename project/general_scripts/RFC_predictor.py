import os
import pickle
import all_parsers
import predict_script
'''
predictiong based on model for PSSM SVC
'''
DB = "../datasets/oldtestDB/1prottest.txt"
windowlen = 5
listofsinglewindows, listofsequences, listofnames = all_parsers.PSSM_input_single(DB, windowlen)
with open("../models/RFC_model", "rb") as f:
    model = pickle.load(f)
stringsofstates = predict_script.predict(model, listofsinglewindows)
resultdir = '../results/'
os.chdir(resultdir)
### if want any differen output name, change one below ###
with open("RFC_predicted.txt", "w") as f:
    for i in range(len(listofnames)):
        f.write(">")
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])
        f.write(("\n"))
        f.write(stringsofstates[i])
        f.write(("\n"))