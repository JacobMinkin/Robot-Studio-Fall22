from math import sin, cos
from lx16a import *
from moving_functions import *
import time
import math
import numpy as np
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
y = np.array([[165.12, 72.0  , 69.12,156.96],[186.48,117.12, 52.8 ,108.24],[162.48,135.6 , 71.28, 93.84],[162.48,117.84, 71.04,110.88],[162.0  ,101.52, 73.2 ,129.36],
[143.52, 79.2 , 88.32,150.  ], [120.96, 64.08,118.08,166.56], [ 93.36, 56.16,140.64,171.36],[113.52, 47.28,115.92,180.96],
[127.92, 40.56, 93.84,180.24],[161.28, 65.76, 66.48,153.6 ]])
size = y.shape
x = np.arange(0, size[0])

f_11 = UnivariateSpline(x, y[:,0])
f_12 = UnivariateSpline(x, y[:, 1])
f_13 = UnivariateSpline(x, y[:, 2])
f_14 = UnivariateSpline(x, y[:, 3])
f_11.set_smoothing_factor(.5)
f_12.set_smoothing_factor(.5)
f_13.set_smoothing_factor(.5)
f_14.set_smoothing_factor(.5)

spl = UnivariateSpline(x, y_s)
xs = np.linspace(0, 10, 1000)
#plt.plot(xs, spl(xs), 'g', lw=3)

""" spl = splrep(x, y[:,0], s= 100)
y2 = splev(x, spl)
plt.plot(x, y[:,0], 'o', x, y2, '-') """

spl.set_smoothing_factor(.5)
plt.plot(xs, spl(xs), 'b', lw=3)

