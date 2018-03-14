import pickle
import os
import all_parsers
import predict_script

#buried_exposed_beta.3line
###EXTRACTING NAME, SEQUENCE AND TOPOLOGY FROM FILE INTO DIFFERENT LISTS##
DB = "../datasets/oldtestDB/1prottest.txt"
windowlen = 17
with open("../models/no_PSSM_model", "rb") as f:
    model = pickle.load(f)
X, listofsequences, listofnames = all_parsers.no_PSSM_input_single(DB, windowlen)
stringsofstates = predict_script.predict(model, X)
resultdir = '../results/'
os.chdir(resultdir)
with open("predictor2.txt", "w") as f:
    for i in range(len(listofnames)):
        f.write(listofnames[i])
        f.write(("\n"))
        f.write(listofsequences[i])
        f.write(("\n"))
        f.write(stringsofstates[i])
        f.write(("\n"))
### TODO: encode using one hot encoder, one by one and predict one by one ###
### TODO: if one aminoacid not present ruin the whole thing ###