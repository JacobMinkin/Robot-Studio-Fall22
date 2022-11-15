import numpy as np
from scipy import interpolate

y =  np.genfromtxt('pos.csv', delimiter=',')
size = y.shape
x = np.arange(0, size[0])
print(size)
print(np.array2string(y, separator=","))
print(np.array2string(x, separator=","))
f_11 = interpolate.interp1d(x, y[:,0])
f_12 = interpolate.interp1d(x, y[:,1])
f_13 = interpolate.interp1d(x, y[:,2])
f_14 = interpolate.interp1d(x, y[:,3])

f_21 = interpolate.interp1d(x, y[:,4])
f_22 = interpolate.interp1d(x, y[:,5])
f_23 = interpolate.interp1d(x, y[:,6])
f_24 = interpolate.interp1d(x, y[:,7])

