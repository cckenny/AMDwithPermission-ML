import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV,cross_validate
from sklearn import metrics
from sklearn.preprocessing import Normalizer
import matplotlib.pylab as plt


traindata = pd.read_csv('bjtuTrain.csv')
testdata = pd.read_csv('drebin88.csv')

X = traindata.iloc[:,0:88]
Y = traindata.iloc[:,88]
C = testdata.iloc[:,88]
T = testdata.iloc[:,0:88]

traindata = np.array(X)
trainlabel = np.array(Y)

testdata = np.array(T)
testlabel = np.array(C)

param_test1 = {'n_estimators':[10,20,30,40,50,60,70,80,90,100,200,300,400]}
gsearch1 = GridSearchCV(estimator = RandomForestClassifier(min_samples_split=100,
                                  min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10), 
                       param_grid = param_test1, scoring='roc_auc',cv=5)
gsearch1.fit(traindata, trainlabel)
print(gsearch1.best_params_)
print(gsearch1.best_score_)
#10


param_test2 = {'max_depth':[3,5,7,9,11,13], 'min_samples_split':[50,70,90,110,130,150,170,190]}
gsearch2 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 200, n_jobs = -1,
                                  min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10),
   param_grid = param_test2, scoring='roc_auc',iid=False, cv=5)
gsearch2.fit(traindata, trainlabel)
print(gsearch2.best_params_)
print(gsearch2.best_score_)
#13 50


param_test3 = {'min_samples_split':[2,3,4,5,6,7,8,9,10], 'min_samples_leaf':[1,2,4,6,8,10]}
gsearch3 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 200,  n_jobs = -1,
                                  max_features=9 ,oob_score=True, random_state=10),
   param_grid = param_test3, scoring='roc_auc',iid=False, cv=5)
gsearch3.fit(traindata, trainlabel)
print(gsearch3.best_params_)
print(gsearch3.best_score_)
# 4 1


param_test4 = {'max_features':[3,5,7,9,11,15,22]}
gsearch4 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 200,  n_jobs = -1, min_samples_split=120,
                                  min_samples_leaf=20 ,oob_score=True, random_state=10),
   param_grid = param_test4, scoring='roc_auc',iid=False, cv=5)
gsearch4.fit(traindata, trainlabel)
print(gsearch4.best_params_)
print(gsearch4.best_score_)
#22


param_test3 = {'min_samples_split':[4], 'min_samples_leaf':[1]}
gsearch3 = GridSearchCV(estimator = RandomForestClassifier(n_estimators= 200,  n_jobs = -1,
                                  max_features=9 ,oob_score=True, random_state=10),
   param_grid = param_test3, scoring='roc_auc',iid=False, cv=5)
gsearch3.fit(traindata, trainlabel)
print(gsearch3.best_params_)
print(gsearch3.best_score_)
# 4 1
