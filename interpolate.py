import numpy as np
from scipy import interpolate
from scipy.interpolate import splev, splrep, UnivariateSpline
import matplotlib.pyplot as plt

""" y1 = np.array([158.16, 174.48, 165.6, 97.2, 150.96])
y2 = np.array([62.4, 140.88, 87.36, 49.68, 56.16])
y3 = np.array([73.2, 59.04, 69.6, 140.64, 80.16])
y4 = np.array([163.44, 88.08, 144.24, 182.64, 169.92])
size = y1.shape """

y = np.array([[165.12, 72.0  , 69.12,156.96],[186.48,117.12, 52.8 ,108.24],[162.48,135.6 , 71.28, 93.84],[162.48,117.84, 71.04,110.88],[162.0  ,101.52, 73.2 ,129.36],
[143.52, 79.2 , 88.32,150.  ], [120.96, 64.08,118.08,166.56], [ 93.36, 56.16,140.64,171.36],[113.52, 47.28,115.92,180.96],
[127.92, 40.56, 93.84,180.24],[161.28, 65.76, 66.48,153.6 ]])
size = y.shape
x = np.arange(0, size[0])
print(size)
print(np.array2string(y, separator=","))
print(np.array2string(x, separator=","))
f_11 = interpolate.interp1d(x, y[:, 0])
f_12 = interpolate.interp1d(x, y[:, 1])
f_13 = interpolate.interp1d(x, y[:, 2])
f_14 = interpolate.interp1d(x, y[:, 3])



y_s = np.transpose(y[:,1])
#plt.plot(x, y_s, 'ro', ms=5)

spl = UnivariateSpline(x, y_s)
xs = np.linspace(0, 10, 1000)
#plt.plot(xs, spl(xs), 'g', lw=3)

""" spl = splrep(x, y[:,0], s= 100)
y2 = splev(x, spl)
plt.plot(x, y[:,0], 'o', x, y2, '-') """

spl.set_smoothing_factor(.5)
plt.plot(xs, spl(xs), 'b', lw=3)


xnew = np.arange(0, 10, 0.1)
ynew = f_11(xnew)   # use interpolation function returned by `interp1d`
plt.plot(x, y[:,0], 'o', xnew, ynew, '-')
plt.show()
