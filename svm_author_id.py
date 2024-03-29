#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
from sklearn.metrics import accuracy_score
t0 = time()

print "Start time:", round(time()-t0, 3), "s"
clf = svm.SVC(kernel="rbf", C=10000.0)

#features_train = features_train[:len(features_train)/100] #Here we are selecting 10% features for training
#labels_train = labels_train[:len(labels_train)/100] #Here we are selecting 10% labels for training

clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
counter = 0;

pred = clf.predict(features_test)

print "accuracy:", accuracy_score(labels_test, pred)

print "Counter total:", counter
print "Prediction time:", round(time()-t0, 3), "s"

print "No. of predicted to be in the 'Chris'(0):", sum(pred)

#########################################################


