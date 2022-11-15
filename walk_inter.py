from math import sin, cos
from lx16a import *
import time
import math
import numpy as np
from scipy import interpolate

y = np.array([[165.12, 72.0  , 69.12,156.96],[186.48,117.12, 52.8 ,108.24],[162.48,135.6 , 71.28, 93.84],[162.48,117.84, 71.04,110.88],[162.0  ,101.52, 73.2 ,129.36],
[143.52, 79.2 , 88.32,150.  ], [120.96, 64.08,118.08,166.56], [ 93.36, 56.16,140.64,171.36],[113.52, 47.28,115.92,180.96],
[127.92, 40.56, 93.84,180.24],[161.28, 65.76, 66.48,153.6 ]])
size = y.shape
x = np.arange(0, size[0])

f_11 = interpolate.interp1d(x, y[:, 0])
f_12 = interpolate.interp1d(x, y[:, 1])
f_13 = interpolate.interp1d(x, y[:, 2])
f_14 = interpolate.interp1d(x, y[:, 3])


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
for z in range (0, 5):
    for x in range (0, 250, 1):
        if(x<125):
            y = x+125
        else:
            y = x -125
        servo11.move (f_11(x/25.0) )
        servo12.move ( f_12(x/25.0) )
        servo13.move (f_13(y/25.0))
        servo14.move ( f_14(y/25.0) )
        servo21.move (f_11(y/25.0) )
        servo22.move ( f_12(y/25.0) )
        servo23.move (f_13(x/25.0))
        servo24.move ( f_14(x/25.0)) 
        #time.sleep(.0001)
servo13.move (f_13(x/25.0))
servo14.move ( f_14(x/25.0) )
servo21.move (f_11(x/25.0) )
servo22.move ( f_12(x/25.0) )
time.sleep(5)
servo11.disable_torque()
servo12.disable_torque()
servo13.disable_torque()
servo14.disable_torque()
servo21.disable_torque()
servo22.disable_torque()
servo23.disable_torque()
servo24.disable_torque() 
quit()