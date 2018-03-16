from sklearn.model_selection import cross_val_predict
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
def matrix(model, X, y_test):
    predictions = cross_val_predict(model, X, y_test)
    cnf_matrix = confusion_matrix(y_test, predictions)
    np.set_printoptions(precision=2)
    return cnf_matrix
def plot(model, X, y_test):
    cnf_matrix = matrix(model, X, y_test)
    cn = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
    plt.ylabel('True state')
    plt.xlabel('Predicted state')
    print(cn)
    