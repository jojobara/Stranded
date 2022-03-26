import matplotlib.pyplot as plt
#import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

n = 200
x = np.random.rand(n)
# print(x)
y = np.random.rand(n)
# print(y)

plt.scatter(x, y,edgecolor='k', s=25)
#plt.show()

X = []

for i in range(n) :
    X.append([x[i], y[i]])

Y = np.array(X)
#print(Y)

km = KMeans(n_clusters = 5)
km.fit(Y)

new_labels = km.labels_

#print(new_labels)
plt.scatter(Y[:, 0], Y[:, 1], c=new_labels, cmap='gist_rainbow',
edgecolor='k', s=25)