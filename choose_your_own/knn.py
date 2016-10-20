#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import make_terrain_data
from class_vis import pretty_picture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# the training data (features_train, labels_train) have both "fast" and "slow"
# points mixed together - separate them so we can give them different colors
# in the scatter plot and identify them visually
features_train, labels_train, features_test, labels_test = make_terrain_data(3000)

grade_fast = [features_train[i][0] for i in range(len(features_train)) if labels_train[i] == 0]
bumpy_fast = [features_train[i][1] for i in range(len(features_train)) if labels_train[i] == 0]
grade_slow = [features_train[i][0] for i in range(len(features_train)) if labels_train[i] == 1]
bumpy_slow = [features_train[i][1] for i in range(len(features_train)) if labels_train[i] == 1]

# initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()

classifier = KNeighborsClassifier(weights='distance', algorithm='brute', p=3)
classifier.fit(features_train, labels_train)
predicted_labels = classifier.predict(features_test)
score = accuracy_score(labels_test, predicted_labels)
print("Predicted score: ", score)

try:
    pretty_picture(classifier, features_test, labels_test)
except NameError:
    pass
