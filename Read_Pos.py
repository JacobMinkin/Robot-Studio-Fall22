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
servo_pos13 = servo13.get_physical_angle()
servo_pos14 = servo14.get_physical_angle()

servo_pos21 = servo21.get_physical_angle()
servo_pos22 = servo22.get_physical_angle()
servo_pos23 = servo23.get_physical_angle()
servo_pos24 = servo24.get_physical_angle()

print("Servo 11: " + str(servo_pos11) + " Servo 12: " + str(servo_pos12))
print("Servo 13: " + str(servo_pos13) + " Servo 14: " + str(servo_pos14))

print("Servo 21: " + str(servo_pos21) + " Servo 22: " + str(servo_pos22))
print("Servo 23: " + str(servo_pos23) + " Servo 24: " + str(servo_pos24))

quit()
