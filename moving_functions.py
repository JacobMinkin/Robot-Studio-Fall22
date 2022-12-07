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
    print("ERROR")
    quit()


def move_small(y):
    for i in range (1,5):
        if( i&2 == 0):
            x = 1
        else:
            x = -1
        servo11.move (y + 3*x )
        servo12.move ( y + 3*x )
        servo13.move (y + 3*x)
        servo14.move ( y + 3*x )
        servo21.move (y + 3*x )
        servo22.move (y + 3*x )
        servo23.move (y + 3*x)
        servo24.move (y + 3*x) 
        time.sleep(.1)

def move_step(steps = 5, speed = 250):
    servo11.enable_torque()
    servo12.enable_torque()
    servo13.enable_torque()
    servo14.enable_torque()
    servo21.enable_torque()
    servo22.enable_torque()
    servo23.enable_torque()
    servo24.enable_torque()
    half_speed = (speed/2)
    speed_ten = speed/10
    for z in range (0, steps):
        for x in range (0, speed, 1):
            if(x<half_speed):
                y = x + half_speed
            else:
                y = x - half_speed
            servo11.move (f_11(x/speed_ten) )
            servo12.move ( f_12(x/speed_ten) )
            servo13.move (f_13(y/speed_ten))
            servo14.move ( f_14(y/speed_ten) )
            servo21.move (f_11(y/speed_ten) )
            servo22.move ( f_12(y/speed_ten) )
            servo23.move (f_13(x/speed_ten))
            servo24.move ( f_14(x/speed_ten)) 
            #time.sleep(.0001)
    servo11.move (f_11(5) )
    servo12.move ( f_12(5) )
    servo13.move (f_13(5))
    servo14.move ( f_14(5) )
    servo21.move (f_11(5) )
    servo22.move ( f_12(5) )
    servo23.move (f_13(5))
    servo24.move ( f_14(5)) 
    time.sleep(5)
    servo11.disable_torque()
    servo12.disable_torque()
    servo13.disable_torque()
    servo14.disable_torque()
    servo21.disable_torque()
    servo22.disable_torque()
    servo23.disable_torque()
    servo24.disable_torque() 

def move_time(endtime = 15, speed = 250):
    servo11.enable_torque()
    servo12.enable_torque()
    servo13.enable_torque()
    servo14.enable_torque()
    servo21.enable_torque()
    servo22.enable_torque()
    servo23.enable_torque()
    servo24.enable_torque() 
    half_speed = (speed/2)
    speed_ten = speed/10
    startTime = time.time()
    newTime = time.time()
    while startTime + endtime > newTime:
        for x in range (0, speed, 1):
            if(x<half_speed):
                y = x + half_speed
            else:
                y = x - half_speed
            servo11.move (f_11(x/speed_ten) )
            servo12.move ( f_12(x/speed_ten) )
            servo13.move (f_13(y/speed_ten))
            servo14.move ( f_14(y/speed_ten) )
            servo21.move (f_11(y/speed_ten) )
            servo22.move ( f_12(y/speed_ten) )
            servo23.move (f_13(x/speed_ten))
            servo24.move ( f_14(x/speed_ten)) 
            newTime = time.time()
            #time.sleep(.0001)
    servo11.move (f_11(5) )
    servo12.move ( f_12(5) )
    servo13.move (f_13(5))
    servo14.move ( f_14(5) )
    servo21.move (f_11(5) )
    servo22.move ( f_12(5) )
    servo23.move (f_13(5))
    servo24.move ( f_14(5)) 
    time.sleep(5)
    servo11.disable_torque()
    servo12.disable_torque()
    servo13.disable_torque()
    servo14.disable_torque()
    servo21.disable_torque()
    servo22.disable_torque()
    servo23.disable_torque()
    servo24.disable_torque() 

def move_turn(steps = 5, side = "right", speed = 250):
    servo11.enable_torque()
    servo12.enable_torque()
    servo13.enable_torque()
    servo14.enable_torque()
    servo21.enable_torque()
    servo22.enable_torque()
    servo23.enable_torque()
    servo24.enable_torque()

    half_speed = (speed/2)
    speed_ten = speed/10
    for z in range (0, steps):
        for x in range (0, speed, 1):
            if side == "right":
                servo13.move (f_13(x/speed_ten))
                servo14.move (f_14(x/speed_ten) )
                servo23.move (f_13(x/speed_ten))
                servo24.move ( f_14(x/speed_ten))   
            else:
                servo11.move (f_13(x/speed_ten))
                servo12.move (f_14(x/speed_ten) )
                servo21.move (f_13(x/speed_ten))
                servo22.move ( f_14(x/speed_ten)) 


    servo11.move (f_11(5) )
    servo12.move ( f_12(5) )
    servo13.move (f_13(5))
    servo14.move ( f_14(5) )
    servo21.move (f_11(5) )
    servo22.move ( f_12(5) )
    servo23.move (f_13(5))
    servo24.move ( f_14(5)) 
    time.sleep(5)
    servo11.disable_torque()
    servo12.disable_torque()
    servo13.disable_torque()
    servo14.disable_torque()
    servo21.disable_torque()
    servo22.disable_torque()
    servo23.disable_torque()
    servo24.disable_torque() 

"""    
         y = speed - x
            if side == "right":
                temp = y
                y = x
                x = temp       
            # Front Right
            servo11.move (f_11(x/speed_ten) )
            servo12.move (f_12(x/speed_ten) )
            # Front Left
            servo13.move (f_13(y/speed_ten))
            servo14.move (f_14(y/speed_ten) )
            # Back Right
            servo21.move (f_11(x/speed_ten) )
            servo22.move ( f_12(x/speed_ten) )
            # Back Left
            servo23.move (f_13(y/speed_ten))
            servo24.move ( f_14(y/speed_ten))  
            """
            #time.sleep(.0001)
