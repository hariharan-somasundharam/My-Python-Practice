import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings("ignore")
def importdata():
    balance_data=pd.read_csv('pima indian.csv')
    print("Data Length:",len(balance_data))
    print("Data Set Shape:",balance_data.shape)
    print("DataSet:",balance_data.head())
    return balance_data
def splitdataset(balance_data):
    X=balance_data.values[:,1:5]
    y=balance_data.values[:,0]
    X-train,X_test,Y_train,Y_test==train_test_split(X,Y,test_size=0.3,random_state=100)
    return X,y,X_train,X_test,Y_train,Y_test
def train_using_gini(X_train,X_test,Y_train):
    clf_gini=DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3,min_samples_leaf=5)
    clf.gini.fit(X_train,Y_train)
    return clf_gini
def train_using_entropy(X_train,X_test,Y_train):
    clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)
    clf_entropy.fit(X_train,Y_train)
    return clf_entropy
def prediction(X_test,clf_object):
    Y_pred=clf_object.predict(X_test)
    print("Predicted Values:")
    print(Y_pred)
    return Y_pred
def cal_accuracy(Y_test,Y_pred):
    print("Confusion Matrix:",confusion_matrix(Y_test,Y_pred))
    print("Accuracy:",accuracy_score(Y_test,Y_pred)*100)
    print("Report:",classification_report(Y_test,Y_pred))
def main():
    data=importdata()
    X,Y,X_train,X_test,Y_train,Y_test=splitdataset(data)
    clf_gini=train_using_gini(X_train,X_test,Y_train)
    clf_entropy=train_using_entropy(X_train,X_test,Y_train)
    print("Results Using Gini Index:")
    Y_pred_gini=prediction(X_test,clf_gini)
    cal_accuracy(Y_test,Y_pred_gini)
    print("Results Using Entropy:")
    Y_pred_entropy=prediction(X_test,clf_entropy)
    cal_accuracy(Y_test,Y_pred_entropy)
    if_name_=='_main_'
    main()
    
    







    
