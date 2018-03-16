import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.model_selection import StratifiedKFold
from scipy import interp
import all_parsers
from sklearn import svm
'''
take PSSM file and state
'''
DB = "../datasets/full DB/buried_exposed_beta.3line.txt"
windowlen = 17
X, y = all_parsers.PSSM_input(DB, windowlen)
model = svm.SVC(kernel = "linear", cache_size = 3000, probability=True)
model.fit(X, y)
tprs = []
mean_fpr = np.linspace(0, 1, 100)
cv = StratifiedKFold(n_splits=3)
for train, test in cv.split(X, y):
    probas_ = model.fit(X[train], y[train]).predict_proba(X[test])
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    tprs.append(interp(mean_fpr, fpr, tpr))
plt.plot([0, 1], [0, 1], color='r', label='Random')
mean_tpr = np.mean(tprs, axis=0)
mean_tpr[-1] = 1.0
plt.plot(mean_fpr, mean_tpr, color='b', label=r'model')
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic(ROC) for best SVC model')
plt.legend(loc="lower right")
plt.show()