import pickle
import os
import all_parsers
import predict_script
'''
predictor single sequence information.
'''
DB = "../datasets/oldtestDB/1prottest.txt"
windowlen = 11
with open("../models/no_PSSM_model", "rb") as f:
    model = pickle.load(f)
X, listofsequences, listofnames = all_parsers.no_PSSM_input_single(DB, windowlen)
stringsofstates = predict_script.predict(model, X)
resultdir = '../results/'
os.chdir(resultdir)
with open("predictor_single.txt", "w") as f:
    for i in range(len(listofnames)):
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])
        f.write(("\n"))
        f.write(stringsofstates[i])
        f.write(("\n"))