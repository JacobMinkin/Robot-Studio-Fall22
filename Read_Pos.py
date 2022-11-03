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
    #servo11.set_angle_limits(0, 240)
    #servo12.set_angle_limits(0, 240)
    #servo13.set_angle_limits(0, 240)
    #servo14.set_angle_limits(0, 240)
    #servo21.set_angle_limits(0, 240)
    #servo22.set_angle_limits(0, 240)
    #servo23.set_angle_limits(0, 240)
    #servo24.set_angle_limits(0, 240)
except ServoTimeoutError as e:
    
    quit()
servo_pos11 = servo11.get_physical_angle()
servo_pos12 = servo12.get_physical_angle()

print("Servo 11: " + str(servo_pos11) + " Servo 12: " + str(servo_pos12)
quit()
