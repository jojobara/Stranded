import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

Z = np.random.randn(100,2)

km = KMeans(n_clusters = 3)
km.fit(Z)

new_labels = km.labels_

#넘파이 배열 슬라이싱 :,0 첫번째열 전체
plt.scatter(Z[:, 0], Z[:, 1], c=new_labels, cmap='rainbow',
edgecolor='k', s=25)