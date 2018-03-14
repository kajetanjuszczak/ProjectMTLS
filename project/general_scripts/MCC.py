from sklearn.metrics import matthews_corrcoef
from sklearn.model_selection import cross_val_predict
'''
Input: model, 2Darray of windows, True states
Return: MCC value
'''
def MCC(model, X, Y):
    predictions = cross_val_predict(model, X, Y)
    MCC = matthews_corrcoef(Y, predictions)
    return MCC
if __name__ == "__main__":
    print(MCC())