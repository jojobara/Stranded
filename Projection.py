# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:13:05 2024

@author: d00r0
"""

import matplotlib.pyplot as plt

import numpy as np

v = [0, 2]

x = 10

y = 10

def myProjection(v):
  v = np.array(v)
  xy = np.array([x, y])    
  vprime = xy * np.dot(v, xy) / np.dot(xy, xy)
  return vprime
vprime = myProjection(v)

plt.figure(figsize = (7,7))
plt.xlim(0,10)          
plt.ylim(0,10)
plt.xticks(ticks=np.arange(0, 10, step=1))
plt.yticks(ticks=np.arange(0, 10, step=1))

plt.arrow(0, 0,x, y, color = 'red', alpha = 0.5)
plt.arrow(v[0], v[1],vprime[0]-v[0], vprime[1]-v[1], color = 'orange', alpha = 0.5)

plt.scatter(vprime[0], vprime[1])
plt.scatter(v[0], v[1])

print(vprime[0], vprime[1])
print((vprime[0]**2+vprime[1]**2)**(1/2))

plt.plot(x, y)