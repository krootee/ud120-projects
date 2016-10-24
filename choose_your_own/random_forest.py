#!/usr/bin/python

# import matplotlib.pyplot as plt
from prep_terrain_data import make_terrain_data
from class_vis import pretty_picture
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together - separate them so we can give them different colors
# in the scatter plot and identify them visually
features_train, labels_train, features_test, labels_test = make_terrain_data(10000)

grade_fast = [features_train[i][0] for i in range(len(features_train)) if labels_train[i] == 0]
bumpy_fast = [features_train[i][1] for i in range(len(features_train)) if labels_train[i] == 0]
grade_slow = [features_train[i][0] for i in range(len(features_train)) if labels_train[i] == 1]
bumpy_slow = [features_train[i][1] for i in range(len(features_train)) if labels_train[i] == 1]

# # initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()

gini_total = 0.0
entropy_total = 0.0
samples = 10

for i in range(samples):
    classifier = RandomForestClassifier(criterion="gini", n_estimators=50)
    classifier.fit(features_train, labels_train)
    predicted_labels = classifier.predict(features_test)
    score = accuracy_score(labels_test, predicted_labels)
    print("Predicted gini score: ", score)
    gini_total += score

for i in range(samples):
    classifier = RandomForestClassifier(criterion="entropy", n_estimators=50)
    classifier.fit(features_train, labels_train)
    predicted_labels = classifier.predict(features_test)
    score = accuracy_score(labels_test, predicted_labels)
    print("Predicted entropy score: ", score)
    entropy_total += score

print("Predicted average gini score: ", gini_total / samples)
print("Predicted average entropy score: ", entropy_total / samples)

try:
    pretty_picture(classifier, features_test, labels_test)
except NameError:
    pass
