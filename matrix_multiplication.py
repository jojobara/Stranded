import numpy as np

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])

print(np.dot(A, B))

print("\n\n")

X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print(Y)