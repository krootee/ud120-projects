#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import os
from time import time
sys.path.append(os.path.abspath("../tools"))
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
classifier = SVC(kernel='rbf', C=10000.0)

# features_train = features_train[:round(len(features_train)/10)]
# labels_train = labels_train[:round(len(labels_train)/10)]

t0 = time()
classifier.fit(features_train, labels_train)
print("fit took: ", round(time()-t0, 3), " seconds")

t1 = time()
predicted = classifier.predict(features_test)
print("prediction took: ", round(time()-t1, 3), " seconds")

score = accuracy_score(labels_test, predicted)
print("predicted accuracy: ", score)

print("size of predicted array: ", len(predicted))

counter = 0
for i in predicted:
    if i == 1:
        counter += 1

print("Predicted Chris emails: ", counter)
