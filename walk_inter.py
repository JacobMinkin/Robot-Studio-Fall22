from math import sin, cos
from lx16a import *
import time
import math
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


LX16A.initialize('/dev/ttyUSB0')




    

try:
    servo11 = LX16A(11)
    servo12 = LX16A(12)
    servo13 = LX16A(13)
    servo14 = LX16A(14)
    servo21 = LX16A(21)
    servo22 = LX16A(22)
    servo23 = LX16A(23)
    servo24 = LX16A(24)
    servo11.set_angle_limits(0, 240)
    servo12.set_angle_limits(0, 240)
    servo13.set_angle_limits(0, 240)
    servo14.set_angle_limits(0, 240)
    servo21.set_angle_limits(0, 240)
    servo22.set_angle_limits(0, 240)
    servo23.set_angle_limits(0, 240)
    servo24.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    
    quit()

for x in range (0, 4, 0.1):
    servo11.move (f_11(x) )
    servo12.move ( f_12(x) )
    servo13.move (f_13(x))
    servo14.move ( f_14(x) )
    time.sleep(.5)
quit()