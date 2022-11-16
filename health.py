# Health Function for the Robot. This will be run at start-up

from math import sin, cos
from lx16a import *
import time
import math
import numpy as np

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
# Disable Torque
servo11.disable_torque()
servo12.disable_torque()
servo13.disable_torque()
servo14.disable_torque()
servo21.disable_torque()
servo22.disable_torque()
servo23.disable_torque()
servo24.disable_torque() 

#Check Voltage
if(LX16A.get_vin() <5 ):
    print("LOW VOLTAGE")
    quit()
#Check Position
    servo_pos = [servo11.get_physical_angle(), 
    servo12.get_physical_angle(), servo13.get_physical_angle(), 
    servo14.get_physical_angle(), servo21.get_physical_angle(), 
    servo22.get_physical_angle(), servo23.get_physical_angle(), 
    servo24.get_physical_angle()]

# Enable Torque
servo11.enable_torque()
servo12.enable_torque()
servo13.enable_torque()
servo14.enable_torque()
servo21.enable_torque()
servo22.enable_torque()
servo23.enable_torque()
servo24.enable_torque() 

# Small movements of motor
for i in range (1,3):
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