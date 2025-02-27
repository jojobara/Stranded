import matplotlib.pyplot as plt

x = [3,5]

y = [5,3]
z = [1,2]

plt.arrow(z[0], z[1], y[0]-z[0], y[1]-z[1])

ans = [0,0]

def MyProjection(x,y,z):
  slope1 = (y[1] - z[1]) / (y[0] - z[0])
  slope2 = -1/slope1
  
  v1 = x[1] - (x[0]*slope2)
  v2 = y[1] - (slope1*y[0])
  
  print(slope1,v1,v2)
  
  ans[0] = (v1-v2)/(slope1-slope2)
  ans[1] = slope1*ans[0] + v2
  
  return ans

ans = MyProjection(x,y,z)
print(ans)

plt.scatter(x[0], x[1])
plt.scatter(y[0], y[1])
plt.scatter(z[0], z[1])
plt.text(x[0], x[1], 'X')
plt.text(y[0], y[1], 'Y')
plt.text(z[0], z[1], 'Z')

plt.arrow(x[0], x[1], ans[0]-x[0], ans[1]-x[1])

def Pythagoras(a,b) :
    c = (a**2+b**2)**(1/2)
    return c

print(Pythagoras(ans[0]-x[0], ans[1]-x[1]))