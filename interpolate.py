import numpy as np
from scipy import interpolate

y =  np.genfromtxt('pos.csv', delimiter=',')
size = y.shape
x = np.arange(0, size[0])
print(np.array2string(y, separator=","))
print(np.array2string(x, separator=","))
f = interpolate.interp1d(x, y)

