import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

y1 = np.array([158.16, 174.48, 165.6, 97.2, 150.96])
y2 = np.array([62.4, 140.88, 87.36, 49.68, 56.16])
y3 = np.array([73.2, 59.04, 69.6, 140.64, 80.16])
y4 = np.array([163.44, 88.08, 144.24, 182.64, 169.92])
size = y1.shape
x = np.arange(0, size[0])
print(size)
print(np.array2string(y1, separator=","))
print(np.array2string(x, separator=","))
f_11 = interpolate.interp1d(x, y1)
f_12 = interpolate.interp1d(x, y2)
f_13 = interpolate.interp1d(x, y3)
f_14 = interpolate.interp1d(x, y4)

xnew = np.arange(0, 4, 0.01)
ynew = f_12(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y2, 'o', xnew, ynew, '-')
plt.show()