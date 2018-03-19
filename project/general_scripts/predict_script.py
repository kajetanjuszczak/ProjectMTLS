'''
Predicting function, changing directrory to predicting one
'''
def predict(model, X):
    listofpredictions = []
    for i in range(len(X)):
        prediction = model.predict(X[i])
        listofpredictions.append(prediction)
    seqpred = []
    for seq in listofpredictions:
        newstate = []
        for possition in seq:
            if possition == 0:
                newstate.append("B")
            else:
                newstate.append("E")
        seqpred.append(newstate)
    stringsofstatessigle = []
    for i in range(len(seqpred)):
        stringsofstatessigle.append("".join(seqpred[i]))
    return stringsofstatessigle