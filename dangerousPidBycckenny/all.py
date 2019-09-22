import numpy as np
import pandas as pd
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error)
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error, roc_curve, classification_report,auc)
from sklearn.externals import joblib

traindata = pd.read_csv('train.csv')
testdata = pd.read_csv('newTest.csv')

X = traindata.iloc[:,0:34]
Y = traindata.iloc[:,34]
C = testdata.iloc[:,34]
T = testdata.iloc[:,0:34]

#scaler = Normalizer().fit(X)
#trainX = scaler.transform(X)

#scaler = Normalizer().fit(T)
#testT = scaler.transform(T)


traindata = np.array(X)
trainlabel = np.array(Y)

testdata = np.array(T)
testlabel = np.array(C)



model = LogisticRegression()
model.fit(traindata, trainlabel)


# make predictions
expected = testlabel
predicted = model.predict(testdata)
np.savetxt('res\\predictedLR.txt', predicted, fmt='%01d')
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")
print('LogisticRegression')
cm = metrics.confusion_matrix(expected, predicted)
print(cm)
fpr = float(cm[0][1])/np.sum(cm[0])
frr = float(cm[1][0])/np.sum(cm[1])
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("FPR")
print("%.3f" %fpr)
print("FRR")
print("%.3f" %frr)
print("***************************************************************")


# fit a Naive Bayes model to the data
model = GaussianNB()
model.fit(traindata, trainlabel)
print(model)
# make predictions
expected = testlabel
predicted = model.predict(testdata)
np.savetxt('res\\predictedNB.txt', predicted, fmt='%01d')
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")
print('GaussianNB')
cm = metrics.confusion_matrix(expected, predicted)
print(cm)
fpr = float(cm[0][1])/np.sum(cm[0])
frr = float(cm[1][0])/np.sum(cm[1])
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("FPR")
print("%.3f" %fpr)
print("FRR")
print("%.3f" %frr)
print("***************************************************************")



# fit a k-nearest neighbor model to the data
model = KNeighborsClassifier()
model.fit(traindata, trainlabel)
print(model)
# make predictions
expected = testlabel
predicted = model.predict(testdata)
np.savetxt('res\\predictedKNN.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")
print('KNeighborsClassifier')
cm = metrics.confusion_matrix(expected, predicted)
print(cm)
fpr = float(cm[0][1])/np.sum(cm[0])
frr = float(cm[1][0])/np.sum(cm[1])
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("FPR")
print("%.3f" %fpr)
print("FRR")
print("%.3f" %frr)
print("***************************************************************")



model = DecisionTreeClassifier()
model.fit(traindata, trainlabel)
print(model)
# make predictions
expected = testlabel
predicted = model.predict(testdata)
np.savetxt('res\\predictedDT.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")

cm = metrics.confusion_matrix(expected, predicted)
print('DecisionTreeClassifier')
print(cm)
fpr = float(cm[0][1])/np.sum(cm[0])
frr = float(cm[1][0])/np.sum(cm[1])
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("FPR")
print("%.3f" %fpr)
print("FRR")
print("%.3f" %frr)
print("***************************************************************")




'''

model = AdaBoostClassifier(DecisionTreeClassifier(min_samples_split=4, min_samples_leaf=1),
                         algorithm="SAMME",
                         n_estimators=600, learning_rate=0.7)
model.fit(traindata, trainlabel)

# make predictions
expected = testlabel
predicted = model.predict(testdata)
np.savetxt('res\\predictedABoost.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")

cm = metrics.confusion_matrix(expected, predicted)
print('AdaBoostClassifier')
print(cm)
fpr = float(cm[0][1])/np.sum(cm[0])
frr = float(cm[1][0])/np.sum(cm[1])
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("FPR")
print("%.3f" %fpr)
print("FRR")
print("%.3f" %frr)
print("***************************************************************")
'''



model = RandomForestClassifier(n_estimators= 100, n_jobs = -1, random_state=2)
                                    #,max_features=9)
                                  #,min_samples_split=4, min_samples_leaf=1)
model = model.fit(traindata, trainlabel)

# make predictions
expected = testlabel
predicted = model.predict(testdata)
np.savetxt('res\\predictedRF.txt', predicted, fmt='%01d')
# summarize the fit of the model
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary")
f1 = f1_score(expected, predicted , average="binary")
print('RF')
cm = metrics.confusion_matrix(expected, predicted)
print(cm)
fpr = float(cm[0][1])/np.sum(cm[0])
frr = float(cm[1][0])/np.sum(cm[1])
print("Accuracy")
print("%.3f" %accuracy)
print("precision")
print("%.3f" %precision)
print("recall")
print("%.3f" %recall)
print("f-score")
print("%.3f" %f1)
print("FPR")
print("%.3f" %fpr)
print("FRR")
print("%.3f" %frr)
joblib.dump(model, 'rfRe.model')##模型存储

print("***************************************************************")


