import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x/2.0)

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A*B)

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])
for row in X:
    print(row)
X = X.flatten()
print(X)
print(X[np.array([0, 2, 4])])
print(X > 15) #참과 거짓
print(X[X>15]) #X안에서 15보다 큰 값들
