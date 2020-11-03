# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mlxtend.plotting import plot_decision_regions
 
# Importing the dataset
dataset = pd.read_csv('HueValueFinal.csv')
X = dataset.iloc[1:, 1:].values
y = dataset.iloc[1:, 0].values
 
dataset = pd.read_csv('TestHueValue.csv')
X_test = dataset.iloc[:, 1:2].values
y_test = dataset.iloc[:, 0].values
 
X_train = X
y_train = y
 
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
 
# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p=2)
classifier.fit(X_train,y_train) 
 
 
# Predicting the Test set results
y_pred = classifier.predict(X_test)
 
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred)*100)
 
plot_decision_regions(X, y, clf = classifier, legend = 2)
plt.show()
 
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(y_test, y_pred)
print(cm)
report = classification_report(y_test, y_pred)
print(report)
