'''
Predicting function, changing directrory to predicting one
'''
def predict(model, X):
    listofpredictions = []
    for i in range(len(X)):
        prediction = model.predict(X[i])
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
    return stringsofstates