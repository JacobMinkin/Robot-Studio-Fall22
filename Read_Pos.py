from math import sin, cos
from lx16a import *
import time
import math
import numpy as np

LX16A.initialize('/dev/ttyUSB0')



def Read_leg ():
    print("Servo 11: " + str(servo11.get_physical_angle()) + " Servo 12: " + str(servo12.get_physical_angle()))
    print("Servo 13: " + str(servo13.get_physical_angle()) + " Servo 14: " + str(servo14.get_physical_angle()))
    print("Servo 21: " + str(servo21.get_physical_angle()) + " Servo 22: " + str(servo22.get_physical_angle()))
    print("Servo 23: " + str(servo23.get_physical_angle()) + " Servo 24: " + str(servo24.get_physical_angle()))
    

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
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()
Read_leg ()
quit()
