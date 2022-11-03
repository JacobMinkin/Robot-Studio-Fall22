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

servo_front_pos = [servo11.get_physical_angle(), servo12.get_physical_angle(), servo13.get_physical_angle(), servo14.get_physical_angle()]
servo_back_pos = [servo21.get_physical_angle(), servo22.get_physical_angle(), servo23.get_physical_angle(), servo24.get_physical_angle()]

servo11_new = 209.52 
servo12_new = 124.56
servo13_new = 25.68 
servo14_new = 105.84
servo21_new = 209.52 
servo22_new = 137.76
servo23_new = 32.4 
servo24_new = 109.44

servo11.move (servo11_new )
servo12.move ( servo12_new )
servo13.move (servo13_new )
servo14.move ( servo14_new )
servo21.move (servo21_new )
servo22.move ( servo22_new )
servo23.move (servo23_new )
servo24.move ( servo24_new )

time.sleep(5)

servo_front_pos_new = [servo11.get_physical_angle(), servo12.get_physical_angle(), servo13.get_physical_angle(), servo14.get_physical_angle()]
servo_back_pos_new = [servo21.get_physical_angle(), servo22.get_physical_angle(), servo23.get_physical_angle(), servo24.get_physical_angle()]

servo11.disable_torque()
servo12.disable_torque()
servo13.disable_torque()
servo14.disable_torque()
servo21.disable_torque()
servo22.disable_torque()
servo23.disable_torque()
servo24.disable_torque()

save_front_pos = np.asarray([ servo_front_pos_new ])
save_front_pos.tofile('front_pos.csv', sep = ',')   
save_back_pos = np.asarray([ servo_front_pos_new ])
save_back_pos.tofile('back_pos.csv', sep = ',')   
quit()
