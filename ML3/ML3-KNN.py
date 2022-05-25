# K-Nearest Neighbors (K-NN)
#import packages
import numpy as np
import pandas as pd

# Read dataset
dataset = pd.read_csv("kdata.csv")
dataset

X = dataset.iloc[:,:-1].values
X

y = dataset.iloc[:,2].values
y

#import KNeighborsClassifier and create object of it
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(X,y)

#predictclass for the points(6,6)
X_test = np.array([6,2])
y_pred = classifier.predict([X_test])
print("General KNN:",y_pred)

classifier = KNeighborsClassifier(n_neighbors = 3, weights = 'distance')
classifier.fit(X,y)

#predict class for the points(6,6)
X_test = np.array([6,2])
y_pred = classifier.predict([X_test])
print("Distance Weighted KNN:",y_pred)
