from sklearn.model_selection import cross_val_predict
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import itertools
def matrix(model, X, y_test):
    predictions = cross_val_predict(model, X, y_test)
    cnf_matrix = confusion_matrix(y_test, predictions)
    np.set_printoptions(precision=2)
    return cnf_matrix
def plot(model, X, y_test):
    cnf_matrix = matrix(model, X, y_test)
    cn = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
    cmap=plt.cm.Blues
    classes = ("Burried", "Exposed")
    plt.imshow(cn, interpolation='nearest', cmap=cmap)
    title = "SVC"
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f'
    thresh = cn.max() / 2.
    for i, j in itertools.product(range(cn.shape[0]), range(cn.shape[1])):
        plt.text(j, i, format(cn[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cn[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True state')
    plt.xlabel('Predicted state')
    plt.show()
    print(cn)
